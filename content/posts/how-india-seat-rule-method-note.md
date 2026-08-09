---
title: "How I worked out India's seat rule: sources, code and corrections"
date: 2026-08-07
lastmod: 2026-08-07
description: "The method note behind the delimitation piece. Every source with a full citation, every model choice, what each test does and does not establish, and a log of the claims that were retracted along the way."
summary: "Companion to the main piece. Formal citations for every document, the three carve-out models and how much they matter, what the code proves and what it only suggests, and an honest list of the numbers this project got wrong before it got them right."
keywords: ["delimitation methodology", "apportionment method India sources", "1963 Delimitation Commission Order", "Lok Sabha seat calculation method", "reproducible data journalism"]
tags: ["delimitation", "india", "data", "methodology", "apportionment"]
categories: ["Data"]
readingTime: true
showToc: true
TocOpen: false
image: "/images/delimitation-1963-cover.png"
cover:
  image: "/images/delimitation-1963-cover.png"
  alt: "India's 1963 seat allocation rule, written out"
  caption: "The method behind the main piece."
  relative: false
---

This is the companion to [The rule India wrote down in 1963](/posts/the-rule-india-wrote-down-in-1963/), and to the [interactive calculator](/delimitation/). It exists so that someone who wants to disagree with that piece can find out exactly what to attack.

Three things are in here: where every number came from, what the code does and does not establish, and a list of the claims this project made and then had to withdraw.

## The question

India allocates Lok Sabha seats among its states by a procedure a Delimitation Commission set out in 1963. The project asked what that procedure is, under what conditions the documentation actually determines an answer, and how specified counterfactual models compare on named measures of representation.

That third question is a **model-based decomposition and not a fact read off the data.** It needs a metric, a unit universe, a House size, a treatment of union territories and of states that have split, an allocation baseline, and a completion of the procedure wherever the documentation runs out. Every one of those is a choice, and the choices are set out below.

## Sources

Each is a document that was opened and read. Nothing here is from a search summary or from memory.

**The Orders.**

1. Delimitation Commission **Order No. 1**, S.O. 874, made under section 8(a) of the Delimitation Commission Act 1962, dated **20 March 1963**, published in the *Gazette of India Extraordinary*, Part II, Section 3, Sub-section (ii), No. 50. This is the one that states the rule in words. Found in the Election Commission's archive inside the volume catalogued as "Delimitation Orders (1967)", which is why it is easy to miss: these volumes are catalogued by the year of the consolidated orders, not the year of the Commission.
2. **Delimitation of Parliamentary and Assembly Constituencies Order, 1976**, Election Commission of India, signed T. Swaminathan, Chief Election Commissioner, 1 December 1976. Made under section 8(1) of the Representation of the People Act 1950 as amended in 1976, pursuant to delimitation under the Delimitation Act 1972.
3. **Delimitation of Parliamentary and Assembly Constituencies Order, 2008**, Election Commission of India. Used as an independent cross-check on the 1976 Order, because its Schedule I tabulates the 1976 allocation beside the 2008 one.

**The Constitution.**

4. **The Constitution (Thirty-first Amendment) Act, 1973**, and the Statement of Objects and Reasons appended to the Bill, signed H. R. Gokhale, Minister of Law, 18 April 1973. Source of the six-million proviso to article 81(2), and of the government's own phrase "fifteen major States".

**The censuses.**

5. Census of India 1961, **Paper No. 1 of 1962, "Final Population Totals"**, A. Mitra, Registrar General and Census Commissioner.
6. Census of India 1971, Series 1, **Paper 1 of 1972, "Final Population"**, Registrar General and Census Commissioner.
7. Census of India 2011, **Table A-2, Decadal Variation in Population Since 1901**. This is the basis used throughout, and it restates every state's population at every census from 1901 to 2011, so it cross-checks the 1961 and 1971 figures at the same time.

**The theorems.**

8. M. L. Balinski and H. P. Young, "A New Method for Congressional Apportionment", *Proceedings of the National Academy of Sciences USA* **71**(11): 4602-4606, November 1974. Theorem 1 is the one used.
9. M. L. Balinski and H. P. Young, "The Webster method of apportionment", *Proceedings of the National Academy of Sciences USA* **77**(1): 1-4, January 1980. Theorems 3 and 5.

**The prior work.**

10. Alistair McMillan, "Delimitation, Democracy, and End of Constitutional Freeze", *Economic and Political Weekly* **35**(15): 1271-1276, 8 April 2000. DOI 10.2307/4409148. **Paywalled and not read.**
11. Alistair McMillan, "Population change and the democratic structure", *Seminar* **506**, October 2001. Free, read in full. Its footnote 2 is a complete statement of his method and is quoted in the main piece.
12. Pankaj Kumar Patel and T. V. Sekher, "Parliamentary Delimitation: A Study on India's Demographic Struggle for Political Representation", *Journal of Asian and African Studies*, 2024. DOI 10.1177/00219096241295634.
13. Milan Vaishnav and Jamie Hintson, "India's Emerging Crisis of Representation", Carnegie Endowment, 14 March 2019. Read in full. The origin of the "848 seats" figure, which is their projection to 2026 rather than a 2011 result. It also gives 718 as the House at which no state loses on 2011 figures, against 709 here under the carve-out model, the gap being Webster against India's rule and a different treatment of Delhi.
14. Louise Tillin, Milan Vaishnav and Andy Robaina, "Delimitation After Defeat: India's Unfinished Debate Over Representation", Carnegie Endowment, May 2026.

**Not read, and it matters.**

15. Rein Taagepera, "The size of national assemblies", *Social Science Research* **1**(4): 385-401, 1972. DOI 10.1016/0049-089X(72)90084-1. Paywalled. The cube root is therefore attributed through a peer-reviewed paper that cites it, and the derivation is **contested** in print, so it is written as an empirical **regularity** rather than a law.

## Data

Every population and seat figure lives in a Python file that asserts its own totals on import, so a transcription error fails loudly rather than propagating. Two such errors were caught that way: an OCR misreading of Madras in the 1961 table, and a units mismatch in Assam.

**Every figure is corroborated by two independent official tables.** The 2011 A-2 table restates the 1971 figures and agrees on 27 of 29 units; the exceptions are a 377-person adjustment between Uttar Pradesh and Haryana that cancels exactly, and Sikkim, which acceded in 1975.

**Three different 2011 national totals exist** and the choice matters for the cube root but for nothing else. The provisional figure of 1,210,193,422 is superseded and should never be used. The Primary Census Abstract gives 1,210,569,573. Table A-2, used here, gives 1,210,854,977. The gap between the last two is 285,404 and it is entirely Manipur: the 2011 results for three sub-divisions of Senapati district were cancelled, so no Primary Census Abstract exists for them while A-2 carries an estimate.

## Method

Seven methods are implemented from scratch, with no library that hides the rounding: Adams, Dean, Huntington-Hill, Webster, Jefferson, Hamilton, and India's own 1963 rule.

**Each divisor method is implemented twice**, by a priority queue and by a divisor search. These rest on different facts, so if they disagree one of them is wrong, and the code asserts they agree. That caught a real tie-handling bug on lopsided populations.

**The suite reproduces the published 1940 United States apportionment exactly** before being used on any Indian data. This was the highest-value hour in the project: it is the only check that tests the implementation against a result somebody else published.

**The 1971 result is confirmed in exact rational arithmetic**, using Python fractions with no floating point anywhere, so no conclusion rests on a rounding artefact in the code that is meant to be studying rounding.

**The interactive calculator re-implements everything in JavaScript**, and that port is tested rather than trusted. The test extracts the apportionment core out of the shipped HTML file, so there is one source of truth and no stale copy, and checks it against fixtures generated by the Python: 2,163 seat tables across 309 cases, including every real exercise and 300 randomised ones.

## The models, and how much they matter

The proviso to article 81(2) says that proportionality does not apply to states under six millions. **It does not say what those states should get instead.** Nor does anything fix the number of seats for the union territories. So any present-day calculation needs a model, and this project uses three.

| Model | What it does | Status |
|:--|:--|:--|
| **Carve-out** | Holds the 15 sub-six-million states and union territories at their current seats; apportions the rest among the 20 states above the line | The default. Every headline figure |
| **One-seat floor** | All 35 units in the pool, with a guaranteed minimum of one seat each | Reported alongside |
| **No carve-out** | All 35 units apportioned together, no floor | **A stress test, not a proposal.** It gives seven units zero seats |

**What survives all three: the losses.** Tamil Nadu falls to 32 and Kerala to 15 in every model. **What does not survive: the gains.** Uttar Pradesh ranges from +5 to +10 depending on the model. So a loss can be stated as a finding; a gain must always carry its model.

**And a note on the fairness metrics, because the first draft of the main piece got this wrong.** The freeze is eight to twelve times worse than a recomputed allocation on the **distributional** measures (**Loosemore**-Hanby 10.1x, root-mean-square deviation from quota 12.0x, **Gini** of representation 8.3x). It is much closer on the extremal ones: max-to-min ratio 1.36x, maximum people per seat 1.09x, and minimum people per seat 0.80x, meaning the least-represented state is slightly better off under the freeze. "Worse on every measure" is false and was published in a draft before being caught.

One trap worth naming, because it was live in the calculator for an hour. **Exempting units by population is wrong.** The proviso speaks of *States*, so a union territory is outside the pool however large it is. Delhi had 16.8 million people in 2011, far above the six-million line, and is a union territory. A tool that exempts by population puts Delhi in the pool and silently produces a different model from every published number. There is now a test that asserts the split unit by unit rather than checking the arithmetic, because **the arithmetic was perfect and the answer was still wrong.**

## The branch the Order does not cover

The 1963 Order says what to do when rounding to nearest leaves the total **short** of the House size. It says nothing about what to do when rounding **overshoots**.

Across the sweeps in this project, roughly a third of House sizes land on that silent branch, where the code supplies a symmetric step. That step is a **completion** of the documented rule and not the rule, and it changes results.

**And a second tightening, 2026-08-08, after a further outside review.** The Order does not merely cover the shortfall case in general. It works one example and places exactly **one** spare seat. Placing two or more extends its stated principle by rank; the Order never does it. So there are three tiers of evidence, not two, and `apportionment.evidence_tier()` labels them.

Every row below extends the procedure **mechanically** to **hypothetical** House sizes the Commission never applied it to, which is itself a caveat that has to travel with them:

| | Strictly demonstrated (0 or 1 spare) | Principle extended (2+ spares) | Including overshoot |
|:--|--:|--:|--:|
| Alabama paradox, House 543 to 1100 | **11 drops, 6 states** | 26 drops, 9 states | 50 drops, 11 states |
| Population paradox, House 15 to 1100 | **0 instances** | 0 instances | 1 instance |

Across the 543 to 1100 sweep, 31% of House sizes need no spare seat, 24% need exactly one, 11% need two or more, and 34% overshoot. **Publish the strict column.** The finding survives all three; the count does not.

**Both real exercises are in the strict column**: 1961 placed exactly one spare seat and 1971 placed none. So nothing historical depends on any extension. What moved was everything computed at House sizes India has never used, and the published figures are the documented-branch ones.

## What each check establishes, and what it does not

| Check | Establishes | Does not establish |
|:--|:--|:--|
| Reproducing US 1940 | the method implementations are right | anything about Indian inputs or the reading of the 1963 Order |
| Exact rational arithmetic on 1971 | the result is not a floating-point artefact | that the inputs or the unit set are right |
| Two implementations agreeing | ordinary coding errors are absent | that both are not wrong the same way |
| Reproducing the 1961 and 1971 tables | the stated rule produces the real allocations | that the Commission worked from the published census figures rather than internal ones |
| The Vinton equivalence proof | the two procedures coincide where the Order speaks | anything about the overshoot branch |
| The JavaScript-versus-Python test | the calculator computes what the project computes | that the calculator's model is the project's model, which is a separate test |
| The population-paradox search | the paradox was not found in this model | that it does not occur |

That last row deserves emphasis. **It is a negative result produced by a search written by the same person who wanted the answer.** A bug in such a search returns "not found", which is exactly what gets published, and the failure is invisible and self-confirming. Mitigations: a positive control that fires on a constructed case where the paradox is known to be present, a hard gate requiring two readings of an ambiguous territorial boundary to agree on both House sizes and state pairs, exact rational growth comparisons, and a published sweep. **None of that is independent reproduction, which is what it actually needs.**

## Corrections

Every project should publish this and almost none do. These are claims this project made internally and then withdrew, in order of how badly they would have aged.

**The Tamil Nadu counterfactual, wrong three times.** The original line was "Tamil Nadu was 18,113 people short of a 40th seat". That conflates a margin with a counterfactual. The first replacement, 96,397 people, was computed under Webster, which the project insists is not India's rule. The second, 110,001, was an artefact of the project's own invented overshoot step, which hands the seat straight back to Tamil Nadu. **There is no safe form of this number**, because the case that arises is the one the 1963 Order does not cover. What is publishable is the margin, 18,113, and the reading it depends on.

**"848 seats".** Carried for several sessions as though it were legislative. It is a 2019 Carnegie projection. The 2026 Bill proposed 850, with 815 from the states and 35 from the union territories.

**The novelty claim.** The plan said no published treatment ran India's allocation through the classical apportionment methods. That was false when written. McMillan did it in 2000 and Patel and Sekher in 2024. What has **not been found** is anyone identifying the rule in the 1963 Order and testing it against the allocations actually made, and even that is "not found" rather than "does not exist": one search, no systematic index coverage, three of the items paywalled.

**"No discretionary step anywhere in it".** Refuted by the project's own sources three times over. The House size is discretionary and the 1963 Order says so. The proviso does not fix what small states get. The split between pool and carve-out follows from no rule.

**"Exactly fifteen states above six millions" as a discovery.** It is a drafting artefact. The Statement of Objects and Reasons names the six smaller states, so Parliament drew the line around a list it had already written.

**"All three 2026 bills failed."** One was negatived. The other two became **infructuous** and were never voted on.

**"The rule that keeps every state closest to its fair share."** The main piece's closing paragraph said this, and the counterexample was in its own worked example: Uttar Pradesh's 84.48 is nearer to 84 than to 85, and the rule gave it 85. The rule does not minimise distance to fair share; it guarantees every state its lower or upper quota, which is weaker and different. Caught by an outside reviewer, 2026-08-08.

**A two-tier scope gate that should have had three.** The project gated its sweeps on short-versus-overshoot, having been told once already that it was reading the Order too generously. It was still too generous: the Order places one spare seat, and placing several is an extension. The Alabama count has now moved twice for scope reasons, from 50 to 26 to 11, each time because a reviewer looked and not because the author did.

**"Worse on every standard measure."** The main piece said the frozen allocation was several times worse than a recomputed one on every standard measure of malapportionment. Three of six measures do not support it, and on one the frozen allocation is slightly better. Corrected before publication, but it was written and it survived a linter pass, because the linter checks numbers and this was an adjective.

**Citing Carnegie 2019 without opening it.** The 848 attribution was taken from a think tank quoting a think tank. It turned out to be correct, but the check should have come first, and reading the paper produced two findings that the second-hand version could not have.

**A territorial mismatch in the paradox search.** It compared 1971 Assam excluding Mizo district against 2011 Assam including Mizoram, inflating Assam's growth from +113.4% to +120.9%. Found while writing a review brief, which is an argument for writing review briefs.

**The Delhi bug in the calculator.** Described above.

Six of these were caught by review rather than by self-checking, and three survived a round of self-review before an outside reader found them. The pattern is consistent: **the arithmetic was almost never the problem. The sentences were.**

## Reproducing any of it

```
python3 tests/test_apportionment.py     the methods, including US 1940
python3 tests/test_phase3_exact.py      the 1971 result in exact arithmetic
python3 tests/test_gates.py             the documented-versus-completion gates
python3 tests/test_tool_model.py        the calculator's model against the project's
node    tests/test_tool_js.js           the calculator's arithmetic against the Python
python3 src/phase3_reverse_engineer.py  which methods reproduce 1976
python3 src/phase3b_1961_exercise.py    which methods reproduce 1963
python3 src/india_rule_is_hamilton.py   the Vinton equivalence
python3 src/population_paradox.py       the paradox search, with its positive control
python3 src/phase4_headline.py          the present-day scenarios
python3 src/claims.py                   rebuilds the claim register and lints the prose
```

That last one is the unusual piece. Every publishable number is registered with the caveat that must travel with it, computed live from the code that produced it, and a linter reads the prose and fails if a registered number appears without its caveat nearby. It exists because the same failure happened four times: a number established correctly in one document, restated in another without the thing that bounded it.

## What is still open

- **McMillan's 2000 EPW paper is unread.** His method is known from the free 2001 companion, but the earlier paper is the closest prior work and remains behind a paywall.
- **Taagepera 1972 is unread**, so the cube root stays an empirical regularity.
- **No Commission working paper has been found**, so whether the 1963 Commission used published final census figures or internal ones is unknown.
- **The population-paradox negative result wants independent reproduction.**
- **The literature search was one pass.** "I have not found" is not "nobody has".

---

*Code, data and the full claim register are published alongside. Released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Suggested citation: Anand Raj, "How I worked out India's seat rule: sources, code and corrections." ndranandraj.com, August 2026.*
