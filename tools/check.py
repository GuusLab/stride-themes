#!/usr/bin/env python3
"""Checks the repository without Stride (which is private, so CI cannot run
`stride theme validate`).

For every themes/<id>/:
  - every .json file parses; theme.json has the contract's fields and limits
  - the required templates exist, homeTemplate names one of them
  - icon.png is 512x512, screenshots are 1600x1000 PNGs, 2 to 5 of them
  - images are at most 350 KB, fonts at most 1 MB, only allowed file types
For site/ (when present):
  - index.json lists every theme, and every file it names exists with the
    published size and sha256
  - each theme.zip holds exactly the files of themes/<id>/ at its published
    version, byte for byte (so a zip always matches the source it claims)

Usage: python3 tools/check.py [repo-root]
"""
import hashlib, json, os, re, struct, sys, zipfile

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
errors = []
def err(msg): errors.append(msg)

CATEGORIES = {'business', 'portfolio', 'blog', 'shop', 'restaurant', 'agency', 'personal', 'event', 'nonprofit', 'landing'}
ALLOWED = {'.json', '.png', '.jpg', '.jpeg', '.webp', '.woff2', '.md', '.txt', '.svg'}

def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return struct.unpack('>II', head[16:24])

def theme_files(d):
    out = []
    for base, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        for f in files:
            if f.startswith('.'):
                continue
            out.append(os.path.relpath(os.path.join(base, f), d).replace(os.sep, '/'))
    return sorted(out)

themes_dir = os.path.join(root, 'themes')
ids = sorted(x for x in os.listdir(themes_dir) if os.path.isdir(os.path.join(themes_dir, x)))
manifests = {}
for tid in ids:
    d = os.path.join(themes_dir, tid)
    where = f'themes/{tid}'
    for rel in theme_files(d):
        p = os.path.join(d, rel)
        ext = os.path.splitext(rel)[1].lower()
        if ext not in ALLOWED:
            err(f'{where}/{rel}: file type not allowed')
        if ext == '.json':
            try:
                json.load(open(p, encoding='utf-8'))
            except Exception as e:
                err(f'{where}/{rel}: not valid JSON ({e})')
        if rel.startswith('assets/') and ext in {'.jpg', '.jpeg', '.webp', '.png'} and os.path.getsize(p) > 350 * 1024:
            err(f'{where}/{rel}: image over 350 KB')
        if ext == '.woff2' and os.path.getsize(p) > 1024 * 1024:
            err(f'{where}/{rel}: font over 1 MB')
    try:
        m = json.load(open(os.path.join(d, 'theme.json'), encoding='utf-8'))
    except Exception as e:
        err(f'{where}/theme.json: {e}')
        continue
    manifests[tid] = m
    if m.get('id') != tid:
        err(f'{where}/theme.json: id is not the directory name')
    if not re.fullmatch(r'\d+\.\d+\.\d+', str(m.get('version', ''))):
        err(f'{where}/theme.json: version is not MAJOR.MINOR.PATCH')
    if m.get('author') != {'id': 'guuslab', 'name': 'GuusLab'}:
        err(f'{where}/theme.json: author must be GuusLab')
    if not 1 <= len(m.get('tagline', '')) <= 80:
        err(f'{where}/theme.json: tagline must be 1-80 characters')
    if len(m.get('longDescription', '')) > 4000:
        err(f'{where}/theme.json: longDescription over 4000 characters')
    cats = m.get('categories') or []
    if not cats or any(c not in CATEGORIES for c in cats):
        err(f'{where}/theme.json: categories must be from {sorted(CATEGORIES)}')
    if not re.fullmatch(r'#[0-9A-Fa-f]{6}', str(m.get('accent', ''))):
        err(f'{where}/theme.json: accent must be #RRGGBB')
    icon = os.path.join(d, m.get('icon', 'icon.png'))
    if not os.path.isfile(icon) or png_size(icon) != (512, 512):
        err(f'{where}: icon must be a 512x512 PNG')
    shots = m.get('screenshots') or []
    if not 2 <= len(shots) <= 5:
        err(f'{where}/theme.json: needs 2 to 5 screenshots')
    for s in shots:
        p = os.path.join(d, s.get('file', ''))
        if not os.path.isfile(p) or png_size(p) != (1600, 1000):
            err(f'{where}/{s.get("file")}: must be a 1600x1000 PNG')
    for f in m.get('fonts') or []:
        if not os.path.isfile(os.path.join(d, f.get('file', ''))):
            err(f'{where}: font file {f.get("file")} is missing')
    templates = {os.path.splitext(x)[0] for x in os.listdir(os.path.join(d, 'templates'))} if os.path.isdir(os.path.join(d, 'templates')) else set()
    for need in ('home', 'about', 'contact', '404'):
        if need not in templates:
            err(f'{where}: templates/{need}.json is missing')
    if not templates & {'blog-index', 'services'}:
        err(f'{where}: needs templates/blog-index.json or templates/services.json')
    if m.get('homeTemplate') not in templates:
        err(f'{where}/theme.json: homeTemplate is not a template')
    for req in ('tokens.json',):
        if not os.path.isfile(os.path.join(d, req)):
            err(f'{where}: {req} is missing')

site = os.path.join(root, 'site')
if os.path.isfile(os.path.join(site, 'index.json')):
    base = 'https://guuslab.github.io/stride-themes/'
    index = json.load(open(os.path.join(site, 'index.json'), encoding='utf-8'))
    listed = {t['id']: t for t in index.get('themes', [])}
    if sorted(listed) != ids:
        err(f'site/index.json lists {sorted(listed)}, the repo has {ids}')

    def check_file(entry, what):
        url = entry.get('url', '')
        if not url.startswith(base):
            err(f'{what}: url {url} is not under {base}')
            return None
        p = os.path.join(site, url[len(base):])
        if not os.path.isfile(p):
            err(f'{what}: {p} is missing')
            return None
        data = open(p, 'rb').read()
        if len(data) != entry.get('size') or hashlib.sha256(data).hexdigest() != entry.get('sha256'):
            err(f'{what}: size or sha256 does not match index.json')
        return p

    for tid, t in listed.items():
        check_file(t['icon'], f'{tid} icon')
        for i, s in enumerate(t.get('screenshots', [])):
            check_file(s, f'{tid} screenshot {i + 1}')
        for r in t.get('releases', []):
            p = check_file(r, f'{tid} {r.get("version")} zip')
            if not p or tid not in manifests or r.get('version') != manifests[tid].get('version'):
                continue
            d = os.path.join(themes_dir, tid)
            with zipfile.ZipFile(p) as z:
                names = sorted(n for n in z.namelist() if not n.endswith('/'))
                prefix = os.path.commonprefix(names) if len(names) > 1 else ''
                prefix = prefix[: prefix.rfind('/') + 1] if '/' in prefix else ''
                inside = {n[len(prefix):]: n for n in names}
                source = theme_files(d)
                if sorted(inside) != source:
                    missing = sorted(set(source) - set(inside))
                    extra = sorted(set(inside) - set(source))
                    err(f'{tid} {r["version"]} zip: files differ from themes/{tid} (missing {missing[:5]}, extra {extra[:5]}); bump the version and republish')
                    continue
                for rel, n in inside.items():
                    if z.read(n) != open(os.path.join(d, rel), 'rb').read():
                        err(f'{tid} {r["version"]} zip: {rel} differs from themes/{tid}; bump the version and republish')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'{len(ids)} theme(s) ok' + (' and site/ matches them' if os.path.isdir(site) else ''))
