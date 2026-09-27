# Guide for AI coding agents

Read this before changing anything in this repository.

## What this repo is

The official theme store for [Stride](https://github.com/GuusLab/Stride). Each theme in
`themes/<id>/` is a complete site design: tokens, components, page templates, images and fonts.
`site/` is the published store (signed `index.json`, zips, icons, screenshots and the
`index.html` gallery), deployed to GitHub Pages on every push to `main`.

## Layout

- `themes/<id>/` – theme sources (`theme.json`, `tokens.json`, `components/`, `templates/`,
  `assets/`, `icon.svg`/`icon.png`, `screenshots/`, `README.md`). The format is documented in
  Stride's `docs/themes.md`.
- `site/` – generated. Never edit by hand.
- `tools/check.py` – what CI checks (runs without Stride). A theme not yet in `site/index.json`
  passes as a submission; a published one must match its zip byte for byte.
- `tools/gallery.py` – writes `site/index.html` from `site/index.json`.
- `tools/demo-server.sh`, `tools/shoot.mjs`, `tools/icon.mjs` – demo server, screenshots, icons.
- `.github/workflows/` – `validate` (check.py, `stride theme validate` from npm, gallery up to
  date) and `pages` (deploy).

## Build, test, publish

The `stride` CLI comes from npm; never build Stride from source to get it.

```sh
npm install -g @guuslab/stride        # or prefix commands with: npx @guuslab/stride
stride --version                       # features must include "themes"
stride theme new <id> --dir themes/<id>   # scaffold that already validates
stride theme validate themes/<id>
stride theme index . --key ~/.stride/stride-themes.key \
  --base-url https://guuslab.github.io/stride-themes   # maintainer only; signs site/
python3 tools/gallery.py
python3 tools/check.py
```

`stride theme validate --help` and `stride theme index --help` print the general
`stride theme` help; `index` takes only `--key`, `--base-url`, `--out` and `--generated-at`.
`stride doctor` checks a machine's setup and `stride upgrade` updates an npm install.

Tools that run a Stride binary (`tools/demo-server.sh`) take it from `STRIDE_BIN`, defaulting to
`stride` on `PATH`. Set it explicitly when in doubt, for example when npm's global bin is not on
`PATH` in a non-interactive shell:

```sh
export PATH="$HOME/.npm-global/bin:$PATH"   # wherever `npm prefix -g`/bin is
STRIDE_BIN="$(command -v stride)" tools/demo-server.sh 8960 .demo/<id>
node tools/shoot.mjs <id> http://127.0.0.1:8960 <template-a> <template-b>
kill $(cat .demo/<id>/stride.pid)
```

The npm build has the editor inside, so no Stride checkout is needed. If `../Stride` has a built
`apps/editor/dist`, `demo-server.sh` serves that instead. `shoot.mjs` and `icon.mjs` need
`npm ci && npx playwright install chromium`.

## Rules that matter

- **Everything under `themes/<id>/` is signed.** Each published zip must match its source byte
  for byte, including the theme's `README.md`. Any change to a theme means bumping its
  `version` in `theme.json` and re-running `stride theme index`. Published versions are
  immutable.
- **Keys never go in the repo.** Signing keys stay in `~/.stride/` on the maintainer's machine.
  Never commit, print, copy or upload them. `.gitignore` is not a safety net.
- After editing `tools/gallery.py`, regenerate `site/index.html` or CI fails.
- Run `python3 tools/check.py` and `stride theme validate` on every theme you touch before you
  commit. CI runs both, but a failure is cheaper to hear locally.
- `theme.json` `author` must be `{"id": "guuslab", "name": "GuusLab"}` (check.py enforces it);
  contributors are credited in the theme's `README.md`.
- Keep `README.md` in step with the CLI: its commands are what newcomers copy.

## Copy standard

- **English only**: code, comments, docs, commit messages, captions and every other string.
- Short, clear, confident and honest about limits. Sentence case. Buttons are verbs.
- Say what happens and what to do next. Avoid jargon a site owner would not know.
- Keep one word per concept: page, post, site, theme, plugin, component, media.
- Comments explain why, not what. Never change behaviour for the sake of wording.
