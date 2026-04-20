# Social distribution — TN-2026 Dummy Candidates

Two deliverables below:

1. **8-tweet X/Twitter thread** — ready to post. Each tweet is under 280 chars.
2. **10-slide LinkedIn carousel** — slide-by-slide copy + design notes.

Post timing: **Tuesday 9:00 AM IST** (highest engagement window for Indian political Twitter; catches US wake-up secondary wave at 11:30 PM PT).

---

## Part A — X / Twitter thread

> **1/** Perambur's ballot has FIVE candidates named Vijay.
>
> Alandur has FOUR candidates named Saravanan.
>
> I scraped 4,000 nominations from the ECI portal and ran a name-match across every constituency in TN. The result is a pattern that isn't a coincidence. 🧵

> **2/** The ECI Affidavit Portal lists every nominee for the 2026 Tamil Nadu Assembly Election. I pulled all 4,000. Cleaned the names. Ran a similarity match within each of the 234 constituencies.
>
> 77 seats have EXACT name duplicates. 100+ have near-matches.

> **3/** Textbook case: Perambur.
>
> Star candidate: C. Joseph Vijay (TVK).
> Also on the ballot:
>  • "Vijay" — AIJMK
>  • Vijay. G — Independent
>  • M. Joseph — Independent
>  • S. Joseph — Independent
>
> Four people carrying fragments of one man's name.

> **4/** Alandur is quieter but just as telling.
>
> ADMK candidate: S. Saravanan.
> Independents also contesting Alandur: A. Saravanan, D. Saravanan, R. Saravanan.
>
> None have a party machine. None have alliance backing. None will win. They exist to make voters hesitate at the EVM.

> **5/** The obvious question: is this a random sample of common names?
>
> It isn't. The dummies cluster disproportionately in seats where the 2021 margin was under 5%. That's not what random looks like. That's targeting.

> **6/** Why it matters: Tamil Nadu's 2026 election is shaping up to be the closest in a generation. TVK is a new entrant. DMK and ADMK are both leaking voters. In a tight three-way race, 2,000 confused votes can flip a seat.

> **7/** The ECI's own rules say ballot order is alphabetical within party/independent blocks. That makes the tactic cheap and reliable: pick a surname that sorts next to your target, file as an Independent, disappear after the count.
>
> It's legal. It's also manipulation.

> **8/** Full analysis + constituency-level breakdown:
> ndranandraj.com/posts/tn-2026-dummy-candidates/
>
> Raw dataset on GitHub (CC-BY) so anyone can verify, extend, or argue with the methodology:
> [GitHub link]
>
> If you cover TN politics and want the constituency list early, DM me.

### Design notes for the thread

- **Tweet 3 and Tweet 4** need image cards — use the Perambur and Alandur screenshots from the post (ballot mockups). Image cards roughly double engagement on data threads.
- **Tweet 5** benefits from a scatter plot (margin % vs number of namesakes) — generate one from the dataset before posting.
- Pin tweet 1 to your profile for a week.
- Reply to your own thread with a tweet quoting anyone who shares it — it boosts the algorithm.

### Seed audience (DM 12–24 hours before posting)

Prime the thread by sending a DM with "posting this tomorrow, thought you'd find it useful" — no ask attached. People who reply to the DM usually engage with the live thread.

- Savukku Shankar (@savukku)
- Rangaraj Pandey (@pandeyvarma)
- Shiv Aroor (@ShivAroor)
- Rohini Singh (@rohini_sgh)
- Nitin Sethi (@nit_set)
- Pratik Sinha (@free_thinker)
- The News Minute (@thenewsminute)
- BOOM Live (@boomlive_in)
- AltNews (@AltNews)
- Newslaundry (@newslaundry)
- Barkha Dutt (@BDUTT)
- Sreenivasan Jain (@SreenivasanJain)

---

## Part B — LinkedIn carousel (10 slides)

**Format:** 1080×1350 PDF carousel (upload as PDF document for maximum reach).
**Tone:** serious, analytical, professional — LinkedIn punishes Twitter snark.
**Fonts:** match your blog — Inter for headings, Merriweather for body.

### Slide 1 — Cover

```
Title: When the ballot has five candidates named Vijay
Subtitle: A data investigation into how dummy nominations
are being engineered in Tamil Nadu 2026
Byline: Anandraj — Software Engineer & Data Analyst
Visual: Mock EVM screen with five "Vijay" buttons
```

### Slide 2 — The question

```
Header: Is voter confusion being manufactured?
Body:
On 10 May, 6.2 crore Tamil Nadu voters will step into a booth.
On the ballot of 100+ constituencies, they will find multiple
candidates carrying the same name, sorted next to each other.
Is that a coincidence of common names — or a tactic?
```

### Slide 3 — Methodology

```
Header: How the dataset was built
Body:
• Source: ECI Affidavit Portal (public record)
• Scope: All 4,000 accepted nominations across 234 constituencies
• Method: Exact + fuzzy (Jaro-Winkler) name matching within each seat
• Null hypothesis: common names should distribute uniformly
Visual: A simplified flow diagram
```

### Slide 4 — Headline number

```
Header: 77
Body:
Constituencies where at least two candidates share an
EXACT name. 100+ more have near-matches (same first name,
different initial, for example).

That is 43% of the state's seats.
```

### Slide 5 — Perambur

```
Header: Case study 1 — Perambur
Body:
TVK's debut seat, starring C. Joseph Vijay. The ballot has:
• C. Joseph Vijay — TVK
• Vijay — AIJMK
• Vijay. G — Independent
• M. Joseph — Independent
• S. Joseph — Independent
Visual: Mock ballot or name list
```

### Slide 6 — Alandur

```
Header: Case study 2 — Alandur
Body:
ADMK's S. Saravanan faces three other Saravanans:
• A. Saravanan — Independent
• D. Saravanan — Independent
• R. Saravanan — Independent
No party machinery. No alliance. No campaign.
```

### Slide 7 — The pattern

```
Header: This is not random
Body:
Dummies cluster in constituencies where the 2021 margin
was under 5%. In seats won by 15%+, namesake Independents
are almost absent.

Random common names don't pick their targets.
Visual: Scatter plot (margin % vs namesake count)
```

### Slide 8 — Why it's allowed

```
Header: The loophole is procedural
Body:
Ballot order is alphabetical within each party/independent block.
A candidate whose surname lands next to the target's splits
the visual attention of any voter who reads fast.

It is legal. It is also manipulation.
```

### Slide 9 — What's at stake

```
Header: Why it matters in 2026
Body:
TN 2026 is a tight three-way race.
TVK is new. DMK and ADMK are both shedding base.
A 2,000-vote swing flips a 5%-margin seat.
100+ seats are in that margin zone.
```

### Slide 10 — CTA

```
Header: Read the full investigation
Body:
• Constituency-level breakdown
• Open dataset (CC-BY) on GitHub
• Methodology + reproducible notebooks

ndranandraj.com/posts/tn-2026-dummy-candidates/

"Follow" if you want data journalism like this in your feed.
Visual: QR code linking to the blog post + headshot
```

### LinkedIn caption (paste as the post body)

> Over the last two weeks I scraped every one of the 4,000 accepted candidate nominations on the ECI Affidavit Portal for the Tamil Nadu 2026 Assembly Election and ran a name-similarity analysis across all 234 constituencies.
>
> The result is a pattern that is hard to explain as coincidence: 77 constituencies have exact name duplicates among their candidates, and 100+ have near-matches. They cluster in seats where the 2021 margin was under 5%. Random common names do not pick their targets.
>
> A 10-slide summary is in the carousel. The full analysis — with methodology and the open dataset — is on my blog.
>
> https://ndranandraj.com/posts/tn-2026-dummy-candidates/
>
> Would love to hear how this maps to patterns readers have noticed in their own constituencies. Corrections, counter-examples, and additional data welcome.
>
> #TamilNadu #DataJournalism #Elections #ECI #OpenData

---

## Part C — Reddit plan (separate from thread)

Post the blog link (not the thread) to these subs, staggered by one hour so each post gets a proper front-page ride:

| Sub | Title | Notes |
|---|---|---|
| r/india | "Data: 77 Tamil Nadu constituencies have exact namesake candidates on the 2026 ballot" | No editorializing; the subreddit hates clickbait. |
| r/TamilNadu | "நமக்கு நம்பர் தெரியும்: 4,000 வேட்பாளர்கள் பட்டியலில் ஒரே பெயர்" (or English translation) | Bilingual title works well here. |
| r/chennai | "Perambur has five candidates named Vijay — and the data shows this isn't an accident" | City-specific framing. |
| r/IndiaSpeaks | Skip unless you want the comments section. |
| r/dataisbeautiful | Submit with the scatter plot from slide 7. | Requires OC tag and source. |

Each post: same top-comment with the dataset + methodology link.
