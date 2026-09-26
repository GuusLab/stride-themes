# Pulse

A dark-first theme for SaaS products and startup landing pages: near-black
surfaces with a violet cast, soft radial glows in Pulse violet `#6D28D9` and
magenta, headlines set tight in Sora and running text in Inter.

## Pages (`templates/`)

| File | Page |
| --- | --- |
| `home.json` | Landing page: glow hero with product screenshot, logos strip, feature grid, stats, feature story, testimonial, pricing, FAQ, CTA band |
| `features.json` | Product tour (the "services" page of a SaaS site) |
| `pricing.json` | Pricing table, logos, FAQ, CTA |
| `about.json` | Split hero, stats, mission, gallery, team, CTA |
| `blog-index.json` | Blog intro and six post cards |
| `contact.json` | Contact channels with photo, FAQ |
| `404.json` | Not-found page |

Templates are whole `Document` trees (`{"root": …}`) with the components
inlined, so a page made from one owns its copy. Image sources are theme-relative
(`assets/images/…`); the installer rewrites them to media URLs after upload.

## Components (`components/`)

Header, footer, hero (variants Glow / Flat / Raised), split hero (Glow / Flat),
logos strip, feature grid (Page / Raised), testimonial, pricing table, FAQ,
CTA band, gallery, team, contact block and blog card. Each is a Stride
`Component` with editable props bound to its text, links and images.

## Tokens

`tokens.json` is a Stride `TokenSet`. Stride's token model has one value per
colour and no dark variants, so Pulse's single palette **is** the dark palette.
Accent violet is used only as a fill under white text; accent text on dark uses
`ink.accent` (`#C4B5FD`).

## Fonts

Both fonts are under the SIL Open Font License 1.1 and are bundled as
variable-weight latin subsets from Google Fonts:

- **Sora** — Jonathan Barnbrook and Julián Moncada. `assets/fonts/sora-variable.woff2`
- **Inter** — Rasmus Andersson. `assets/fonts/inter-variable.woff2`

The Stride renderer does not emit `@font-face` itself; the theme installer must
register these files, otherwise the token stacks fall back to system sans.

## Photos and imagery

- `team.webp`, `whiteboard.webp`, `workspace.webp`, `portrait-founder.webp`,
  `portrait-engineer.webp`, `portrait-operations.webp` — generated for this
  theme with Magnific (AI image generation). No real people, brands or logos.
- `product-dashboard.webp` — an original HTML mock of a fictional product
  ("Vantora"), rendered for this theme.
- `icon.svg` / `icon.png` — original.

All brand and company names in the copy (Vantora, Halcyon, Northbeam, …) are
invented.
