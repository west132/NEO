# Combat test S3 — SCP Class of '99: the Route 9 ambush corridor (public ambush)

Test of the NEO play set on the `design-tripod` branch, with the SCP Omega-99 background and the modules file. The stand-in player is Claude; every roll, time step and save comes from the tool.

**Test start (fixture):** Day 12, 17:15, New Jersey pine barrens. Sam West as in S1–S2. Quest K (`buck_stops_here`) assigned by Rosa on Day 11 (her pace, "by Day 20 at the latest"). The deer network's Day 10 moves are marked as done: the coordinator visited the new cell, and the pressure advanced once (pine barrens undercurrent tension −1). The cell leader's bare `Day 12` due is given its place and time from the pressure's own trajectory ("attacks during the evening rush"): `K-2 Day 12 18:15 hits the Route 9 corridor`. The NJ team's lead is developed as Agent Vega. West is issued a tranquilliser rifle for the op (the background's calibration).

**Scene:** public ambush. The deer cell's attack on cars at the evening rush. The public are the drivers; the team is there to stop it.

---

## Round 1

**▶ Player:** Where do you want me, Agent Vega?

```text
ROUND 1 | Day 12 | 17:30 | Route 9, the pine barrens | saved R0 · save R10

GM-Δ 1 ⟵ 0
  + player.routines.road_watch :: posted at the Cedar Run curve with Rosa, tranquilliser rifle, radio to Vega
  ~ npcs.marisol_vega.state.due :: K-1s road watch posted; K-1 Day 12 21:00 ends the watch
  + locations.cedar_run_curve :: the Cedar Run curve, Route 9, zone pine_barrens; two lanes through pines, a sand pull-off, rush traffic both ways
  ~ world_state.time :: Day 12 17:45, afternoon
```

"The Cedar Run curve," Vega says, without looking up from her tablet. "It's where they've hit twice. You and Delgado on the pull-off. Tranq the big one if he shows. Don't shoot anything that isn't about to go through a windshield. The Ethics Committee reads these reports, and so do I."

The curve is a long bend of two-lane road through pitch pines, with a sand pull-off and a deer-crossing sign someone has shot full of buckshot. The evening rush is starting: headlights coming home from Atlantic City, one car every few seconds.

*[test note: the PC moved into a newly recorded spot inside the same zone, and the GM passed `arrived: true` for it, so **the tool rolled pine barrens' afternoon surface encounter a second time** (17:15 and 17:45, both nothing). `arrived` should only be passed on entering a new zone, and the tool doesn't check whether that zone already rolled this daypart. The evening undercurrent roll (contact: out during its hours on its site, the sand roads at the evening rush) came up nothing.]*

---

## Round 2

**▶ Player:** I glass the pine edge on the far side. I'm looking for deer that are watching the traffic instead of eating.

```text
ROUND 2 | Day 12 | 17:45 | the Cedar Run curve | saved R0 · save R10

2d10: 4+7 | Capability: +0 | Tool: +0 | Total: 11
Difficulty: 11 [sensory +1: dusk and headlights flaring off the trees] | Stakes: setback/full | Outcome: Success

GM-Δ 2 ⟵ 1
  ~ player.skills.field_investigation.evidence :: 1
  + locked_case_truths.stag_case.state.tonight :: two scout does on the far shoulder; Twelve-Point and five attacker bucks in the pines, waiting for the signal at the 18:15 peak
  + npcs.stag_cell_east_attackers :: five attacker bucks, depth 0, level 2
  + npcs.stag_cell_east_scouts :: two scout does, depth 0, level 1
  + player.knowledge.facts.cell :: two does watching cars; behind them a twelve-point buck and five more bucks standing dead still
  ~ world_state.time :: Day 12 18:05, evening
```

At first it's just trees and headlights. Then you see her: a doe on the far shoulder, a hundred yards up, head up, ears turning to every engine that passes. She isn't eating. Another one twenty yards on, doing the same.

Behind them, in the dark between the pines, are shapes that are too still. Five bucks, side by side. And in front of them a big one with a rack like a hat stand: twelve points, nose up, watching the road.

The traffic is getting heavier. The radio says it's six o'clock.

*[test note: success at full reach = the true picture, developed now and recorded as the case's state before it was shown. The background's numbers: the cell leader at level 4; attackers and scouts at the band's low end, from "scouts flee and warn; attackers commit and rarely survive; cell leaders withdraw to save the herd".]*

---

## Round 3

**▶ Player:** (radio) Vega, cell at the Cedar Run curve: one big buck, five more, two scouts. Rosa, flashers on and slow the traffic down to a crawl. I'm putting a dart in the big one now, before they move.

*[test note: the PC's side acts first (seen at R2). Action form: tranquilliser, firearms T1 with the scope (fit good +1) against Twelve-Point (level 4). Sensory +1 (dusk, pines, headlights) and position +1 (a hundred yards across moving traffic) → Difficulty 12. A miss can't hurt the PC; the cost is a setback: the cell knows it's seen. Then the cell's choice: their norms pull both ways ("attackers commit" against "cell leaders withdraw to save the herd") → `ask`: for +1, +1; against −2.]*

```text
ROUND 3 | Day 12 | 18:05 | the Cedar Run curve | saved R0 · save R10

2d10: 1+7 | Capability: +0 | Tool: +1 [scoped tranquilliser rifle] | Total: 9
Difficulty: 12 [sensory +1: dusk, pines, headlights flaring; position +1: a hundred yards across two lanes of moving traffic] | Stakes: setback/full | Outcome: Failure
stag_cell_leader_east — 2d10: 1+5 | Likelihood: +0 [for: attackers commit; it is the nature of the cell +1; the rush traffic is right in front of them +1; against: cell leaders withdraw to save the herd when threatened -2] | Total: 6 → NO, AND

GM-Δ 3 ⟵ 2
  ~ player.equipment.tranq_rifle.special_properties :: five darts left
  ~ npcs.stag_cell_leader_east.state.due :: K-2f the 18:15 hit called off; K-2 Day 12 18:30 leads the cell back through the pines toward the bogs
  ~ npcs.stag_cell_leader_east.state.plan :: withdraw to the bogs; move the corridor away from the curve
  + world_state.pending.network_warned :: the scouts carry it back; the coordinator will move the next corridor; due Day 15 evening
  ~ npcs.rosa_delgado.state.plan :: flashers on; traffic slowed past the curve
  ~ world_state.time :: Day 12 18:08, evening
```

Rosa's flashers go on and the cars slow, brake lights in a red chain round the curve.

You take the shot. The dart goes into a pine trunk a foot above the big buck's back. He swings his head round and looks straight across the road at you, and you'd swear, though it's a deer, that he knows exactly what you are.

Then he snorts once. The two scout does turn and go up into the trees like smoke. The five bucks behind him turn as one, and the whole cell melts away into the pines, not running, walking, in single file.

The traffic crawls on past the curve. Nobody in it saw anything at all.

*[test note: NO, AND = they don't attack, plus the smallest trouble their side can make: the network learns this curve is watched, and its next attack moves somewhere else (written as a pending consequence with a due). **The public ambush didn't happen.** As in S1, the creatures' own norms and an honest roll turned the planned fight into something else. Now the player has a real choice: follow the retreat (one of quest K's listed routes) or hold the curve.]*

---

## Round 4

**▶ Player:** We follow them. Rosa and me on foot, with tranqs and radios. Agent Vega?

*[test note: Vega's answer is settled from her plan and quest K's routes ("follow the retreat"): yes, she sends her two agents with them and holds the road. Tracking: field investigation against the cell (4); sensory +1 (night, red-filtered flashlights), environment −1 (soft sand holds prints). The danger is bound and shown: attackers turn on pursuers in the dark (loss, "a threat acts").]*

```text
ROUND 4 | Day 12 | 18:08 | the pines east of Route 9 | saved R0 · save R10

2d10: 2+5 | Capability: +0 | Tool: +0 | Total: 7
Difficulty: 10 [sensory +1: night in the pines; red-filtered flashlights; environment -1: soft sand holds fresh hoofprints] | Stakes: loss/full | Outcome: Failure
Damage: 1d6 (6) − soak 1 = 5 | West HP 12 → 7

GM-Δ 4 ⟵ 3
  + npcs.nj_agents :: Hollis and Diaz, NJ team, depth 0, level 3
  ~ npcs.marisol_vega.state.plan :: K-2 follow the retreat with West, Delgado, Hollis and Diaz; she holds the road
  ~ player.condition.hp :: 7
  + world_state.pending.pines_ambush :: the track went cold in scrub oak; three attacker bucks came out of the dark; one hit West in the side
  ~ npcs.stag_cell_east_attackers.state.due :: K-2 Day 12 18:40 three turn on the pursuers to cover the retreat
  ~ world_state.time :: Day 12 18:40, evening
```

"Go," Vega says. "Hollis, Diaz, with them. Bring me antlers, not bodies."

For half an hour the tracks are easy: sharp hoofprints in the soft white sand, single file, going east. Then they run into a stand of scrub oak and you lose them. You're bent over with the red flashlight, trying to find the next print, when Rosa says "West—" in a voice you've never heard her use.

It comes out of the dark at chest height. A buck, head down, and it hits you in the side like a car door. You go down in the sand with your rifle under you. Your ribs are on fire and you can't get a breath in.

Two more are coming out of the oaks behind it, and they're not running away.

Hollis has his pistol out. "Do we shoot? Delgado, do we shoot?"

*[test note: a failed roll's bound cost: a threat acts, as one hit from the source (RULES §5 APPLY: loss = one hit). The world acts first here because the PC had no way to see it coming; the failed tracking was exactly that. Hand back now. The fight that follows has a real choice in it: tranquillise (slow, a minute to drop, Ethics-safe) or shoot to kill (fast, and Vega asked for antlers, not bodies). Neither the order ("follow, with tranqs") nor anything else covers it. The player is at HP 7 of 12.]*

---

## Round 5

**▶ Player:** Shoot them. They're trying to kill us, and the Ethics Committee can read that in the report. Pistols, everyone. I'm getting up with Patience.

*[test note: the combat form: West (HP 7, vest), Rosa (level 6, firearms T2), Hollis and Diaz (level 3) against three attacker bucks (level 2, man-sized 1d6). Sensory +1 (dark scrub oak, red flashlights). The player gave no stop condition, so none was added this time (cf. S2). The cell's morale needs no settling: "attackers commit and rarely survive".]*

```text
ROUND 5 | Day 12 | 18:40 | the scrub oak, east of Route 9 | saved R0 · save R10

— exchange 1 —
pc vs buck 1 — 2d10: 1+3 | Capability: +0 | Tool: +0 | Total: 4 | Difficulty: 11 | Failure
Damage: 1d6 (6) − soak 1 = 5 | pc HP 7 → 2
rosa_delgado vs buck 2 — 2d10: 10+9 | Capability: +4 | Tool: +0 | Total: 23 | Difficulty: 11 | Success
Damage: 1d8 (5) − soak 0 = 5 | buck 2 HP 12 → 7
Hollis vs buck 3 — 2d10: 8+10 | Capability: +0 | Tool: +0 | Total: 18 | Difficulty: 11 | Success
Damage: 1d8 (8) − soak 0 = 8 | buck 3 HP 12 → 4
Diaz vs buck 1 — 2d10: 6+1 | Capability: +0 | Tool: +0 | Total: 7 | Difficulty: 11 | Failure
Damage: 1d6 (5) − soak 0 = 5 | Diaz HP 14 → 9

GM-Δ 5 ⟵ 4
  + player.fighting_style.deer :: they're trying to kill us: pistols, shoot to stop them
  ~ player.condition.hp :: 2
  + player.condition.conditions.ribs :: cracked ribs; hard to breathe; harder to run, climb or aim steady
  + world_state.pending.pines_fight :: West hit again; Rosa and Hollis hit two bucks hard; Diaz knocked down and up again
  ~ world_state.time :: Day 12 18:41, evening
```

You get one knee under you and the gun up, and the same buck comes again before you've found it in the dark. The antlers catch you across the vest and you're on your back in the sand again, with a weight on your chest you realise is your own ribs.

Around you the pines are full of gunshots and red light. Rosa fires twice and a buck screams and staggers. Hollis hits another square, and it goes down on its front knees and gets up again. Diaz gets knocked flat and gets up swearing.

The buck that hit you is standing over you in the sand, lowering its head again. You're on your back, at HP 2. Patience is somewhere in the sand by your hand.

*[test note: **the most important finding of the S runs.** The batch paused only because a buck was badly hurt. The PC dropping from 7 to 2 in one exchange wasn't a pause point: a 5-point hit isn't half of max, and the PC wasn't down. If no buck had been badly hurt, the batch would have rolled the next exchange with the PC at HP 2 and no player say. The tool stops for the PC only at 0 HP, or at a stop the player gave. That's processing running past a decision, the thing the design record now forbids. The GM hands back here, because a lethal danger to the PC is a real decision the order doesn't cover. The GM noticed only because the pause happened to come.]*

---

## Round 6

**▶ Player:** I roll away under the oak toward Rosa. Rosa, cover me.

*[test note: Rosa's shot is her own act, from her own record (line: never leaves her crew behind): action form, firearms T2 (8) against level 2; sensory +1 (dark), position +1 (West right under the buck). Success → one hit with the harm form, and the buck reels off. Then the combat form again without West, who stays down (the player's choice): Rosa, Hollis and Diaz against the three, with the GM re-sending at each pause (full log: fight_log.txt).]*

```text
ROUND 6 | Day 12 | 18:41 | the scrub oak | saved R0 · save R10

rosa_delgado — 2d10: 8+2 | Capability: +4 | Tool: +0 | Total: 14
Difficulty: 12 [sensory +1: dark scrub oak; position +1: West is right under it; she must not hit him] | Stakes: setback/full | Outcome: Success
Damage: 1d8 (6) − soak 0 = 6 | buck 1 HP 12 → 6
  … two more exchanges: buck 3 falls; then buck 1 and buck 2 fall — no opponent left standing …
XP +32 (the three attacker bucks beaten in the scrub oak (R5–R6)) → level 2, 32 XP

GM-Δ 6 ⟵ 5
  + world_state.pending.pines_fight_end :: Rosa shot the buck off West; West rolled clear and stayed down; all three bucks down, alive
  ~ npcs.stag_cell_east_attackers.state.status :: three down in the scrub oak; two went on with Twelve-Point to the bogs
  ~ npcs.stag_cell_east_attackers.state.due :: K-2 when the cell regroups at the bogs, the two rejoin Twelve-Point
  ~ npcs.rosa_delgado.state.plan :: get West out; capture the three downed bucks alive for Vega
  ~ player.progression.state :: {level: 2, xp: 32}
  ~ world_state.time :: Day 12 18:45, evening
```

Rosa's pistol goes off right over your head, and the buck standing over you jerks and goes sideways into the oaks. You roll the other way, under the nearest branches, and lie there with sand in your mouth, breathing in little sips because big ones hurt.

It's over in under a minute. Two more shots from Hollis, three from Rosa, a lot of Jersey swearing from Diaz. Then it's quiet except for a buck breathing heavily somewhere in the dark.

Three of them are lying in the sand. None of them is dead.

Rosa kneels beside you, her face very close in the red light. "Don't move. Can you feel your feet?" You can. "Good. You're welcome," she says, and for once it sounds like she means something else.

*[test note: XP for the fight won (level 2, meaningful), paid at the close of the fight this time. The attacker bucks are down at 0, not dead. RULES §5's survival roll after an hour untreated applies to them too, so capturing them alive is a real task, not a formality.]*

---

## Round 7

**▶ Player:** Don't chase the rest. Dart the three while they're down and tie them before they wake. They're Vega's antlers. And somebody help me up, slowly.

```text
ROUND 7 | Day 12 | 18:45 | the scrub oak | saved R0 · save R10

GM-Δ 7 ⟵ 6
  ~ npcs.stag_cell_east_attackers.state.status :: three captured alive: darted while down, wounds packed from the field kits (treatment, stabilised), legs hobbled; two still free with Twelve-Point
  ~ player.equipment.tranq_rifle.special_properties :: two darts left
  ~ world_state.time :: Day 12 19:05, evening
```

You can't kneel, so you tell Hollis where to put the darts, and he puts them in. Diaz packs the bullet wounds from the field kit with gauze and swearing. By seven the three bucks are asleep in the sand with their legs hobbled with cable ties, and Rosa has you sitting against a pine with her coat over you.

*[test note: darting a helpless target is certain, no roll. The field-kit packing counts as treatment and stabilises the downed bucks (RULES §5 DOWN), so no survival roll is made. That's the GM's call: the rules don't say whether field first aid on a deer is "real treatment".]*

---

## Round 8

**▶ Player:** I radio Vega. Three alive, the big one and two others got away east toward the bogs.

```text
ROUND 8 | Day 12 | 19:05 | the scrub oak → the road | saved R0 · save R10

GM-Δ 8 ⟵ 7
  ~ npcs.marisol_vega.state.due :: K-2p took the three captured bucks into the van; the cell leader and two escaped; K-3 Day 15 evening watches the network's next corridor
  + npcs.marisol_vega.relationships.pc :: approving, dry; credit: spotted the cell before the rush; brought them in alive
  ~ quests.buck_stops_here.parts.cell_leader.status :: partly → K-2p
  ~ world_state.time :: Day 12 19:40, evening
```

Vega comes up the sand track with the van's lights off and counts the bucks by flashlight, then you. "Three alive and two of ours hurt. And the big one knows our faces now." She thinks about it. "It'll do." She writes something on her tablet. "The shoot decision goes to Ethics. They'll read it. I'll tell them what I'd have told them anyway: you stopped shooting the second you could."

**Code K-2: partly.** The Cedar Run corridor is broken. Twelve-Point is still out there.

*[test note: K-2's objective ("a cell leader's ambush corridor") is partly met: the corridor broken and three captured, the leader escaped. The network now knows the curve is watched (pending, due Day 15), so K-3 will start harder. **GM slip:** no span ran during Rounds 4–6. Twelve-Point's 18:30 move was never listed, and it's been written as having happened by its own logic. The pattern repeats in every run: the GM stops running time while a fight is on.]*

---

## Round 9

**▶ Player:** Can Vega's medic look at me before the drive?

*[test note: the heal form with a minor healing item (the setting's field kit, RULES §5: minor 2d6): HP 2 → 8. The cracked ribs are a body condition; HP healing doesn't remove it. It heals with rest over about a week.]*

```text
ROUND 9 | Day 12 | 19:40 | the van on Route 9 | saved R0 · save R10

GM-Δ 9 ⟵ 8
  ~ player.condition.hp :: 8 (Vega's medic kit, minor healing 2d6 = 6)
  ~ player.condition.conditions.ribs :: two cracked ribs, strapped; heals in about a week with rest
  + world_state.pending.incident_report :: three captured alive, two agents hurt, no civilian contact; Ethics will read the shoot decision
  ~ world_state.time :: Day 12 20:30, evening
```

The medic is Diaz, it turns out. He straps your ribs in the back of the van and gives you two pills that taste like chalk. "Week," he says. "No running. No getting hit by deer."

---

## Round 10

**▶ Player:** Motel. Sleep.

```text
ROUND 10 | Day 12 | 20:30 | the Cedar Run motel | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ player.condition.hp :: 12 (a night's rest, paid lodging)
  ~ player.condition.last_rest :: Day 12 night, the Cedar Run motel (good rest)
  ~ player.growth_period :: {opened: 13, credited: []} (growth boundary: no tier change)
  ~ world_state.time :: Day 13 07:00, morning
```

You sleep sitting up because lying down hurts. At seven Rosa bangs on the door with two coffees and a box of donuts. "Vega says thank you," she says. "In her way. She said 'adequate'."

*[test note: a good rest (paid lodging) → full HP; the ribs stay. Growth boundary: field_investigation has 1 evidence, no change. Save due.]*

---

## Save R10

`save_scp_S3_R10.md`: merge → valid; validate → **valid: true**, with an overdue list that's mostly right:

- Rosa's K move, Twelve-Point's 18:30 move and the scouts' 18:15 move were never marked resolved (GM slips: the fight rounds again).
- Darrow's Day 8 and the `darrow_scheme` clock were skipped by the fixture (a fixture gap, as in S1).
- The coordinator's line is flagged because "Day 10 visited (done)" still reads as a dated move (fixture wording).

The midnight surface roll came up an ordinary encounter, "top + rare of band" (a ranger and a bogged car on the sand road). It passed the sleeping PC by.

---

## Findings from this run

1. **The tool doesn't pause when the PC is near death.** West went from 7 to 2 HP in one exchange, and only a coincidental pause (a buck badly hurt) stopped the batch. The PC's own stops are a fall to 0 HP or a stop the player gave. A big drop, or a low-HP line for the PC, isn't a pause. This is the clearest case of the tool running past a decision.
2. **The public ambush became a chase, then a fight.** The cell's own norms (leaders withdraw to save the herd) and an honest roll called off the attack on the road. The fight came later, from a failed tracking roll's bound cost ("a threat acts"). The world decided where the fight was.
3. **Bystanders have no place in the combat form.** The cars on Route 9 never needed it here, but if the deer had charged the road, an enemy acting against a bystander "gets its own roll" (RULES §8), and the form has no slot for a bystander's harm. The GM would have run each one by hand.
4. **The GM stops running time during fights.** No span ran in R4–R6; moves at 18:15 and 18:30 were missed and written in later. Same in A2. The turn's step 1 (WORLD) says it always runs; under combat load it didn't.
5. **`arrived` on a move inside the same zone rolled the daypart's encounter twice.** The tool doesn't remember what it already rolled.
6. **Nerve day marks** (a day of fear −1, a good rest +1) were applied by the GM's memory, not prompted. The span only says "day begins: nerve day marks".
7. **Field first aid on a downed creature** counts as "real treatment" only by the GM's call; the rules don't say.
