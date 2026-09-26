#!/usr/bin/env python3
"""Writes site/index.html, the public gallery, from site/index.json.

Run after `stride theme index`. Usage: python3 tools/gallery.py [repo-root]
"""
import html, json, os, sys

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
site = os.path.join(root, 'site')
index = json.load(open(os.path.join(site, 'index.json'), encoding='utf-8'))
base = index['registry'].rstrip('/') + '/'
rel = lambda url: url[len(base):] if url.startswith(base) else url
e = html.escape

cards = []
for t in index['themes']:
    shots = t['screenshots']
    release = next(r for r in t['releases'] if r['version'] == t['latest'])
    thumbs = ''.join(
        f'<a href="{e(rel(s["url"]))}"><img loading="lazy" src="{e(rel(s["url"]))}" alt="{e(s["caption"])}" width="1600" height="1000"></a>'
        for s in shots[1:]
    )
    paras = ''.join(f'<p>{e(p)}</p>' for p in t['longDescription'].split('\n\n')[:1])
    cats = ''.join(f'<li>{e(c)}</li>' for c in t['categories'])
    cards.append(f'''
<article class="theme" id="{e(t["id"])}" style="--accent:{e(t["accent"])}">
  <a class="hero" href="{e(rel(shots[0]["url"]))}"><img loading="lazy" src="{e(rel(shots[0]["url"]))}" alt="{e(shots[0]["caption"])}" width="1600" height="1000"></a>
  <div class="body">
    <header>
      <img class="icon" src="{e(rel(t["icon"]["url"]))}" alt="" width="64" height="64">
      <div><h2>{e(t["name"])}</h2><p class="tag">{e(t["tagline"])}</p></div>
    </header>
    <ul class="cats">{cats}</ul>
    <div class="desc">{paras}</div>
    <div class="thumbs">{thumbs}</div>
    <p class="meta">Version {e(t["latest"])} &middot; {release["size"] / 1e6:.1f} MB &middot; <a href="{e(rel(release["url"]))}">theme.zip</a></p>
  </div>
</article>''')

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stride Themes</title>
<meta name="description" content="The official theme store for Stride: {len(index["themes"])} complete site designs with tokens, components, page templates, photos and fonts.">
<style>
:root {{ --bg:#f6f5f2; --fg:#16171b; --muted:#5b5e66; --card:#fff; --line:#e4e2dc; color-scheme: light dark; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#111214; --fg:#f0efec; --muted:#a3a6ad; --card:#1a1b1f; --line:#2a2c31; }} }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; }}
a {{ color:inherit; }}
.wrap {{ max-width:1200px; margin:0 auto; padding:0 16px; }}
.top {{ padding:72px 0 40px; }}
.top h1 {{ font-size:clamp(2.2rem,6vw,3.6rem); line-height:1.05; letter-spacing:-.02em; margin:0 0 16px; }}
.top p {{ color:var(--muted); max-width:640px; margin:0 0 12px; font-size:1.1rem; }}
.top code {{ font-size:.9em; }}
.grid {{ display:grid; gap:32px; padding-bottom:80px; }}
.theme {{ background:var(--card); border:1px solid var(--line); border-radius:20px; overflow:hidden; display:grid; }}
@media (min-width: 900px) {{ .theme {{ grid-template-columns: 1.35fr 1fr; }} }}
.hero img {{ display:block; width:100%; height:auto; }}
.hero {{ border-bottom:4px solid var(--accent); display:flex; align-items:center; background:#16171b; }}
@media (min-width: 900px) {{ .hero {{ border-bottom:0; border-right:4px solid var(--accent); }} }}
.body {{ padding:24px; min-width:0; }}
.body header {{ display:flex; gap:16px; align-items:center; }}
.icon {{ border-radius:16px; flex:none; }}
h2 {{ margin:0; font-size:1.5rem; }}
.tag {{ margin:2px 0 0; color:var(--muted); }}
.cats {{ list-style:none; padding:0; margin:16px 0; display:flex; flex-wrap:wrap; gap:6px; }}
.cats li {{ font-size:.8rem; padding:2px 10px; border-radius:99px; border:1px solid var(--line); text-transform:capitalize; }}
.desc p {{ margin:0 0 10px; color:var(--muted); font-size:.95rem; }}
.thumbs {{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin:16px 0; }}
.thumbs img {{ display:block; width:100%; height:auto; border-radius:8px; border:1px solid var(--line); }}
.meta {{ font-size:.85rem; color:var(--muted); margin:0; }}
footer {{ border-top:1px solid var(--line); padding:24px 0 48px; color:var(--muted); font-size:.9rem; }}
</style>
</head>
<body>
<div class="wrap">
  <section class="top">
    <h1>Stride Themes</h1>
    <p>Complete designs for a Stride site: design tokens, a component library, page templates, photographs and fonts. Applying a theme never changes or deletes your pages, and it can be undone.</p>
    <p>To install one, open <strong>Admin &rarr; Themes</strong> in Stride, pick a theme, and choose <strong>Install</strong>, then <strong>Apply</strong>. Stride downloads the zip itself and checks its signature against the built-in key.</p>
  </section>
  <main class="grid">{"".join(cards)}
  </main>
</div>
<footer><div class="wrap">Signed index: <a href="index.json">index.json</a> &middot; Source: <a href="https://github.com/GuusLab/stride-themes">GuusLab/stride-themes</a> &middot; Updated {e(index["generatedAt"][:10])}</div></footer>
</body>
</html>
'''
open(os.path.join(site, 'index.html'), 'w', encoding='utf-8').write(page)
print('wrote site/index.html')
