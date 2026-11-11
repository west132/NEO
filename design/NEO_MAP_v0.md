# Neo — Rule map (v0)

Design note, not a play file. Every rule in RULES is listed with the loop step that calls it. A rule with no caller is cut or wired. Made Nov 11 after the whole-set audit.

## 1. Every RULES section and its caller

| RULES | What it does | Called from (GM) | Verdict |
|---|---|---|---|
| §1 The law | — | moved to GM §1 | **moved**: one top law, in the file read every turn |
| §2 Possibility | can it be done at all | §5.5 PC ACTION | keep |
| §3 Action form | the roll | §5.5 PC ACTION | keep |
| §4 Stakes | cost ladder, cost forms, reach | §5.5 PC ACTION | keep; owns the cost-forms list (was also in GM) |
| §5 Vitals | HP, damage, recovery | §5.5 PC ACTION · §5.1 REST | keep; **was not wired for rest** |
| §6 Gear tiers | the gear slot | §5.5 PC ACTION | keep |
| §7 Growth | evidence, tiers, class | tool on each roll · §5.1 REST (boundary) | keep; **boundary had no caller** |
| §8 Combat | batch fight, morale | §5.5 PC ACTION · §7 FIGHT | keep; owns the pause procedure (was also in GM) |
| §9.1 NPC answer | plan → settled → ask roll, torn | §5.5 NPC ANSWER | keep; sole owner (was also in GM, twice) |
| §9.2 Help | exists / 15+ with reach / no | §5.5 ASKS FOR HELP · §10.4 | keep; sole owner (was in four places) |
| §10 Quests | record, level, accept, close, codes | §5.2 NEW · §5.6 AFTERMATH | keep; sole owner of acceptance (was also in GM) |
| §11 Nerve | horror, marks, steps | §5.5 · §5.1 REST, DAY | keep; **day marks had no caller** |
| §12 Consequences, resources | payoffs, wear, supplies, prices, fatigue | §5.6 AFTERMATH · §5.5 SEEN · §5.1 REST | keep; **had no caller at all** |
| §13 XP | awards, levels | §5.6 AFTERMATH | keep; **had one passing mention** |
| §14 Item points | buy back skipped prep | §5.4 SPEND · §5.1 REST (refill) | keep; **had no caller** |
| §15.1 Actors | plans, dues, re-plan, relations, joining | §5.1 FIRES · §5.2 NEW · §5.6 AFTERMATH | keep; **temper roll and join aim had no caller** |
| §15.2 Time | the span, stop, fire | §5.1 TIME | keep; sole owner of the stop rule |
| §15.3 Encounters | surface, undercurrent | §5.1 FIRES | keep |
| §15.4 Places, stability | band, marks, steps | §5.2 NEW · §5.6 AFTERMATH · §5.1 DAY | keep; **marks had no caller** |
| §15.5 Pressures | tracks, clocks, check | §5.1 FIRES · §5.6 AFTERMATH | keep |
| §15.6 Cases | hidden truth, evidence, three routes | §5.5 SEEN | keep |
| §15.7 Witnesses | chain, response | §5.5 SEEN | keep |
| §15.8 Character | behaviour source, trait vs dice | §5.5 NPC v NPC | keep; judgement and enemies **moved** to GM §6 (narration owns them) |
| §15.9 Threads | the PC's long aims | §5.6 AFTERMATH | keep |
| §15.10 Endings | conditions, check | §5.6 AFTERMATH · §10.6 | keep |
| §16 The tool | form list | every → | keep |

Result: before the map, 8 of 25 sections were wholly or partly unreached from the loop (§5 rest, §7 boundary, §11 day marks, §12, §13, §14, §15.1 temper and joining, §15.4 marks). Now every section has at least one caller.

## 2. Duplicates collapsed (one rule, one home)

| Rule | Home now | Removed from |
|---|---|---|
| The top law (three ideas + I1–I12) | GM §1 | RULES §1 (now a pointer); GM "CORE" line |
| NPC answer order | RULES §9.1 | GM §5.5 |
| Torn NPCs | RULES §9.1 | GM §4 (keeps only how it shows) |
| Cost forms list | RULES §4 | GM §5.5 |
| Help rule | RULES §9.2 | GM §5.5, GM §10.4, WORLD §3 |
| Who is important | WORLD §11 | GM §5.1 |
| Always a due | RULES §15.1 | GM §5.1, WORLD §11 prose |
| Time stops at what could reach the PC | RULES §15.2 | GM §5.1 (keeps only the judging) |
| Quest acceptance | RULES §10 | GM §5.2 |
| Judgement, no pity for enemies | GM §6 | RULES §15.8 |
| Combat pause procedure | RULES §8 | GM §7 |
| Stakes shown | GM §5.3 | RULES §4 |
| Developing the unwritten | GM §10.4 | GM §5.5, WORLD §3, WORLD §11 |

## 3. Cut

| What | Why |
|---|---|
| GM §9 "Never" list (6 lines) | four were the law said again (I2, I4, I5, I9); one was the help rule. The two that lived nowhere else were kept and moved: "never swing to the opposite extreme" → GM §10.5; "never roll to avoid being the one who said yes" → RULES §9.1 |

## 4. Added

| What | Why |
|---|---|
| One precedence list (GM header ORDER) | three partial statements in three files, no single order |
| GM §9 Words | "material", "good rest", "established" and others were used and never defined |
| GM §5.1 TIME reworded | it said "the PC's action" at a step where no action exists yet |

## 5. Has a caller, but is it needed? — for the person to decide

Wired is not the same as needed. These carried rules run only in some worlds or rarely; none was cut, because nothing in the audit proves them dead.

| Rule | When it matters | Option |
|---|---|---|
| RULES §11 nerve and horror | settings with horror or a hidden layer | load only when the background uses it |
| RULES §5 MP and casting | settings with powers | same |
| RULES §13 OFF branch (no numeric levels) | a background that turns levels off | same |
| RULES §15.1 CANON MODE | canon-mode backgrounds only | same |
| RULES §15.1 NPC GROWTH | long campaigns with rivals | keep, or cut until a run needs it |
| RULES §15.9 development threads | a PC with a stated long aim | keep, or cut until a run needs it |
| RULES §12 food/water, usage dice | survival-pressure settings | keep, or make it a background switch |

## 6. Size

| | Before the map | After |
|---|---|---|
| GM | 27.7 KB | 31.4 KB |
| RULES | 59.7 KB | 57.3 KB |
| WORLD | 49.8 KB | 49.9 KB |
| Total | 137.5 KB | 138.6 KB |

The set did not shrink. The fault the audit found was wiring and ownership, not volume: the GM file grew because it now holds the law, the word list, and a call line for every rule it used to leave unreached. Section 5 is where real size could come out.
