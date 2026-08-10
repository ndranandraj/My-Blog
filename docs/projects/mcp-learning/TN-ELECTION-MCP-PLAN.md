# Plan: TN 2026 Election MCP Server

**Rung 5 of the learning track. The main event.**

Working name: `tn-election-mcp`
Deliverable: a working MCP server, plus a blog post about building it.

---

## 1. Why this is the right project to learn on

You already own the data, so no scraping, no permissions, no API keys. It is small
enough to hold entirely in memory, which removes a whole category of complexity.
And the questions people actually ask about election data are exactly the kind that
a natural-language interface is good at and a dashboard is bad at.

Nobody has published an Indian election MCP server.

---

## 2. The data you already have

All in `static/election-dashboard/data/`, roughly 1.3 MB total. Real schemas,
verified:

| File | Shape | Contents |
|:---|:---|:---|
| `explorer_ac_2026.json` | `{as_of, source, per_ac[234]}` | Winner, runner-up, votes, share, margin per AC |
| `all_candidates_2026.json` | `{as_of, source, rows[4257]}` | Every ballot row: candidate, party, votes, share, position |
| `winners_2021.json` | `{as_of, rows[234]}` | 2021 winners with runner-up |
| `swing_2021_to_2026.json` | `{as_of, rows[234]}` | Nested `winner_2021` / `winner_2026`, `flipped`, `share_swing_pp` |
| `defeated_incumbents_2026.json` | `{totals, beaten_by_party_2026, rows[179]}` | Situation-coded incumbent outcomes |
| `new_assembly_profile_2026.json` | `{overall, party_profiles[12], youngest_*, women_*}` | Age, education, assets, gender |
| `party_efficiency_2026.json` | `{total_seats, total_votes, parties[14]}` | Vote share vs seat share, efficiency ratio |
| `regional_all_parties_2026.json` | `{regions[9]}` | Cross-party breakdown by the custom 9-region geography |
| `dummy_near_misses_2026.json` | `list[25]` | Dummy-candidate near misses |
| `tvk_*` (4 files) | various | TVK-specific cuts, largely derivable from the above |

**Design consequence:** load everything into memory at boot. No database, no cache
layer, no async I/O. That is a gift for a first server, because it means every hard
problem you hit will be a *tool design* problem rather than an infrastructure one.

### Known data hazards to handle explicitly

- **AC name spelling is inconsistent across files.** `Gummidipoondi` in
  `explorer_ac_2026`, `GUMMIDIPOONDI` in `swing_2021_to_2026`, `GUMMIDIPUNDI` in
  `defeated_incumbents_2026` and `winners_2021`. Same for districts
  (`Thiruvallur` vs `TIRUVALLUR`).
- **`ac_no` is the only reliable join key.** Build every internal lookup on it.
- **`dummy_near_misses_2026.json` stores numbers as strings.** Coerce at load.
- Resolve names through a normalisation function plus fuzzy matching, and always
  return `ac_no` alongside the name so callers can be certain what they got.

This normalisation layer is the first real design lesson of the project.

---

## 3. Tool design

The MoSPI server needs enforced four-step sequencing because its API has thousands
of arbitrary filter codes that no model could guess. **Your dataset is small and
fixed, so you should not copy that pattern.** The entire schema fits in the tool
descriptions, which means you can offer a handful of direct, well-documented tools
and skip the discovery dance entirely.

Recognising when *not* to copy the reference implementation is the point of doing
Rung 2 first.

### Proposed tools (6)

| Tool | Signature sketch | Answers |
|:---|:---|:---|
| `get_constituency` | `(name_or_ac_no)` | Everything about one seat, 2021 and 2026 side by side, all candidates, swing, incumbent fate |
| `search_candidates` | `(name?, party?, district?, region?, position?, min_share?)` | "Every candidate named Stalin", "all TVK runners-up in Kongu" |
| `party_summary` | `(party)` | Seats, vote share, efficiency ratio, regional breakdown, demographic profile |
| `list_flips` | `(from_party?, to_party?, region?, district?, min_swing?)` | "Which seats went DMK to TVK", sorted by swing |
| `defeated_incumbents` | `(party?, district?, situation?)` | The 179 rows, filtered |
| `assembly_profile` | `(party?)` | Age, education, gender, assets, with the youngest and oldest lists |

Plus one **resource** (not a tool): a data dictionary describing every field,
the 9-region geography definition, and provenance. Resources are for context the
model should have; tools are for actions. Getting that distinction right is worth
the ten minutes it takes to read the spec section on it.

### Tool design rules to follow

1. **Write docstrings for the model, not for a human.** State exactly what each
   parameter accepts, give example values, and say what the tool returns.
2. **Always return `ac_no` and `as_of`.** Identity and provenance in every response.
3. **Never return more than about 50 rows without saying so.** Include
   `returned`, `total_matched`, and a hint about narrowing. This is the exact
   failure you are documenting in the MoSPI benchmark, so do not reproduce it.
4. **Fail loudly and usefully.** An unknown party name should return the valid list,
   not an empty result. Empty results are how models start inventing.
5. **No tool should require another tool to have run first.** If you find yourself
   wanting that, the tool is under-specified.

---

## 4. Stack

Match the reference implementation so Rung 2 transfers directly:

- Python 3.11+, FastMCP
- Plain `json` at load, `dataclasses` or Pydantic for response shapes
- `pytest`, tests running in-process against the server, no live server needed
- Optional: OpenTelemetry, so you can point Jaeger at your own server the way you
  did at MoSPI's in Rung 3

```
tn-election-mcp/
  server.py            # FastMCP server, the 6 tools
  data/
    loader.py          # load + normalise the 13 JSON files at boot
    names.py           # AC/district name normalisation and fuzzy matching
    schema.py          # response dataclasses
  resources/
    data_dictionary.md # served as an MCP resource
  tests/
  Dockerfile
  README.md
```

Keep it a **separate repo**, not inside the blog. Either its own, or a folder in
the existing Election-Analysis sibling repo so the data and the server ship together.
The latter is probably better: the JSON files are already there and mirroring is
already a documented workflow.

---

## 5. Milestones

### M1: It loads (1-2 hrs)
- [ ] Repo scaffolded, FastMCP installed
- [ ] All 13 JSON files load at boot
- [ ] Name normalisation working, `ac_no` join verified across all files
- [ ] One trivial tool (`get_constituency`) returns real data over stdio

### M2: The six tools (3-4 hrs)
- [ ] All six implemented
- [ ] Row caps and `total_matched` on every list-returning tool
- [ ] Helpful errors on unknown party, district, constituency
- [ ] Data dictionary served as a resource

### M3: Tests (1-2 hrs)
- [ ] In-process pytest covering every tool
- [ ] Regression tests on known facts: TVK 108 seats, Stalin lost Kolathur,
      DMK 133 to 59, Chennai 31 to 2, TVK efficiency ratio 1.32
- [ ] A test that asserts row caps actually cap

### M4: Adversarial testing (1-2 hrs)
This is the most valuable milestone and the one most people skip.
- [ ] Ask Claude 20 questions and record where it misuses the tools
- [ ] Every misuse is a docstring bug, not a user error. Fix the docstring.
- [ ] Re-run. Iterate until misuse rate is near zero.
- [ ] Try to make it state something false. Note what let it.

### M5: Ship (2-3 hrs)
- [ ] HTTP transport, Dockerfile
- [ ] Deploy: FastMCP Cloud is the low-friction option
- [ ] Public endpoint, connect instructions in the README
- [ ] MIT licence, matching MoSPI's example
- [ ] Link it from the TN 2026 Explorer page and the dataset release page

### M6: Write it up (2-3 hrs)
- [ ] Blog post, see section 7

---

## 6. Security notes

A public MCP server has a real attack surface, and given the hardening pass in
June, this should not be an afterthought.

- **Read-only by construction.** No writes, no filesystem, no shell. The data is
  static JSON loaded once at boot.
- **Rate limiting** at the edge. An unauthenticated public endpoint invites abuse.
- **Cap response sizes.** Both to protect the model's context and to stop the server
  becoming a bulk-download vector. The whole dataset is public anyway, so link the
  CSV rather than letting anyone dump it 50 rows at a time.
- **Data is not instructions.** Candidate names come from ECI records, but treat
  every string as untrusted anyway and never interpolate them into anything that
  gets executed. Escape on the way out, exactly as `esc()` does in the Explorer.
- **No PII beyond what ECI already publishes.** Candidate names, parties, votes,
  declared assets and education are all public record. Do not add anything else.

---

## 7. The blog post

Working title: **"I built an MCP server for Tamil Nadu's election data"**

Angle: not a tutorial. A design writeup. The interesting content is the decisions,
not the code.

1. The problem: a dashboard answers the questions you anticipated, a CSV answers
   none of them until you write code.
2. What MCP actually is, briefly, aimed at readers who have not met it.
3. **The design decision worth the post:** MoSPI needed forced four-step sequencing.
   You did not. Explain why, because it teaches the reader when each pattern applies.
4. The name normalisation mess. Three spellings of Gummidipoondi is a good, concrete,
   funny detail and it is the kind of thing every real data project hits.
5. Adversarial testing: the questions that broke it and the docstring fixes.
6. What it can and cannot do. Be explicit that it does not reason, it retrieves.
7. Connect instructions, so readers can use it in 60 seconds.

Front matter: `categories: ["Data"]`, `tags: ["mcp", "ai", "elections",
"tamil-nadu", "open-data", "python"]`, `showToc: true`.

This should publish **after** the MoSPI benchmark post, and link back to it. Two
posts, one arc: measured someone else's, then built my own.

---

## 8. Success criteria

You are done when someone who has never seen your dataset can connect the server
and correctly answer "who lost Kolathur and by how much" in one question, without
you explaining anything.
