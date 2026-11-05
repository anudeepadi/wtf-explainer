# Per-episode extraction schema (narrative layer)

Goal: we are building a skill that explains ANY concept in the style of Nikhil Kamath's "WTF is" podcast — first-principles, follow-the-money, architectural. We need the reusable *patterns*, not a summary of the episode. Quote at most a few short phrases (under 15 words each) as evidence; describe everything else in your own words.

Write the output as markdown with these sections:

1. **Concept & framing** — the one-line question the episode is really answering. How the title/cold open frames it (e.g. a paradox: "If UPI is free, who pays?").
2. **Cold open / hook** — how the first ~3 minutes work. Structure, not content (e.g. "sweeping history in 5 eras → present tension → open question → introduce guests as the people who built the last era").
3. **Question ladder** — the sequence of Nikhil's key questions across the episode, abstracted into *question types* (e.g. "Who pays?", "Walk me through what happens when I tap pay", "What would you build if you were 25 today?"). List 10–20 with timestamps and the type label.
4. **First-principles moves** — moments where a concept is rebuilt from the base. For each: timestamp, the move type (decompose into actors / follow a single transaction / unit economics / counterfactual "why didn't this exist before" / compare to another country / historical arc / ask the naive question), and a one-line paraphrase of the insight.
5. **Non-obvious insights** — 5–10 insights a smart outsider wouldn't already know. Paraphrase. Note what *made* each insight land (a number, a contrast, a story, an analogy).
6. **Analogies & metaphors** — list with timestamps.
7. **Numbers used for grounding** — how numbers are used (market size, per-unit economics, growth, comparison). Give 5–10 examples with the role they play.
8. **Visual cues in the dialogue** — timestamps where speakers say things like "let me draw", "if you look at this", "on the screen", "this chart", or where a whiteboard/diagram is clearly being referenced, or where a structured breakdown (a chain of actors, a stack, a 2x2, a timeline) is being described verbally. For each, describe what diagram archetype would represent it (value chain, money flow, layered stack, flywheel, 2x2, timeline, then-vs-now, unit-economics waterfall, map, comparison table, org/ecosystem map, other). Aim for 15–30 entries — this is the most important section.
9. **Arc of the episode** — the macro structure in 5–10 acts (e.g. personal journeys → system mechanics → economics → debate → future → "what would you build").
10. **Host persona techniques** — how Nikhil plays the role: naive questioner, devil's advocate, investor lens, personal confession, steering away from jargon, forcing simple answers, etc. Give examples by timestamp.
11. **Reusable template** — in 10 lines, how you'd re-use this episode's structure to explain a *different* concept.
