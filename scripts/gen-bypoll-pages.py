#!/usr/bin/env python3
"""
Generate the Tamil Nadu by-election results section: one static Hugo page per
bypoll seat plus the section index, from the bypoll data files mirrored from the
Election-Analysis repo (static/election-dashboard/data/bypoll_*.json, written by
that repo's pipeline 29).

Same approach as gen-constituency-pages.py: content is baked into markdown so
search engines index it fully, using the existing kpi shortcodes and the
cand-table styles.

Usage:
    python3 scripts/gen-bypoll-pages.py

Re-run whenever a bypoll_*.json file changes or a new one is added.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "static" / "election-dashboard" / "data"
OUT = ROOT / "content" / "tn-bypoll-results"
DASHBOARD_URL = "/election-dashboard/bypolls-2026.html"

LABEL = {"TVK": "TVK", "ADMK": "AIADMK", "DMK": "DMK", "BJP": "BJP", "NTK": "NTK",
         "CPM": "CPI(M)", "CPI": "CPI", "INC": "INC", "IND": "IND", "NOTA": "NOTA",
         "BSP": "BSP", "PMK": "PMK", "LEFT": "Left", "OTHERS": "Others"}
NAME_FIX = {"S.KANITHASAMPATH": "S. Kanitha Sampath",
            "MARAGATHAM KUMARAVEL.K": "K. Maragatham Kumaravel"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def nice_name(n):
    """ECI prints 'SATHYABAMA.P' or 'K.MARAGATHAM KUMARAVEL'; show 'P. Sathyabama'."""
    if n in NAME_FIX:
        return NAME_FIX[n]
    initials, words = [], []
    for part in n.split("."):
        for w in part.split():
            (initials if len(w) <= 2 and w.upper() != "DR" else words).append(w)
    name = " ".join("Dr." if w.upper() == "DR" else w.capitalize() for w in words)
    return (" ".join(f"{i.upper()}." for i in initials) + " " + name).strip()


def fmt_in(n):
    """Indian digit grouping: 1,85,292."""
    s = str(abs(int(n)))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        s = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head) + "," + tail
    return ("-" if int(n) < 0 else "") + s


def long_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def badge(code):
    """Short party codes as a coloured badge; long full names as muted text
    (same rule as gen-constituency-pages.py's party_cell)."""
    lab = LABEL.get(code, code)
    if len(lab) <= 9:
        return f'<span class="pbadge" data-party="{lab}">{lab}</span>'
    return f'<span class="pname">{lab.title()}</span>'


def esc(s):
    return s.replace('"', "'")


def candidate_table(s):
    namesakes = {n["name"]: n for n in s.get("namesakes", [])}
    trs = []
    for c in s["candidates"]:
        nota = c["party_code"] == "NOTA"
        cls = []
        if c["position"] == 1:
            cls.append("winner")
        elif c["position"] == 2:
            cls.append("runner")
        if c["pct"] < 1:
            cls.append("minor")
        tag = ""
        if c["position"] == 1:
            tag = ' <span class="rtag win">Winner</span>'
        elif c["position"] == 2:
            tag = ' <span class="rtag run">2nd</span>'
        if c["name"] in namesakes:
            tag += f' <span class="rtag">Namesake of {nice_name(namesakes[c["name"]]["of"])}</span>'
        cls_attr = f' class="{" ".join(cls)}"' if cls else ""
        trs.append(
            f'<tr{cls_attr}><td class="rank">{"" if nota else c["position"]}</td>'
            f'<td class="cand">{"NOTA" if nota else nice_name(c["name"])}{tag}</td>'
            f'<td class="pcell">{"" if nota else badge(c["party_code"])}</td>'
            f'<td class="num">{fmt_in(c["evm"])}</td><td class="num">{fmt_in(c["postal"])}</td>'
            f'<td class="num">{fmt_in(c["total"])}</td><td class="num share">{c["pct"]:.2f}%</td></tr>')
    trs.append(f'<tr><td class="rank"></td><td class="cand"><b>Total</b></td><td></td><td></td>'
               f'<td class="num">{fmt_in(s["postal_votes"])}</td><td class="num"><b>{fmt_in(s["total_votes"])}</b></td><td></td></tr>')
    return ('<div class="cand-table-wrap">\n<table class="cand-table">\n'
            '<thead><tr><th class="rank">#</th><th>Candidate</th><th>Party</th>'
            '<th class="num">EVM</th><th class="num">Postal</th><th class="num">Total</th>'
            '<th class="num">Vote&nbsp;%</th></tr></thead>\n<tbody>\n' + "\n".join(trs) +
            '\n</tbody>\n</table>\n</div>')


def comparison_table(s):
    y, sw = s["y2021"], s["swing"]
    rows = ["| Party | 2021 | May 2026 | Oct 2026 bypoll | Change since May |",
            "|:---|---:|---:|---:|---:|"]
    for k in ("TVK", "ADMK", "DMK", "BJP", "NTK", "LEFT", "OTHERS", "NOTA"):
        a21, may, octo = y["shares"].get(k, 0) or 0, sw[k]["april_pct"], sw[k]["bypoll_pct"]
        if not (a21 or may or octo):
            continue
        cell = lambda v: f"{v:.2f}%" if v else "did not stand"
        ch = f'{sw[k]["delta_pp"]:+.2f} pts' if (may or octo) else "n/a"
        rows.append(f"| {LABEL[k]} | {cell(a21)} | {cell(may)} | {cell(octo)} | {ch} |")
    a = s["april2026"]
    rows.append(f'| **Winner** | {LABEL[y["winner"]["party_code"]]} by {fmt_in(y["margin"])} ({y["margin_pct"]:.2f}%) '
                f'| {LABEL[a["winner"]["party_code"]]} by {fmt_in(a["margin"])} ({a["margin_pct"]:.2f}%) '
                f'| **{LABEL[s["winner"]["party_code"]]} by {fmt_in(s["margin"])} ({s["margin_pct"]:.2f}%)** |  |')
    rows.append(f'| **Votes polled** | {fmt_in(y["total_votes"])} | {fmt_in(a["total_votes"])} | {fmt_in(s["total_votes"])} |  |')
    rows.append(f'| **Turnout** | {y["turnout_pct"]:.2f}% | {s["turnout"]["april_pct"]:.2f}% | {s["turnout"]["bypoll_pct"]:.2f}% |  |')
    return "\n".join(rows)


def rounds_table(s):
    T = s.get("timeline") or []
    if not T:
        return "Round-by-round figures were not saved for this seat."
    rows = ["| Round | TVK | DMK | AIADMK | Leader | Lead |", "|---:|---:|---:|---:|:---|---:|"]
    for t in T:
        v = t["votes"]
        rows.append(f'| {t["round"]} | {fmt_in(v["TVK"])} | {fmt_in(v["DMK"])} | {fmt_in(v["ADMK"])} '
                    f'| {LABEL.get(t["leader"], t["leader"])} | {fmt_in(t["lead"])} |')
    return "\n".join(rows)


def build_seat(s, data):
    name, w, r = s["ac_name"], s["winner"], s["runner_up"]
    wn, rn = nice_name(w["name"]), nice_name(r["name"])
    wl, rl = LABEL[w["party_code"]], LABEL[r["party_code"]]
    a = s["april2026"]
    slug = f"{slugify(name)}-by-election-{s['count_date'][:4]}"
    poll, count = long_date(s["poll_date"]), long_date(s["count_date"])
    title = f"{name} By-election Result 2026: {wn} ({wl}) Wins by {fmt_in(s['margin'])} Votes"
    desc = (f"{wn} of {wl} won the {name} by-election, counted on {count}, with {w['pct']:.2f}% of the vote, "
            f"defeating {rn} ({rl}) by {fmt_in(s['margin'])} votes ({s['margin_pct']:.2f}%). "
            f"Full candidate list, round-by-round count, and comparison with May 2026 and 2021.")
    summary = (f"{name} by-election {s['count_date'][:4]}: {wn} ({wl}) won by {fmt_in(s['margin'])} votes "
               f"({s['margin_pct']:.2f}%). In May 2026 the {LABEL[a['winner']['party_code']]} won the seat by "
               f"{fmt_in(a['margin'])}.")
    flip = next((i for i, t in enumerate(s.get("timeline") or []) if t["leader"] == w["party_code"]), 0)
    T = s.get("timeline") or []
    if T and flip > 0:
        count_line = (f"{LABEL.get(T[0]['leader'], T[0]['leader'])} led the first {T[flip - 1]['round']} "
                      f"round{'s' if T[flip - 1]['round'] > 1 else ''}; {wl} led from round {T[flip]['round']} "
                      f"to the end of the {T[-1]['round']}-round count.")
    elif T:
        count_line = f"{wl} led in every one of the {T[-1]['round']} rounds."
    else:
        count_line = ""
    ns = s.get("namesakes") or []
    ns_line = ""
    if ns:
        parts = ", ".join(f"{nice_name(n['name'])} ({fmt_in(n['votes'])} votes, sharing a name with "
                          f"{nice_name(n['of'])})" for n in ns)
        ns_line = (f"\n\nThe ballot carried {len(ns)} independent{'s' if len(ns) > 1 else ''} sharing a main "
                   f"candidate's name: {parts}. Together they polled {fmt_in(s['namesake_votes'])} votes, "
                   f"against a margin of {fmt_in(s['margin'])}.")

    fm = f"""---
title: "{esc(title)}"
date: {s['count_date']}
description: "{esc(desc)}"
summary: "{esc(summary)}"
slug: "{slug}"
constituency: "{esc(name)}"
ac_no: {s['ac_no']}
district: "{esc(s['district'])}"
poll_date: {s['poll_date']}
winner: "{esc(wn)}"
winner_party: "{wl}"
margin: {s['margin']}
margin_pct: {s['margin_pct']}
keywords: ["{name} by-election result {s['count_date'][:4]}", "{name} bypoll result", "{name} bye election {s['count_date'][:4]}", "{name} bypoll winner", "{esc(wn)}", "{name} election result October {s['count_date'][:4]}", "{s['district']} bypoll {s['count_date'][:4]}"]
image: "/images/tn-bypolls-oct2026-cover.png"
ShowReadingTime: false
ShowToc: false
---
"""
    body = f"""
{wn} of {wl} won the {name} Assembly by-election ({s['district']} district, reserved for Scheduled Castes), taking {w['pct']:.2f}% of the {fmt_in(s['total_votes'])} votes polled. The margin over {rn} ({rl}) was {fmt_in(s['margin'])} votes, or {s['margin_pct']:.2f}% of votes polled. Polling was on {poll} and the votes were counted on {count}.

{{{{< kpi-row >}}}}
{{{{< kpi value="{wl}" label="Winning party" tone="accent" >}}}}
{{{{< kpi value="{w['pct']:.2f}%" label="Winner vote share" tone="primary" >}}}}
{{{{< kpi value="{fmt_in(s['margin'])}" label="Margin ({s['margin_pct']:.2f}%)" tone="good" >}}}}
{{{{< kpi value="{s['turnout']['bypoll_pct']:.2f}%" label="Turnout" sub="May 2026: {s['turnout']['april_pct']:.2f}%" tone="muted" >}}}}
{{{{< /kpi-row >}}}}

## Why {name} went to a by-election

In the May 2026 general election the {LABEL[a['winner']['party_code']]}'s {nice_name(a['winner']['name'])} won {name} by {fmt_in(a['margin'])} votes ({a['margin_pct']:.2f}%). On {long_date(s['vacated_on'])} the MLA resigned and joined TVK, which fielded {s['defector']} again in the same seat. {"The defecting MLA won the seat back on TVK's ticket." if s.get('defector_won') else ""} The {LABEL['ADMK']} finished {"third" if s.get('third') and s['third']['party_code'] == 'ADMK' else "behind the winner"}.

## Full candidate results, {name} by-election {s['count_date'][:4]}

{candidate_table(s)}{ns_line}

## {name}: 2021, May 2026 and the by-election

{comparison_table(s)}

The 2021 figures are the ECI's, as published by OpenCity. Percentages are of all votes polled, NOTA included. A party marked "did not stand" had no candidate in that election.

## How the count went

{count_line} Cumulative votes after each EVM round, from the ECI results pages saved during counting:

{rounds_table(s)}

## More on this by-election

- The May 2026 result for this seat: [{name}, May 2026](/tn-2026-results/{slugify(name)}/)
- Every by-election, with the seats still vacant: [Tamil Nadu by-elections 2026](/tn-2026-bypolls/)
- Charts, the count and all candidates: [the bypoll dashboard]({DASHBOARD_URL})
- The analysis: [Two AIADMK defectors won their seats back on TVK's ticket](/posts/tn-bypolls-2026-madurantakam-dharapuram/)

*Source: Election Commission of India. Turnout figures are the ECI's polling-day numbers as reported by DT Next, The News Minute and Free Press Journal.*
"""
    return slug, fm + body


def build_index(all_seats, vacancies):
    rows = ["| Seat | District | Polled | Winner | Margin | May 2026 |", "|:---|:---|:---|:---|---:|:---|"]
    for s in sorted(all_seats, key=lambda x: (x["count_date"], x["ac_no"]), reverse=True):
        slug = f"{slugify(s['ac_name'])}-by-election-{s['count_date'][:4]}"
        a = s["april2026"]
        rows.append(f"| [{s['ac_name']}]({{{{< ref \"/tn-bypoll-results/{slug}\" >}}}}) (AC {s['ac_no']}) | {s['district']} "
                    f"| {long_date(s['poll_date'])} | {nice_name(s['winner']['name'])} ({LABEL[s['winner']['party_code']]}) "
                    f"| {fmt_in(s['margin'])} ({s['margin_pct']:.2f}%) | {LABEL[a['winner']['party_code']]} by {fmt_in(a['margin'])} |")
    vac = ["| AC | Seat | May 2026 winner | Status |", "|---:|:---|:---|:---|"]
    for v in vacancies:
        vac.append(f"| {v['ac_no']} | [{v['ac_name']}](/tn-2026-results/{slugify(v['ac_name'])}/) "
                   f"| {nice_name(v['april_winner'])} ({LABEL.get(v['april_party'], v['april_party'])}) | {v['status']} |")
    n = len(all_seats)
    tvk = sum(1 for s in all_seats if s["winner"]["party_code"] == "TVK")
    latest = max(s["count_date"] for s in all_seats)
    return f"""---
title: "Tamil Nadu By-election Results 2026: Every Bypoll, Seat by Seat"
description: "Results of every Tamil Nadu Assembly by-election since the May 2026 general election: winner, party, margin, full candidate list, round-by-round count and comparison with May 2026 and 2021 for each seat."
summary: "Every Tamil Nadu Assembly by-election since May 2026, seat by seat: winner, margin, all candidates, the count, and how each seat voted in May 2026 and 2021."
keywords: ["Tamil Nadu by-election results 2026", "TN bypoll results", "Tamil Nadu bypoll result list", "TN by-election winners 2026", "Madurantakam bypoll result", "Dharapuram bypoll result"]
date: {latest}
lastmod: {latest}
ShowReadingTime: false
ShowToc: false
---

Every Assembly by-election held in Tamil Nadu since the May 2026 general election, with a full results page for each seat: the winner, the margin, every candidate's EVM and postal votes, the round-by-round count, and how the same seat voted in May 2026 and in 2021.

{{{{< kpi-row >}}}}
{{{{< kpi value="{n}" label="By-elections held" tone="primary" >}}}}
{{{{< kpi value="{tvk} / {n}" label="Won by TVK" tone="accent" >}}}}
{{{{< kpi value="{len(vacancies)}" label="Seats still vacant" tone="muted" >}}}}
{{{{< /kpi-row >}}}}

## Results

{chr(10).join(rows)}

## Seats still vacant

No poll dates have been announced for these seats. Each will get a results page here when it votes.

{chr(10).join(vac)}

For the analysis, comparisons and charts, see [Tamil Nadu by-elections 2026](/tn-2026-bypolls/) and the [bypoll dashboard]({DASHBOARD_URL}). For the general election, see the [results for all 234 seats](/tn-2026-results/).
"""


def main():
    files = sorted(DATA.glob("bypoll_*.json"))
    all_seats, vacancies = [], []
    OUT.mkdir(parents=True, exist_ok=True)
    for f in files:
        d = json.loads(f.read_text(encoding="utf-8"))
        if not d.get("all_declared"):
            print(f"Skipping {f.name}: not all results declared")
            continue
        for s in d["seats"]:
            slug, page = build_seat(s, d)
            (OUT / f"{slug}.md").write_text(page, encoding="utf-8")
            all_seats.append(s)
        vacancies = d.get("vacancies", vacancies)  # the newest file's list wins
    (OUT / "_index.md").write_text(build_index(all_seats, vacancies), encoding="utf-8")
    print(f"Wrote {len(all_seats)} bypoll pages and the index to {OUT}")


if __name__ == "__main__":
    main()
