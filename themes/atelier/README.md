# Atelier

An editorial theme for creative studios and agencies: Instrument Serif display type,
off-white paper (`#F5F1EA`), ink black (`#141312`), one terracotta accent (`#C2562F`),
generous whitespace and asymmetric 7/5 and 4/8 grids that collapse to one column on phones.
Demo copy is written for an invented studio, "Hollis & Vane".

## Pages (`templates/`)

| File | Page |
| --- | --- |
| `home.json` | Home (the `homeTemplate`): editorial hero, work gallery, services, testimonial, stats, journal, call to action |
| `about.json` | Studio: page hero, team photo, principles, people, stats, testimonial |
| `services.json` | Services: services list, full-bleed case study, process, work |
| `blog-index.json` | Journal: featured essay and a grid of journal cards |
| `contact.json` | Contact: contact block and a visiting note |
| `404.json` | Not found (Stride has no reserved 404 slug; validated as slug `not-found`) |

## Components (`components/`)

header, footer, hero-editorial, hero-page (variants plain/raised/dark), hero-image,
section-intro, services-list, feature-grid (variants paper/raised), testimonial
(variants accent/ink), cta-band (variants paper/raised), gallery, stats, team,
contact-block, blog-card. Every content field is a prop bound with `bindings`.

## Notes for the installer

- Component ids in the files are stable theme ids (`atelier-header`, ...).
  `components.create` mints its own id, so the installer must map
  `atelier-*` to the new ids and rewrite `kind.component` in the templates
  before `documents.update`.
- Image references are relative (`assets/images/*.webp`) in `Image.src` and in
  `image`-kind prop defaults and overrides. Upload them with `media.upload` and
  rewrite them to the returned URL.
- `tokens.json` keeps every token name that Stride's starter tokens and built-in
  templates use (`surface.*`, `ink.*`, `type.*`, `text.*`, `brand.primary`,
  `space.*`, `radius.*`, `shadow.card`). Existing pages restyle and do not lose
  their colours. `TokenSet` has no dark-mode variants, so none are shipped.
- Stride's renderer has no `@font-face` support yet. Until the installer adds
  it, pages fall back to `Iowan Old Style`/Palatino/Georgia and Helvetica, which
  was checked and still reads well.

## Fonts

- Instrument Serif, by Rodrigo Fuenzalida and Jordan Egstad, is licensed under the
  SIL Open Font License 1.1.
- Inter Tight, by Rasmus Andersson, is licensed under the SIL Open Font License 1.1.

The `.woff2` files (latin subset) come from Google Fonts.

## Photographs

All six images in `assets/images/` are original AI-generated photographs made
for this theme with Magnific. They show no real people, brands or logos, and they
may be used with the theme.
