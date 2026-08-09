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
- `software/` — section index plus one folder per tool (`openmbb/`)
- `designs/` — the 3D-printed parts: `foglightkit/` (with `installguide/` and
  `diyinstallguide/` beneath it), `headlightcaps/`, `glovebox/`
- `projects/` — index, the four category pages, and one folder per project post
- `about/`, `reviews/`, `contact/`, `privacy-policy/`, `terms-of-service/`
- `shop/`, `clients/`, `projects/openmbb-…/` — meta-refresh redirect stubs left
  behind by renames; `noindex` + canonical, not real pages
- `assets/site.css` — the entire design system (colors, cards, buttons, layout)
- `assets/img/` — images, grouped by section
- `assets/fonts/` — Audiowide, Inter, Fragment Mono, self-hosted (no external calls)
- `tools/cachebust.py` — stamps stylesheet URLs with a content hash

### House rules

- **Run `python tools/cachebust.py` after any `assets/*.css` edit, before you
  commit.** Pages serves CSS with `max-age=600`, so shipping new markup against
  an unchanged stylesheet URL means anyone with a warm cache gets the new HTML
  rendered by the old CSS for up to ten minutes. This happened once and the home
  page looked broken. The hash in `site.css?v=…` makes the pair atomic.
- **Two install guide URLs are load-bearing in the physical world.**
  `/shop/auxlightkit/installguide/` and `/shop/diylightkit/diyinstallguide/`
  were printed as QR codes on cards shipped with kits. Those cards can't be
  reissued. The guides now live under `/designs/foglightkit/`, and the old paths
  are redirect stubs — **keep the stubs**, and never delete `shop/`.
- **Moving a page means leaving a redirect stub** at the old path — meta-refresh,
  `<meta name="robots" content="noindex">`, and a `<link rel="canonical">` to the
  new URL. External links (Thingiverse, GitHub, forums) point at the old paths.
- **No `<form>` without a real endpoint.** The contact and review forms used to
  POST to a `mailto:` URL, which browsers handle inconsistently and often deliver
  empty. Use a plain `mailto:` link with a prefilled `subject`/`body` instead.
- Section indexes use `.list-cards` — one full-width row per item. The old
  `.grid`/`.card` layout is gone; don't reintroduce it for a new section.
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
