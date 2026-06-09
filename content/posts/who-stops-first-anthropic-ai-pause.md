---
title: "Who stops first? Anthropic just asked the hardest question in AI"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "Anthropic says the world should have the option to slow down AI before it starts building itself. The idea sounds reasonable. The problem is that nobody wants to be the one who stops first."
summary: "Anthropic's new piece argues AI is now speeding up its own development, and that we may want a way to pause. But a pause only works if everyone stops together, and the incentives all point the other way. A look at why."
keywords: ["Anthropic AI pause", "recursive self-improvement", "when AI builds itself", "AI slowdown 2026", "AI prisoner's dilemma", "AI arms control", "Jack Clark Marina Favaro", "AI safety", "pause AI development", "AI race coordination"]
tags: ["AI", "tech"]
categories: ["Tech"]
pillar: true
readingTime: true
image: "/images/viki-irobot-cover.jpg"
cover:
    image: "/images/viki-irobot-cover.jpg"
    alt: "A glowing blue holographic face behind a wall of glass panels, evoking VIKI, the AI from the film I, Robot"
    caption: "VIKI from I, Robot. The version of the story everyone shared. The real post was a lot quieter."
    relative: false
---

For a couple of days, my X (Twitter) timeline would not stop pointing at one post by Anthropic. Everyone was deep in the doomsday version of it. And I kept wondering why the X algorithm was only feeding me the take where the world gets taken over, I, Robot style, machines like VIKI turning on us. So I did the boring thing. I stopped reading the hot takes and actually read the blog. These are my thoughts.

A bit about where I am coming from. I have spent close to two decades around mainframe systems, the kind that move slowly on purpose. You test, you wait, you test again, because getting it wrong costs real money and affects real people. "Slow down" is not a dirty phrase in my world. So a post from the people building the fastest-moving technology in history, asking for a way to slow down, caught my attention for reasons that had nothing to do with killer robots.

The post came out on June 4. It is called [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement), written by Jack Clark and Marina Favaro. The short version: AI is now helping build AI, that loop is getting faster, and the world should have the *option* to slow down before the loop closes completely.

It is a thoughtful post. But the part that stuck with me is not the warning. It is the trap hiding inside the solution.

## What they actually said

Let me give you the honest summary, because the headlines made it sound scarier than the post reads.

Anthropic is not saying the robots are about to take over. They are saying that more and more of the work of building AI is now done by AI itself. The proof is internal and pretty striking: as of May 2026, more than 80% of the code Anthropic merges into its own codebase is written by Claude, their AI model. The typical engineer now ships about eight times as much code per quarter as they did in 2024.

Push that trend far enough, they argue, and you reach something called *recursive self-improvement*: an AI system capable of designing and training its own successor, with humans mostly watching. We are not there. They are clear about that. But they think it could arrive sooner than most governments and institutions are ready for.

So their ask is modest on the surface. Not "stop now." Just: build the ability to slow down or pause, so that safety research and society can catch up if we need them to.

Reasonable, right? Here is where it gets hard.

## The catch: a pause only works if everyone stops together

A pause is not like a light switch in your house. One lab hitting the brakes does almost nothing on its own.

Anthropic says this part plainly, which I respect. If one careful company slows down while everyone else keeps sprinting, all that happens is the careful company falls behind. The lead passes to whoever cared the least about stopping. The technology does not get safer. It just gets built by the people least interested in slowing down.

So a real pause needs multiple top labs, in multiple countries, all agreeing to stop under the same conditions, at the same time. And here is the harder part: each one has to be able to *verify* that the others actually stopped.

If you have read my piece on [the AI layoff trap](/posts/the-ai-layoff-trap/), this shape will feel familiar. It is a Prisoner's Dilemma again. Everyone is better off if they cooperate. But each individual player is better off defecting, quietly, while the others hold back. And when everyone reasons that way, nobody stops at all.

## Why "just verify it" is so much harder for AI

We have done arms control before. The world built treaties to count missiles and inspect warheads. So why not do the same for AI?

Because AI hides better than a missile.

A missile silo is a giant hole in the ground. A satellite can see it. A training run is just software running on chips inside a building that looks like every other data center. The two things it needs, computer chips and electricity, are the same everyday stuff that powers Netflix and your bank. There is no smoke, no launch, no obvious sign.

Anthropic makes this point directly. Catching someone who secretly kept training is much harder than spotting a missile, and the reward for cheating is huge. Whoever keeps going while everyone else pauses takes the lead. So there is a strong reason to cheat quietly, and only a weak way to catch anyone who does.

They also note the timeline problem. The arms control regimes we do have, like the old nuclear treaties, took decades to build the trust and the inspection machinery. Anthropic's whole point is that we may not have decades. The technology is moving faster than the diplomacy ever has.

## The part I keep coming back to

What I appreciate about this post is that it does not pretend the answer is easy. It is a company saying, in public, "here is a thing we might want to do, and here is exactly why it is really hard to pull off, including for us."

That honesty is rare. Most AI announcements are confident to the point of being annoying. This one is closer to a confession.

But honesty does not solve the dilemma. You can describe the trap perfectly and still be standing inside it. Anthropic knows this too, which is why their actual proposal is not "everyone pause now." It is smaller and more practical: start building the verification tools and the international conversations now, so that *if* we ever need a credible pause, the machinery exists. A brake that nobody has installed is not much use in an emergency.

From where I sit, having watched big institutions try to coordinate on far simpler things than this, I am not optimistic it happens quickly. Getting a handful of fierce competitors in different countries to stop at the same moment, and trust that the others really stopped, is one of the hardest coordination problems I can think of. But I would rather we start arguing about how to build the brake now than go looking for it on the way down the hill.

## The bottom line

Anthropic asked a fair question: should the world be able to slow AI down before AI starts building itself?

The uncomfortable answer is that we technically could, but the incentives are arranged so that almost nobody wants to be the one who stops first. A pause that only one player honors is not a pause. It is just a handoff.

That does not make the idea worthless. It makes it urgent. The time to build a brake is before you need it, not while you are already rolling.

Whether we actually do is, like most things with AI right now, an open question. I just think it is the right one to be asking.

---

*Read Anthropic's original piece here: [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) by Marina Favaro and Jack Clark (June 2026).*
