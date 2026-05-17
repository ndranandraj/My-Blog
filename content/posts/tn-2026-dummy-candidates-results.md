---
title: "How Many of the 329 Dummies Actually Mattered"
date: 2026-05-04
lastmod: 2026-05-04
description: "Three weeks ago I flagged 329 suspected dummy candidates in TN 2026. The results are in. In the cleanest test, zero seats flipped. In the noisiest test, two. Here is the full accounting."
summary: "329 suspect pairs flagged before polling. 263 actually contested. 152 targeted majors lost. Consequential seats: 0 by the strict test, 2 by the inclusive test. And why that small number is itself the finding."
keywords: ["dummy candidates Tamil Nadu results", "TN 2026 election dummy candidates follow-up", "dummy candidate impact analysis", "namesake candidates TN 2026 results", "TIRUKKOYILUR election margin", "PALANI election 2026 margin", "Tamil Nadu election spoilers", "EVM voter confusion Tamil Nadu"]
tags: ["elections", "tamil-nadu", "data", "politics", "dummy-candidates", "2026", "results", "investigation"]
categories: ["Data"]
pillar: true
readingTime: true
showToc: true
TocOpen: false
image: "/images/dummy-candidates-results-cover.png"
cover:
  image: "/images/dummy-candidates-results-cover.png"
  alt: "How Many of the 329 Dummies Actually Mattered — TN 2026 post-results analysis"
  caption: "329 flagged pairs. 263 contested. Zero strict-test consequential seats. Two near misses."
  relative: false
---

Three weeks before polling, I published a list of **329 suspect candidate pairs**: major-alliance nominees who shared a name, exactly or near-exactly, with another candidate in the same constituency. Almost always an independent. The thesis was straightforward. At least some of these are deliberate vote-splitters, fielded to confuse voters at the EVM and bleed the major candidate's tally.

Today the votes are in. So: **did it work?**

The honest answer is the kind that does not write its own headline. In the cleanest test, the strategy did not move a single seat. In the noisiest test, two razor-thin TVK losses had enough flagged-namesake votes to plausibly cover the margin. Both can be true at once, and which one you treat as the "real" answer depends on how generously you classify a dummy.

{{< kpi-row >}}
{{< kpi value="329" label="suspect pairs flagged" sub="three weeks before polling" >}}
{{< kpi value="263" label="actually contested" sub="221 distinct major candidates targeted" >}}
{{< kpi value="0" label="strict-test consequential" tone="good" sub="EXACT + NEAR_FULL dummies covered margin" >}}
{{< kpi value="2" label="loose-test consequential" tone="warn" sub="any flagged dummy covered margin (TVK losses)" >}}
{{< /kpi-row >}}

What is unambiguous: this was a wave year, and waves drown small mechanics.

{{< pullquote >}}
The strategy did not fail in 2026. It ran into a year where margins were too wide for it to matter.
{{< /pullquote >}}

{{< dashboard-cta
    url="/election-dashboard/tn-2026-explorer.html#dummies"
    eyebrow="Interactive · 329 flagged pairs"
    title="Open the dummy-candidates 2026 dashboard"
    body="The 15 closest near-misses with margin-percent context, the full per-pair searchable table, the EXACT / NEAR_FULL / WORD_MATCH classifier breakdown, and a constituency explorer that lets you pull every flagged pair for any of the 234 ACs."
    cta="Open the dashboard"
    accent="dummy"
>}}

---

## The headline number, with two definitions

Of the 329 flagged pairs, **263** had both the major and the suspect actually contest. They were spread across **221** distinct major candidates. **152** of those majors lost their seats.

How many of those losses were "consequential," meaning the dummy votes were at least equal to the margin of defeat?

| Dummy classification | Consequential losses |
| :--- | ---: |
| Strict (EXACT and NEAR_FULL name matches only) | **0** |
| Inclusive (all flagged dummies, including WORD_MATCH) | **2** |

The strict test is the one the headline pipeline uses, and the one I think the data supports for any causal claim. EXACT-tier and NEAR_FULL-tier dummies are the least likely to be coincidence. By that definition, no major candidate lost a seat where engineered name-confusion plausibly covered the gap.

The inclusive test adds WORD_MATCH dummies: cases where one significant name fragment is shared, often a common Tamil first name like Saravanan or Murugan. That produces two cases. Both are TVK losses.

| Constituency | Major (lost) | Party | Margin (votes) | Margin (% of polled) | Combined dummy votes |
| :--- | :--- | :--- | ---: | ---: | ---: |
| TIRUKKOYILUR | Vijay R Baranibalaaji | TVK | **285** | **0.13%** | 571 |
| PALANI | Dr. Praveen Kumar M | TVK | **693** | **0.33%** | 1,057 |

I would not stake a causal claim on either. WORD_MATCH dummies are the noisiest signal in the dataset. A constituency with common Tamil name patterns will throw up a few of these by chance. But they are the only two seats in the entire 263-pair tally where the arithmetic comes close to working, and both being narrow TVK losses in a wave year is worth flagging. Both have margins under half a percent of polled votes, which is the bottom 1% of the statewide distribution.

---

## Why the answer is small, and why that is the finding

The median dummy in the dataset polled about **200 votes** (174 for EXACT, 210 for NEAR_FULL, 197 for WORD_MATCH). The median margin of loss across the 152 lost seats was **27,002 votes**. The 25th-percentile margin was **9,554 votes**.

These are not seats where 200 to 1,000 confused voters tip outcomes. They are seats where the wave carried the winner home by tens of thousands, or where the constituency's traditional base voted as it always has.

The strategy needs a close election to bite. 2026 did not have many.

To put a number on it: in only **3 of 152 lost seats** did the major lose by under 1,000 votes. In only **15** did they lose by under 5,000 votes. The rest ran into a winner who was not winning narrowly.

The dummy-candidate strategy did not "fail" in 2026. It ran into a year where margins were too wide for it to matter. In 2016, when AIADMK won several seats by under 1,000 votes, the same 329 pairs would almost certainly have produced a non-zero strict-test count.

{{< callout title="The takeaway" type="insight" >}}
**The mechanism is intact and waiting for the next close election.** The same 329 pairs deployed in a 2016-style narrow-margin cycle would almost certainly have flipped seats. The story is not that dummies are harmless. The story is that the wave drowned them this time.
{{< /callout >}}

---

## By tier

| Tier | Pairs | Median dummy votes | In lost seats | Strict-consequential |
| :--- | ---: | ---: | ---: | ---: |
| EXACT | 64 | 174 | 30 | 0 |
| NEAR_FULL | 36 | 210 | 19 | 0 |
| WORD_MATCH | 163 | 197 | 103 | 0 (2 by inclusive test) |

EXACT-tier dummies (identical name after normalising prefixes and initials) are the most likely to register as engineered confusion. They polled the fewest votes per pair on average. The ones that look most engineered drew the smallest crowds. That is a useful corrective to the assumption that brazen dummies do more damage.

---

## By alliance

| Alliance | Targeted majors | Of whom lost | Strict-consequential | Total dummy votes against |
| :--- | ---: | ---: | ---: | ---: |
| INDIA (DMK-led) | 68 | 46 | 0 | 28,516 |
| NDA (AIADMK-led) | 66 | 48 | 0 | 25,702 |
| TVK | 61 | 32 | 0 (2 inclusive) | 19,383 |
| NTK | 26 | 26 | 0 | 6,222 |

The ruling DMK was the most-targeted alliance, the predictable pattern: spoilers cluster on incumbents. TVK attracted 61 dummy pairings despite being a debut party. The strategy was deployed defensively against the wave, not just by the usual operators. Total votes across all 263 pairings: roughly **79,823**, small per seat, zero in the column that matters.

---

## The closest the math came to working

| Constituency | Major (lost) | Party | Margin | Margin % | Dummy votes | Ratio |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| TIRUKKOYILUR | Vijay R Baranibalaaji | TVK | 285 | 0.13% | 571 | **2.00** |
| PALANI | Dr. Praveen Kumar M | TVK | 693 | 0.33% | 1,057 | **1.53** |
| KALLAKURICHI | Rajeevgandhi S | ADMK | 798 | 0.32% | 616 | 0.77 |
| TIRUVANNAMALAI | Arul Arumugam | TVK | 2,455 | 1.12% | 850 | 0.35 |
| RISHIVANDIAM | Ashok Kumar G | TVK | 4,862 | 1.99% | 1,212 | 0.25 |

Ratio = combined dummy votes divided by margin. Above 1.0 means the dummies polled more than the gap. Four of the top five near-misses are TVK losses, not by design but by distribution: the wave seats TVK won were not close, so TVK's narrow losses are the only TVK results that show up here at all.

The TIRUKKOYILUR case: TVK's Vijay R Baranibalaaji lost to AIADMK's Palanisamy S by 285 votes (0.13% of polled). A flagged independent polled 571. The door is open. The data does not show anyone walking through it.

The full near-miss table, sortable by ratio and margin percent, is in the [interactive dashboard](/election-dashboard/tn-2026-explorer.html#dummies).

---

{{< callout title="Caveat" type="caveat" >}}
This is not a **causal** claim. Dummy votes are not stolen votes. Voters who chose an unknown `R. Saravanan` may have been confused, making a deliberate protest vote, or genuine supporters. The ECI's published data cannot separate those populations.

It is not a **complete** account either. Tamil Nadu has a finite stock of common names. The dataset gives an upper bound on the strategy's footprint, not its ground truth.
{{< /callout >}}

---

## What "3 crore votes that elected nobody" looks like, three weeks later

In [the earlier post](/posts/tn-elections-2026-analysis/), NTK's strategy of running everywhere was the clearest illustration of how Tamil Nadu's elections work: 19,72,537 votes, 4.00% share, zero seats. The dummy-pair data is the same arithmetic at lower magnitude. The roughly 80,000 flagged-dummy votes are a third example of votes that were cast, were counted, and changed nothing. It is the structural feature of first-past-the-post in a fragmented field.

The mechanism is waiting for a year where margins are narrow. 2026 was not it.

---

## Explore the data

{{< dashboard-cta
    url="/election-dashboard/tn-2026-explorer.html#dummies"
    eyebrow="Primary · interactive"
    title="The dummy candidates 2026 dashboard"
    body="The 15 closest near-misses sorted by margin-percent, the full per-pair table with constituency-level filtering, the EXACT vs NEAR_FULL vs WORD_MATCH tier breakdown, and a constituency explorer that surfaces every flagged pair for any AC."
    cta="Open the Explorer"
    accent="dummy"
>}}

<div class="explore-grid">
<a href="/posts/tvk-debut-2026/">
  <strong>Companion post: TVK 2026 debut, mapped</strong>
  <span>The other half of the May 4 story. 108 seats, 1.32 efficiency, regional anatomy, and the 1st / 2nd / 3rd drill-downs.</span>
</a>
<a href="/election-dashboard/tn-2026-explorer.html">
  <strong>TN 2026 Explorer dashboard</strong>
  <span>Constituency map, regional strike rate, party seat-vs-vote efficiency, and the position-anatomy interactive tables.</span>
</a>
<a href="/data/tn-2026-candidates/">
  <strong>2026 candidates dataset</strong>
  <span>The full 4,023-candidate roster with assets, qualifications, and criminal cases. CC BY 4.0.</span>
</a>
<a href="/posts/tn-2026-dummy-candidates/">
  <strong>The original investigation</strong>
  <span>"Same Name, Different Initial" — the pre-poll piece that flagged the 329 pairs three weeks before voting.</span>
</a>
<a href="/election-dashboard/">
  <strong>Full election dashboard</strong>
  <span>Historical TN results, 2011 to 2026. District swings, strongholds, flipped seats, and the full constituency explorer.</span>
</a>
<a href="/posts/tn-elections-2026-analysis/">
  <strong>"3 crore votes that elected nobody"</strong>
  <span>The earlier piece on Tamil Nadu's structural FPTP asymmetry. Reads as the prequel to both TVK and dummy posts.</span>
</a>
</div>

---

{{< callout title="Methodology" type="method" >}}
Numbers computed by [`pipelines/21_dummy_impact_analysis.py`](https://github.com/ndranandraj/tn-2026-candidates-dataset). All vote counts use the Indian comma format (last 3 digits, then groups of 2). Margin percent is `(margin / total_votes_polled_in_AC) × 100`. The strict test counts only EXACT and NEAR_FULL name matches; the inclusive test adds WORD_MATCH (one shared name fragment). Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
{{< /callout >}}
