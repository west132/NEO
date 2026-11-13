# Combat test S2 — SCP Class of '99: the Oneida Lake pigeons (creature)

Test of the NEO play set on the `design-tripod` branch, with `worlds/BACKGROUND_SCP_OMEGA99_NEO_v0.md` and the modules file (canon mode). The stand-in player is Claude; every roll, time step and save comes from the tool.

**Test start (fixture):** Day 6, 17:30, Oneida Lake. Sam West, set up as in the SCP R10 test (L2, firearms T1, Glock 19 "Patience", HP 12). Orientation week is marked done. Rosa's "Day 5 first real assignment" is quest H, `pest_control`: help MTF Gamma-119 kill or capture the escaped SCP-3683 pigeons before they recombine or reach the raptor sanctuary. The team arrived Day 6 08:00, so the `pigeon_breakout` clock checks every 12 hours from 20:00. Issued for the op (the background's calibration: vest, net launcher, per op): a soft vest and a net launcher with two nets. Gamma-119 is developed as Sergeant Okafor plus two operatives.

**Scene:** creature.

---

## Round 1

*[test note: span from 17:30 (arrived): the afternoon surface roll at Oneida Lake (+1, Calm) came up an encounter, kind ordinary, middle of band. From the ordinary pool ("sanctuary volunteers at work", "a storm on the lake"), the GM picked the one that fits the time (feeding at dusk). The tool also flagged Gus as "important with no due": the fixture had written him as incidental, but he has a relationship with the PC in the background. Given a due.]*

```text
ROUND 1 | Day 6 | 17:30 | Oneida Lake shore, the raptor sanctuary | saved R0 · save R10

GM-Δ 1 ⟵ 0
  + npcs.jenna_kowalski :: Jenna Kowalski, sanctuary volunteer, depth 1; due H Day 6 18:30 finishes feeding and drives home
  + npcs.jenna_kowalski.knowledge.facts.pigeons :: a pigeon the size of a turkey on the aviary roof two nights ago; the red-tail went crazy
  + npcs.jenna_kowalski.knowledge.beliefs.vests :: the men in vests are the state wildlife office, about bird flu (the cover)
  ~ world_state.time :: Day 6 17:40, afternoon
```

The sanctuary is a row of big wire aviaries on the shore, with the lake grey and flat behind them. Sergeant Okafor of Gamma-119 is showing Rosa a map on the hood of a truck when a woman in a fleece and rubber boots comes out of the feed shed with a bucket of dead mice and looks at all of you like you're trespassing.

**▶ Player:** I go and say hello. WHO card out. Bird flu survey, ma'am. Have you seen anything odd round the aviaries?

She looks at the card, then at your vest. "The wildlife people. Again." But she talks. "Odd? Two nights ago there was a pigeon on the aviary roof the size of a Thanksgiving turkey. The red-tail went crazy. I figured I was tired." She hefts the bucket. "Is that your bird flu?"

*[test note: what she says is settled by her knowledge and the cover's belief, no roll. Her sighting is undefined detail the GM filled with what she plausibly saw (the SCP-3683 instance heading for the sanctuary is in the pressure's trajectory). She'd see it; it isn't a hint invented for the PC.]*

---

## Round 2

**▶ Player:** Ma'am, it might well be. Would you go home early tonight? We'll feed the rest; it's safer for your birds if nobody's handling them.

*[test note: INFLUENCE (RULES §9.1): a player action, cover_and_persuasion T1 against Jenna (level 2, animal care T2). The tool refused at first: "npcs.jenna_kowalski has no capability.overall_level — commit it before the roll". Correct; committed. Success → +2 likelihood in the `ask` that follows. Against: −2 (leaving her birds to strangers). The skill earned evidence (a real challenge).]*

```text
ROUND 2 | Day 6 | 17:40 | the raptor sanctuary | saved R0 · save R10

2d10: 10+9 | Capability: +0 | Tool: +0 | Total: 19
Difficulty: 10 | Stakes: setback/full | Outcome: Success
jenna_kowalski — 2d10: 1+8 | Likelihood: +0 [for: West made the bird-flu risk to her birds plain (influence success) +2; against: leaving her birds to strangers in vests -2] | Total: 9 → NO, BUT

GM-Δ 2 ⟵ 1
  ~ player.skills.cover_and_persuasion.evidence :: 1
  ~ npcs.jenna_kowalski.state.plan :: she'll go — after she's fed the owls herself; then she's calling the sanctuary director
  + npcs.jenna_kowalski.relationships.pc :: grudging, half believes him
  ~ world_state.time :: Day 6 17:55, afternoon
```

"I'll go," she says, "when my owls are fed. Not before. And I'm calling Dr. Haas about you people tonight." She stalks off toward the owl aviary with her bucket.

*[test note: NO, BUT = on her own terms (later, and a condition). The undercurrent roll for the PC at the sanctuary at dusk (contact: out during its hours at one of its sites; −2) came up nothing.]*

---

## Round 3

**▶ Player:** I stay by the aviaries with Rosa while Okafor's team sweeps the shore. I keep an eye on Jenna.

*[test note: Okafor's dusk sweep is her own uncertain act → `ask`: for +1 (the instances are near the lake; one heads for the sanctuary, per the pressure), +1 (Gamma-119 does this for a living); against −1 (dusk, mist). **GM slip:** the zone point was left out (span shows Okafor's side "suffers", hidden act at undercurrent −2 → −1). With it the total is 5, still NO, AND, so the outcome stands; noted. NO, AND = they find nothing, plus the smallest trouble from their own state: the noise of the sweep flushes an instance, and it flies the way the pressure's trajectory already points (the sanctuary).]*

```text
ROUND 3 | Day 6 | 17:55 | the raptor sanctuary | saved R0 · save R10

ada_okafor — 2d10: 3+2 | Likelihood: +1 [for: the instances are near the lake and one heads for the sanctuary (the pressure) +1; Gamma-119 hunts these birds for a living +1; against: dusk and mist over the reeds -1] | Total: 6 → NO, AND

GM-Δ 3 ⟵ 2
  ~ npcs.ada_okafor.state.due :: Hs dusk sweep (NO, AND: nothing found; the noise flushed an instance toward the sanctuary); H Day 6 20:00 second sweep
  + world_state.pending.instance_to_sanctuary :: an SCP-3683 instance lands on the red-tail's aviary; due Day 6 18:20
  ~ world_state.time :: Day 6 18:20, evening
```

The radio crackles every few minutes: Okafor counting reed beds out loud, Cole complaining about his boots. Nothing. Nothing. Then, from down the shore, a lot of shouting all at once and Ruiz's voice: "It's up! It's up — heading your way, Omega!"

You hear it before you see it. Wings, too many and too heavy, like someone shaking out a wet carpet. Then it comes out of the dusk over the aviary roofs: a pigeon, grey and green and iridescent, and as big as a turkey. It lands on the wire roof of the red-tail's aviary with a crash. Inside, the hawk goes berserk, screaming and throwing itself at the wire.

Jenna Kowalski is twenty yards away, at the owl aviary door, with her bucket. She's seen it.

*[test note: the instance reaches the PC; they see it coming (it's loud and big) → the PC acts first, the danger shown. Developed from the location's band (3–5) and the background's morale line for SCP-3683 ("bursts into pigeons when cornered or killed; scatters to recombine later"): level 4, harm as a man-sized creature (1d6). It's turkey-sized, so the background's "large" was read as a large bird, not RULES' "large" for harm. That's a GM call, noted.]*

---

## Round 4

**▶ Player:** Rosa, Jenna into the truck. I net it on the roof before it gets through the wire. If it comes at me, Patience, and not toward the hawks.

*[test note: the action form: the net launcher (firearms T1, tool fit good +1) against level 4, sensory adverse +1 (dusk, a dark shape on a dark sky). Danger: the instance comes off the roof at him (loss, inflict harm, 1d6, vest soak 1). Then the combat form. The player gave no stop condition. **GM habit found:** the GM put `stop: half` in the combat form anyway, out of habit from the earlier runs. It paused correctly at HP 5, and a real decision was due there anyway (a danger the order doesn't cover). But the stop came from the GM, not from the player's words.]*

```text
ROUND 4 | Day 6 | 18:20 | the red-tail's aviary | saved R0 · save R10

2d10: 8+1 | Capability: +0 | Tool: +1 [net launcher] | Total: 10
Difficulty: 11 [sensory +1: dusk; the bird is a dark shape against a dark sky] | Stakes: loss/full | Outcome: Failure
Damage: 1d6 (4) − soak 1 = 3 | HP 12 → 9

— exchange 1 —
pc vs SCP-3683 instance — 2d10: 4+2 | Capability: +0 | Tool: +0 | Total: 6 | Difficulty: 11 | Failure
Damage: 1d6 (3) − soak 1 = 2 | pc HP 9 → 7
— exchange 2 —
pc vs SCP-3683 instance — 2d10: 1+3 | Capability: +0 | Tool: +0 | Total: 4 | Difficulty: 11 | Failure
Damage: 1d6 (3) − soak 1 = 2 | pc HP 7 → 5

GM-Δ 4 ⟵ 3
  ~ player.equipment.net_launcher.special_properties :: one net left (the first missed)
  ~ player.condition.hp :: 5
  + world_state.pending.instance_fight :: the instance came off the roof onto West; two shots missed at arm's length
  ~ npcs.rosa_delgado.state.plan :: Jenna into the truck, then back to West
  ~ npcs.jenna_kowalski.knowledge.facts.pigeons :: she saw it go for the WHO man
  ~ world_state.time :: Day 6 18:22, evening
```

The net goes out with a thump and opens like a parachute over empty dusk, a foot behind the bird. The bird turns its head and looks at you with one orange eye, and comes off the roof.

It's like being hit by a sack of wet laundry with a beak. It slams into your chest, the vest takes some of it, and then it's on you, wings beating at your head, the beak going for your face. You get Patience up and fire, and the shot goes somewhere into the dusk. You fire again and hit nothing but air and feathers. Every time you turn, it's turned the other way. Your cheek is open and something in your ribs hurts when you breathe.

Behind you a truck door slams: Rosa getting Jenna inside. Down on the shore, flashlights are coming at a run.

It's still on you. You have one net left in the launcher, a pistol, and a bird the size of a turkey trying to take your eyes out.

*[test note: three failed rolls in a row against level 4 with a T1 skill (needs 11 on 2d10: about 45%). The PC is at HP 5 of 12; the creature is untouched. The batch paused at the stop the GM had added, and the hand-back is right: a danger the order doesn't cover. Rosa coming back and the flashlights are the world moving on its own.]*

---

## Round 5

**▶ Player:** I drop flat on my back. When it comes down at me again, I net it point-blank.

*[test note: action form: the last net, fit good, position favourable −1 (flat, it has to come down into the net's path); same danger. Success → netted. SCP-3683's morale in the background: "bursts into pigeons when cornered or killed". Netted counts as cornered, so it bursts; that's settled, not rolled. Whether the net holds every fragment is honestly open → `ask`: for +1 (a capture net made for these birds); against −1 (dozens bursting at once against a net pinned by one man).]*

```text
ROUND 5 | Day 6 | 18:22 | the red-tail's aviary | saved R0 · save R10

2d10: 10+3 | Capability: +0 | Tool: +1 [net launcher] | Total: 14
Difficulty: 9 [position -1: flat on the ground, it has to come down into the net's path] | Stakes: loss/full | Outcome: Success
scp_3683 — 2d10: 6+7 | Likelihood: +0 [for: a capture net issued for these birds +1; against: dozens of pigeons bursting at once against a net pinned only by West -1] | Total: 13 → YES

GM-Δ 5 ⟵ 4
  ~ player.skills.firearms.evidence :: 1
  ~ player.equipment.net_launcher.special_properties :: no nets left
  + world_state.pending.instance_1_captured :: netted point-blank; burst into about forty pigeons; the net held them all
  ~ active_world_pressures.pigeon_breakout.state :: two large instances still out; one instance's fragments bagged
  ~ world_state.time :: Day 6 18:24, evening
```

You go flat on the gravel. The bird comes down at your face like a falling umbrella, and you fire the net into it from two feet away.

The net wraps it. For one second it's a turkey in a net. Then it isn't. It comes apart, there's no other word for it, into pigeons: ordinary, grey, frightened pigeons, dozens of them, all at once, a heaving, cooing, flapping bag of birds on top of you. You lie on the edge of the net and hold it down with both arms, and not one gets out.

Rosa arrives at a run and kneels on the other edge of the net. "You're welcome," she says, out of breath, though she hasn't done anything yet, and then: "Your face is bleeding."

Okafor's team comes up from the shore a minute later with flashlights. Okafor looks at the bag of pigeons, then at you on the ground. "Forty-one," she says, counting. "Good."

---

## Round 6

**▶ Player:** Jenna saw it come at me. Protocol says an amnestic, and I've got two doses in the kit. Rosa?

*[test note: Rosa's answer is settled by the Foundation's witness protocol and her record ("doing it right") → yes, kindly. The player chose to do it himself: an action form (cover_and_persuasion against Jenna, sensory favourable: she's shaken and cold in the truck; the cost if it fails is a setback: she refuses and drives off to call Dr. Haas).]*

```text
ROUND 6 | Day 6 | 18:24 | Rosa's truck, the sanctuary lot | saved R0 · save R10

2d10: 2+8 | Capability: +0 | Tool: +0 | Total: 10
Difficulty: 9 [sensory -1: she is shaken and cold in the truck] | Stakes: setback/full | Outcome: Success

GM-Δ 6 ⟵ 5
  ~ player.equipment.field_kit.name :: field kit (… one dose of Class-A amnestic left)
  - npcs.jenna_kowalski.knowledge.facts.pigeons :: amnesticised: loses the last two hours
  ~ npcs.jenna_kowalski.state.due :: H Day 7 06:00 back at the sanctuary to feed the raptors
  + world_state.pending.amnestic_jenna :: West gave Jenna a Class-A in tea with Rosa's say-so; logged
  ~ world_state.time :: Day 6 18:45, evening
```

"Do it gently," Rosa says. "She'll have a headache and think she's coming down with something."

Jenna is sitting in the truck with her hands round nothing, shaking. You pour her tea from Rosa's thermos and tip the little pill into it, and she drinks it because she's cold and frightened and you're the man with the WHO card. Ten minutes later she's yawning. By seven she's driving home slowly with no idea why she's so tired.

*[test note: the amnestic removes her knowledge of the sighting (one `−` entry, with the reason) and her memory of the PC. Her routine goes on: back at six to feed the birds. **Two format findings while writing this block:** (1) "(in Rosa's truck)" inside a quoted position broke the tool's position match at the apostrophe; (2) a top-level field value written in quotes (`:: "…"`) keeps the quote marks, so the position matched no location. Inside `{…}` maps values must be quoted; at the top level they must not be. Two different rules for the GM to remember.]*

---

## Round 7

**▶ Player:** I'll go out with Okafor at eight.

```text
ROUND 7 | Day 6 | 18:45 | the sanctuary lot | saved R0 · save R10

ada_okafor — 2d10: 2+6 | Likelihood: +0 [for: Gamma-119 hunts these birds for a living +1; tranquillisers are the right tool: they sedate before the bird feels cornered +1; against: full dark over the reeds now -1; zone point: Gamma-119 suffers in disorder, hidden act at undercurrent -2 -1] | Total: 8 → NO, BUT

GM-Δ 7 ⟵ 6
  ~ npcs.rosa_delgado.state.plan :: keep West at the truck with the bag and the radio; he's hurt
  + npcs.rosa_delgado.relationships.pc.credit.r5 :: held the net alone with a cut face
  ~ active_world_pressures.pigeon_breakout.clock.filled :: 1 (the 20:00 check: two instances still free)
  ~ active_world_pressures.pigeon_breakout.clock.due :: Day 7 08:00
  ~ npcs.ada_okafor.state.due :: Hp second sweep (NO, BUT: one tranquillised but it burst as it fell; about twenty fragments bagged, the rest scattered); H Day 7 05:30 dawn sweep
  ~ active_world_pressures.pigeon_breakout.state :: one large instance free; about twenty loose fragments
  ~ world_state.time :: Day 6 20:40, evening
```

"No, you won't," Rosa says. "You've got a hole in your face and you're breathing like a broken accordion. You're on the bag and the radio." She doesn't say it unkindly, and she doesn't say it twice.

So you sit in the truck with forty-one pigeons cooing in a bag on the back seat and listen to the radio. At eight the team goes out with tranquilliser rifles. At twenty past, Cole: "Got one — it's going down — no — ah, hell." Then a lot of wings. Okafor, very calm: "It burst on the way down. Bagging what we can." Half an hour later they come back with a second bag, about twenty birds in it. The rest went into the dark.

One big one still out there. Twenty-odd loose ones. And Okafor's clock face says they'll start finding each other by morning.

*[test note: Rosa benching West is settled by her record (line: never leaves her crew behind; fear: losing a rookie), not a GM choice made for the player; the player had stated an intent, and his handler overruled it in the world. The sweep happens off-screen: it doesn't touch the PC's people and the PC isn't there (GM §3.5 NPC v NPC). Okafor's `ask` included the zone point this time. The tranquilliser's rule (sedates by dose and size, not by HP) can't go into the combat form, which knows only HP, so the GM ran the sweep as one `ask`. The clock ran on its 20:00 check: the pressure was actually operating (two instances free), so ADVANCE ONCE → 1 of 4.]*

---

## Round 8

**▶ Player:** (on the radio) Sergeant, pigeons can't fly in the dark. Wherever those twenty went, they're sitting somewhere close together under a roof, asleep. Can we go look for them tonight with flashlights, instead of waiting for dawn?

```text
ROUND 8 | Day 6 | 20:40 | Rosa's truck, on the radio | saved R0 · save R10

GM-Δ 8 ⟵ 7
  + npcs.ada_okafor.relationships.pc :: Omega-99's rookie on loan; approving; credit: netted an instance alone; the roost idea
  ~ npcs.ada_okafor.state.due :: H Day 6 23:00 roost search of the sanctuary outbuildings (West's idea); H Day 7 05:30 dawn sweep
  ~ world_state.time :: Day 6 21:00, evening
```

There's a pause on the radio. Then Okafor, sounding almost pleased: "That's correct. I was going to wait for light. We'll do it at eleven, when they've settled."

*[test note: Okafor's answer is settled: it fits her want (every fragment accounted for) and her expertise. Would she have thought of it herself? Her plan said dawn; the PC's idea changed her plan, and that's credit.]*

---

## Round 9

**▶ Player:** I stay on the radio. And Rosa — let me hold the bag open, at least.

*[test note: the roost search is Gamma-119's own act, off-screen → `ask`: for +2 (pigeons can't fly in the dark and roost together under cover: a real fact, at full weight), +1 (expertise); against −1 (zone point).]*

```text
ROUND 9 | Day 6 | 21:00 | the sanctuary lot | saved R0 · save R10

ada_okafor — 2d10: 9+3 | Likelihood: +2 [for: pigeons cannot fly in the dark and roost close together under cover +2; Gamma-119 hunts these birds for a living +1; against: zone point: Gamma-119 suffers in disorder, hidden act at undercurrent -2 -1] | Total: 14 → YES
XP +44 (quest H, the Oneida Lake pigeons) → level 2, 44 XP

GM-Δ 9 ⟵ 8
  ~ npcs.ada_okafor.state.due :: Hs roost search (YES: the last instance and the loose fragments asleep under the boathouse eaves; the instance burst when the nets came down; the nets held); H Day 7 05:30 count and hand-off
  ~ active_world_pressures.pigeon_breakout.state :: stopped: every instance and fragment accounted for; count at dawn
  ~ active_world_pressures.pigeon_breakout.clock.due :: none (stopped)
  ~ quests.pest_control.status :: succeeded → Hs
  ~ player.progression.state :: {level: 2, xp: 44}
  ~ world_state.time :: Day 6 23:50, evening
```

At eleven the team goes through the sanctuary's outbuildings with red-filtered flashlights. Cole finds them under the boathouse eaves: a row of grey shapes on the beam, heads tucked in, and in the middle the last big one, fast asleep like a fat grey hen. The nets come down. The big one bursts in its net with a sound like a pillow fight and the nets hold. At ten to midnight Ruiz carries the third bag to the truck, cooing.

Okafor counts all three bags by flashlight, twice, out loud. "A hundred and one. That's all of them."

**Code H: done.**

*[test note: the quest's end, "every instance and fragment accounted for", is met → succeeded, quest XP at its level, once. **GM slip caught before the block was shown:** the GM typed XP 58 into GM-Δ instead of the tool's 44. Fixed to the tool's line. It's the failure the "copy the tool's line word for word" rule is there for, and it happened anyway; no tool check compares GM-Δ numbers with the tool's own output.]*

---

## Round 10

**▶ Player:** I sleep in the truck. At dawn I want to see Jenna come in, just to check the amnestic took.

```text
ROUND 10 | Day 6 | 23:50 | the sanctuary lot | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ player.condition.hp :: 12 (a night's rest in the truck with the team)
  ~ player.condition.last_rest :: Day 6 night, with allies (good rest)
  ~ player.growth_period :: {opened: 7, credited: []} (growth boundary: no tier change)
  + player.condition.conditions.cut_cheek :: beak cut, stitched by Ruiz; no effect on rolls
  ~ npcs.ada_okafor.state.due :: Hs counted and handed the bags to the Site-19 courier
  ~ npcs.jenna_kowalski.state.due :: Hs Day 7 06:00 fed the raptors, no memory of last night; Day 8 06:00 feeds them again
  ~ world_state.time :: Day 7 06:30, morning
```

You wake stiff in the back of the truck with the pigeon smell still in your clothes. Ruiz stitched your cheek last night by flashlight, badly, and told you it'd make you look interesting.

At six Jenna Kowalski's car comes down the track. She gets out yawning, with her bucket, and walks right past the truck to the aviaries. The red-tail screams at her the way it always does in the morning. She says good morning to it by name. She never looks at you once.

Okafor's courier left for Site-19 at half past five with three bags of pigeons and the count signed in her neat hand: one hundred and one.

Rosa hands you a coffee from the gas station. "Your first real job," she says. "You're welcome."

*[test note: a good rest (with allies) → full HP, a growth boundary (no tier: T1→T2 needs 10 evidence, the PC has 1 in each of two skills), the night roll (nothing), the day rollover. **GM slip caught:** the GM first wrote Jenna's depth down to 0; NEO_SAVE §1 says depth rises, never down. Removed, and her due set to her daily routine instead (she's still depth 1 and still has a routine). Save due.]*

---

## Save R10

`save_scp_S2_R10.md`: merge → valid; validate → **valid: true**, with three false "overdue" items. The fixture wrote incidental dues as `none (incidental; Day 4 sparring done)`, and validate read "Day 4" as a date in the past (finding 7).

---

## Findings from this run

1. **The creature fight was short and dangerous, as it should be:** three failed rolls took the PC to 5 of 12 HP before one good roll ended it. The danger came from the dice and the creature's level, with no GM thumb on either side.
2. **The creature's own nature did the work.** "Bursts into pigeons when cornered" turned a kill into a capture puzzle (nets, the roost at night). The background's morale line was the most useful single line in the scene.
3. **A non-HP weapon has no place in the combat form.** The tranquilliser "sedates by dose and size, not HP" (the background's own calibration), but the combat form knows only HP. The GM had to run Gamma-119's sweep as an `ask`. Any capture or sedation tool falls outside the batch.
4. **The GM added a stop condition the player never gave** (`stop: half`), from habit. It happened to fall on a real decision. The form should take stops from the player's words only, with the PC going down as the tool's own stop.
5. **The missed daypart roll again:** a span that stops at a due at a daypart's first minute doesn't roll that daypart when it resumes (as in A2).
6. **Two quoting rules:** quote inside `{…}`, never at the top level of `::`. Both broke a position match in this run, and an apostrophe inside a quoted position broke it too.
7. **validate flags "none (incidental; Day 4 …)" as overdue,** because it reads any "Day N" in the text.
8. **The GM slips caught by the GM:** a missing zone point in an `ask`, a mistyped XP number, and a depth lowered when depth never goes down. None were caught by the tool. A check that GM-Δ progression lines match the last `award` output would catch the XP one, and it's processing.
9. **The amnestic worked as plain record-keeping:** one `−` entry on her knowledge, and her routine went on. That's the rules handling a setting-specific power without a special rule.
