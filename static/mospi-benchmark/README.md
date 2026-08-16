# Release package

This folder makes the benchmark's evidence and scoring rules explicit without
rewriting the historical August run.

## Contents

- `scoring-review.csv` is the publication scoring layer. It reclassifies each
  original result according to the support actually documented in this workspace.
- `SHA256SUMS` fixes the identity of the original run transcripts and the primary
  verification captures at the time of this release review.

## Scope

The original run has 16 question rows. It touches 14 dataset codes, but only seven
of those datasets have a result with any ground-truth assessment. The questions are
purposeful usability probes, not a random or stratified sample of the catalogue.

The release therefore evaluates the assistant-plus-server retrieval path, including
metadata and pagination behaviour. It is not a direct audit of upstream source data,
nor a server-wide accuracy estimate.

## Scoring convention

- `full_exact` means every material value in the recorded answer is supported by the
  cited source at the required precision.
- `qualified_match` means the values appear consistent but a stated caveat prevents
  an unqualified exact label.
- `partial` means the source supports part of the answer but not the exact claim that
  was asked or returned.
- `spot_check` means selected observations were checked, with the checked count
  recorded. It is not an exhaustive answer-level match.
- `unscored` means the server returned an answer but no ground-truth assessment is
  recorded.

## Reproduction

Use `../capture-live-evidence.sh` to run the current inventory and the two filed
metadata checks in fresh sessions with stream JSON capture. It is intentionally not
a full rerun of the historical benchmark, because a live rerun would measure a
changed server and data catalogue.
