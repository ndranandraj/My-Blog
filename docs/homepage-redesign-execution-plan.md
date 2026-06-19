# Homepage redesign: detailed execution + rollback plan

Companion to `docs/homepage-redesign-plan.md` (the scope/effort overview). This file is the step-by-step build order, verification gates, and a layered rollback plan.

Design source (latest stored): `Anand - Homepage.dc.html`, extracted from `Website blog design improvement.zip` (repo root, June 18 2026). No newer design file has landed since. If a newer direction is exported, re-extract and re-check the token table in the overview doc before following this.

Repo state at planning time: branch `main`, clean tree, last commit `d30ce3f`. Remote `origin` = github.com/ndranandraj/My-Blog. Deploys auto-fire on push to `main` via `.github/workflows/deploy.yml`; `pr-preview.yml` builds PR previews; Lighthouse CI runs as a post-deploy gate; Cloudflare proxy is ON (edge cache up to ~10 min).

---

## Phase 0: Safety net (do before touching any file)

1. **Tag the known-good baseline** so there is always a one-command return point:
   ```bash
   cd ~/Documents/Claude-Projects/Blog/anand-blog
   git tag pre-redesign-2026-06 && git push origin pre-redesign-2026-06
   ```
2. **Work on a branch, never on main:**
   ```bash
   git checkout -b redesign-homepage
   ```
3. **Snapshot the exact files this project will edit** into a gitignored backup, as a belt-and-suspenders copy independent of git:
   ```bash
   mkdir -p .redesign-backup
   cp assets/css/extended/custom.css .redesign-backup/
   cp layouts/partials/index_profile.html .redesign-backup/
   cp layouts/partials/extend_head.html .redesign-backup/
   cp layouts/_default/single.html .redesign-backup/
   cp hugo.toml .redesign-backup/
   echo ".redesign-backup/" >> .gitignore
   ```
4. **Confirm the local toolchain matches CI:** `hugo version` should report `0.153.0` (extended). Drift has caused render differences before.

Exit gate: `git status` shows the new branch, baseline tag pushed, backup folder present and gitignored.

---

## Phase 1: Global design tokens (site-wide)

Files: `layouts/partials/extend_head.html`, `assets/css/extended/custom.css`.

1. Swap the Google Fonts load in `extend_head.html` from Inter + Merriweather to Instrument Serif (or Newsreader) + Hanken Grotesk + IBM Plex Mono. Keep weights minimal.
2. In the "DESIGN PASS" block of `custom.css`, change accent tokens amber to indigo: light `#B45309` to `#5b5bd6`, dark `#F59E0B` to `#9a8bff`.
3. Add the design's surface variables (`--glass`, `--strong`, `--line`, `--soft`, `--blobop`, `--onaccent`) into the existing `html[data-theme="light"]` / `html[data-theme="dark"]` blocks. Map, do not duplicate, the theme system. Do NOT import the design's own theme toggle; PaperMod's stays.

Verify: `hugo server -D`, load the site, toggle light/dark. Links, reading-progress bar, eyebrows, active menu item should be indigo. Body text should be Hanken Grotesk, H1s the serif. Check an article page and a dashboard page too, since these tokens are global.

Commit as its own step: `git commit -am "Redesign 1/6: global tokens (fonts + indigo accent + glass vars)"`. Committing each phase separately is what makes phase-level rollback possible later.

---

## Phase 2: Hero

File: `layouts/partials/index_profile.html`.

Rework the centered profile into the two-column grid: left = mono eyebrow, big serif "Hi, I'm Anand.", subtitle, two buttons, social row; right = portrait card with the floating "NOW" badge. Reuse the existing avatar image pipeline. Add a `[params.now]` value in `hugo.toml` for the badge text so it is editable without code.

Verify: hero matches the mockup at desktop and collapses sanely on mobile (stack to one column). Commit: `Redesign 2/6: two-column hero`.

---

## Phase 3: Dashboards & tools bento (new section)

New file: `layouts/partials/custom/home_dashboards.html`, rendered from the home template; CSS in `custom.css`.

Three glass cards: featured Explorer (CSS bar-chart motif), "All 234 seats" results (dot-grid motif), "The dataset" (CSV-preview motif). Links to the existing Explorer, results hub, dataset. Drive copy from `[params]` or a `data/` file, not hard-coded.

Verify: three cards render, links resolve, motifs theme correctly in dark. Commit: `Redesign 3/6: dashboards bento`.

---

## Phase 4: Latest writing restructure

File: `index_profile.html`.

Change the 4-card grid to one lead card plus three compact list rows. Same `site.RegularPages` query. Commit: `Redesign 4/6: latest-writing lead + rows`.

---

## Phase 5: Topics, newsletter, footer

Files: `index_profile.html`, `extend_footer.html`, `custom.css`.

Topics to 4 glass cards with inline counts; newsletter to the full-width indigo panel around the existing Buttondown CTA; footer restyle to match. Commit: `Redesign 5/6: topics, newsletter, footer`.

---

## Phase 6: Carry rebrand across the rest of the site

Files: `single.html`, shortcodes (`kpi`, `callout`, `pullquote`, `dashboard-cta`), and `static/election-dashboard/*`.

Sweep for hard-coded colors that did not pick up the new tokens. Check every shortcode in light and dark. If any dashboard file changes, **mirror the change back to the sibling Election-Analysis repo** or the next mirror overwrites it (per CLAUDE.md). Commit: `Redesign 6/6: rebrand article pages, shortcodes, dashboards`.

---

## Verification gate before merge

1. Production-parity build: `HUGO_ENVIRONMENT=production hugo --gc --minify --logLevel warn`, then `python3 -m http.server --directory public 8080` and click through home, an article, a per-seat page, both dashboards, in light AND dark.
2. **Local Lighthouse** on the homepage (mobile profile). The blob wash + `backdrop-filter` blur are the performance risk. If performance drops below the CI threshold, reduce blur radius, cut the number of blob layers, or drop `backdrop-filter` on below-the-fold cards. Do this before pushing, because Lighthouse is a deploy gate.
3. Push the branch and let `pr-preview.yml` build a preview. Review the live preview URL before merging anything to `main`.

---

## Rollback plan (layered, least to most drastic)

**Level 1: mid-edit, uncommitted.** Revert a single file to its last commit:
```bash
git restore assets/css/extended/custom.css
```
Or discard everything uncommitted on the branch: `git restore .`. The `.redesign-backup/` copies are an independent fallback if git state is confusing.

**Level 2: undo one phase.** Because each phase is its own commit, revert just that phase without losing the others:
```bash
git revert <phase-commit-sha>
```

**Level 3: abandon the whole effort before merge (cleanest).** Nothing reached `main`, so just leave the branch unmerged or delete it:
```bash
git checkout main && git branch -D redesign-homepage
```
Production is untouched.

**Level 4: it merged and production looks wrong.** Do NOT force-push main. Revert the merge and let CI redeploy the previous look:
```bash
git checkout main
git revert -m 1 <merge-commit-sha>   # or: git revert <range of phase commits>
git push origin main                  # auto-deploys the revert
```
Then **purge Cloudflare cache** (Cloudflare to Caching to Purge Everything) and hard-refresh, because the proxy holds edge cache up to ~10 min and a "still broken" page is often just cache.

**Level 5: nuclear, return main to the tagged baseline.** Only if a revert is somehow tangled:
```bash
git checkout main
git reset --hard pre-redesign-2026-06
git push --force-with-lease origin main
```
Force-push rewrites history; prefer Level 4. After this, purge Cloudflare cache.

**Cross-repo note:** if Phase 6 touched dashboards and you rolled back here but already pushed the mirror to Election-Analysis, revert it there too so the two repos stay in sync.

---

## Known gotchas to respect (from CLAUDE.md)

- **Sandbox git lock.** Run git from a normal terminal, not an agent sandbox. If you hit "Unable to create '.git/index.lock'", run `sudo rm -f .git/index.lock` from the repo root and retry.
- **Dashboard mirror is a file copy, not a symlink.** Any `static/election-dashboard/*` edit must be copied back to the sibling repo.
- **CSP / security headers** live in a Cloudflare rule, mirrored in `static/_headers`. New font origins (fonts.googleapis.com, fonts.gstatic.com) are already allowed; if you add any new CDN, update both places or it gets blocked.
- **No em dashes** in any copy (author preference).
- **IndexNow after deploy:** `./scripts/indexnow-submit.sh https://ndranandraj.com/` once the redesign is live.

---

## One-glance summary

Tag baseline, branch, snapshot files. Build in 6 committed phases (tokens, hero, bento, latest, topics/newsletter/footer, site-wide sweep). Gate on a production build + local Lighthouse + PR preview before merge. Roll back at whatever level fits: restore a file, revert a phase, delete the branch, revert the merge, or reset to the `pre-redesign-2026-06` tag, and purge Cloudflare cache whenever the change already reached production.
