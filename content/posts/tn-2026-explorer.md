---
title: "TN 2026 Explorer: Every Seat, Every Party, Every Region in One Dashboard"
date: 2026-05-17
lastmod: 2026-05-17
description: "An interactive dashboard for Tamil Nadu's 2026 Assembly election. 234 constituencies, 12 parties with seats, 4.93 crore votes polled. Map, party efficiency, regional anatomy, 2021 to 2026 swing, demographics, defeated incumbents, dummy near-misses, all in one page."
summary: "The TN 2026 Explorer is the new canonical home for the 2026 election data on this site. Seven sections, one page. An interactive 234-seat map, party seat-vs-vote efficiency, a 9-region cross-party anatomy, the 2021 to 2026 swing for every seat, demographics of all 234 winners, the 196 incumbents who didn't return, and the 25 closest dummy near-misses. Companion to the five-post series."
keywords: ["TN 2026 dashboard", "Tamil Nadu 2026 Assembly election interactive", "TN 2026 results map", "TVK 108 seats dashboard", "DMK collapse dashboard", "Tamil Nadu constituency map 2026", "TN 2026 party efficiency", "Tamil Nadu Assembly 2026 demographics", "TN 2026 swing analysis"]
tags: ["elections", "tamil-nadu", "data", "politics", "2026", "results", "dashboard", "tvk", "dmk"]
categories: ["Data"]
featured: true
readingTime: true
showToc: false
image: "/images/tn-2026-explorer-cover.png"
cover:
  image: "/images/tn-2026-explorer-cover.png"
  alt: "TN 2026 Explorer: every seat, every party, every region in one dashboard."
  caption: "Interactive dashboard for Tamil Nadu's 2026 Assembly election."
  relative: false
---

Tamil Nadu's 2026 Assembly election was the largest single-cycle electoral reset the state has produced in modern times. **164 of 234 seats flipped party**. A debutant won **108 of them**. The sitting Chief Minister lost his own seat by 8,795 votes. To put all of that into a single navigable view that anyone can pull on, I built the TN 2026 Explorer.

{{< dashboard-cta
    url="/election-dashboard/tn-2026-explorer.html"
    eyebrow="Live · interactive · 234 seats"
    title="Open the TN 2026 Explorer"
    body="Seven sections in one page. Map, party efficiency, regional anatomy, 2021 → 2026 swing, demographics, defeated incumbents, dummy near-misses. Hover any seat for the candidate, party, vote total, and margin. Sort any table. Filter by region, alliance, or party."
    cta="Open the dashboard"
    accent="primary"
>}}

## What's inside

Seven sections in one page. An **interactive map** of every constituency, colored by winner with hover tooltips for candidate, votes, and margin. **Party efficiency** ranks all 12 parties with seats by seat-share over vote-share ratio. **Regional anatomy** breaks the state into nine political-geography regions for every major party. **2021 to 2026 swing** lists all 234 seats side by side, sortable. **Demographics** profiles the 234 winners by age, education, gender, and assets. **Defeated incumbents** is the sortable list of the 196 sitting MLAs who didn't return. **Dummy near-misses** ranks the 25 closest races where flagged spoilers exceeded the margin of loss.

## Four findings that anchor the data

- **TVK polled 34.9% of the vote and won 46.2% of the seats.** Efficiency ratio 1.32, the highest of any major party. AIADMK's 21.2% delivered 47 seats (0.95). BJP's 2.97% delivered just one (0.14). NTK's 4.0% delivered zero.
- **DMK collapsed from 133 seats to 59.** The fall was not uniform. Chennai &amp; Suburbs alone dropped from 31 of 37 wins in 2021 to 2 of 37. Their three strongest 2021 regions (Chennai, Central, North) each lost 17 to 19 percentage points of vote share.
- **Only 38 incumbents held their seat. 56 defended and lost.** 37 of those defeats came directly at TVK's hands. M.K. Stalin lost Kolathur to a 75-year-old debutant.
- **The new assembly is 12 years younger than the outgoing one.** Median MLA age fell from 64 to 52. 41 MLAs are under 40, 35 of those from TVK. 22 women elected, 13 from TVK alone, zero from DMK.

## Read the five-post series

The dashboard is the data spine. The narrative analyses live in the five posts of the TN 2026 series.

<div class="explore-grid">
<a href="/posts/tvk-debut-2026/">
  <strong>TVK 233: A Debut, Mapped</strong>
  <span>108 seats, 1.32 efficiency, the regional and position anatomy.</span>
</a>
<a href="/posts/dmk-collapse-2026/">
  <strong>How DMK Lost Tamil Nadu, Region by Region</strong>
  <span>From 133 seats to 59. Chennai 31→2. 65 seats lost directly to TVK.</span>
</a>
<a href="/posts/tn-2026-incumbents-defeated/">
  <strong>The Chief Minister lost his seat</strong>
  <span>M.K. Stalin defeated in Kolathur by 8,795 votes. 56 sitting MLAs defeated.</span>
</a>
<a href="/posts/tn-2026-new-assembly-profile/">
  <strong>The youngest assembly TN has elected</strong>
  <span>Median MLA age fell 12 years. 41 under 40. 22 women. The generational reset.</span>
</a>
<a href="/posts/tn-2026-dummy-candidates-results/">
  <strong>Did the 329 dummies matter?</strong>
  <span>Strict test: 0 consequential. Loose test: 2, both razor-thin TVK losses.</span>
</a>
</div>

The Explorer is built on the same authoritative ECI tally that drives the five posts, plus a per-AC sidecar built fresh from the raw CSV. All numbers reconcile. Use the filters, sort the tables, and feel free to deep-link straight into any section.

{{< callout title="What this is, and isn't" type="method" >}}
The Explorer is a presentation layer over data that has been published openly. Sources: the official ECI 2026 tally (`tn_2026_results.csv`), the 4,023-row candidate dataset already released at [/data/tn-2026-candidates/](/data/tn-2026-candidates/), and the cross-year `winner_history` block in the project's `data.json`. Code and data are open. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
{{< /callout >}}
