#!/usr/bin/env node
// Usage: node tools/shoot.mjs <theme-id> <base-url> <page-a> <page-b>
//
// Takes a theme's store screenshots from a real Stride. Expects a running
// server (tools/demo-server.sh) with a fresh database. It zips
// themes/<id>/, uploads it (themes.upload), applies it with createHome,
// makes pages from templates <page-a> and <page-b>, publishes all three and
// writes themes/<id>/screenshots/:
//   01.png  the home page, first screen, at 1600x1000
//   02.png  <page-a>, first screen
//   03.png  <page-b>, first screen
//   04.png  three phone views (390 wide) side by side
// Captions are written into theme.json.
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, mkdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const [id, base, pageA, pageB] = process.argv.slice(2);
if (!id || !base || !pageA || !pageB) {
  console.error('usage: node tools/shoot.mjs <theme-id> <base-url> <page-a> <page-b>');
  process.exit(2);
}
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const dir = join(root, 'themes', id);
const manifestPath = join(dir, 'theme.json');
const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));

// A theme needs 2-5 screenshots to validate; before its first shoot, give it
// two plain placeholders so it can be uploaded.
if (!(manifest.screenshots?.length >= 2)) {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 });
  await pg.setContent(`<body style="margin:0;background:${manifest.accent}"></body>`);
  mkdirSync(join(dir, 'screenshots'), { recursive: true });
  manifest.screenshots = [];
  for (const n of ['01', '02']) {
    await pg.screenshot({ path: join(dir, 'screenshots', n + '.png') });
    manifest.screenshots.push({ file: `screenshots/${n}.png`, caption: 'placeholder' });
  }
  await b.close();
  writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
}

// Zip the theme directory (contents at the root of the archive).
const work = join(tmpdir(), `stride-shoot-${id}-${process.pid}`);
mkdirSync(work, { recursive: true });
const zip = join(work, 'theme.zip');
execFileSync('zip', ['-qr', '-X', zip, '.', '-x', '.*', '-x', '*/.*'], { cwd: dir });
const data = readFileSync(zip).toString('base64');

let cookie = '';
async function call(path, body) {
  const r = await fetch(base + path, {
    method: 'POST',
    headers: { 'content-type': 'application/json', cookie },
    body: JSON.stringify(body),
  });
  const set = r.headers.getSetCookie?.() ?? [];
  if (set.length) cookie = set.map((c) => c.split(';')[0]).join('; ');
  const text = await r.text();
  if (!r.ok) throw new Error(`${path} ${r.status}: ${text.slice(0, 600)}`);
  return text ? JSON.parse(text) : {};
}
const act = (name, body) => call('/api/actions/' + name, body);

await call('/api/login', { email: 'demo@stride.test', password: 'stride-demo-password-2026' });
await act('themes.upload', { data });
const applied = await act('themes.apply', { siteId: 'default', themeId: id, createHome: true });
const homeId = applied.homeDocumentId;
await act('publish.document', { documentId: homeId });
const pages = [];
for (const template of [pageA, pageB]) {
  const p = await act('themes.createpage', { siteId: 'default', template });
  await act('publish.document', { documentId: p.documentId });
  pages.push(p.slug);
}

const templates = (await act('themes.templates', { siteId: 'default' })).templates;
const titleOf = (slug) => templates.find((t) => t.slug === slug)?.title ?? slug;

const out = join(dir, 'screenshots');
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });

const browser = await chromium.launch();
async function settle(page) {
  await page.evaluate(() => document.fonts.ready);
  // Scroll through once so lazy images and reveal animations fire.
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
  });
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(900);
}
try {
  const desk = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 });
  const urls = ['/', '/' + pages[0], '/' + pages[1]];
  for (let i = 0; i < urls.length; i++) {
    const r = await desk.goto(base + urls[i], { waitUntil: 'networkidle' });
    if (!r || r.status() !== 200) throw new Error(`${urls[i]} answered ${r?.status()}`);
    await settle(desk);
    await desk.screenshot({ path: join(out, `0${i + 1}.png`) });
  }
  const phone = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
  const shots = [];
  for (const u of urls) {
    await phone.goto(base + u, { waitUntil: 'networkidle' });
    await settle(phone);
    shots.push((await phone.screenshot()).toString('base64'));
  }
  const accent = manifest.accent;
  const board = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 });
  await board.setContent(`<!doctype html><html><head><style>
    html,body{margin:0;height:100%}
    body{display:flex;align-items:center;justify-content:center;gap:56px;
      background:radial-gradient(120% 90% at 50% 0%, ${accent}33, transparent 60%), #16171b;}
    .ph{width:390px;height:844px;border-radius:44px;overflow:hidden;
      box-shadow:0 0 0 10px #0b0b0d,0 0 0 11px #3a3b40,0 30px 80px rgba(0,0,0,.55)}
    .ph img{display:block;width:390px;height:844px}
  </style></head><body>${shots.map((s) => `<div class="ph"><img src="data:image/png;base64,${s}"></div>`).join('')}</body></html>`);
  await board.waitForTimeout(300);
  await board.screenshot({ path: join(out, '04.png') });
} finally {
  await browser.close();
  rmSync(work, { recursive: true, force: true });
}

manifest.screenshots = [
  { file: 'screenshots/01.png', caption: `${titleOf(manifest.homeTemplate)} page` },
  { file: 'screenshots/02.png', caption: `${titleOf(pageA)} page` },
  { file: 'screenshots/03.png', caption: `${titleOf(pageB)} page` },
  { file: 'screenshots/04.png', caption: 'On a phone: home, ' + titleOf(pageA).toLowerCase() + ' and ' + titleOf(pageB).toLowerCase() },
];
writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
console.log(`${id}: 4 screenshots, pages /, /${pages[0]}, /${pages[1]}`);
