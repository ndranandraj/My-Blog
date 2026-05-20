---
title: "Tamil Nadu 2026 Assembly Election: The Complete Analysis"
date: 2026-05-18
lastmod: 2026-05-18
description: "The complete data analysis of Tamil Nadu's 2026 Assembly Election. TVK won 108 of 234 seats with 34.9% of the vote. DMK collapsed from 133 to 59. M.K. Stalin lost Kolathur. The interactive dashboard, the five-post series, the dataset, and the methodology, all in one place."
summary: "Five investigations, one interactive dashboard, and the open dataset behind them. Everything published on this site about Tamil Nadu's 2026 Assembly Election, organised."
keywords: ["Tamil Nadu 2026 election analysis", "TN 2026 results", "TVK 108 seats", "DMK collapse 2026", "MK Stalin Kolathur defeat", "Tamil Nadu Assembly election data", "TN 2026 interactive dashboard", "Vijay TVK debut", "Tamil Nadu election dataset", "TN 2026 incumbents defeated", "Tamil Nadu youngest assembly", "TN 2026 dummy candidates"]
tags: ["elections", "tamil-nadu", "data", "politics", "tvk", "dmk", "2026", "results", "pillar"]
categories: ["Data"]
pillar: true
readingTime: true
showToc: true
TocOpen: false
weight: 1
image: "/images/tn-2026-explorer-cover.png"
cover:
  image: "/images/tn-2026-explorer-cover.png"
  alt: "Tamil Nadu 2026 Assembly Election analysis: TVK 108 seats, DMK 59, interactive dashboard and five-post series."
  caption: "Tamil Nadu's 2026 Assembly Election, mapped end to end."
  relative: false
sitemap:
  priority: 0.9
  changefreq: monthly
---

Tamil Nadu's 2026 Assembly Election was the largest single-cycle electoral reset the state has produced in modern times. **164 of 234 seats flipped party.** A first-time party won **108 of them**. The sitting Chief Minister lost his own seat by 8,795 votes. The new Assembly's median MLA age fell by twelve years.

This page is the canonical hub for everything published on this site about that election. One interactive dashboard. Five investigations. The open dataset behind all of it. Plus the pre-poll work that shaped what to look for once the results came in.

If you arrived here from search, social, or a citation, start with the dashboard. If you arrived here from one of the individual posts, the other four investigations linked below cover the angles that piece did not.

{{< dashboard-cta
    url="/election-dashboard/tn-2026-explorer.html"
    eyebrow="Interactive · 234 seats · 12 parties · 4.93 crore votes"
    title="Open the TN 2026 Explorer"
    body="Seven sections in one page. Constituency map, party seat-vs-vote efficiency, 9-region cross-party anatomy, 2021 to 2026 swing per seat, demographics of all 234 winners, defeated incumbents, dummy near-misses. Hover any seat, sort any table, filter any view."
    cta="Open the dashboard"
    accent="primary"
>}}

## The findings, in five investigations

Each card targets a distinct angle of the same election: its headline number and the one finding it turns on. They cross-link tightly, and the full posts carry the regional and demographic anatomy behind each figure.

<div class="hub-grid">
<a class="hub-card" href="/posts/tvk-debut-2026/">
<span class="hub-card-cover" style="background-image:url('/images/tvk-debut-cover.png');"></span>
<span class="hub-card-body">
<span class="hub-card-stat"><b>108</b><i>of 233 seats won</i></span>
<span class="hub-card-title">TVK 233: A Debut, Mapped</span>
<span class="hub-card-take">A tsunami in Chennai, a ripple in the Cauvery delta. The debut wave mapped to exactly where it broke, at a 1.32 seat-to-vote efficiency.</span>
<span class="hub-card-cta">Read the analysis →</span>
</span>
</a>
<a class="hub-card" href="/posts/dmk-collapse-2026/">
<span class="hub-card-cover" style="background-image:url('/images/dmk-collapse-cover.png');"></span>
<span class="hub-card-body">
<span class="hub-card-stat"><b>133 → 59</b><i>seats, in one cycle</i></span>
<span class="hub-card-title">How DMK Lost Tamil Nadu, Region by Region</span>
<span class="hub-card-take">The taller they stood in 2021, the harder they fell (a +0.67 correlation). Chennai dropped from 31 wins to 2.</span>
<span class="hub-card-cta">Read the analysis →</span>
</span>
</a>
<a class="hub-card" href="/posts/tn-2026-incumbents-defeated/">
<span class="hub-card-cover" style="background-image:url('/images/incumbents-defeated-cover.png');"></span>
<span class="hub-card-body">
<span class="hub-card-stat"><b>56 / 234</b><i>incumbents kept their seat</i></span>
<span class="hub-card-title">The Chief Minister Lost His Seat</span>
<span class="hub-card-take">M.K. Stalin lost Kolathur by 8,795 votes. Of the 93 incumbents who fell, 64 went straight to TVK.</span>
<span class="hub-card-cta">Read the analysis →</span>
</span>
</a>
<a class="hub-card" href="/posts/tn-2026-new-assembly-profile/">
<span class="hub-card-cover" style="background-image:url('/images/new-assembly-profile-cover.png');"></span>
<span class="hub-card-body">
<span class="hub-card-stat"><b>52</b><i>median MLA age, down 12 years</i></span>
<span class="hub-card-title">The Youngest, Most-Educated Assembly TN Has Elected</span>
<span class="hub-card-take">41 MLAs under 40 and 22 women elected. A generational reset in a single election.</span>
<span class="hub-card-cta">Read the analysis →</span>
</span>
</a>
<a class="hub-card" href="/posts/tn-2026-dummy-candidates-results/">
<span class="hub-card-cover" style="background-image:url('/images/dummy-candidates-results-cover.png');"></span>
<span class="hub-card-body">
<span class="hub-card-stat"><b>0 / 2</b><i>seats flipped (strict / loose)</i></span>
<span class="hub-card-title">How Many of the 329 Dummies Actually Mattered</span>
<span class="hub-card-take">The mechanism stayed intact, the wave drowned it. Zero consequential seats by the strict test, two by the loose one.</span>
<span class="hub-card-cta">Read the analysis →</span>
</span>
</a>
</div>

## The dataset

The full **4,257-row candidate dataset** plus the **329 flagged name-match pairs** are released under CC-BY-4.0 on GitHub. Free to use, cite, and remix.

Two CSVs. Per-candidate metadata scraped from the Election Commission of India's Affidavit Portal, plus the name-similarity match pairs that drove the dummy-candidates investigation. Sourced cleanly. Schema documented. Reconciled against the published results within 1 to 2 rows on every headline figure.

**[Open the dataset release page →](/data/tn-2026-candidates/)**

Repository: [github.com/ndranandraj/tn-2026-candidates-dataset](https://github.com/ndranandraj/tn-2026-candidates-dataset)

## Methodology, briefly

Three technical pieces hold the analysis together.

A custom **nine-region political geography** for Tamil Nadu (Chennai and Suburbs, North, Central, Cauvery Delta, Krishnagiri Belt, Northeast Coast, Madurai Region, Kongu, Deep South). Standard published groupings stop at five or six regions and obscure the most interesting cross-regional asymmetries. The nine-region cut is what makes the DMK collapse visible as a non-uniform phenomenon rather than a flat statewide drop.

A **three-tier dummy candidate classifier** (EXACT, NEAR_FULL, WORD_MATCH), each tier using a different name-normalisation pass. The strict test (EXACT plus NEAR_FULL only) is what supports any causal claim. The loose test (all tiers) is what catches the noisiest signal.

**Token-based incumbent matching** across 2021 and 2026 ECI filings. Indian politician names drift across cycles (initials swapped, caste suffixes added or dropped, transliteration variants, post-marriage name changes). Exact match misses roughly half the real cases. Token-set fuzzy matching scoped to "same person ran in some constituency in cycle N and again in cycle N+1" recovers the rest. The published incumbents post reconciles within 1 to 2 rows on every headline figure.

A separate methodology post walking through the incumbent-matching algorithm is in the queue. When it ships, it links here.

## Pre-poll companion pieces

Three posts published before the May 4 vote, mostly to set up what to watch for. They read differently from the post-results work because they were written without knowing the answer. All three predictions land partially: TVK did spread its support widely, the dummy mechanism did not bite, and the regional asymmetry in DMK's footprint did predict where the collapse hit hardest.

- **[3 Crore Votes That Elected Nobody](/posts/tn-elections-2026-analysis/)**: The FPTP arithmetic of TN elections, the NTK spoiler effect, and 100 constituencies flagged as 2026 battlegrounds.
- **[Same Name, Different Initial: The Dummy Candidate Factory](/posts/tn-2026-dummy-candidates/)**: The original investigation into 329 suspected dummy pairs filed before the vote.
- **[The Thalapathy Bench](/posts/thalapathy-bench-2026/)**: A short note from the floor of the vote of confidence. Twelve of TVK's 108 MLAs carry "Vijay" somewhere in their name.

## A note on what this analysis is and is not

This is a data-driven account of what happened. It is not a political analysis of why it happened. The structural drivers (anti-incumbency, alliance fatigue, Vijay's brand reach, cadre defections, the AIADMK organisational drift) are layered and seat-specific, and serious causal claims require more than vote tallies.

What the data does support is the regional and demographic anatomy: where the wave concentrated, which incumbents could not survive it, what the new bench looks like, and what the dummy-candidate mechanism did and did not do under wave conditions.

If you use any of this work in your own writing or research, citation back to this site is appreciated. If you find an error, the dataset repository is the right place to file an issue.
