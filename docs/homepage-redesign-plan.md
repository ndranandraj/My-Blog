# Homepage redesign + full rebrand plan

Source design: `Anand - Homepage.dc.html` (the chosen direction) plus `Homepage Directions.dc.html` (eight alternates), both downloaded to the repo root inside `Website blog design improvement.zip`.

Decision (June 17 2026): **full rebrand** (new type system + accent + glass styling across the whole site, not just the homepage). Status: plan only, no templates touched yet.

## What the design is

A standalone React/inline-styled prototype, not Hugo. None of its code transfers directly. The job is to translate its look into the existing Hugo + PaperMod templates and `assets/css/extended/custom.css`. Structurally the homepage already matches: `layouts/partials/index_profile.html` already renders a hero, a featured block, "Latest writing", and "Browse by topic", all wired to real data. So this is a reskin plus one new section, not a from-scratch build.

## Design tokens to adopt

| Token | Current | New (from design) |
|---|---|---|
| Display font | Merriweather | Instrument Serif (modern) or Newsreader (editorial) |
| Body font | Inter | Hanken Grotesk |
| Mono/label font | (none) | IBM Plex Mono |
| Accent (light) | `#B45309` amber | `#5b5bd6` indigo |
| Accent (dark) | `#F59E0B` | `#9a8bff` |
| Surfaces | solid cards | glass: translucent fill + `backdrop-filter: blur` |
| Background | flat | colored blob wash (indigo / pink / teal, blurred) |

The design also exposes a font-pairing switch (modern / editorial / grotesk) and four accent swatches. Pick one of each before building; do not ship the switcher.

## Work breakdown

### 1. Global token swap (site-wide, do first)
- Add the three Google Fonts to `layouts/partials/extend_head.html` (replace the Inter + Merriweather load). Keep the weight list minimal for performance.
- Update the accent tokens in the "DESIGN PASS" block of `custom.css` from amber to indigo, both light and dark. This automatically recolors links, section ticks, eyebrows, active menu item, and the reading-progress bar (already token-driven per CLAUDE.md).
- Map the design's `--bg / --ink / --muted / --glass / --strong / --line / --soft` variables onto the existing PaperMod `data-theme` system. Do NOT add the design's separate theme toggle; reuse PaperMod's.

### 2. Hero (rework `index_profile.html`)
- Change from centered profile to a two-column grid: text left (mono eyebrow "Writing · Data · Photography", big serif "Hi, I'm Anand.", subtitle, two buttons, social row), portrait card right with the floating "NOW" badge.
- Reuse the existing avatar/image pipeline; just restyle. Pull the "NOW" line from a new `[params]` value so it's editable without code.

### 3. Dashboards & tools bento (NEW section, biggest piece)
- New partial, e.g. `layouts/partials/custom/home_dashboards.html`, rendered from the home template.
- Three cards: featured Explorer (with the CSS bar-chart motif), "All 234 seats" results (dot-grid motif), "The dataset" (CSV-preview motif). Link to the existing Explorer, results hub, and dataset.
- Drive content from `[params]` or a data file so it is not hard-coded.

### 4. Latest writing (restructure)
- From the current 4-card grid to: one lead card (cover + category + headline + dek + meta) plus three compact list rows (category / title+dek / date·readtime). Same `site.RegularPages` query, new markup + CSS.

### 5. Topics + newsletter + footer (restyle)
- Topics: 4 glass cards with inline post counts (data already computed).
- Newsletter: full-width indigo panel around the existing Buttondown CTA.
- Footer: already a 3-column `extend_footer.html`; restyle to match.

### 6. Carry rebrand to the rest of the site
- Article pages (`single.html`), shortcodes (kpi / callout / pullquote / dashboard-cta), and the two dashboard pages all read the same tokens. Verify each in light and dark after the token swap; adjust any hard-coded colors.
- Glass treatment is optional on article bodies; keep reading surfaces high-contrast for legibility.

## Risks and gotchas

- **Lighthouse gate.** CI runs Lighthouse on deploy. Heavy `backdrop-filter` blur and large blurred blobs can hurt performance/paint, especially mobile. Limit the number of blur layers, cap blob size, and test the score before merging.
- **Accent ripple.** Changing the accent token recolors the whole site by design. Sanity-check the dashboards and shortcodes, not just the homepage.
- **Dark mode.** Every new surface needs both light and dark values. The design already provides both; wire them to `html[data-theme]`.
- **Dashboard mirror.** If any restyle touches `static/election-dashboard/*`, mirror it back to the sibling Election-Analysis repo or the next mirror overwrites it (per CLAUDE.md).
- **No em dashes** anywhere in copy (author preference).

## Rough effort

- Token swap + hero: half a day.
- Dashboards bento: half a day (new section).
- Latest/topics/newsletter/footer restyle: half a day.
- Carrying rebrand across article pages + shortcodes + dashboards and QA in both themes: half to a full day.

Total: roughly 1.5 to 2 focused days for a faithful full rebrand.

## Suggested order

1. Branch off `main`.
2. Global tokens (fonts + accent + theme variable mapping). Commit, eyeball the whole site.
3. Homepage: hero, then dashboards bento, then latest/topics/newsletter/footer.
4. Sweep article pages + shortcodes + dashboards for color/contrast regressions.
5. Local Lighthouse check, fix performance hits.
6. PR preview, then merge to deploy.
