# Error ledger

Every claim I made about the MoSPI MCP server that was written down, looked
plausible, and was then checked. Published because the failures are the most useful
output of the project.

**Fourteen claims checked. Twelve were wrong.** One held up under challenge. One was
accurate when recorded and was overtaken two days later by MoSPI loading new data,
which is a different kind of failure and is counted separately.

Accompanies the post "I benchmarked India's official statistics server, and got
twelve things wrong" at ndranandraj.com.

---


**Fourteen claims** in this project were generated or recorded, then checked before
publication.

- **Twelve were wrong** at the time they were made: items 1 to 6, 8, and 10 to 14.
- **One was checked and held**: item 7.
- **One (item 9) was correct when made** and was overtaken by an upstream data
  update in the days since, a freshness drift rather than a reasoning error. It is
  kept separate for that reason.

All fourteen are listed because the survival, and the drift, are as informative as
the failures. **Use 14 checked / 12 wrong in any published tally.** Earlier figures
in this file ("nine claims, seven wrong", then "13 / 11") predate items 10 to 14 and
should not be quoted.

1. Their CI AI reviewer, on PR #33, via truncation
2. My source read of `mospi_server.py`, via truncation
3. My "22 datasets, README overstates" claim
4. My prediction that Q13 would truncate
5. The run's Q14 "CRITICAL silently dropped" finding
6. This audit's own "Q4 contradicts Q15" alarm, which dissolved on inspection
7. Q3's "136.5 Provisional, revised to 135.9 Final" claim, first written as an
   explanation rather than a quotation. A challenge asked for the alternative
   reading, that 135.9 might just be October's own index value misread as August's
   revision. Re-checked by column header and by DPIIT's own prose ("August, 2024
   (Final)") rather than by argument. The original claim held: August 2024 Final is
   135.9 in a distinct, clearly headed table column, not a misattributed October
   figure. This one is item 7 precisely because it turned out correct, a claim that
   needed a second independent check to survive the challenge is still worth
   recording, since the first pass had produced the right number for the wrong
   depth of evidence.

8. **The "deployment runs ahead of public `main`" claim.** Inferred from a
   truncated source read plus the observation that PR #33 was still open while
   NSS80 was live. It was about to be sent to MoSPI as a question. Killed by
   reading their CHANGELOG, which records NSS80 shipping under v2.3.0 and
   `[Unreleased]` taking the count to 25. An open PR is not an unmerged feature.
   **This is the most consequential catch in the ledger**, because the claim was
   one email away from being put to a government ministry, and the file that
   disproved it had been sitting in the repo root the whole time.

9. **The UDISE indicator-scoping claim (Q4 vs Q15), the intended lead finding —
   data freshness, not a wrong claim.** `Q15.txt`, run 2026-08-01, recorded
   `get_data(dataset="UDISE", indicator_code=2, state_code=25, year="2024-25")` →
   `{"data":[],"msg":"No Data Found"}`, and the transcript itself annotated this at
   the time as `"2024-25 not yet populated"`. Written up later as "the cleanest
   illustration" of the metadata defect and slated to lead the GitHub issue and the
   outreach email, without being re-queried in between. Re-run live on 2026-08-03,
   immediately before those went out, the identical call returned real data:
   12,518,167 total enrolments. The likeliest explanation is that UDISE loaded
   Tamil Nadu's 2024-25 figures sometime in the two-day gap, which means the
   original transcript was correct when it was written and even flagged its own
   uncertainty about it. **Distinct from items 1-6 and 8 above: those were
   fabrications, truncated reads, or reasoning that was wrong at the time it was
   made. This one was right at the time and was overtaken by an upstream data
   update — a freshness drift, not an error, and the ledger should not count it as
   the same kind of failure.** What still matters for this project: the finding
   could not be assumed to hold two days later without a fresh call, and the same
   live-re-query discipline as item 8 caught the drift before publication, again
   one step away from becoming a headline claim in an email to MoSPI.

### Items 10 to 13: found by a cold independent audit, 2026-08-03

A reviewer with no prior context on this project read every file and every
transcript. The four items below had survived every self-audit, including three
rounds in which I checked my own work and pronounced it sound.

10. **Both surviving findings cited transcripts that do not contain them.**
    `Q14.txt` does not contain the word `series` anywhere; `Q12.txt` holds an
    ellipsized paraphrase, not the verbatim string quoted in `ISSUES-DRAFT.md`. Both
    came from live re-queries that saved no artifacts, while the email offered to
    share the transcripts. **The most serious item in the ledger**, because the
    error would have been discovered by the recipient rather than by us.
11. **A replication claim that was not a replication.** Q13 was presented as
    failing to reproduce Aman's sampling finding. Different indicator, 513 records
    against his ~5,280, different client, and a prompt that explicitly forbade
    sampling and demanded counts.
12. **"Default mode" asserted where the mode was explicitly passed.** `Q7.txt`
    shows `mode:"detail"` supplied in the call. Nothing establishes what the
    Economic Census default is.
13. **Ground truth recorded as the server's own output.** `results.csv` had Bihar's
    published IMR as `46.76`, which is what the server returned. The fact sheet
    prints `46.8`. The row scored the server against itself.

14. **"All five issues are open with no comments", asserted after checking one.**
    On 2026-08-15 I fetched issue #49, saw the repo's "Issues 5" counter, and
    reported to Anand that all five were open and untriaged with no comments. A
    reviewer checking the others found **#52 carries a comment from an outside
    contributor**. The status claim was right for #49 and generalised without
    checking. Same shape as items 3 and 12: a correct local observation extended to
    a population that was never inspected. The draft now reads "all five remained
    open when I last checked; one had an outside-contributor comment; none had a
    maintainer response."

Item 13 also exposed 13a: **Tamil Nadu's IMR of 18.6 cannot be independently
confirmed.** Published summaries say "around 19", and the only source reproducing
`18.64` mirrors the same underlying data files. That corroboration is circular and
the figure is now marked provisional rather than matched.

Every one was caught by a deterministic check: a record count, a live re-query, a
published document, reading the second transcript, a column-header quotation,
a CHANGELOG, and finally by a reader with no stake in the conclusions.
**None was caught by more model output.**

The lesson from items 10 to 13 is narrower and more uncomfortable than the earlier
ones. Self-auditing found real errors repeatedly, and still missed four, including
the worst. What found those was not more rigour applied by the same reader; it was
a different reader who had not spent hours becoming attached to the conclusions.

That is the spine of the post. Items 6 and 7 prove the discipline works when
applied to itself, including when the self-check comes back clean. Item 8 proves
the cheapest check is often the one nobody ran: the answer was in a file named
CHANGELOG.md, in the repo root, from the first day of the project. Item 9 proves a
related but distinct point: even a claim that was accurate when recorded can go
stale, and the only way to know is to ask the live server again immediately before
publishing, not to trust even a two-day-old transcript. It is not evidence that the
original run was wrong, only that state changes and the check has to be re-run
close to publication.

---

