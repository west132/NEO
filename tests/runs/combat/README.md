# Combat test — 3 scenes × 2 worlds, 10 rounds each (Nov 13)

Six runs on the `design-tripod` branch. The play set is unchanged: GM, RULES, SAVE, modules and the tool. The stand-in player is Claude. Every roll, time step and save comes from `neo_math_v0.py`; each run ends with a merged and validated R10 save.

| Scene | AC Syndicate (new NEO conversion) | SCP Omega-99 |
|---|---|---|
| 1 Armed raid | `A1_stronghold_raid` — the cooperage yard, then Kaylock's counter-attack (13 a side) | `S1_storage_raid` — Darrow's storage unit |
| 2 Creature | `A2_mill_hazard` — no creatures in 1868 London; the mill's machinery as the danger | `S2_pigeons` — the SCP-3683 pigeons |
| 3 Public ambush | `A3_pub_raid` — the Blighters hit the Ten Bells | `S3_deer_ambush` — the deer cell on Route 9 |

Each folder holds `transcript.md` (with test notes and the run's own findings), `deltas.txt` (every GM-Δ block) and the R10 save. The fixtures start each run mid-campaign on a recorded due, so no hook was invented to make a fight.

## What the runs say about the three legs

**The tool's processing was accurate wherever it ran.** No roll, damage or merge came out wrong. Every save validated. The validate advisory list was the best drift catch in the set: it found resolved moves left open, and a whole thread a fixture skipped.

**Where the tool ran past a decision, or nearly did:**

1. **A1: a JSON-written location hid the PC's zone, so the span ran straight past Jacob's 21:00 move.** Nothing warned.
2. **A1: mass fights paused on nearly every exchange** (someone is always "badly hurt"); most pauses needed nothing.
3. **S3: the PC went from 7 to 2 HP in one exchange.** The tool did what the rule said: the plan holds until a real decision or fatal damage (0 HP). Since Nov 13 RULES §8 and the tool also stop when **the PC drops to half HP or below** (once, on crossing).

**Where the GM (thinking) slipped:** every slip was a missed step of the turn under combat load, never a wrong judgment call.

- No span during fights (A2, S3), so the world's moves were written in late.
- XP not paid and a quest not activated (A1).
- A mistyped XP number (S2), and a depth lowered when depth never goes down (S2).
- Stop conditions the player never gave (S2).
- A dead-weight man narrated walking (A3).

Each of these is something the tool could flag (processing), not something the GM text can prevent.

**Where the rules (the game) decided well:** morale from each side's norms, NPC answers from plans and fears, the possibility gate, "proof → settle again", the influence chain, the witness chains as dues. In four of six scenes the world turned the planned fight into something else (no gunfight at the storage unit; the deer called off the road attack; Kaylock died in a yard instead of on his train; the mill freed the children and cost a family its rent). That's the core idea holding: the world goes its own way.

## Same scene, two worlds

The scene types didn't carry across. AC 1868 has no creatures, so scene 2 became a hazard scene, and a hazard has no clock of its own: it only acts through a failed roll's cost. A beast acts every exchange. A test plan has to be written from each world's own threat list.

## Findings, by leg

**Tool (processing):**

- Pause when the PC takes a big hit or falls below a line, not only at 0 HP.
- In crowds, pause on the PC, named allies, leaders and falls, not on every badly hurt extra.
- Flag a won combat form with no XP award after it.
- Flag a quest objective being worked while the quest isn't active.
- Remember which zone has rolled this daypart, so `arrived` can't roll it twice.
- Roll the daypart that starts on the minute a span stops at.
- Give pending consequences a zone, so the span can judge whether they reach the PC.
- Read a record whether it's written as YAML flow or JSON, and warn when a record won't parse (silent misparse three times: A3, A1, S2).
- Check that an `ask` form's `who` is a recorded actor.
- Check the readable part exists before validate says `valid: true` (A1).
- Don't read "Day N" inside a `none (incidental; …)` due as a date.
- No travel between unrecorded zones; no shared clock between two batches at once.

**Rules (the game):**

- "Night" in a due is 21:00 to the tool but 00–06 in the daypart table.

Not rule gaps: these are the GM's calls (the runs' own notes listed them wrongly as gaps): how a mid-fight decision ends the round (the plan holds until a real decision or fatal damage), reading "reach" on a hit, striking a target who doesn't see you, using an action roll instead of the combat form for nets, tranquillisers or a tackle, bystanders under attack, a hazard acting, field first aid as treatment, and whether an undercurrent that is a due's own cause also rolls.

**GM (thinking):**

- Who fights whom in a batch was decided by the order the GM typed, not by the plan.
- Two quoting rules for GM-Δ (quote inside `{…}`, never at the top level).
- Background placeholder keys (`[ROLE …]`) can't be retired by GM-Δ.

## The new world

`worlds/BACKGROUND_AC_SYNDICATE_NEO_v0.md` is converted from the author's v6.3 file. It passes the tool's check. What the conversion invented (depth, voice, want, fear, line, secret, pull, belief for every NPC; quest codes; times of day on dues; three positions; ending conditions from the old chapter end) is listed for review in `worlds/AC_SYNDICATE_NEO_invented.md`. The author's word on it is final.
