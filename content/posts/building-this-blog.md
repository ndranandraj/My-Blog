---
title: "How I Built This Blog for ~$10/year"
date: 2026-04-05
draft: false
tags: ["tech", "hugo", "web"]
description: "A simple guide to setting up a personal blog with Hugo, GitHub Pages, and a custom domain."
---

If you're thinking about starting a personal blog but don't want to pay $10–$20/month for hosting — this is the setup I use. Total cost: just the domain name, roughly $10/year.

## The Stack

- **Hugo** — static site generator (free, open source)
- **GitHub Pages** — free hosting, directly from your repo
- **PaperMod** — clean, minimal Hugo theme (free)
- **Custom domain** — bought from Porkbun or Cloudflare (~$10/year)

## How It Works

You write blog posts in Markdown, push them to a GitHub repository, and GitHub Actions automatically builds and publishes your site. Your custom domain points to GitHub Pages.

That's the whole thing. No servers to manage. No WordPress updates. No hosting bills.

## Writing a New Post

Create a new file in `content/posts/` like `my-new-post.md` and add the front matter at the top:

```markdown
---
title: "My New Post"
date: 2026-04-05
tags: ["tag1", "tag2"]
---

Your content here...
```

Push to GitHub and it's live within seconds.

## Final Thoughts

This setup takes maybe an hour to get running, and then it basically takes care of itself. I spend zero time on maintenance and 100% of my time on writing (or not writing, as the case may be).
