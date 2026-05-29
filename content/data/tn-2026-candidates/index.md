---
title: "Dataset: Tamil Nadu 2026 Candidates + Dummy Match Pairs"
date: 2026-04-23
lastmod: 2026-04-23
description: "Open dataset of all ~4,000 candidates contesting the Tamil Nadu 2026 Assembly Election, plus the 329 name-similarity match pairs across 144 constituencies used in the 'Same Name, Different Initial' investigation. Released under CC-BY-4.0."
summary: "~4,000 candidates across 234 constituencies, scraped from the ECI Affidavit Portal. 329 name-match pairs flagged across 144 constituencies. Free to download, cite, and remix."
keywords: ["Tamil Nadu 2026 candidates dataset", "dummy candidates CSV", "ECI affidavit portal data", "TN assembly election dataset", "namesake candidates data", "India election open data", "Tamil Nadu election 2026 candidates list"]
tags: ["data", "elections", "tamil-nadu", "2026"]
categories: ["Data"]
showToc: true
TocOpen: true
ShowReadingTime: false
ShowBreadCrumbs: true
disableShare: false
image: "/images/dataset-tn-2026-cover.png"
cover:
  image: "/images/dataset-tn-2026-cover.png"
  alt: "Tamil Nadu 2026 Dummy Candidates Dataset, v1.1, CC-BY-4.0 — 4,000 candidates, 329 match pairs, 144 constituencies"
  caption: "v1.1 · CC-BY-4.0 · Open data release."
  relative: false
---

**TL;DR** — Two CSVs. ~4,000 rows of candidate metadata scraped from the Election Commission of India's affidavit portal, plus 329 flagged name-similarity pairs used in the [*Same Name, Different Initial* investigation](/posts/tn-2026-dummy-candidates/). Released under CC-BY-4.0. Download, cite, remix.

**Repository:** [github.com/ndranandraj/tn-2026-candidates-dataset](https://github.com/ndranandraj/tn-2026-candidates-dataset)

**Licence:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — free commercial and non-commercial use with attribution.

**Cite as:**

> Anandraj, R. (2026). *Tamil Nadu 2026 Candidates and Dummy Match Pairs Dataset* (v1.1) [Data set]. https://github.com/ndranandraj/tn-2026-candidates-dataset

---

## What's in the release

Two CSV files and the scripts used to generate one from the other.

**`data/candidates_raw_2026.csv`** — ~4,000 rows, one per accepted nomination. Scraped from [affidavit.eci.gov.in](https://affidavit.eci.gov.in/) on April 17, 2026. Columns: constituency, candidate name, party, alliance, nomination status, plus source URL for reproducibility.

**`data/candidates_2026.csv`** — 329 rows, one per flagged name-similarity pair across 144 constituencies. Each row pairs a major-party candidate (ADMK, DMK, TVK, BJP, etc.) with a suspected namesake opponent, along with a similarity score and a category label (`EXACT` / `NEAR_FULL` / `WORD_MATCH`). This is the file that drives every chart and claim in the investigation.

Both files share a `constituency` key, so you can join them to analyse, say, "how many total candidates contest seats that have at least one EXACT match pair" or "what's the party distribution of flagged suspects versus the baseline of all Independents."

See [`DATA_DICTIONARY.md`](https://github.com/ndranandraj/tn-2026-candidates-dataset/blob/main/DATA_DICTIONARY.md) for every column, with examples.

---

## What's in the match pairs file

A quick preview of the 329-pair file to save you a download if you just want to know whether it fits your use case.

| Column | Example | What it means |
|---|---|---|
| `constituency` | `ALANDUR` | Assembly constituency, uppercase. |
| `major_candidate` | `S.Saravanan` | The candidate from a major party. |
| `major_party` | `ADMK` | Party abbreviation. |
| `major_alliance` | `NDA` | Alliance the party belongs to (`NDA`, `INDIA`, `TVK`, or `OTHER`). |
| `suspect_candidate` | `A.Saravanan` | The namesake opponent. |
| `suspect_party` | `IND` | Almost always `IND` (Independent). |
| `similarity` | `1.0` | 0–1 similarity score after name normalisation. |
| `category` | `EXACT` | One of `EXACT`, `NEAR_FULL`, `WORD_MATCH`. |
| `match_detail` | `Identical after normalization: SARAVANAN` | Human-readable explanation. |
| `matched_words` | `SARAVANAN` | The shared tokens. |
| `normalized_major` | `SARAVANAN` | The major candidate's name after stripping initials and honorifics. |
| `normalized_suspect` | `SARAVANAN` | Same for the suspect. |

329 rows like this. Over 90% of suspects are Independents.

---

## Headline numbers

These are the summary statistics the investigation builds on. Reproducible from `data/candidates_2026.csv` alone.

- **329** flagged pairs across **144** constituencies (of 234 total).
- **77** `EXACT` matches (identical after normalising initials and honorifics).
- **~50** `NEAR_FULL` matches (≥ 0.85 similarity, minor spelling variants).
- **~200** `WORD_MATCH` matches (significant shared token, 4+ chars).
- **> 90%** of flagged suspects contest as Independents.

---

## How to use it

Three common starting points, in descending order of ease.

**In a spreadsheet.** Download the match-pairs CSV, open in Excel or Google Sheets, filter by `category == EXACT` to get the 77 strongest cases, then filter by `major_alliance` to see how evenly distributed the tactic is across alliances.

**In Python.** Clone the repo, `cd tn-2026-candidates-dataset`, `pip install -r scripts/requirements.txt`, then:

```python
import pandas as pd
pairs = pd.read_csv("data/candidates_2026.csv")
print(pairs.groupby("category").size())
print(pairs.groupby("major_alliance")["category"].value_counts())
```

For the 4,000-row raw file, same pattern — `pd.read_csv("data/candidates_raw_2026.csv")`.

**Reproducing the investigation's chart.** `python scripts/make_chart.py` regenerates the horizontal stacked bar used on the blog. The scripts are kept deliberately minimal — no config, no CLI flags, just pandas and matplotlib.

---

## Methodology (short version)

Names are normalised before comparison: initials and single letters are stripped, honorifics removed (Thiru., Smt., Dr., etc.), punctuation collapsed, then uppercased. An `EXACT` match is two candidates in the same constituency whose normalised forms are identical. `NEAR_FULL` uses `rapidfuzz.token_sort_ratio` with a 0.85 threshold. `WORD_MATCH` flags any pair sharing a token of 4+ characters that isn't a common Tamil name stem (Kumar, Raja, Selvam, Murugan — these are manually excluded to reduce false positives).

Full details in [`METHODOLOGY.md`](https://github.com/ndranandraj/tn-2026-candidates-dataset/blob/main/METHODOLOGY.md), including the exact stopword list, the scraping procedure, and the known limitations.

---

## Known limitations

Every dataset has them. Listed up front so you don't have to dig.

The `WORD_MATCH` category has the highest false-positive rate because common Tamil name tokens recur naturally. I've excluded the most common stems but the list isn't exhaustive. If you're using the data for a specific claim, treat `EXACT` as the cleanest signal and validate `WORD_MATCH` rows by eye before citing.

The snapshot is from April 17, 2026. Withdrawals and disqualifications after that date are not reflected. The ECI portal updates irregularly — if you want a fresher scrape, the scraping logic is in `scripts/` and you can re-run it yourself.

Constituency names use the ECI's canonical uppercase form. Some sources spell them differently (Tuticorin vs. Thoothukudi, for example). Join carefully.

---

## Contributing

If you find an error — a misclassified pair, a missing candidate, a wrong alliance label — open an issue or a pull request on the repo. Corrections are welcome and will be credited in the release notes.

If you build something on top of this data — a visualisation, a paper, a news piece — I'd love to hear about it. Drop a link in a GitHub issue, or reach out via LinkedIn.

---

*Part of the [Data Releases](/data/) series. Every investigation on this site that runs on original data ships the data with it.*
