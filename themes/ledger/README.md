# Ledger

A Stride theme for consultancies, law firms and finance: midnight navy (`#0E1B2C`), ledger navy (`#1E3A5F`), cool slate mist and a restrained brass accent, set in Inter Tight and Inter with tabular figures. The sample firm, Halden & Vorst, and every client, person and figure in the copy are invented.

## Pages (`templates/`)

| Template | Suggested slug | Contents |
|---|---|---|
| `home` | `home` | Navy split hero with key-figure card, figures strip, practice areas, case studies, client quote, principles, partners, insights, consultation band |
| `about` | `about` | Photo page hero, firm story, figures, partners, principles, offices gallery, quote, consultation band |
| `services` | `services` | Photo page hero, five numbered practice areas with fees, case studies, engagement terms, quote, consultation band |
| `contact` | `contact` | Photo page hero, enquiry block (placeholder fields, connect a Stride form), offices gallery |
| `blog-index` | `insights` | Insights header and six briefing cards, newsletter band |
| `404` | `not-found` | "This page is not on file." |

Image references are package-relative (`assets/images/*.webp`); the installer uploads them to media and rewrites them.

## Components (`components/`)

Header, footer, split hero with photo, page hero (variant `tall`), key figures (variant `mist`), practice areas list (variant `mist`), principles grid, case studies, client quote, partners, offices gallery, consultation band, enquiry block, insight card. Header, heroes, the consultation band, the quote and the insight card expose props. Component ids (`ledger-*`) are package ids; the server mints its own on install.

## Tokens (`tokens.json`)

Colours (`surface.*`, `ink.*`, `line.*`, `brand.primary`), typography (`type.display`, `title`, `subtitle`, `figure`, `quote`, `lead`, `body`, `small`, `eyebrow`, `button`, `price`), spacing `space.1` to `space.32`, tight radii (`2px` to `10px`, plus `radius.full`) and three shadows. Stride's TokenSet has no colour-scheme axis yet, so dark counterparts ship as `dark.*` colour tokens.

## Fonts

- **Inter Tight** and **Inter** by Rasmus Andersson: SIL Open Font License 1.1.

The `.woff2` Latin subsets come from the Fontsource distribution. Token stacks fall back to Helvetica Neue / Arial / system-ui until the installer registers the font files.

## Photos

All seven photographs in `assets/images/` were generated for this theme with Magnific AI image generation. They depict no real people, brands or places and ship with the theme for use on sites built with it.
