# Grove

A calm, organic Stride theme for yoga studios, breathwork teachers and wellness coaches.
Sage (`#6B8F71`) and warm sand, pebble-shaped photo crops, Fraunces headlines and Nunito Sans body copy.

## Pages (`templates/`)

| File | Suggested slug | What it is |
| --- | --- | --- |
| `home.json` | `/` (homeTemplate) | Split hero, stats, offer grid, weekly schedule, testimonial, memberships, journal, booking CTA |
| `about.json` | `/about` | Centred hero, coach intro, stats, gallery, teachers, testimonial |
| `services.json` | `/classes` | Classes & coaching: offer grid, schedule, memberships, private coaching |
| `contact.json` | `/contact` | Contact block with address, email, phone, hours; directions gallery |
| `blog-index.json` | `/journal` | Six journal cards |
| `404.json` | `/404` | Friendly not-found page (noindex) |

Templates place component instances by the theme component id (`grove-header`, ...) and
reference images as `assets/images/<file>`; the installer maps both to the site's ids and media URLs.
Header links point to `/classes`, `/services`, `/about`, `/journal`, `/contact`.

## Components (`components/`)

header, footer, hero-split, hero-centered (variants `sage` and `sand`), features, schedule,
testimonial, pricing, gallery, stats, team, about-split, cta, contact, blog-card.
Every text, image, alt text and link is exposed as a component prop and bound in the subtree.
Layouts are mobile first with `md`/`lg` breakpoint styles; focus rings use `:focus-visible`.

## Tokens

`tokens.json`: 16 colours, 11 typography styles, a spacing scale plus `section.y`, `gutter`, `content.max`,
radii including `radius.organic` (a pebble shape), and three shadows. Stride's token model has
no dark-mode variants yet, so Grove ships a single light palette.

## Fonts (SIL Open Font License 1.1)

- Fraunces, by Undercase Type (Phaedra Charles, Flavia Zimbardi). OFL 1.1.
- Nunito Sans, by Vernon Adams, Jacques Le Bailly, Manvel Shmavonyan, Alexei Vanyashin. OFL 1.1.

The `.woff2` files are latin subsets from the Fontsource packages. The renderer does not emit
`@font-face` yet, so until the theme installer adds it, pages fall back to Georgia and system sans.

## Photos

`studio.jpg`, `class.jpg`, `coach.jpg`, `ritual.jpg` and `outdoor.jpg` are original AI-generated images, made
for this theme with Magnific (September 2026). They show no real people, brands or logos and are licensed
with the theme for use on sites built with it.
