# Nightfall

A dark, image-led portfolio theme for Stride, made for photographers and visual artists.
Warm darkroom black, paper-white type, one safelight-gold accent (`#E0B45C`).

## Pages (templates/)

| Template | Slug suggestion | What it holds |
| --- | --- | --- |
| `home` | `/` | Full-bleed photo hero, statement, staggered gallery, numbers, commissions, testimonial, journal, call to action |
| `about` | `/about` | Portrait split hero, story, numbers, clients, testimonial, call to action |
| `work` | `/work` | Page head, featured series gallery, numbered project index, commissions, call to action |
| `blog-index` | `/journal` | Page head, six journal cards, newsletter call to action |
| `contact` | `/contact` | Contact details and enquiry form layout, call-to-action band |
| `404` | not found | Full-screen "Underexposed." page over a photograph |

## Components (components/)

header (with `overlay` variant for use over a photo), footer, hero-fullbleed (with `short` variant),
hero-split, statement, gallery (staggered 12-column), project-list, services (commissions; `page` variant),
stats, testimonial, cta-band, contact-block, clients, blog-card. All use the theme tokens and have
`md`/`lg` breakpoint styles; they collapse to a single column on phones.

## Tokens

Dark palette on the standard roles (`surface.*`, `ink.*`, `line.*`, `brand.primary`). Stride's TokenSet has no
colour-scheme axis yet, so light counterparts are shipped as `light.*` colour tokens for mapping later.
Type scale `type.hero` to `type.eyebrow`, spacing `space.1`–`space.32` plus fluid `space.gutter` and `space.section`,
radii and shadows.

## Fonts

- **Cormorant Garamond** Light 300, roman and italic — Christian Thalmann, SIL Open Font License 1.1.
- **Manrope** variable 400–600 — Mikhail Sharanda, SIL Open Font License 1.1.

Latin subsets downloaded from Google Fonts as `.woff2` into `assets/fonts/`. Both families have fallbacks in the tokens.

## Photographs

All seven images in `assets/images/` (shore, portrait, street, stairs, photographer, dunes, lantern) are original
AI-generated images made for this theme with Magnific (text-to-image), 2026. They show no real people, brands, text
or logos, and are licensed with the theme for use on sites built with it. People and places named in the copy
(Mara Ellison, Northlight Agency, Meridian Quarterly and so on) are invented.
