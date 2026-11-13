# Combat test S1 — SCP Class of '99: the storage unit raid (armed raid)

Test of the NEO play set on the `design-tripod` branch, with the SCP Omega-99 background and the modules file. The stand-in player is Claude; every roll, time step and save comes from the tool.

**Test start (fixture):** Day 14, 18:30, Trenton self-storage. Sam West as in S2. Leo's dues before Day 14 are written as done: the Day 3 call, and the Day 12 skipped cards night after which West asked and Leo told him everything on Day 13. Quest L (`darrows_list`) is open and the route taken is "report it properly → raid the storage unit with Omega-99". Lindqvist authorised the raid Day 14. Darrow's Thursday meeting with his two hired men is developed from Leo's knowledge and set as Darrow's due for 19:30. The hired men are recorded from Darrow's record (`hired_muscle: two ex-security men, T2 firearms each`).

**Scene:** armed raid.

---

## Round 1

*[test note: span from 18:30 (arrived): the evening surface roll at Trenton storage (−1, Uneasy) gave an encounter, kind ordinary, from the one-line pool: "the storage manager asks for ID". (The tool also flagged Gus again; fixture fixed.)]*

A flashlight hits the van's windshield. A man with a clipboard: "You folks renting here?"

**▶ Player:** I get out with the WHO card. Public health: we've had a report of a gas smell in Row C. We'll sit in the lot quietly, and you stay in your office, please, sir. It's for your own safety.

```text
ROUND 1 | Day 14 | 18:30 | Trenton self-storage, the lot | saved R0 · save R10

2d10: 2+8 | Capability: +0 | Tool: +1 [WHO credentials] | Total: 11
Difficulty: 10 | Stakes: setback/full | Outcome: Success

GM-Δ 1 ⟵ 0
  + npcs.ray_dumont :: Ray Dumont, night manager, depth 0
  + npcs.ray_dumont.knowledge.facts.van :: a WHO team watching for a gas leak in Row C; he's to stay in his office
  ~ world_state.time :: Day 14 18:35, evening
```

Ray Dumont reads the card twice and goes back to his office. You see his flashlight go off behind the blinds.

---

## Round 2

**▶ Player:** We wait and watch C-17.

```text
ROUND 2 | Day 14 | 18:35 | the van, Row C | saved R0 · save R10

GM-Δ 2 ⟵ 1
  ~ npcs.felix_darrow.state.due :: Ls at the unit with Brice and Pell; L Day 15 morning calls Leo
  + npcs.felix_darrow.state.tonight :: inside C-17, door half up: a folding table, a laptop, a list of Site-19 disposal dates
  ~ world_state.time :: Day 14 19:32, evening
```

At half past seven a grey sedan pulls into Row C. A thin man in a sharp suit gets out with a laptop bag, and two big men in work jackets get out of the back. Darrow rolls the door of C-17 halfway up and they duck under it. A light comes on inside.

Dima, in the back of the van, cracks his knuckles very quietly. Rosa looks at you. "Your case, West. Tell us how you want it."

*[test note: the span stopped at 19:30 (Rosa's, Darrow's and the hired men's dues all fall on it); it reaches the PC. Rosa giving the plan to West comes from her record (she "teaches by letting you try").]*

---

## Round 3

**▶ Player:** Dima goes under the door first, shouting Federal agents. Rosa second. I stay outside on the door so nobody leaves. Weapons out but nobody shoots unless they shoot.

*[test note: will the hired men fight? Their reaction is honestly open → `ask`: for +1 (professionals hired for exactly this kind of trouble); against −2 (their own fear: a federal charge).]*

```text
ROUND 3 | Day 14 | 19:32 | unit C-17 | saved R0 · save R10

darrow_muscle — 2d10: 9+2 | Likelihood: -1 [for: professionals hired for exactly this kind of trouble +1; against: their fear: a federal charge -2] | Total: 10 → NO, BUT

GM-Δ 3 ⟵ 2
  + world_state.pending.raid_entry :: Dima went under the door shouting; neither man drew; Pell's hands up; Brice dropped his gun and ran for the door, where West stands
  ~ world_state.time :: Day 14 19:40, evening
```

Dima goes under the door like a bear going under a fence, roaring "Federal agents, hands, hands!", and Rosa is behind him with her pistol up.

Inside, nobody draws. The one called Pell puts his hands straight up. Darrow drops the laptop and starts saying "I want a lawyer" over and over. The other one, Brice, looks at the pistol on the table, doesn't take it, and comes for the door instead, head down, fast. He's going to come under that half-open door straight into you.

He isn't armed. He's big, he's moving, and in two seconds he'll be past you into the dark rows of units. You have your pistol up.

*[test note: NO, BUT = partly, on their own terms: nobody draws, but one runs. A man running unarmed at the PC's door is the real decision the plan didn't settle ("nobody leaves", but "nobody shoots unless they shoot") → stop and hand back, before the consequence (GM §5 MID-JOB). The armed raid has, so far, no gunfight. The hired men's fear decided it, not the GM.]*

---

## Round 4

**▶ Player:** I don't shoot. Holster, and I take him low as he comes under the door.

*[test note: the GM used the combat form for a tackle. **Wrong tool:** the combat form knows only HP, so "stop him and pin him" became three exchanges of fist damage (Brice 14 → 8; West 12 → 10). An action form with reach full = pinned would have said what the player meant in one roll. The GM read the batch for what it was: two exchanges won in three. West is on top, and Dima comes out and sits on Brice. With his own fear in front of him (a federal charge), Brice gives up; settled, not rolled.]*

```text
ROUND 4 | Day 14 | 19:40 | outside unit C-17 | saved R0 · save R10

— exchange 1 —
pc vs Brice — 2d10: 7+9 | Capability: +0 | Tool: +0 | Total: 16 | Difficulty: 9 | Success
Damage: 1d3 (3) − soak 0 = 3 | Brice HP 14 → 11
— exchange 2 —
pc vs Brice — 2d10: 9+4 | Capability: +0 | Tool: +0 | Total: 13 | Difficulty: 9 | Success
Damage: 1d3 (3) − soak 0 = 3 | Brice HP 11 → 8
— exchange 3 —
pc vs Brice — 2d10: 3+5 | Capability: +0 | Tool: +0 | Total: 8 | Difficulty: 9 | Failure
Damage: 1d3 (3) − soak 1 = 2 | pc HP 12 → 10

GM-Δ 4 ⟵ 3
  ~ player.condition.hp :: 10
  + world_state.pending.brice :: West tackled Brice under the door; Dima sat on him; Brice gave up
  ~ npcs.darrow_muscle.state.status :: both detained: Pell inside, Brice outside
  ~ world_state.time :: Day 14 19:43, evening
```

You holster Patience and drop your shoulder as he comes under the door, bent double. You hit him in the middle and you both go down on the asphalt. He gets an elbow into your ribs, right where the vest isn't, and you get your forearm across his throat. Then Dima is there, kneeling on Brice's back like a man sitting on a bench.

"Hi," Dima says to him, gently. "Don't."

Brice lets his head drop onto the asphalt. "I don't get paid for feds," he says.

---

## Round 5

**▶ Player:** I go in to Darrow. Who are you working for, Felix, and what's the list for?

*[test note: INFLUENCE: cover_and_persuasion T1 against Darrow (deception T2, 6); position favourable (caught at the table with the list). Failure → setback, and −2 in any `ask` it feeds.]*

```text
ROUND 5 | Day 14 | 19:43 | inside unit C-17 | saved R0 · save R10

2d10: 3+7 | Capability: -2 | Tool: +0 | Total: 8
Difficulty: 9 [position -1: Darrow is caught at the table with the disposal list in front of him] | Stakes: setback/full | Outcome: Failure

GM-Δ 5 ⟵ 4
  + npcs.felix_darrow.state.tonight_after :: influence failed; he waits for MC&D to cover him
  ~ npcs.felix_darrow.state.status :: detained by Omega-99 in unit C-17
  ~ npcs.felix_darrow.state.due :: L when MC&D answers for him or refuses him, acts on his plan
  ~ world_state.time :: Day 14 19:50, evening
```

Darrow has had a minute to get his breath back, and he's found his voice: smooth, confident, a little too loud. "I think you'll find Marshall, Carter and Dark will want to speak to your superiors. I'm not saying another word to a junior agent in a car park."

He folds his arms. His hands are shaking, slightly.

*[test note: his record: "smooth and confident until pressed, then nervous"; plan: "if exposed, run to MC&D for cover, and if refused, cut a deal". His secret (acting alone, without MC&D's seniors knowing) is what will decide it. Nothing in the scene hands that to the PC; it has to come through a real channel.]*

---

## Round 6

**▶ Player:** Fine. Rosa, call it in, and the commander can ring MC&D. I'm going through the unit: the laptop, the paper on the table, whatever's in the boxes.

```text
ROUND 6 | Day 14 | 19:50 | inside unit C-17 | saved R0 · save R10

GM-Δ 6 ⟵ 5
  + locked_case_truths.darrow_case.evidence.laptop :: emails to Pinnacle's bank and to Brice; a memo to MC&D acquisitions drafted and never sent; no MC&D sign-off anywhere
  + locked_case_truths.darrow_case.evidence.table_list :: the disposal contractor's truck runs (public bids), 26 March circled; no item list — Leo never gave one
  + player.knowledge.facts.darrow_laptop :: no MC&D approval; the unsent memo; 26 March circled; no item list
  + world_state.pending.lindqvist_calls_mcd :: Lindqvist calls her MC&D liaison; due Day 14 21:00
  ~ world_state.time :: Day 14 20:15, evening
```

The laptop isn't even locked. Emails to a bank about Pinnacle Recovery LLC. Emails to Brice about "Thursday rates". And in drafts, a memo to "MC&D Acquisitions, Northeast" proposing "a low-risk opportunity", **never sent**. Nothing in it says anyone at MC&D knows what Felix Darrow is doing.

The paper on the table is the disposal contractor's truck timetable, printed off a public tender site, with Thursday 26 March circled in red pen. There's no list of items anywhere. Leo never gave him one.

*[test note: evidence baseline (RULES §15.6): competent + relevant skill + examining the right place → found, no roll. The laptop's content is the case's committed truth (Darrow's secret: "acting on his own"), written into evidence before it was shown. The case's routes were designed to include it.]*

---

## Round 7

**▶ Player:** I turn the laptop round so he can see the draft. You never sent it, Felix. Nobody at MC&D knows you exist. And my commander is on the phone to them right now.

*[test note: INFLUENCE with a changed fact → SETTLE again (RULES §9.1): the proof touches his recorded fear directly (MC&D's seniors learning he risked a Foundation incident) → settled: he starts bargaining now. No roll.]*

```text
ROUND 7 | Day 14 | 20:15 | inside unit C-17 | saved R0 · save R10

GM-Δ 7 ⟵ 6
  ~ npcs.felix_darrow.state.tonight_after :: shown the memo; his fear touched; he bargains before MC&D answers
  + npcs.felix_darrow.state.offer :: Leo's debt cancelled in writing, the schedule and laptop, never contacts Leo again — if the Foundation tells MC&D he was "helping"
  ~ world_state.time :: Day 14 20:30, evening
```

Darrow looks at the screen for a long moment. The confidence goes out of him all at once, like air out of a tyre.

"Okay," he says. "Okay. Let's — let's be adults about this." He talks fast now. Pinnacle owns the kid's debt and he can sign it away tonight, right now. The laptop, the schedule, all of it. He'll never call Leo again. "And maybe you tell MC&D I was — helping. Looking into a security weakness. For everyone's benefit."

---

## Round 8

**▶ Player:** That's not my call. Rosa?

```text
ROUND 8 | Day 14 | 20:30 | Row C | saved R0 · save R10

XP +50 (quest L, Darrow's list) → level 2, 50 XP

GM-Δ 8 ⟵ 7
  ~ world_state.pending.lindqvist_calls_mcd :: done 21:00: MC&D: no associate named Darrow was authorised; they'll "review his employment"
  ~ npcs.felix_darrow.state.status :: disowned by MC&D; detained for questioning; signed the release of Leo's debt
  ~ npcs.felix_darrow.state.due :: L Day 15 morning questioned at Site-19, then handed back to MC&D under amnestic
  - npcs.felix_darrow.state.offer :: accepted in part: the debt release and the laptop; no promise about MC&D
  + rights_obligations.leo_debt :: cancelled — Pinnacle's signed release, in Rosa's case
  ~ active_world_pressures.darrow_scheme :: stopped
  ~ quests.darrows_list.status :: succeeded → Ls
  ~ player.progression.state :: {level: 2, xp: 50}
  ~ world_state.time :: Day 14 21:05, evening
```

Rosa takes the signed release off the table, reads it, and puts it in her jacket. "The debt, yes. The laptop, yes. What MC&D hears isn't up to us."

At nine her phone goes. She listens, says "Yes, Commander" three times, and hangs up. "MC&D has never heard of an associate named Felix Darrow," she tells him pleasantly. "They're reviewing his employment. We're keeping him overnight."

Darrow sits down on a box and puts his head in his hands.

**Code L: done.** Darrow exposed. Leo's debt is gone.

*[test note: MC&D's answer is settled from Darrow's secret (he acted alone, and MC&D won't cover an unauthorised junior who risked a Foundation incident). Darrow's "if refused, cut a deal" branch runs from his own plan. Lindqvist's ruling (questioning, then an amnestic, then handed back) is Foundation practice; off-screen, told by Rosa. The quest end is met ("Darrow exposed; Leo safe") → quest XP once, at level 5.]*

---

## Round 9

**▶ Player:** We drive back. I write my part of the report in the van.

```text
ROUND 9 | Day 14 | 21:05 | the van → Site-19 | saved R0 · save R10

GM-Δ 9 ⟵ 8
  ~ npcs.darrow_muscle.state.status :: handed to Site-19 security with Darrow; amnestic and release after
  + npcs.rosa_delgado.relationships.pc.credit.r4 :: holstered and tackled an unarmed man instead of shooting
  ~ world_state.location :: site19
  ~ world_state.time :: Day 14 23:40, evening
```

Two and a half hours up the turnpike with Darrow and his men in the back of a second car behind you. You write the report on your knees in the van: the time, the door, Brice, the laptop. Rosa reads it over your shoulder at a red light.

"You put your gun away," she says. "Before you hit him."

"He wasn't armed."

"Mm." She doesn't say anything else, but she doesn't say "you're welcome" either. You've worked with her two weeks now; you know that's her version of a compliment.

*[test note: Rosa's credit entry comes from a real event she saw. The drive crosses unrecorded zones (New Jersey to Site-19), and the rules have no travel encounters between zones the record doesn't hold. The span only knows the start and end zones.]*

---

## Round 10

**▶ Player:** Leo's still up, isn't he. I go to C-14.

```text
ROUND 10 | Day 14 | 23:40 | Site-19, dorm C, room 14 | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ npcs.leo_brandt.state.due :: Ls waited up in C-14; L Day 15 10:00 sees Commander Lindqvist
  ~ npcs.leo_brandt.state.status :: the debt cancelled; the Commander sees him in the morning
  + npcs.leo_brandt.relationships.pc.credit.r10 :: West reported it properly and got the debt cancelled
  ~ npcs.leo_brandt.relationships.pc.attitude :: grateful, ashamed, owes him
  ~ npcs.commander_lindqvist.state.due :: Day 15 10:00 sees Leo about the debt and the broker; Day 75 transfer decision
  ~ world_state.time :: Day 14 23:55, evening
```

Leo is sitting on the top bunk in his jumpsuit with the light on, holding a zip tie he's been tying and untying for an hour.

You show him the release: Pinnacle Recovery LLC, signed, Felix Darrow. He reads it three times.

"That's it? It's just — gone?"

"It's gone. The Commander wants to see you at ten."

His face falls, then rises again, and somewhere in between he laughs, a bit wildly. "Fired, probably. But not owing fourteen thousand dollars to a guy in a suit." He wipes his eyes on his sleeve. "Thanks, man. I mean it. I owe you." Then, because he's Leo: "Want the top bunk? Permanently?"

*[test note: Leo's trigger ("when Darrow is dealt with") was met, so it fires: he's waiting up. His fate (disciplined or gone) is the Commander's decision tomorrow, with its own due. It isn't decided here, and the GM doesn't decide it for her. Save due.]*

---

## Save R10

`save_scp_S1_R10.md`: merge → valid; validate → **valid: true**, with an advisory list that caught real things:

- **Rosa's raid move wasn't marked resolved** (`L` should be `Ls` after R8). A GM slip, caught by the tool.
- **The deer network's dues are overdue** (the coordinator Day 10, the cell leader Day 12, the pressure Day 10). The fixture jumped to Day 14 without running the world through Days 1–13, so those moves never fired. That's a fixture gap, not a play error, and the tool found it. In a real run they'd have fired off-screen.
- Ray Dumont (depth 0) listed as without a plan, though his record says `due: none (incidental)` inside a `{…}` map.

---

## Findings from this run

1. **The armed raid had no gunfight, and that was right.** The hired men's own fear (a federal charge) beat their pay in an honest `ask` (NO, BUT): one surrendered and one ran. The world went its own way; an "armed raid" scene doesn't promise shooting.
2. **The combat form was the wrong tool for a tackle.** A non-lethal objective ("stop him, pin him") became an HP grind. The rules don't say when to use an action form instead of a combat form; the GM has to know that the combat form measures only HP.
3. **Proof → settle again worked cleanly.** The laptop evidence (committed truth) touched Darrow's recorded fear, and the record decided the rest with no roll. His secret, his plan's "if refused" branch and MC&D's answer chained together without any GM invention.
4. **validate's advisory list is the best drift catch in the set:** it found a resolved move left open and a whole thread the fixture skipped. It only runs at save time, though; ten rounds of drift can pile up before it looks.
5. **Travel between zones the record doesn't hold has no rules:** no encounters on the turnpike, because the span only knows the start and end zones.
