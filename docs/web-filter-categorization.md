# Web filter categorization tracker

`ndranandraj.com` is blocked on many corporate networks because enterprise web
filters classify it as "Uncategorized" or "Newly Registered Domain" and most
corporate policies block both categories by default. The fix is to submit the
domain to each major filter vendor's reclassification portal and ask for the
"Personal Sites and Blogs" category (or each vendor's equivalent).

Most vendors process requests within 24 to 72 hours; corporate filters then
pick up the new category on their next signature update, usually within a
week. The slowest part of the loop is the time between submitting and the
signature reaching every customer.

This doc tracks which vendors have been submitted to and the status of each.

## Boilerplate to paste into each form

Copy-paste this when a form asks for "reason for request" or similar. Edit
the bracketed pieces only if the vendor's form has a specific dropdown for
the current category.

```
ndranandraj.com is a personal blog with a single individual author
(Anandraj R, ndr.anandraj@outlook.com). The site has been live since 2024
and covers data analysis, technology, travel, and photography. Recent
posts include analysis of the 2026 Tamil Nadu Assembly Election (see
/posts/tvk-debut-2026/) and personal essays.

The site has a clear About page at /page/about/ with identifying
information, a humans.txt at /humans.txt, valid HTTPS, no malware history
on Google Safe Browsing or VirusTotal, and is built from a public
codebase (Hugo + PaperMod). It is hosted on GitHub Pages with a
Cloudflare front.

Currently classified as [Uncategorized / Newly Registered Domain / other].
Requesting reclassification to "Personal Sites and Blogs" (or your
equivalent personal-blog category).

Domain owner contact: ndr.anandraj@outlook.com
```

## Vendor checklist

Fill in the Submitted column with the date you submitted. Fill in Response
when the vendor confirms. The last column is for any notes (e.g. specific
category they assigned, follow-up needed).

| Vendor | Used by (examples) | Submission URL | Submitted | Response | Notes |
|---|---|---|---|---|---|
| Cisco Talos | Cisco Umbrella, OpenDNS, Meraki | https://talosintelligence.com/reputation_center | | | Search domain, then "Request a reclassification" |
| Palo Alto PAN-DB | Palo Alto NGFW, Prisma Access | https://urlfiltering.paloaltonetworks.com/ | | | Look up URL, click "Request Change" |
| Fortinet FortiGuard | Fortinet firewalls, FortiClient | https://www.fortiguard.com/webfilter | | | Submit URL for review |
| Symantec / Broadcom (Sitereview) | Bluecoat, Symantec WSS, ProxySG | https://sitereview.bluecoat.com/ | | | Enter URL, click "Request Review" |
| Forcepoint (formerly Websense) | Forcepoint Web Security | https://csi.forcepoint.com/ | | | URL Lookup, then submit |
| Zscaler | Zscaler ZIA / ZPA | https://csbe.zscaler.com/submission | | | URL submission form |
| Trend Micro Site Safety | Trend Micro IWSVA, Apex One | https://global.sitesafety.trendmicro.com/ | | | Submit URL for safety rating |
| McAfee / Trellix TrustedSource | McAfee Web Gateway, SiteAdvisor | https://www.trustedsource.org/ | | | Submit URL |
| Sophos | Sophos XG / Web Appliance | https://support.sophos.com/support/s/filesubmission?type=URLReclassification | | | URL reclassification form |
| Cloudflare Radar / Family DNS | Cloudflare 1.1.1.1 family, Gateway | https://radar.cloudflare.com/domains/feedback/ndranandraj.com | | | Domain feedback form |

## Trust-signal checklist

These don't directly change filter categories, but they all help when a
vendor reviews the site manually.

- [x] `humans.txt` deployed at `https://ndranandraj.com/humans.txt`
- [ ] Search Console verified (token in `hugo.toml` `params.siteVerification.google`)
- [ ] Bing Webmaster Tools verified (token in `hugo.toml` `params.siteVerification.bing`)
- [ ] Internet Archive snapshot of homepage: visit https://web.archive.org/save and paste the URL
- [ ] Internet Archive snapshot of `/page/about/`
- [ ] Google Safe Browsing clean: https://transparencyreport.google.com/safe-browsing/search?url=ndranandraj.com
- [ ] VirusTotal clean: https://www.virustotal.com/gui/home/url
- [ ] Sucuri SiteCheck clean: https://sitecheck.sucuri.net/

## How to know which vendor is blocking you specifically

If a colleague is on a blocked network, ask them to share a screenshot of
the block page. Most filters display the vendor name and the category that
caused the block. Common examples:

- "This site is blocked by Cisco Umbrella under category 'Newly Seen Domains'"
- "URL filtering blocked: ndranandraj.com (Personal Sites)" → Palo Alto
- "Access denied by Zscaler. Categorization: Miscellaneous"

Once you know the vendor, the resubmission to that vendor is the highest
priority follow-up.

## Cadence

- **Day 0**: submit to all ten vendors in a single sitting (about 20 minutes
  total once the boilerplate is in your clipboard).
- **Week 1**: re-check from a previously-blocked network. Most vendors will
  have reclassified by now and signature updates should have propagated.
- **Week 2-4**: if still blocked, identify the specific vendor (block-page
  screenshot from someone on the blocked network) and resubmit with a more
  pointed message referencing the previous ticket.
- **Quarterly**: re-verify the site is still cleanly categorized at the
  vendors most relevant to your readers' employers. Re-categorization can
  drift if the site is dormant for long stretches.

## What to do if a vendor explicitly refuses to reclassify

Rare, but happens. Ask for the specific reason in their response. The most
common refusal reasons are:

1. **Content is borderline for a different category**. E.g. the TVK 2026
   election post might trip a "Politics" classifier. Argue that political
   *commentary and analysis* is not the same as *political advocacy* and
   that the site overall is general-interest.
2. **Domain history**. If `ndranandraj.com` was previously owned by someone
   else who got a bad reputation, ask the vendor to reset based on current
   ownership (provide WHOIS / domain registration date).
3. **Hosting reputation**. GitHub Pages / Cloudflare sometimes carries shared
   reputation. Reference that the domain has a unique apex record and a
   verified owner.
