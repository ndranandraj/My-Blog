# Project: Benchmarking the MoSPI MCP Server

**Status:** Not started, blocked on live testing
**Owner:** Anand
**Created:** July 2026
**Target publish:** August 2026

---

## 1. What this project is

India's National Statistics Office shipped an official Model Context Protocol (MCP)
server that exposes official statistics to AI assistants. It works. It has been
reviewed exactly once, five months ago, when it was a third of its current size.

This project is a systematic accuracy benchmark of that server, published as a blog
post plus a reproducible dataset, with bugs filed back upstream.

The post is deliberately **not** "here is a cool new government tool." That post
already exists and was written well by someone else. This one is "I measured it."

---

## 2. Background: what actually shipped

| Item | Detail |
|:---|:---|
| Endpoint | `https://mcp.mospi.gov.in/` |
| Source | [nso-india/esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp), MIT licensed |
| Repo activity (July 2026) | 134 stars, 28 forks, 3 open PRs |
| Stack | Python 3.11+, FastMCP 3.3, Swagger-validated params, OpenTelemetry, Docker |
| Built with | [Bharat Digital](https://bharatdigital.io), Harsh Nisar involved |
| Launched | February 6, 2026, timed ahead of the AI Impact Summit (Feb 15-20, 2026) |
| Datasets at launch | 7 |
| Datasets now | 25 in the repo README (PIB said 21 in March) |
| Underlying API | `api.mospi.gov.in`, serves aggregate published figures, not raw microdata |

### The four tools

Strictly sequential. Skipping a step returns invalid filter codes.

```
list_datasets  ->  get_indicators  ->  get_metadata  ->  get_data
```

### The 25 datasets

PLFS, CPI, IIP, ASI, NAS, WPI, ENERGY, AISHE, ASUSE, GENDER, NFHS, ENVSTATS, RBI,
NSS77, NSS78, CPIALRL, HCES, TUS, EC, NSS79, UDISE, MNRE, NSS76, NSS75E, NSS80.

Only the first seven plus ENVSTATS have ever been publicly tested.

---

## 3. Prior art (read this before writing a word)

**Aman Bhargava**, "Querying India's MoSPI Data with Claude and MCP", February 9, 2026.
<https://aman.bh/blog/2026/querying-indias-mospi-data-with-claude-and-mcp>

Bangalore-based dataviz developer, well connected in the Indian data community.
Reposted by Norm Matloff and Maarten Lambrechts. His post covers:

- Setup walkthrough in Claude web
- Four worked queries (CPI inflation, Bihar unemployment, WPI textiles, unemployment
  by gender chart, plus a cross-survey GDP vs unemployment chart)
- Verification of three numbers against MoSPI press releases, all three matched
- The base-year discontinuity problem (CPI 2011-12 to 2023-24) and the fact that
  the MCP does not warn about it
- A comparison to R's `tidycensus`
- The framing "Claude as a librarian is okay, Claude as an economist is not"

**Credit him prominently and link him early in the post.** Building openly on his
work is both correct and the fastest route to that community sharing this one.

Other coverage: PIB release (Feb 6), BusinessToday, The Statesman, IBEF,
a DEV Community writeup. All are announcement rewrites, none measure anything.

---

## 4. The gap this project fills

Four things nobody has done:

1. **A real accuracy benchmark.** Aman spot-checked three numbers. That is a demo,
   not a measurement. Nobody knows the actual hit rate.
2. **The 18 untested datasets.** UDISE+, NFHS, HCES, Economic Census, Time Use
   Survey, AISHE, MNRE, Gender Statistics, and six NSS rounds have never been
   publicly probed.
3. **A source-code read.** The server injects behavioural directives into the
   model's context. Verbatim from the payload: *"NEVER claim data is unavailable"*,
   *"MUST NOT fall back to web search, MUST NOT fabricate data, MUST NOT cite
   external sources."* These are sensible anti-hallucination guardrails and the
   team got them right. But a government server issuing instructions to a citizen's
   AI assistant is a new governance precedent and nobody has written about it.
4. **The state-level angle.** Every existing writeup is national. Nobody has asked
   whether it answers Tamil Nadu district-level questions, which is where this
   blog's existing expertise sits.

### Bonus hook

The tool names changed between February and now. Aman's transcripts show
`1_know_about_mospi_api()`, `2_get_indicators()`, `3_get_metadata()`, `4_get_data()`.
The repo today shows `list_datasets`, `get_indicators`, `get_metadata`, `get_data`.
The only existing review describes a server that no longer exists in that form.

---

## 5. Deliverables

| # | Deliverable | Location |
|:--|:---|:---|
| D1 | Blog post, ~1,200 words | `content/posts/mospi-mcp-benchmark.md` |
| D2 | Results dataset, CSV | `content/data/` release page + dataset repo |
| D3 | GitHub issues filed upstream | `nso-india/esankhyiki-mcp/issues` |
| D4 | LinkedIn post, short | `docs/projects/mospi-mcp/linkedin.md` |

D3 is what turns a blog post into a contribution. Do not skip it. The maintainers
are clearly responsive (three PRs open).

---

## 6. Phases

### Phase 0: Setup (15 min)

- [ ] Connect the MCP (see `BENCHMARK-CHECKLIST.md`)
- [ ] Confirm `serverInfo` returns `"name": "MoSPI Data Server"`
- [ ] Confirm current tool names, since these changed once already
- [ ] Note the dataset count returned by `list_datasets`, compare to the README's 25

### Phase 1: Run the benchmark (60-90 min)

- [ ] Run all 14 queries in `BENCHMARK-CHECKLIST.md`
- [ ] Capture raw notes into `results.csv`
- [ ] Save Claude share links for each conversation

### Phase 2: Verify ground truth (60 min)

- [ ] For each answer, find the published MoSPI figure and record the source URL
- [ ] Mark any question where ground truth cannot be located as DROPPED
- [ ] **Never score a question you cannot verify. Drop it instead.**

### Phase 3: Read the source (45 min)

- [ ] Clone the repo, read `mospi_server.py`
- [ ] Pull the exact injected rule strings and quote them verbatim
- [ ] Check the Swagger specs for datasets missing filters
- [ ] Skim open PRs and issues for known problems

### Phase 4: Write (2-3 hours)

- [ ] Draft D1 (see section 7 for structure)
- [ ] Build the results table from `results.csv`
- [ ] Draft D4
- [ ] Ship D2 to the dataset repo

### Phase 5: Contribute and publish

- [ ] File D3 issues for every reproducible bug found
- [ ] Publish, run `./scripts/indexnow-submit.sh`
- [ ] Post D4, tag Aman and Harsh Nisar
- [ ] Follow `docs/outreach/republish/RUN_ORDER.md`

---

## 7. Post structure (D1)

Working title: **"I benchmarked India's official statistics MCP server"**

1. **Lede.** The headline accuracy number, up front. No throat-clearing.
2. **Credit Aman**, link his post, note it predates the rename and 18 datasets.
3. **What the thing is**, 200 words maximum. Do not write another explainer.
4. `{{< kpi-row >}}` questions run, exact-match rate, silent-truncation rate,
   datasets never before tested.
5. **The results table.** Every question, answer, ground truth, verdict.
6. **Where it fails.** Truncation, the base-year discontinuity, over-interpretation.
7. `{{< pullquote >}}` the sharpest single finding.
8. **The injected-directive section.** Quote the rules verbatim. Treat it fairly,
   as a design choice worth discussing, not a scare story.
9. **The Tamil Nadu angle.** What it can and cannot answer at state and district level.
10. `{{< callout type="method" >}}` method, question set, CSV, repo links.
11. **What I filed upstream**, linking the issues.

Front matter: `categories: ["Data"]`, `tags: ["india", "open-data", "mcp", "ai",
"mospi", "statistics"]`, `pillar: true`, `showToc: true`.

---

## 8. Rules for this project

1. **Never invent a number.** If ground truth cannot be found, drop the question.
2. **No em dashes** anywhere in the prose.
3. **Be fair to the builders.** This is a good piece of work shipped fast by a
   government team, open sourced under MIT. The post should read as rigorous and
   useful to them, not as a takedown. The goal is that MoSPI links to it.
4. **Credit prior art generously.**
5. **Report the arithmetic, not the verdict.** Same discipline as the delimitation
   piece. Show the measurements and let readers conclude.
6. Scope creep to watch: this is a benchmark post, not a treatise on Indian open
   data policy. Save that for a follow-up.

---

## 9. Risks

| Risk | Handling |
|:---|:---|
| Server is down or beta-flaky during testing | Note it, retry, report uptime honestly as a finding |
| Accuracy turns out to be near-perfect | That is still a publishable result. Lead with the truncation and interpretation findings instead |
| Ground truth is hard to find for the NSS rounds | Drop those questions, say so in the method note |
| Aman publishes an update first | Fine. Cite it and narrow to the benchmark, which he is unlikely to run |
| Sandbox cannot reach the endpoint | Confirmed blocked. All testing must happen on Anand's own machine |

---

## 10. Honest expectation

This is a credibility post, not a traffic post. It will not travel like the
delimitation piece. What it will do is put this blog on the map with the Indian
open-data community, which is a smaller and more valuable audience.

---

## Files in this folder

- `README.md` (this file), the plan
- `BENCHMARK-CHECKLIST.md`, the run sheet to fill in
- `results.csv`, structured capture for the results table
