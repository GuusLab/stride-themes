# Stride Themes

The official theme store for [Stride](https://github.com/GuusLab/Stride). A theme is a whole
design for a Stride site: design tokens (colours, type, spacing, corners, shadows), a component
library, page templates, photographs and fonts.

**Browse the store:** https://guuslab.github.io/stride-themes

## The themes

|      | Theme | Home | On a phone |
| ---- | ----- | ---- | ---------- |
| <img src="themes/atelier/icon.png" width="64" alt=""> | **[Atelier](themes/atelier)**<br>Editorial theme for studios and agencies: serif type, paper, ink, terracotta.<br><sub>agency · portfolio · business</sub> | <a href="themes/atelier/screenshots/01.png"><img src="themes/atelier/screenshots/01.png" width="320" alt="Atelier home page"></a> | <a href="themes/atelier/screenshots/04.png"><img src="themes/atelier/screenshots/04.png" width="320" alt="Atelier on a phone"></a> |
| <img src="themes/grove/icon.png" width="64" alt=""> | **[Grove](themes/grove)**<br>A calm, organic theme for yoga teachers, studios and wellness coaches.<br><sub>personal · business</sub> | <a href="themes/grove/screenshots/01.png"><img src="themes/grove/screenshots/01.png" width="320" alt="Grove home page"></a> | <a href="themes/grove/screenshots/04.png"><img src="themes/grove/screenshots/04.png" width="320" alt="Grove on a phone"></a> |
| <img src="themes/harbor/icon.png" width="64" alt=""> | **[Harbor](themes/harbor)**<br>A warm, appetizing theme for restaurants, cafes and local food businesses.<br><sub>restaurant · business</sub> | <a href="themes/harbor/screenshots/01.png"><img src="themes/harbor/screenshots/01.png" width="320" alt="Harbor home page"></a> | <a href="themes/harbor/screenshots/04.png"><img src="themes/harbor/screenshots/04.png" width="320" alt="Harbor on a phone"></a> |
| <img src="themes/ledger/icon.png" width="64" alt=""> | **[Ledger](themes/ledger)**<br>A composed navy-and-slate theme for consultancies, law firms and finance.<br><sub>business · agency</sub> | <a href="themes/ledger/screenshots/01.png"><img src="themes/ledger/screenshots/01.png" width="320" alt="Ledger home page"></a> | <a href="themes/ledger/screenshots/04.png"><img src="themes/ledger/screenshots/04.png" width="320" alt="Ledger on a phone"></a> |
| <img src="themes/nightfall/icon.png" width="64" alt=""> | **[Nightfall](themes/nightfall)**<br>Dark, image-led photography portfolio: full-bleed plates, quiet serif, gold.<br><sub>portfolio · personal</sub> | <a href="themes/nightfall/screenshots/01.png"><img src="themes/nightfall/screenshots/01.png" width="320" alt="Nightfall home page"></a> | <a href="themes/nightfall/screenshots/04.png"><img src="themes/nightfall/screenshots/04.png" width="320" alt="Nightfall on a phone"></a> |
| <img src="themes/pulse/icon.png" width="64" alt=""> | **[Pulse](themes/pulse)**<br>Dark-first SaaS landing theme: violet glow, bold geometric type, pricing, FAQ.<br><sub>landing · business</sub> | <a href="themes/pulse/screenshots/01.png"><img src="themes/pulse/screenshots/01.png" width="320" alt="Pulse home page"></a> | <a href="themes/pulse/screenshots/04.png"><img src="themes/pulse/screenshots/04.png" width="320" alt="Pulse on a phone"></a> |

Every screenshot is taken from a real Stride: the theme is uploaded, applied with a new home
page, and its pages are published (see [`tools/shoot.mjs`](tools/shoot.mjs)).

## Installing a theme

In Stride, open **Admin → Themes**. The store lists these themes from the signed index at
`https://guuslab.github.io/stride-themes/index.json`. Pick a theme to see its screenshots, then:

1. **Install** — the server downloads the zip itself, checks its size, SHA-256 and Ed25519
   signature against the built-in themes key, and validates every file against Stride's own types.
2. **Preview** — see your own pages in the theme before anything is saved.
3. **Apply** — sets the site's tokens, adds the theme's components to the library, uploads its
   images to Media and, if you choose, creates a new home page from the theme's home template.
   Existing pages are never changed or deleted, and **Undo** puts the previous tokens back.

The other templates show up under **New page** in the editor.

Themes need a Stride with the `themes` feature. The npm CLI (`@guuslab/stride`) has it. The
release binaries and container images are the default build and do not; a build with
`--features plugins` does.

<p>
  <img src="docs/store-list.png" width="49%" alt="The Themes store in Stride">
  <img src="docs/store-detail.png" width="49%" alt="A theme's page in the store">
</p>

After applying Harbor with a new home page and publishing it, the site's home page:

<img src="docs/store-applied-home.png" width="640" alt="The home page after applying Harbor">

## Make a theme in 10 minutes

All you need is Node.js (for npm) on macOS (Apple silicon) or Linux (x64, arm64). You do not
need to build Stride.

### 1. Install the Stride CLI

```sh
npm install -g @guuslab/stride
stride --version          # stride 0.0.2 or newer, features include "themes"
```

Or skip the install and put `npx @guuslab/stride` in front of every command below instead of
`stride`. `stride upgrade` keeps an npm install current, and `stride doctor` checks your machine
and configuration and says how to fix each problem.

### 2. Scaffold a theme

```sh
stride theme new my-theme
```

This writes a `my-theme/` folder that already passes validation. The id (`my-theme`) is 2 to 40
characters of `a-z`, `0-9` and `-`, starts with a letter, and is also the folder name. Use
`--dir <path>` to write it somewhere else; the last part of the path must still be the id.

```text
my-theme/
  theme.json            id, name, version, author, tagline, longDescription, categories,
                        accent, icon, screenshots, fonts, homeTemplate
  tokens.json           the design tokens: colors, typography, spacing, radius, shadows
  components/*.json     component masters, one per file (the scaffold has header, hero, footer)
  templates/<slug>.json page templates: home, about, contact, 404, and blog-index or services
  assets/images/*       .jpg / .webp / .png, at most 350 KB each
  assets/fonts/*.woff2  at most 1 MB each
  icon.png              512 x 512
  screenshots/NN.png    1600 x 1000, two to five of them
  README.md             optional; .md, .txt and a source icon.svg are allowed and ignored
```

Nothing else is accepted: a file of any other type refuses the whole theme. The files use exactly
the shapes Stride's own actions use: `tokens.json` is what `tokens.get` returns,
`components/*.json` what `components.get` returns, `templates/*.json` what `documents.get`
returns. A quick way to make them is to design the pages in Stride's editor and save those
answers into the files. Any string starting with `assets/` must name a file in the theme; on
apply, images go to Media and fonts are served with the site. The full format is in Stride's
[`docs/themes.md`](https://github.com/GuusLab/Stride/blob/main/docs/themes.md).

### 3. Validate it

```sh
stride theme validate my-theme
# my-theme 0.1.0 is valid: 5 template(s), 3 component(s), 1 image(s), 0 font(s).
```

This checks the folder exactly as an installation will and lists everything that is wrong in one
go, including a misspelt key deep in a component (`components/hero.json:
.root.children[0].kind.colour`). Run it after every change.

### 4. Preview it on a local Stride

Start a Stride in an empty folder. The npm build has the editor inside it.

```sh
mkdir stride-local && cd stride-local
stride serve              # http://127.0.0.1:8080, database in ./data/stride.db
```

Open `http://127.0.0.1:8080/admin/`. A fresh install asks for a **setup token** first: it is
printed in the server's output at start-up, and `stride setup-token` prints it again (run it in
the same folder). Then create your account and your site.

Zip the theme folder, from the folder that holds it:

```sh
zip -r my-theme.zip my-theme -x '*.DS_Store'
```

In Stride, open **Admin → Themes**, choose **Upload theme** and pick `my-theme.zip`. The upload
is validated like a store install; it just has no signature and is marked **Uploaded**. Preview
it, then **Apply to this site**. To try a change, zip and upload it again. Images are copied to
Media once per theme version, so bump `version` in `theme.json` when you change one.

### 5. Make it yours

Edit `tokens.json`, `components/` and `templates/`, add your images and fonts, and validate
again. Before you submit, replace the scaffold's placeholder icon and screenshots with real ones:

- `icon.png`, 512 x 512. In this repository, `node tools/icon.mjs icon.svg icon.png` renders an
  SVG to it (after `npm ci && npx playwright install chromium`).
- Two to five `screenshots/NN.png` at 1600 x 1000, each listed with a caption under
  `screenshots` in `theme.json`. In this repository, `tools/shoot.mjs` takes them from a real
  Stride for you (see [Screenshots](#screenshots)).

## Submit it to the store

You need no key. A maintainer signs and publishes your theme after review.

1. **Fork** [GuusLab/stride-themes](https://github.com/GuusLab/stride-themes) and clone your fork.
2. **Add your theme** as `themes/<id>/`: scaffold it there with
   `stride theme new <id> --dir themes/<id>`, or copy your folder in. It needs its real
   `icon.png`, two to five screenshots and a `README.md` that says what the pages and components
   are, and who made the fonts and photographs and under which licence.
3. **Set the author** in `theme.json` to `{ "id": "guuslab", "name": "GuusLab" }`: the store
   publishes every theme under its own account, and CI checks this. Credit yourself in the
   theme's `README.md`.
4. **Check it** locally:

   ```sh
   stride theme validate themes/<id>
   python3 tools/check.py
   ```

5. **Open a pull request.** Do not touch `site/`: it is generated and signed.

What CI checks on a pull request (`tools/check.py`, Python only, no Stride): every JSON file
parses; `theme.json` has the id of its folder, a `MAJOR.MINOR.PATCH` version, the GuusLab
author, a 1 to 80 character tagline, a long description of at most 4000 characters, known
categories and a `#RRGGBB` accent; the required templates exist and `homeTemplate` is one of
them; `icon.png` is 512 x 512 and there are two to five 1600 x 1000 PNG screenshots; images are
at most 350 KB, fonts at most 1 MB, and only allowed file types are present. A theme that is not
in `site/index.json` yet passes as a submission. A theme that is already published must match its
published zip byte for byte, so a change to one needs a new `version` and a republish by a
maintainer. CI also runs `stride theme validate` on every theme, with the published npm CLI.

Then a maintainer reviews the theme, runs `stride theme validate`, takes the store screenshots
if needed, signs it with the store key (`stride theme index`) and pushes, which publishes it to
the store every Stride sees.

### Screenshots

`tools/shoot.mjs` uploads a theme to a throwaway Stride, applies it with a new home page, makes
two more pages from its templates, publishes them and writes `screenshots/01.png` to `04.png`
(three desktop pages and a phone view) plus their captions in `theme.json`:

```sh
npm ci && npx playwright install chromium     # once
tools/demo-server.sh 8960 .demo/<id>          # a Stride with a fresh database, in the background
node tools/shoot.mjs <id> http://127.0.0.1:8960 <template-a> <template-b>
kill $(cat .demo/<id>/stride.pid)
```

`tools/demo-server.sh` uses the `stride` on your `PATH`; set `STRIDE_BIN` to use another one.

## Run your own theme store

A store is a folder of `themes/<id>/` directories, a signing key and a static web host. Stride
trusts one themes registry: this one by default, or yours once you point it there.

1. **Make a key**, once, and keep the private half secret:

   ```sh
   stride plugin keygen --out ~/.stride/my-themes.key
   # public key: <64 hex characters>   (you need it in step 4)
   ```

2. **Build the index** from the folder that holds `themes/`:

   ```sh
   stride theme index . --key ~/.stride/my-themes.key \
     --base-url https://example.com/themes
   ```

   This validates every `themes/<id>/` and writes, into `site/` (or `--out <dir>`):

   ```text
   site/index.json                         signed
   site/themes/<id>/<version>/theme.zip    zipped reproducibly
   site/themes/<id>/icon.png
   site/themes/<id>/screenshots/NN.png
   ```

   Releases already in `site/index.json` are kept, so older versions stay installable. Changing a
   theme without bumping its `version` is refused. `--generated-at <rfc3339>` fixes the index's
   timestamp.

3. **Host `site/`** at the base URL over https, for example on GitHub Pages as this repository
   does (`.github/workflows/pages.yml`). `index.json` must end up at `<base-url>/index.json`.

4. **Point Stride at it** with two environment variables on the server:

   ```sh
   STRIDE_THEME_REGISTRY_URL=https://example.com/themes/index.json \
   STRIDE_THEME_REGISTRY_KEY=<the 64 hex public key> \
     stride serve
   ```

   The `themes.configure` action (API or MCP, admins only) saves the same two settings in the
   database; the environment wins. `stride doctor` checks that the store is reachable and its
   signature is valid.

## Maintaining this store

To publish submitted or changed themes:

```sh
stride theme validate themes/<id>
stride theme index . --key ~/.stride/stride-themes.key \
  --base-url https://guuslab.github.io/stride-themes
python3 tools/gallery.py      # site/index.html
python3 tools/check.py        # what CI checks
```

A published version is immutable: change a theme, bump its version. Pushing `main` deploys
`site/` to GitHub Pages.

The private key never leaves the maintainer's machine. The index is signed with the themes
registry key whose public half is

```text
c7aae1439b9c52db5b0520ae68d2b1d34364ab56415a13e30bec4d007860310f
```

which is built into Stride as the default trusted themes key.

## Licence

Code and JSON are MIT. Fonts are under the SIL Open Font License 1.1, and the photographs are
original images made for these themes; see [LICENSE](LICENSE) and each theme's README.
