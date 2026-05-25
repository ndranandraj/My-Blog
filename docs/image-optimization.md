# Image optimization: how it works, and the WebP follow-up

Internal note. Not gitignored, so it ships unless you add it to `.gitignore`.

## What the build does today

Every published raster image lives in two places:

- `static/images/<file>` — the verbatim copy. It keeps the stable public URL
  (`/images/<file>`), which is what the OpenGraph and JSON-LD tags point at, and
  it is the safe fallback.
- `assets/images/<file>` — the processing master. Hugo Pipes can only resize
  files under `assets/`, never under `static/`.

Three template entry points route an absolute `/images/...` reference through
one shared partial, `layouts/partials/responsive-image.html`:

- `layouts/_default/_markup/render-image.html` — markdown `![alt](/images/...)`
- `layouts/shortcodes/figure.html` — the `{{< figure >}}` shortcode
- `layouts/partials/cover.html` — the post cover (overrides PaperMod's), with
  `loading="eager" fetchpriority="high"` because the cover is the LCP element

The partial resolves the `assets/images/` master, emits a resized `srcset`
(480 / 720 / 1080 / 1500w, capped at 1500), and sets explicit `width`/`height`
so there is no layout shift. It is safe-by-fallback: SVGs, external URLs, missing
masters, or undecodable files (a `try` probe catches the WebP-saved-as-`.jpg`
case) all fall back to a plain `<img>` at the original `/images/...` URL.

The big win here is **right-sizing**, not format: a phone pulls the 480w variant
(~30-60 KB) instead of the full 1920px master (300-700 KB).

## Why there is no build-time WebP

We tried generating WebP at build time. It works locally (Hugo 0.160 on macOS)
but **OOMs the GitHub Actions runner** (Hugo 0.153 extended, linux/amd64):

```
WebPEncode failed: 1 (OUT_OF_MEMORY: Out of memory allocating objects)
... Error encoding NRGBA to WebP
```

It failed even on modest ~2.8 MP images (1920x1440), so it is a memory-fragility
issue in that Hugo build's bundled libwebp under parallel encodes, not a
raw-size problem. Capping dimensions or tuning `GOMAXPROCS` are guesses that
cannot be verified without burning CI runs, so build-time WebP was removed. The
trade-off is documented in the header comment of `responsive-image.html`.

## The follow-up: WebP/AVIF at the Cloudflare edge

The clean place to get WebP (and AVIF) is the CDN, since the domain already
proxies through Cloudflare. The edge converts the origin JPEG/PNG to the best
format the requesting browser advertises in its `Accept` header, with zero build
cost and no CI risk. Two options:

### Option A — Polish (simplest, needs Pro plan)

Cloudflare dashboard path: **your domain → Speed → Optimization → Image
Optimization → Polish**.

- Set Polish to **Lossy** (or Lossless if you want zero quality change).
- Tick **WebP** (Polish serves WebP/AVIF to browsers that accept it, and the
  original to those that do not).

That is the whole setup. Nothing in the repo changes. Verify afterwards:

```bash
# Should return content-type: image/webp when Accept allows it
curl -sI -H 'Accept: image/avif,image/webp,image/*' https://ndranandraj.com/images/mojave-sign.jpg | grep -iE 'content-type|cf-polished'
```

`cf-polished:` in the response headers confirms Polish acted on the image.

### Option B — Image Resizing / transform URLs (free-tier capable, more work)

If you are not on Pro, Cloudflare Image Resizing can convert via `format=auto`,
but it requires either rewriting image URLs to the `/cdn-cgi/image/...` form or
adding a transform rule, and it is a metered feature. Polish is the lower-effort
path if the plan allows it; otherwise revisit build-time WebP with a serialized
image step once Hugo's encoder is less fragile.

## Open cleanup item: de-duplicate the rasters

`assets/images/` currently duplicates the `static/images/` rasters (~11 MB) so
the fallback stays intact. Once you are happy with the pipeline, the `static/`
copies of images that are referenced **only** as inline images (not as a cover
or OG URL) can be removed to reclaim that space. Classify before deleting:

- Keep in `static/` (used as a literal URL by OG/JSON-LD/cover front matter):
  anything named `*-cover.*`, `og-default.png`, and the profile/avatar
  (`Anand_enhanced.jpg`).
- Candidate for `static/` removal (inline-only, served via the partial from
  `assets/`): the Mojave photo set, `spelling-bee-daughter.jpg`, and similar
  in-body images.

This is optional and purely about repo/deploy size; correctness does not depend
on it.
