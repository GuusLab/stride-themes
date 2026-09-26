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
- `tools/check.py` – what CI checks (runs without Stride).
- `tools/gallery.py` – writes `site/index.html` from `site/index.json`.
- `tools/demo-server.sh`, `tools/shoot.mjs`, `tools/icon.mjs` – demo server, screenshots, icons.
- `.github/workflows/` – `validate` (check.py, gallery up to date) and `pages` (deploy).

## Build, test, publish

```sh
stride theme validate themes/<id>
stride theme index . --key ~/.stride/stride-themes.key \
  --base-url https://guuslab.github.io/stride-themes
python3 tools/gallery.py
python3 tools/check.py
```

The `stride` binary lives at `../Stride/target/debug/stride` when it is not on `PATH`.

## Rules that matter

- **Everything under `themes/<id>/` is signed.** Each published zip must match its source byte
  for byte, including the theme's `README.md`. Any change to a theme means bumping its
  `version` in `theme.json` and re-running `stride theme index`. Published versions are
  immutable.
- **Keys never go in the repo.** Signing keys stay in `~/.stride/` on the maintainer's machine.
  Never commit, print, copy or upload them. `.gitignore` is not a safety net.
- After editing `tools/gallery.py`, regenerate `site/index.html` or CI fails.
- Run `python3 tools/check.py` before every commit.

## Copy standard

- **English only**: code, comments, docs, commit messages, captions and every other string.
- Short, clear, confident and honest about limits. Sentence case. Buttons are verbs.
- Say what happens and what to do next. Avoid jargon a site owner would not know.
- Keep one word per concept: page, post, site, theme, plugin, component, media.
- Comments explain why, not what. Never change behaviour for the sake of wording.
