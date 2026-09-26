# Harbor

A Stride theme for restaurants, cafes and local food businesses: warm linen surfaces, harbour teal (`#1F6F78`), terracotta highlights, an expressive serif for headlines and a rounded sans for reading. The sample brand, Tidewater Kitchen, is invented.

## Pages (`templates/`)

| Template | Suggested slug | Contents |
|---|---|---|
| `home` | `home` | Split photo hero with "tonight" card, numbers, features, menu preview, guest quote, gallery, hours and address, journal teaser, reservation band |
| `about` | `about` | Full-bleed photo hero, story, numbers, team, quote, reservation band |
| `menu` | `menu` | Photo hero, full menu with price leaders, dietary notes, gallery, reservation band |
| `contact` | `contact` | Photo hero, booking block (placeholder fields, connect a Stride form), hours and map card |
| `blog-index` | `journal` | Journal header and six post cards, newsletter band |
| `404` | `not-found` | Friendly not-found page |

Image references in templates and components are package-relative (`assets/images/*.webp`); the installer uploads them to media and rewrites them.

## Components (`components/`)

Header, footer, hero with photo, full-bleed photo hero (variant `tall`), feature grid, menu section (variant `linen`), guest quote, reservation band, photo gallery, numbers, team, hours and address, booking block, journal card. Headers, heroes, the reservation band, the quote and the journal card expose props (text, links, images). Component ids (`harbor-*`) are package ids; the server mints its own on install.

## Tokens (`tokens.json`)

Colours (`surface.*`, `ink.*`, `line.*`, `brand.primary`), typography (`type.display`, `title`, `subtitle`, `quote`, `lead`, `body`, `small`, `eyebrow`, `button`, `price`), spacing `space.1` to `space.32`, radii `radius.sm` to `radius.full` and three shadows. Stride's TokenSet has no colour-scheme axis yet, so dark counterparts are shipped as `dark.*` colour tokens for a future dark mode to map onto.

## Fonts

- **Fraunces** by Undercase Type (Phaedra Charles, Flavia Zimbardi): SIL Open Font License 1.1.
- **Nunito** by Vernon Adams, Cyreal and Jacques Le Bailly: SIL Open Font License 1.1.

The `.woff2` subsets (Latin) come from the Fontsource distribution. The token font stacks fall back to Iowan Old Style/Georgia and system rounded sans until the installer registers the font files.

## Photos

All six photographs in `assets/images/` (hero, table, chef, coffee, terrace, dessert) were generated for this theme with Magnific AI image generation. They show no real people, brands or places, and ship with the theme for use on sites built with it.
