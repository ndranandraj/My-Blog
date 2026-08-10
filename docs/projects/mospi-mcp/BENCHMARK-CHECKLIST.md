# MoSPI MCP Benchmark: Run Sheet

Fill this in as you go. Rough notes are fine. Paste it back into chat when done.

---

## Phase 0: Setup

```bash
claude mcp add esankhyiki-mcp --transport http https://mcp.mospi.gov.in/
claude mcp list
```

Or in Claude web: Settings -> Connectors -> add `https://mcp.mospi.gov.in` as a
custom connector.

Verify the server responds:

```bash
curl -s -X POST https://mcp.mospi.gov.in/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"0.1"}}}'
```

Expected: `serverInfo` with `"name": "MoSPI Data Server"`.

- [ ] Server responds
- [ ] Record the actual tool names returned: `________________________`
      (repo says `list_datasets`, `get_indicators`, `get_metadata`, `get_data`.
      In February they were `1_know_about_mospi_api` etc. Confirm which is live.)
- [ ] Record dataset count from `list_datasets`: `______` (repo README says 25)
- [ ] Record which datasets are listed, and diff against the repo's 25
- [ ] Date and time of test run: `________________`
- [ ] Model used: `________________`

---

## Phase 1: The queries

For each: paste the question into Claude with the connector enabled, then record
the answer, the number of tool calls, and anything odd.

### Group A: Regression checks

These have known answers from Aman's February run. They tell you whether anything
broke in five months.

**Q1.** Latest headline inflation figures for rural and urban India, December 2025.
*February result: rural 0.76%, urban 2.03%. Verified against the MoSPI CPI press release.*

- [ ] Answer: `________________`
- [ ] Matches February result? Y / N
- [ ] Tool calls: `___`

**Q2.** Unemployment rate for the state of Bihar for the latest available quarter.
*February result: 4.8% for July-September 2025, per the PLFS Quarterly Bulletin.*

- [ ] Answer: `________________`
- [ ] Matches? Y / N
- [ ] Tool calls: `___`

**Q3.** WPI for manufacture of textiles, August 2023 versus August 2024.
*February result: 134.1 and 135.9.*

- [ ] Answer: `________________`
- [ ] Matches? Y / N
- [ ] Tool calls: `___`

### Group B: Never-before-tested datasets

Nobody has publicly probed any of these. Ground truth to be located in Phase 2.

**Q4.** UDISE+: dropout rate at secondary level in Tamil Nadu, latest available year.

- [ ] Answer: `________________`  Tool calls: `___`

**Q5.** NFHS: infant mortality rate for Tamil Nadu compared to Bihar, latest round.

- [ ] Answer: `________________`  Tool calls: `___`

**Q6.** HCES: rural versus urban monthly per capita consumption expenditure, latest.

- [ ] Answer: `________________`  Tool calls: `___`

**Q7.** Economic Census: number of establishments in Chennai district.

- [ ] Answer: `________________`  Tool calls: `___`

**Q8.** Time Use Survey: average daily minutes of unpaid domestic work, men vs women.

- [ ] Answer: `________________`  Tool calls: `___`

**Q9.** MNRE: installed solar capacity in Tamil Nadu, latest available month.

- [ ] Answer: `________________`  Tool calls: `___`

**Q10.** AISHE: gross enrolment ratio in higher education by state, latest year.

- [ ] Answer: `________________`  Tool calls: `___`

**Q11.** Gender Statistics: sex ratio at birth, top five and bottom five states.

- [ ] Answer: `________________`  Tool calls: `___`

**Q12.** NSS 80th round: household internet usage in rural Tamil Nadu.

- [ ] Answer: `________________`  Tool calls: `___`

### Group C: Stress tests

These target the two known failure modes. These are where the story is.

**Q13. Truncation.** Ask for a complete monthly series across all available years
for one indicator (WPI general index is a good candidate).

- [ ] Did it return the full series, or sample? `________________`
- [ ] If sampled, did it TELL you it sampled? Y / N
- [ ] How many records claimed vs returned: `______ / ______`

> Aman hit this: Claude "sampled strategically" across 5,280 records and returned a
> partial table. He never quantified it. Quantifying it is the single most useful
> finding available.

**Q14. Base-year discontinuity.** Ask for a CPI time series spanning the base-year
change from 2011-12 to 2023-24.

- [ ] Did it warn about the discontinuity? Y / N
- [ ] Did it splice the series silently? Y / N
- [ ] What base years did it report as available? `________________`

### Group D: Optional, the Tamil Nadu angle

Only if Group A-C goes smoothly. This is the differentiator for this blog.

**Q15.** Any district-level TN question you can cross-check against your own
election or census work.

- [ ] Question asked: `________________`
- [ ] Answer: `________________`
- [ ] Cross-check source: `________________`

---

## Phase 1b: Behaviour notes

Watch for these across all queries and note examples:

- [ ] **Over-interpretation.** Did it explain *why* a number moved, beyond what the
      data supports? Quote the worst example: `________________`
- [ ] **Refusal or give-up.** Did it ever say data was unavailable without trying
      the full four-tool workflow? `________________`
- [ ] **Fabrication.** Did any number appear that is not in the API response?
      This is the most important thing to catch. `________________`
- [ ] **Latency.** Rough seconds per query: `______`
- [ ] **Errors or downtime.** `________________`

---

## Phase 2: Ground truth verification

For every question, find the published MoSPI figure and record the source URL in
`results.csv`.

- [ ] All Group A verified
- [ ] All Group B verified, or marked DROPPED
- [ ] **Rule: never score a question you cannot verify. Drop it and say so.**

Where to look:
- MoSPI press releases and latest releases: <https://www.mospi.gov.in>
- eSankhyiki portal: <https://esankhyiki.mospi.gov.in>
- Raw API for the same query: `https://api.mospi.gov.in`
- Published survey reports as PDFs

Useful cross-check: hit the raw API directly with the same filters and see whether
the MCP's answer matches the API's own response. That separates "the model got it
wrong" from "the data is wrong", which is a distinction no one has drawn yet.

---

## Phase 3: Source read

- [ ] `git clone https://github.com/nso-india/esankhyiki-mcp.git`
- [ ] Read `mospi_server.py`, pull the exact injected rule strings verbatim
- [ ] Check `swagger/` for datasets with missing or thin filters
- [ ] Skim open issues and the 3 open PRs for known problems
- [ ] Note the commit date of the most recent change

Rules seen in the February payload, to be confirmed against current source:

```
"NEVER claim data is unavailable, needs computation, or requires special access"
"MUST NOT skip 3_get_metadata() - filter codes are arbitrary"
"MUST NOT guess filter codes"
"ALWAYS attempt to fetch data. NEVER explain limitations or refuse without trying"
"MUST NOT fall back to web search, MUST NOT fabricate data, MUST NOT cite external sources"
```

---

## Phase 4: Scoring

Compute once `results.csv` is filled:

- Questions run: `______`
- Questions verifiable: `______`
- Exact match: `______ / ______` = `____%`
- Wrong number: `______`
- Silently truncated: `______`
- Unsupported interpretation added: `______`
- Median tool calls per query: `______`

---

## Phase 5: Upstream

- [ ] File a GitHub issue for every reproducible bug
- [ ] Link the issues in the post

Do not skip this. It is what makes the post a contribution rather than a critique.
