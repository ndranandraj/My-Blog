---
title: "I benchmarked India's official statistics server, and got twelve things wrong"
date: 2026-08-16
lastmod: 2026-08-16
description: "India's statistics ministry shipped a server that connects AI assistants directly to official data. I spent two weeks testing it. Nothing I checked contradicted an official publication. My own claims about it mostly did not survive checking."
summary: "No value I checked on MoSPI's MCP server contradicted an official publication. Finding the data was the hard part. And the more useful story turned out to be how many of my own findings failed checking."
keywords: ["MoSPI", "MCP", "open data", "India statistics", "AI", "benchmark"]
tags: ["india", "open-data", "mcp", "ai", "statistics", "verification"]
categories: ["Data"]
pillar: true
readingTime: true
showToc: true
TocOpen: false
image: "/images/mospi-mcp-benchmark-cover.png"
cover:
  image: "/images/mospi-mcp-benchmark-cover.png"
  alt: "A magnifying glass over a data table, surrounded by index cards of charts and figures, most of them struck through with red crosses and circled corrections"
  caption: "Every value I checked held up. Twelve of my own claims about them did not."
  relative: false
---

In February, India's National Statistics Office did something unusual. It published
a server that lets you plug Claude or ChatGPT straight into official government
statistics, so you can ask a question in plain English and get back a real figure
from a real release rather than whatever the model half-remembers.

It is open source, MIT licensed, and it works.

I spent two weeks testing it. This is what I found, and it is not the post I
expected to write.

## The short version

**No value I checked contradicted an official publication.** Getting to those values
is the problem.

Across sixteen questions there was one answer I could fully support against a
published source, four I could support with qualifications, four where I checked
only a sample of the values returned, and seven I never verified at all. Every
problem I found was about discovery: metadata that describes something other than
what you asked for, error messages that blame the wrong thing, and codes that mean
different things in different places.

Then there is the other half of this post, which I think is the more useful half.
**Fourteen of my own claims about this server were written down, looked plausible,
and were then checked. Twelve of them were wrong.** The four worst survived three
rounds of me checking my own work and were caught only when someone with no stake in
it read the files.

## Credit where it is due

[Aman Bhargava](https://aman.bh/blog/2026/querying-indias-mospi-data-with-claude-and-mcp)
wrote the first hands-on review three days after launch, and it is the reason I
looked at this at all. Much of what follows builds on his work, and one of his
findings does not reproduce for me, which I get to below with more caveats than
conclusions.

Since he wrote, the server has grown from 7 datasets to 27, its tools have been
renamed twice, and a block of instructions it used to send the model has been
removed entirely.

## What the thing actually is

Ignore the acronym. In practice you paste one address into Claude's settings, and
from then on Claude can fetch real numbers from MoSPI instead of guessing.

Behind that, it offers four operations, meant to be used in order: list the
datasets, list what is in one, ask what filter values are valid, then fetch. Most
of what I found lives in the gap between the third step and the fourth.

## Results

Sixteen questions, each asked in its own fresh session so answers could not
contaminate each other. I checked the answers against official publications that I
downloaded and read, which included MoSPI and DPIIT releases, NFHS fact sheets,
Ministry of Education reports and Census material.

| How well it was checked | Count |
|:---|---:|
| Fully supported by a published source | 1 |
| Supported with a qualification | 4 |
| Sample of returned values checked | 4 |
| Not checked against any source | 7 |

That single fully supported answer is one question carrying two inflation figures,
rural and urban, both confirmed against the same release.

Two things about that table. It is a sample rather than coverage, since sixteen
questions touched a fraction of the catalogue. And what I measured is really the
assistant plus the server working together, because I drove it through Claude and
recorded what came out, not the raw traffic on every call.

I want to be plain about why so few are in the top row. It is not that the answers
were wrong. It is that an answer listing enrolment ratios for every state contains
thirty-seven numbers, and I checked two of them. Calling that an exact match would
be flattering myself.

## Two metadata defects I could confirm

These are two separate problems, not one pattern with two examples. They share a
symptom, but the mechanisms differ, and I originally wrote them up as a single
finding until a reviewer pointed out that this claimed more than the evidence
supported.

### The metadata does not answer the question you asked

Ask the server which years of inflation data exist, and it gives you a list. Ask it
the same question about a different edition of the same series, and it gives you an
identical list. Byte for byte identical, which I only noticed because I compared the
files.

That matters because the two editions genuinely cover different years. One starts in
2013. So the list tells you 2011 is available, you ask for 2011, and you get nothing
back, along with a message suggesting you check your codes against the very list
that sent you there.

The data is fine. The map to the data is wrong.

### It warns you about a problem it does not have

For one survey, the server returns a full set of valid filter values and, in the same
response, a note saying the upstream system returned no filter values and your
codes are probably out of range. Both things in one payload. The note is not describing
what it is attached to.

### Tamil Nadu has four different codes

This one is my favourite, because nothing is broken and it will still catch people
out.

Tamil Nadu is state 24 in three datasets, 25 in two, 32 in another and 33 in the
Economic Census. Every one of those is correct for its own dataset, inherited from
whichever survey it came from. But ask a question that spans two datasets, which is
exactly what a plain-English interface invites, and you can carry a code across and
get a confident answer about the wrong state. Not an error. A different state.

### Smaller things

The default page of results can hand you the parts without the total. Some responses
run to 145,000 characters. The wholesale price index uses a different code for the
same concept depending on which edition you ask for. And the education dataset has no
district filter, despite standing for Unified **District** Information System for
Education.

### One thing I asked about rather than concluded

Buried in the project's own changelog, under Security, is a line saying that one of
the operations no longer echoes your question back in its response, but that the
question "is still accepted and captured for telemetry."

That is MoSPI disclosing it themselves, in public, which is more than many services
do. It is also worth pausing on, because of what this thing is for. You are being
invited to connect a government endpoint to the assistant you use for everything
else, and what you ask it is logged. I could not find anything user-facing that says
so. Not the changelog, which is written for developers, but a note where someone
setting this up would actually see it.

I put that to MoSPI as a question rather than a finding, because there may well be a
notice I did not find, or one planned. No reply so far, so it stays a question.

I filed all of this as [issues #49 to #53](https://github.com/nso-india/esankhyiki-mcp/issues)
on 3 August and emailed the division that owns the server the same day.

Checking again on 16 August, thirteen days later: all five issues are still open, one
carries a comment from an outside contributor, none has a maintainer response, and
there is no reply in my inbox. That is a short window for a government repository and
I would not read much into it.

## The finding that did not survive

Aman found the assistant quietly sampling a large series and handing back a partial
table while implying it was complete. I tried to reproduce it and got all 513 records
with the totals stated.

I nearly published that as "fixed." It is not a replication. He tested a different
indicator with roughly ten times as many records, in a different client, and my
prompt explicitly said "all of it, not a sample" and demanded record counts, which is
close to telling the model not to do the thing I was testing for.

So: a large request behaved well under favourable conditions. That is all it shows.

## The part I actually want you to read

Fourteen claims in this project were written down, looked plausible, and were then
checked. **Twelve were wrong.** One held up under challenge. One was accurate when I
recorded it and was overtaken two days later by MoSPI loading new data, which is not
the same kind of failure and I count it separately.

I said the repository documented more datasets than the code had. Backwards; the code
had more. I predicted the truncation above and was wrong. A "CRITICAL" finding about
silently dropped data turned out to be a series that legitimately starts later. I
inferred that the running server was ahead of its public source code, and was one
email from putting that to a government ministry, when the file disproving it had
been sitting in the repository the whole time, in a file called CHANGELOG.

The last four were the worst, and none of them was caught by me. I had audited my own
work three times and pronounced it sound. What found them was a reader with no
attachment to the conclusions, who opened the files and checked whether they said
what I claimed. Two of my headline findings cited transcripts that did not contain
them. I described a "default" setting that had in fact been passed explicitly. And I
had recorded the server's own output as the published figure it was being checked
against, which is a benchmark grading itself.

Every single one was caught the same way: by a record count, a re-run, a published
document, or reading the second file. **None of them was caught by more thinking.**

There is a fashionable worry that AI tools hallucinate. The failure I kept hitting was
narrower and more awkward. The tool was usually right. My account of what the tool had
done was what kept being wrong, and it was wrong in ways that looked completely
reasonable until someone opened the file.

If you take one thing from this, take that. Not the accuracy score.

## What MoSPI got right

Shipping this openly under MIT is what made an independent benchmark possible at all.
The team also caught their own automated code reviewer hallucinating on a large diff
and rebuilt it, and removed a code path that was fetching from a third-party service.
Both are in their public changelog. They audit their own work in the open, which is
rarer than it should be, and it is the same discipline this post is about.

## Method

Sixteen questions, each in an isolated session. The benchmark transcripts record the
assistant's own account of each run, including what it said the server returned. For
the two metadata defects above I went back and captured the raw tool-level responses
directly, because a summary of a payload is not evidence about a payload, which is a
lesson this project learned the hard way.

Published alongside: the [scoring table](/mospi-benchmark/scoring-review.csv) with a coverage
column saying how many of how many values were checked per question, the
[evidence package](/mospi-benchmark/) of raw captures, and the full
[error ledger](/mospi-benchmark/error-ledger.md).

Where I could not source a figure, the question is marked unscored rather than
assumed correct. Where I checked a sample, it says how many of how many.

This is a small, non-random probe of a server that now carries 27 datasets. It is not
a server-wide accuracy rate and should not be read as one.

Corrections welcome, and given the above, expected.
