# smithtronic.com

The SMITHTRONIC website — plain static HTML, hosted free on GitHub Pages.

## License — read this before reusing anything

This repository is public because GitHub Pages requires it, **not** because its
contents are free to reuse. All site content — page copy, photos, the
SMITHTRONIC name and logo, and the site design — is
**© 2024–2026 Smithtronic, all rights reserved**, and is not licensed for
republication or rehosting. Viewing and forking on GitHub (per GitHub's Terms
of Service) does not grant any right to reproduce this site elsewhere.

The **open-source hardware designs** are a different story on purpose: the fog
light kit and vented headlight caps live in the
[`smithtronic`](https://github.com/rodu4835/smithtronic) repo under
**CC BY-NC-SA 4.0** — those you're invited to print, remix, and share with
attribution, non-commercially.

Rebuilt from the original Framer site in August 2026 so the domain could stay
while the Framer subscription went away. No build step, no framework, no
dependencies: what's in this repo is exactly what the browser gets.

## Editing

Every page is a standalone `.html` file. Open it, change the text, commit, push —
GitHub Pages redeploys within a minute or two.

- `index.html` — home
- `shop/` — product pages (`auxlightkit/`, `diylightkit/`, `headlightcaps/`) and
  the install guides beneath them
- `projects/` — index, the four category pages, and one folder per project post
- `reviews/`, `clients/`, `contact/`, `privacy-policy/`, `terms-of-service/`
- `assets/site.css` — the entire design system (colors, cards, buttons, layout)
- `assets/img/` — images, grouped by section
- `assets/fonts/` — Audiowide, Inter, Fragment Mono, self-hosted (no external calls)

### House rules

- **URL paths are load-bearing.** The install guide paths
  (`/shop/auxlightkit/installguide/`, `/shop/diylightkit/diyinstallguide/`) are
  printed as QR codes on cards shipped with every kit. Never rename those folders.
- Internal links end with a trailing slash (`../reviews/`, not `../reviews`).
- Colors live in `:root` at the top of `site.css` — change them there, not per page.

## Design tokens

| Token | Value |
|---|---|
| Cyan (brand) | `#01D0FE` |
| Cyan (hover/deep) | `#0099FF` |
| Ink (dark cards) | `#1A1A1A` |
| Display font | Audiowide |
| Body font | Inter |

## Hosting

GitHub Pages serves the `master` branch from the repository root. The custom
domain is configured by the `CNAME` file plus DNS records at the domain
registrar. Cost: the domain renewal only — hosting is free.

## Content provenance

Page copy, images, and structure were recovered from the original Framer site
(archived page-by-page before the subscription lapsed) and reproduced verbatim.
Product "Buy Now" buttons now point to the open-source files instead of the
retired Stripe checkout.
