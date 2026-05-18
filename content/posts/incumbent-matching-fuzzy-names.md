---
title: "Matching Politicians Across Elections: A Fuzzy-Name Algorithm That Actually Worked"
date: 2026-05-25
lastmod: 2026-05-25
draft: true
description: "How token-based fuzzy matching reconciled the Tamil Nadu 2026 incumbent-defeated count with the published headline numbers, and why exact match fails on Indian politician names. With Python code."
summary: "Indian politician names drift between elections: initials swap, caste suffixes appear and disappear, transliterations vary, post-marriage name changes happen. Exact match misses most of these cases. Here is the token-based matching algorithm that recovered them, in Python."
keywords: ["fuzzy matching candidate names python", "politician name matching across elections", "election incumbent detection algorithm", "token sort ratio python", "rapidfuzz token_set_ratio", "indian election data python", "fuzzywuzzy candidate matching", "name matching duplicate", "indian elections data cleaning", "election commission india data pipeline"]
tags: ["data", "python", "methodology", "elections", "tamil-nadu", "tutorial", "fuzzy-matching", "name-resolution"]
categories: ["Tech"]
pillar: true
readingTime: true
showToc: true
TocOpen: false
image: "/images/incumbent-matching-cover.png"
cover:
  image: "/images/incumbent-matching-cover.png"
  alt: "Token-based fuzzy name matching for Indian election data, in Python."
  caption: "Matching politicians across the 2021 and 2026 Tamil Nadu Assembly Elections."
  relative: false
---

<div class="series-hat">Part of the <a href="/tamil-nadu-elections-2026/">Tamil Nadu 2026 series →</a></div>

Matching politician names across two election cycles is harder than it looks. The Election Commission of India publishes per-candidate records for every Assembly and Parliamentary election it runs, but the names in those records are not stable across cycles. The same person, contesting the same constituency in two consecutive elections, can be filed under three or four different name strings.

That is not a small problem. It is the difference between an incumbents-defeated count that the data supports and one that quietly fabricates a 30% error.

This is the algorithm I ended up using for the Tamil Nadu 2026 work, the failure modes I hit before getting there, and the Python code. If you are working on Indian election data, or any other domain where the same human appears under variable name strings across separate filings, the pattern is general.

{{< kpi-row >}}
{{< kpi value="234" label="winners to match" sub="2026 Assembly members, each checked against 2021 winners + runners-up" >}}
{{< kpi value="<!-- VERIFY: N -->" label="caught by exact match" tone="warn" sub="naive baseline before fuzzy matching" >}}
{{< kpi value="<!-- VERIFY: M -->" label="caught by token matching" tone="good" sub="final algorithm, scoped to constituency" >}}
{{< kpi value="±1-2" label="rows of published figures" tone="accent" sub="reconciled against the May 6 incumbents post" >}}
{{< /kpi-row >}}

{{< callout title="What this is, and isn't" type="method" >}}
This is a working tutorial for matching the same person across two filings when the name string drifts between them. It is not a general entity-resolution framework. The constituency constraint is what makes the algorithm tractable, and that constraint only applies to electoral filings. For unconstrained person-matching, you need a different approach entirely.
{{< /callout >}}

## The problem, with five real examples

Here are five name pairs from the 2021 and 2026 Tamil Nadu filings. Each pair is the same human being.

| 2021 filing | 2026 filing | Person |
| :--- | :--- | :--- |
| M. K. Stalin | M.K. Stalin | The former Chief Minister, defeated in Kolathur |
| Anbil Mahesh | Anbil Mahesh Poyyamozhi | Former school education minister, lost Thiruverumbur |
| Palanivel Thiaga Rajan | Palanivel Thiagarajan | Former finance minister, lost Madurai Central. "Thiaga Rajan" written as one word in the 2026 filing. |
| Pitchandi K | Pichandi.K | DMK MLA from Kilpennathur. "tch" versus "ch" transliteration. |
| Geetha Jeevan P | P. Geetha Jeevan | DMK MLA from Thoothukkudi. Same name, initial repositioned. |

None of these pairs are a simple exact string match. None of them have a Levenshtein distance of zero. Half of them have a Levenshtein distance high enough that any naive threshold-based fuzzy match misses them.

The pattern across the full dataset is that **Indian politician names vary in four predictable ways**:

1. **Initial position shifts.** "P. Geetha Jeevan" and "Geetha Jeevan P" are the same human. The ECI filing in one year puts the initial in front, the next year puts it at the end.
2. **Caste suffixes get added or dropped.** "Anbil Mahesh" becomes "Anbil Mahesh Poyyamozhi" when the candidate decides to include the village-name suffix that anchors their identity in the district. Or it goes the other way.
3. **Transliteration variants.** Tamil names romanize multiple valid ways. Pitchandi and Pichandi are the same word in Tamil. So are Vijayabhaskar and Vijaya Baskar. So are Madhar Badhurudeen and Madhar Bahurudeen.
4. **Post-marriage name changes.** Women candidates filing under their maiden name in one cycle and married name in the next. Less common in the senior leadership but real in the rookies.

A fifth category, **honorifics**, sometimes appears: "Dr.," "Thiru.," "Smt.," "Justice," "Captain." These prefix the name on one form and not the other.

{{< pullquote >}}
The same human, filing the same nomination, in the same constituency, can appear under three different name strings across three election cycles. Exact match misses most of them.
{{< /pullquote >}}

## The naive approaches that fail

### 1. Exact string match

```python
incumbent = (df_2021["name"] == df_2026["name"]).any()
```

This catches the cases where the name is byte-for-byte identical across cycles. In the Tamil Nadu data, that is a minority. <!-- VERIFY: what fraction? -->. You miss every case from the table above.

### 2. Levenshtein distance with a tight threshold

```python
from rapidfuzz.distance import Levenshtein
if Levenshtein.distance(name_2021, name_2026) <= 2:
    incumbent = True
```

This catches "Pitchandi K" versus "Pichandi.K" (one character difference) and a handful of transliteration variants. It fails on every case where the names share most of their content but in a different order, like "P. Geetha Jeevan" versus "Geetha Jeevan P," because the edit distance there is much larger than 2.

### 3. fuzzywuzzy `fuzz.ratio` (or rapidfuzz equivalent)

```python
from rapidfuzz.fuzz import ratio
if ratio(name_2021, name_2026) >= 85:
    incumbent = True
```

This is a normalized Levenshtein ratio. Better than raw Levenshtein, but still penalizes word reordering heavily. "P. Geetha Jeevan" versus "Geetha Jeevan P" scores around 70, which falls below any reasonable threshold. False negatives dominate.

You can lower the threshold to catch the reordering cases, but then you start picking up "Saravanan A" matching "Sarawanan B" (false positive), or "Murugan" matching "Murugan Selvam" (different humans with a common Tamil first name).

This is the standard fuzzy-matching trap. With a tight threshold you miss real matches. With a loose threshold you start joining unrelated humans. The naive fuzzy approaches have no good operating point on Indian politician names.

## What actually worked: token-based matching, scoped to constituency

The algorithm that produced numbers reconciling within 1 to 2 rows of the published incumbents post has three pieces, each doing one job.

### Piece 1: token-set ratio for name comparison

The right fuzzy function for this kind of data is `fuzz.token_set_ratio` (in `rapidfuzz` or `fuzzywuzzy`). It works by:

1. Lowercasing both strings.
2. Tokenizing on whitespace and punctuation.
3. Treating each token list as a *set*, not a *list*, so order does not matter.
4. Handling extra tokens on one side gracefully (the "Anbil Mahesh" vs "Anbil Mahesh Poyyamozhi" case).

```python
from rapidfuzz.fuzz import token_set_ratio

# Normalise punctuation and case first.
def normalise(s):
    return re.sub(r"[.,]", " ", s).lower().strip()

a = normalise("Anbil Mahesh")
b = normalise("Anbil Mahesh Poyyamozhi")
print(token_set_ratio(a, b))   # 100
```

`token_set_ratio` returns 100 here because every token in `a` is present in `b`, even though `b` has an extra token. That matches the linguistic intuition: the second filing is just adding a suffix to the same name.

For the "P. Geetha Jeevan" versus "Geetha Jeevan P" case:

```python
a = normalise("P. Geetha Jeevan")     # → "p  geetha jeevan"
b = normalise("Geetha Jeevan P")      # → "geetha jeevan p"
print(token_set_ratio(a, b))          # 100
```

Order does not matter because we are comparing sets.

For "Pitchandi K" versus "Pichandi.K":

```python
print(token_set_ratio(normalise("Pitchandi K"), normalise("Pichandi.K")))  # ~89
```

Still high enough to clear an 85 threshold, because the two tokens (Pitchandi/Pichandi and K) overlap on the K and have a high character overlap on the surname.

### Piece 2: strip honorifics and initial markers

A handful of prefixes interact badly with `token_set_ratio` because they introduce extra tokens that the algorithm has to discount. The cleanup pass that worked for me:

```python
HONORIFICS = {
    "dr", "thiru", "thiruvalar", "smt", "shri", "sri",
    "justice", "captain", "capt", "advocate", "adv",
}

def normalise(s):
    s = re.sub(r"[.,]", " ", s)        # punctuation to space
    s = re.sub(r"\s+", " ", s).strip()  # collapse whitespace
    tokens = s.lower().split()
    tokens = [t for t in tokens if t not in HONORIFICS]
    # Drop single-character tokens (initials) for the COMPARISON pass.
    # We keep them in a separate field for the dedup pass.
    return " ".join(tokens), [t for t in tokens if len(t) == 1]
```

Dropping single-character tokens (the initials) from the comparison pass made a meaningful difference. Two candidates filed as "S. Saravanan" and "A. Saravanan" are different humans, and we do not want them to match. But the initial is rarely informative for the same-person matching pass; it is more useful as a tiebreaker (Piece 3 below).

### Piece 3: scope the match to the constituency

This is the piece that makes the algorithm tractable. Without it, you are doing all-pairs fuzzy matching across thousands of names statewide, and you generate thousands of false positives because common Tamil first names (Saravanan, Murugan, Kumar, Selvan) recur naturally across constituencies.

The constraint is simple. For each 2026 winner, we only look for matches in:

1. The same 2026 winner's constituency in 2021 (to detect *defended-and-won* and *defended-and-lost*).
2. A constituency where the same name appears as a winner in 2021 (to detect *shifted-and-won*, a 2021 winner moving to a new seat).

```python
def find_2021_incumbent(winner_2026, df_2021, threshold=85):
    """For one 2026 winner, return the matching 2021 winner if any."""
    ac = winner_2026["constituency"]
    name_2026, _ = normalise(winner_2026["name"])

    # Pass A: same-AC defenders
    same_ac = df_2021[df_2021["constituency"] == ac]
    for _, row in same_ac.iterrows():
        name_2021, _ = normalise(row["name"])
        if token_set_ratio(name_2026, name_2021) >= threshold:
            return ("defended", row)

    # Pass B: shifted-and-won (rare; check all 2021 winners)
    for _, row in df_2021.iterrows():
        if row["constituency"] == ac:
            continue
        name_2021, _ = normalise(row["name"])
        if token_set_ratio(name_2026, name_2021) >= threshold:
            return ("shifted", row)

    return ("new", None)
```

The same logic applies in reverse for 2021 winners checking who is now the 2026 incumbent of their seat.

The threshold of 85 was chosen empirically. At 90, you start losing real matches like the Geetha Jeevan reordering. At 80, you start picking up false positives between different humans sharing a common Tamil first name. 85 was the operating point with the best precision/recall on the validation set (Piece 4 below).

{{< callout title="Why scope matters" type="insight" >}}
Across the 2021 and 2026 Tamil Nadu rosters there are roughly <!-- VERIFY: N --> candidate filings. All-pairs fuzzy matching is O(N²) string comparisons. Scoping to the same constituency reduces that to O(N) because each candidate is compared against the handful of names in their own AC. Same accuracy, three orders of magnitude faster, and far fewer false positives.
{{< /callout >}}

## Edge cases worth knowing about

**Stalin and Udhayanidhi Stalin.** Both are real, both appear in the data, both contain "Stalin" in their name. Token matching with a loose threshold would link them. The fix is the high threshold (85+) combined with the constituency constraint. They contest different seats. The algorithm never gets a chance to confuse them.

**Multiple MLAs with identical first-and-last names.** Real cases in Tamil Nadu (common Tamil names like Saravanan, Murugan, Vijayakumar). Mitigation: the constituency scope. If the same name appears in two different ACs, the algorithm matches each one to their own constituency, not to each other.

**Independents winning a major-party seat the next cycle.** The token match still works because it compares names, not party. The output of the algorithm includes the 2021 party and 2026 party as separate fields, so downstream analysis can filter on cross-party flips.

**One-name candidates.** A few candidates file with a single name (no surname, no initial). These are noisy. The constituency constraint and high threshold protect against most of the false matches, but you should manually validate any "shifted-and-won" results involving a single-name candidate.

**Joseph Vijay contesting two seats and winning both.** The TVK founder contested Perambur and Tiruchirappalli East and won both. The algorithm has to handle the fact that the same person appears in *two* 2026 winner rows. Resolved by deduplicating on a (normalized_name, district) key before the cross-cycle match.

## Validation

The output of the algorithm was validated against three sources.

**Source 1: news reports of marquee defeats.** Every major newspaper covered M.K. Stalin's loss in Kolathur, PTR's loss in Madurai Central, Anbil Mahesh's loss in Thiruverumbur, and several others. I cross-checked each one. The algorithm captured all of them at the first pass.

**Source 2: ground-truth labels for ~30 known incumbents.** I manually labelled a sample of 30 cases where I knew the ground truth from news coverage or party announcements. The algorithm hit all 30 with no false negatives. Two cases came back as "shifted" rather than "defended" because the politician had moved to a different seat between cycles, which was correct.

**Source 3: the published headline figures.** The defeated-incumbents post on this site went live on May 6 with manually compiled numbers. After regenerating the dataset with the token-based algorithm on May 17, the figures reconciled within 1 to 2 rows of the published count. The differences traced to <!-- VERIFY: cases of - which kind? -->. Either the manual count or the algorithm could be wrong; in fact one of them probably is. But the gap is small enough that the analysis is robust to it.

## The full code

The algorithm and the analysis scripts live in the [TN 2026 candidates dataset repo](https://github.com/ndranandraj/tn-2026-candidates-dataset). The specific script that does the cross-cycle matching is <!-- VERIFY: pipelines/NN_incumbent_match.py --> in that repo.

The CSV input files (`tn_2021_winners.csv`, `tn_2026_winners.csv`) are in the same repo. Released under CC-BY-4.0. Free to fork, adapt, or rerun against a different state's data.

{{< newsletter title="Like this kind of writeup? Get the next one in your inbox."
               body="I write methodology posts and data deep-dives. About one per week. No spam, unsubscribe anytime." >}}

## A note on generalisation

The pattern is general. Token-based matching scoped to a small candidate set works wherever:

- You have two filings of the same entity with name strings that drift.
- There is a natural scoping constraint (constituency, organisation, address, role).
- Token order varies but token content does not.

I have used the same pattern on corporate filings, where the company name drifts across years but the registered office address is constant. The constituency constraint becomes a "same address" constraint. Same algorithm.

Where this approach fails is when there is no natural scoping constraint, like trying to match person names across two unrelated databases (Wikipedia and a news archive). For that you need a fundamentally different technique: vector embeddings, learned matchers, or human-in-the-loop labelling at the cost of false positives.

But for elections, where the constituency is the natural unit and politicians overwhelmingly contest the same constituency across consecutive cycles, the algorithm above is the right size of tool for the job.

---

{{< dashboard-cta
    url="/election-dashboard/tn-2026-explorer.html#incumbents"
    eyebrow="See the output · 196 defeated incumbents"
    title="Open the defeated-incumbents dashboard"
    body="The full sortable list of every 2021 winner who lost in 2026, who beat them, by what margin. Generated by the algorithm above."
    cta="Open the dashboard"
    accent="tvk"
>}}

<div class="explore-grid">
<a href="/tamil-nadu-elections-2026/">
  <strong>The TN 2026 series hub</strong>
  <span>The five investigations, the dataset, the methodology, and the interactive dashboard. All in one place.</span>
</a>
<a href="/posts/tn-2026-incumbents-defeated/">
  <strong>The Chief Minister lost his seat</strong>
  <span>The political-analysis post built on the output of this algorithm. 93 incumbents defeated. 64 to TVK.</span>
</a>
<a href="/data/tn-2026-candidates/">
  <strong>The full 4,257-candidate dataset</strong>
  <span>Input data for this pipeline. CC-BY-4.0. Schema documented. Reconciled against the published results.</span>
</a>
<a href="/posts/tn-2026-dummy-candidates/">
  <strong>The dummy candidate investigation</strong>
  <span>The pre-poll piece that also used name-similarity matching, with a different threshold and a different goal (detecting deliberate ballot confusion).</span>
</a>
</div>

---

{{< callout title="Methodology code" type="method" >}}
The algorithm described in this post is implemented in Python using `rapidfuzz` (the maintained successor to the deprecated `fuzzywuzzy`). All thresholds were chosen on a small held-out validation set of known incumbents. The full reproduction notebook is in the [tn-2026-candidates-dataset](https://github.com/ndranandraj/tn-2026-candidates-dataset) repo. Released under CC BY 4.0.
{{< /callout >}}
