# Security headers: where they actually come from

Internal note. Not published (the whole `docs/` tree is unmounted from Hugo).

## The problem

`static/_headers` uses the **Cloudflare Pages** `_headers` syntax. But this site
does not deploy to Cloudflare Pages. It deploys to **GitHub Pages** (see
`.github/workflows/deploy.yml`), with Cloudflare sitting in front only as a
**proxy/CDN** for the custom domain.

Two consequences:

1. GitHub Pages does not read `_headers` at all. It serves the file verbatim as
   a static asset at `/_headers` and ignores its contents.
2. Cloudflare's reverse proxy does **not** apply Cloudflare Pages `_headers`
   rules either. That feature only runs when Cloudflare is the host (Pages), not
   when it is proxying an external origin like GitHub Pages.

So unless something else is setting them, the site's security headers
(`X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`,
`Permissions-Policy`, and now CSP + HSTS) may not be reaching browsers in
production at all. The `_headers` file is correct and worth keeping (it is the
source of truth, and it would take effect immediately if hosting ever moves to
Cloudflare Pages), but it is probably not what is live today.

## Step 1: verify what is actually served

From any normal terminal (not the sandbox):

```bash
curl -sI https://ndranandraj.com/ | grep -iE 'content-security|strict-transport|x-frame|x-content-type|referrer-policy|permissions-policy|server'
```

Read the result:

- If the headers are **present**, something is already applying them (a
  Cloudflare rule someone set up earlier, or a Worker). Confirm the values match
  the set below and you are done.
- If they are **absent**, GitHub Pages is serving raw and you need Step 2.
- The `server:` line tells you the path: `GitHub.com` means the origin is
  reaching the browser without Cloudflare header injection; `cloudflare` on its
  own does not guarantee the security headers are set, so still check each one.

## Step 2: apply the headers in Cloudflare (recommended)

Since Cloudflare already proxies the domain (the Web Analytics beacon confirms
it), add a **Response Header Transform Rule**. This is the lowest-effort fix and
keeps the headers in one place.

Dashboard path: **Cloudflare → your domain → Rules → Transform Rules →
Modify Response Header → Create rule**.

- Rule name: `Security headers`
- When incoming requests match: `Hostname equals ndranandraj.com` (or "All
  incoming requests")
- Then, **Set static** header for each of the following:

| Header | Value |
|---|---|
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `Content-Security-Policy` | (the single-line value from `static/_headers`) |

Keep these values byte-for-byte in sync with `static/_headers` so the repo stays
the documented source of truth even though Cloudflare is what enforces them.

HSTS note: `includeSubDomains` commits every subdomain of ndranandraj.com to
HTTPS for a year. That is fine today (root domain only). Do **not** add
`preload` until you are certain every current and future subdomain will always
serve valid HTTPS, because `preload` is hard to undo. Consider starting with a
short `max-age` (e.g. `300`) for a day to confirm nothing breaks, then raising it
to `31536000`.

## The CSP, explained

The policy in `static/_headers` is pragmatic, not maximal. It still has
`'unsafe-inline'` on `script-src` and `style-src`, which is required because the
site relies on inline scripts and styles in several places that cannot be moved
without a refactor:

- `layouts/partials/extend_head.html`: inline `<script>` blocks (reading
  progress bar, sticky-TOC observer, outbound-click tracking) and the inline
  `onload="this.media='all'"` on the font stylesheet.
- `layouts/partials/custom/post_cta.html`: inline `onsubmit=` handler on the
  Buttondown form.
- `static/election-dashboard/tn-2026-explorer.html`: a large inline `<script>`
  plus many inline `style="…"` attributes.

External origins the policy allows, and why:

- `script-src` / `img-src` / `connect-src` for `www.googletagmanager.com` +
  `*.google-analytics.com` + `region1.google-analytics.com`: GA4.
- `static.cloudflareinsights.com` + `cloudflareinsights.com`: Cloudflare Web
  Analytics beacon.
- `unpkg.com`: Leaflet JS + CSS on the dashboard.
- `*.basemaps.cartocdn.com` (`img-src`): Leaflet dark map tiles.
- `fonts.googleapis.com` (`style-src`) + `fonts.gstatic.com` (`font-src`):
  Google Fonts.
- `form-action https://buttondown.com`: the newsletter form POST target.

### Hardening path (optional, later)

To drop `'unsafe-inline'` from `script-src` you would either (a) move every
inline script into a hashed/nonced external file, or (b) emit a per-request
nonce. GitHub Pages cannot generate per-request nonces (it is fully static), so
the realistic route is **hashes**: compute the SHA-256 of each inline script
block and list them as `'sha256-…'` in `script-src`. That is brittle (every edit
to an inline script changes its hash) and is probably not worth it for a static
personal blog with no authenticated surface. Document it here as a known
trade-off rather than a TODO.

## Why this is a "prepare + hand off" item

I cannot finish this one autonomously: verifying the live headers needs network
access to ndranandraj.com (blocked in this environment), and applying the
Cloudflare rule needs access to your Cloudflare dashboard. The repo side is done
(`_headers` updated, deprecated `X-XSS-Protection` removed, HSTS + CSP added).
The remaining work is Steps 1 and 2 above.
