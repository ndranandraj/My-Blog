---
title: "How I Built a Spelling Bee App for My Daughter (and Why This Win Feels a Little Bit Mine Too)"
date: 2026-04-06
lastmod: 2026-04-06
draft: false
tags: ["AI", "Claude", "web development", "PWA", "parenting", "side project", "JavaScript"]
categories: ["Tech"]
description: "I'm a Mainframe/COBOL developer who had never built a web app. Then my daughter needed to practice for her school Spelling Bee — so I built one with Claude as my AI pair programmer."
keywords: ["spelling bee app", "Claude AI", "AI pair programming", "progressive web app", "COBOL developer builds web app", "side project parenting"]
image: "/images/spelling-bee-daughter.jpg"
cover:
    image: "/images/spelling-bee-daughter.jpg"
    alt: "Champion with the Spell Bee Practice App"
    caption: "The champion herself, with the app she used to get there."
---

Earlier this year, my daughter won her school Spelling Bee. Every single word.

{{< figure src="/images/spelling-bee-daughter.jpg" alt="Champion with the Spell Bee Practice App" caption="The champion herself — medal, trophies, and the app she used to get there." >}}

And honestly, this win feels a little bit mine too. Let me tell you why.

I am a Mainframe developer. COBOL, JCL, batch processing — that has been my world for years. Web apps, mobile apps? Completely foreign territory.

Back in January, my daughter came home excited about her school Spelling Bee. She needed to practice. A lot. We started by looking for apps in the App Store, but nothing quite fit what we needed. Some were too basic, others were cluttered with features that got in the way. And somewhere between being a frustrated parent and a curious developer, I thought... what if I just build something for her?

So I did.

## The App

With Claude as my AI pair programmer, I built the **Spell Bee Practice App** from scratch.

The app reads out words at multiple speeds so she could hear every syllable, pulls real-time definitions from the Merriam-Webster Dictionary API, lets you upload your own word list or type words in manually, and tracks progress as you go. It works as a Progressive Web App with separate versions optimized for mobile and iPad. And the whole thing lives in a single HTML file. No backend. No build process. Deployed free on GitHub Pages.

## The Honest Part

I could not have built this alone. Tailwind CSS, async API calls, the Web Speech API, PWA manifests — all new to me. But Claude did not just write code. It explained the reasoning behind every decision and flagged things I would never have considered. It felt less like using a tool and more like working with someone who knew what they were doing and had the patience to bring me along.

We built the whole thing conversationally, one feature at a time, inside a single Claude Project.

## What This Changes (and What It Doesn't)

I have written before about how AI is not a magic wand — especially when it comes to complex legacy modernization, where the real challenges are organizational, not technical. I still believe that.

But this experience showed me the other side. When the scope is clear, the motivation is real, and you are willing to think through every decision yourself, AI can genuinely help you build something meaningful in a space you have never worked in before.

You do not need to know everything before you start building. Sometimes a single HTML file is all you need. And the best motivation for any side project? Someone you love depending on it.

The app is live and the code is open below. Go build something for someone you love. 🐝

**Live App & Repo:** [github.com/ndranandraj/spellbee-mobile-enhanced](https://github.com/ndranandraj/spellbee-mobile-enhanced)
