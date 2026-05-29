#!/usr/bin/env python3
"""
Generate one static Hugo page per Tamil Nadu 2026 constituency from the
dashboard data files. Build-time generation: every page is plain markdown
with content baked in, so it renders as server-side HTML that search
engines index fully. Reuses the existing kpi / kpi-row / callout shortcodes
and the framed-table CSS already shipped on the blog.

Usage:
    python3 scripts/gen-constituency-pages.py            # all 234
    python3 scripts/gen-constituency-pages.py 1 13 50    # only these ac_no (POC)

Regenerate whenever the sibling Election-Analysis data files change.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "static" / "election-dashboard" / "data"
OUT  = ROOT / "content" / "tn-2026-results"
PUBLISH_DATE = "2026-05-04"  # results day

EXPLORER_URL = "/election-dashboard/tn-2026-explorer.html"


def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def load():
    per = json.load(open(DATA / "explorer_ac_2026.json"))["per_ac"]
    cand = json.load(open(DATA / "all_candidates_2026.json"))["rows"]
    swing = json.load(open(DATA / "swing_2021_to_2026.json"))["rows"]
    cand_by_ac = {}
    for r in cand:
        cand_by_ac.setdefault(r["ac_no"], []).append(r)
    swing_by_ac = {r["ac_no"]: r for r in swing}
    return per, cand_by_ac, swing_by_ac


def yaml_escape(s):
    return s.replace('"', "'")


def build_page(ac, cands, sw):
    name = ac["ac_name"]
    winner, wparty = ac["winner_candidate"], ac["winner_party"]
    second, sparty = ac["second_candidate"], ac["second_party"]
    share, margin, mpct = ac["winner_share"], ac["margin"], ac["margin_pct"]
    total = ac["total_votes"]
    district, region = ac["district"], ac["region"]

    title = f"{name} Election Result 2026: {winner} ({wparty}) Wins"
    desc = (f"{winner} of {wparty} won {name} in the Tamil Nadu 2026 Assembly "
            f"election with {share}% of the vote, defeating {second} ({sparty}) "
            f"by a margin of {margin:,} votes.")
    summary = (f"{name} ({district} district) result for the 2026 Tamil Nadu "
               f"Assembly election: {winner} ({wparty}) won {share}% of {total:,} "
               f"votes, a margin of {margin:,} ({mpct}%) over {sparty}.")

    # swing context: short line for the lead, richer table for its own section
    if sw:
        w21, w26 = sw["winner_2021"], sw["winner_2026"]
        flipped = sw.get("flipped")
        swing_pp = sw.get("share_swing_pp")
        if flipped:
            swing_line = (f"The seat **flipped from {w21['party']} to "
                          f"{w26['party']}** since 2021.")
        else:
            swing_line = f"{w26['party']} held the seat it won here in 2021."
        swing_kpi = (f'{{{{< kpi value="{w21["party"]} → {w26["party"]}" '
                     f'label="2021 → 2026 winner" tone="{"warn" if flipped else "muted"}" >}}}}')
        pp_txt = (f"a swing of {swing_pp:+.2f} percentage points in the winning "
                  f"vote share" if swing_pp is not None else "")
        swing_section = (
            f"| Year | Winning candidate | Party | Vote share |\n"
            f"|:---|:---|:---|---:|\n"
            f"| 2021 | {w21['candidate']} | {w21['party']} | {w21['share']}% |\n"
            f"| 2026 | {w26['candidate']} | {w26['party']} | {w26['share']}% |\n\n"
            f"{'The seat changed hands' if flipped else 'The same party retained the seat'}, "
            f"{pp_txt}.")
    else:
        swing_line = ""
        swing_kpi = ""
        swing_section = "No 2021 comparison is available for this seat."

    # candidate table (sorted by position)
    rows = sorted(cands, key=lambda r: r["position"])
    table = ["| # | Candidate | Party | Votes | Vote % |",
             "|---:|:---|:---|---:|---:|"]
    for r in rows:
        mark = " **" if r.get("winner") else " "
        cand_name = f"**{r['candidate']}**" if r.get("winner") else r["candidate"]
        table.append(f"| {r['position']} | {cand_name} | {r['party']} | "
                     f"{r['votes']:,} | {r['share']}% |")
    table = "\n".join(table)

    fm = f"""---
title: "{yaml_escape(title)}"
date: {PUBLISH_DATE}
description: "{yaml_escape(desc)}"
summary: "{yaml_escape(summary)}"
slug: "{slugify(name)}"
constituency: "{yaml_escape(name)}"
ac_no: {ac['ac_no']}
district: "{yaml_escape(district)}"
region: "{yaml_escape(region)}"
keywords: ["{yaml_escape(name)} election result 2026", "{yaml_escape(name)} 2026 winner", "Tamil Nadu 2026 {yaml_escape(district)}"]
ShowReadingTime: false
ShowToc: false
---
"""

    body = f"""
{winner} of {wparty} won the {name} Assembly constituency ({district} district, {region}) in the Tamil Nadu 2026 election, taking {share}% of {total:,} votes cast. The winning margin over {second} ({sparty}) was {margin:,} votes, or {mpct} percentage points. {swing_line}

{{{{< kpi-row >}}}}
{{{{< kpi value="{wparty}" label="Winning party" tone="primary" >}}}}
{{{{< kpi value="{share}%" label="Winner vote share" tone="accent" >}}}}
{{{{< kpi value="{margin:,}" label="Margin ({mpct}%)" tone="good" >}}}}
{swing_kpi}
{{{{< /kpi-row >}}}}

## Full candidate results, {name} 2026

{table}

## How {name} compares to 2021

{swing_section}

This page is part of the full [Tamil Nadu 2026 election results]({{{{< ref "/tn-2026-results" >}}}}) set. Explore every seat, party efficiency, regional swing and demographics in the [TN 2026 Explorer]({EXPLORER_URL}). For the wider story, see [TVK's debut mapped]({{{{< ref "/posts/tvk-debut-2026" >}}}}), [the incumbents who lost]({{{{< ref "/posts/tn-2026-incumbents-defeated" >}}}}), and [how DMK collapsed]({{{{< ref "/posts/dmk-collapse-2026" >}}}}).
"""
    return slugify(name), fm + body


def main():
    only = set(int(x) for x in sys.argv[1:]) if len(sys.argv) > 1 else None
    per, cand_by_ac, swing_by_ac = load()
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for ac in per:
        if only and ac["ac_no"] not in only:
            continue
        slug, page = build_page(ac, cand_by_ac.get(ac["ac_no"], []),
                                swing_by_ac.get(ac["ac_no"]))
        (OUT / f"{slug}.md").write_text(page, encoding="utf-8")
        n += 1
    print(f"Wrote {n} constituency pages to {OUT}")


if __name__ == "__main__":
    main()
