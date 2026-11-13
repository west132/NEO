# Combat test A3 — AC Syndicate: the Blighters hit the Ten Bells (public ambush)

Test of the NEO play set on the `design-tripod` branch: GM, RULES, SAVE, the tool, modules (canon mode), and `worlds/BACKGROUND_AC_SYNDICATE_NEO_v0.md`. The player is a **stand-in** played by Claude. Every roll, time step and save comes from `neo_math_v0.py`. Notes in *[test note: …]* are outside the game.

**Test start (fixture, not play):** the run starts on Day 7 at 18:00 instead of Day 0. GM-Δ 0 sets the PC (a Rook, Tom Kell) and marks the dues before Day 7 as done the way the canon course has them (Henry Day 1, Evie Day 2, Jacob takes the Clinkers' pub Day 3, Abberline's bounties Day 4, Clara's runner Day 5). The Ten Bells is recorded as the Rooks' pub. Jacob's next move is set for Day 8 (the rail-yard stronghold); tonight he and Evie are scouting it.

**Scene:** public ambush. Kaylock's recorded due, `A-1 Day 7 night his men start breaking Rook pubs`.

---

## Round 0: setup

**▶ Player:** Rook role. Tom Kell, 24, man, docker's son from Whitechapel, broad, broken nose, red Rook scarf. Ex-Clinker.

> Play your character as a real person. I treat your character as a real person, and the world as a real place with its own logic.

London, February 1868. Crawford Starrick's companies own the mills, the trains and the omnibuses, and the Blighters in green own the streets for him. Four days ago two young strangers, Jacob and Evie Frye, beat a Blighter crew in a Whitechapel pub. On Day 3 Jacob walked into the Ten Bells, where the Clinkers drank, and walked out their boss. The Clinkers are the Rooks now. You were one of them, so you're a Rook.

**Tom Kell.** You grew up on the London Docks and you fight like it. Brawling and streetwise are the things you're good at (T2); you can use a blade (T1). You carry a knuckle-duster, a weighted cane and a leather cosh, and 3 shillings. HP 14. You know every pub and fence in Whitechapel, you can't read much beyond your name, and you know the Blighters want the Ten Bells back.

```text
GM-Δ 0
  (test fixture: the player block, role gear, the Ten Bells, and the dues before Day 7 marked done — see deltas.txt)
```

18:00, Day 7. Cold fog off the river, coal smoke, a thin rain on the windows. The Ten Bells is half full: dockers off shift, two old women by the fire, and the Rooks' corner by the back door.

*[test note: span from Day 7 18:00 at the Ten Bells (arrived). Evening surface roll 6, nothing. It stops at Kaylock's A-1 due, 21:00 ("night" taken as 21:00 by the tool), could reach the PC. The player acts before that.]*

---

## Round 1

**▶ Player:** I get a pint and sit with the lads. Did Jacob leave any orders for tonight?

```text
ROUND 1 | Day 7 | 18:00 | the Ten Bells, Whitechapel | saved R0 · save R10

GM-Δ 1 ⟵ 0
  + npcs.alf_tanner :: Big Alf Tanner, Rook, depth 1, level 2, brawling T1; steady, few words
  + npcs.mick_doyle :: Mick Doyle, Rook, 17, depth 1, level 1; eager, scared and hiding it
  + npcs.davey_shaw :: Davey Shaw, Rook, depth 1, level 2, knife; wants Blighter blood for his brother's arm
  + npcs.sal_pruitt :: Sal Pruitt, landlady, depth 1; wants her pub standing, fears fire
  + npcs.alf_tanner.knowledge.facts.orders :: hold the Ten Bells tonight; Jacob and Evie at the rail yards
  ~ world_state.time :: Day 7 18:15, evening
```

Sal pulls your pint without asking and takes a penny for it. "Your lot can have the corner," she says, "long as the windows stay in."

Big Alf moves his elbow off the table so you can sit. Mick Doyle is there, the youngest, talking too fast about nothing, and Davey Shaw is cleaning his nails with a knife.

"Jacob said hold the pub," Alf says. That's the whole of it for Alf. Then, because you're still looking at him: "Him and the sister's up the rail yards. Looking at Kaylock's lot. Back late, he said. Nobody goes out looking for trouble."

"Trouble'll come looking," Davey says, and doesn't look up from his nails.

Everyone in the Ten Bells knows what Davey means. The Blighters lost this pub to a man nobody had heard of four days ago, and Kaylock is not a man who lets that stand. It's been quiet since. Too quiet, the old women by the fire would say.

*[test note: Alf's answer is settled by the record (Jacob's order to hold the pub, Alf's own knowledge), no roll. Four NPCs developed at first meeting (GM §7.5), depth 1. The PC's knowledge that the Blighters want the pub back is told in the prose (GM §2.3 point 4).]*

---

## Round 2

**▶ Player:** Mick — go stand under the lamp at the Commercial Street corner. Anything in green coming this way, you whistle and run back. Alf, Davey, we stay put. If it comes, the tables go against the front door. I drink slow.

```text
ROUND 2 | Day 7 | 18:15 | the Ten Bells, Whitechapel | saved R0 · save R10

GM-Δ 2 ⟵ 1
  + npcs.mick_doyle.state.plan :: lookout at the Commercial Street corner; whistle and run back at green coats (Tom's order)
  ~ npcs.mick_doyle.state.position :: Commercial Street corner by the Ten Bells
  + player.routines.tonight :: hold the Ten Bells; tables ready by the front door
  ~ npcs.henry_green.state.due :: A-3 Day 8 morning works through Ethan Frye's notes with Evie at his shop
  + npcs.nobby_crane :: Blighter crew boss, depth 1, level 3, brawling T2; plan A-1 break the Ten Bells
  + world_state.pending.ten_bells_raid :: Nobby Crane and seven Blighters (level 2; two sledgehammers, five cudgels), due Day 7 21:00
  ~ npcs.rexford_kaylock.state.due :: A-1s (sent Nobby Crane's crew to the Ten Bells); A-1 Day 8 morning hears how it went
  ~ world_state.time :: Day 7 21:00, night
```

Mick goes out pulling his collar up, proud to be given a job. You can see him through the fogged window, a shape under the gas lamp, stamping his feet.

The evening goes the way evenings go. The dockers drink. One of the old women falls asleep by the fire. Sal counts the till twice. Davey wins a farthing off Alf at shove-ha'penny and Alf doesn't argue.

At a few minutes to nine a whistle cuts through the fog, two short and one long, and Mick comes through the door so fast he hits the frame.

"Green coats!" He's out of breath. "Down Commercial Street. Eight. Nobby Crane in front. Two of them's got sledges, Tom. Sledges."

Sledgehammers are for doors and bars, not for people. Eight Blighters is twice what's in this corner. They're maybe a minute off, walking, not running, the way men walk when they think nobody will stop them. The front door is oak and the bolt is good; the windows are not. The back door goes out to the yard and the alley.

The dockers have already stood up. Sal is looking at you, not at them.

*[test note: span 18:25 → 21:00, stopped at Kaylock's A-1 due; it reaches the PC (the Ten Bells is the Rooks' pub), so time stops and the scene opens. Who first: the PC posted a lookout, so they see it coming → the PC acts first, the danger shown (GM §3.2 WHO FIRST). The tool flagged Henry as important with no due (the fixture had closed his only move); given one. The crew's size and gear were developed from Kaylock's record ("a train full of Blighters, T1–T2") and the encounter "Blighters breaking a pub that won't pay". Whitechapel's undercurrent (−2, always) is the protection racket, and this raid IS that racket acting through a due; no separate undercurrent roll, or the same cause would count twice. The rules don't say this; the GM judged it.]*

---

## Round 3

**▶ Player:** Bolt the front, tables against it. Sal, get the dockers and the old girls out the back. I take the cane. Alf with me either side of the door, Davey and Mick behind us. When they break the door they come through one or two at a time, and we hit them in the doorway. If two of us go down or it goes bad, we go out the back and down the alley. Nobody dies for a pub.

*[test note: `ask` — does Nobby send men round the back? for +1 (covering the back is ordinary on a pub job here), against −1 (he thinks the Rooks will run). 2d10 6+2 = 8 → NO, BUT: not at first; one man goes round when the door holds. Then the combat form: the PC and Alf at the door against the two sledge men, position favourable −1 (the doorway), stop at the PC's half HP.]*

```text
ROUND 3 | Day 7 | 21:00 | the Ten Bells, Whitechapel | saved R0 · save R10

nobby_crane — 2d10: 6+2 | Likelihood: +0 [for: covering the back door is ordinary on a pub job here +1; against: he thinks the Rooks will run, not fight (Kaylock: a pub brawl) -1] | Total: 8 → NO, BUT

— exchange 1 —
pc vs Blighter sledge 1 — 2d10: 7+1 | Capability: +2 | Tool: +0 | Total: 10 | Difficulty: 9 | Success
Damage: 1d8 (5) − soak 0 = 5 | Blighter sledge 1 HP 12 → 7
alf_tanner vs Blighter sledge 2 — 2d10: 2+9 | Capability: +0 | Tool: +0 | Total: 11 | Difficulty: 9 | Success
Damage: 1d6 (5) − soak 0 = 5 | Blighter sledge 2 HP 12 → 7
— exchange 2 —
pc vs Blighter sledge 1 — 2d10: 7+8 | Capability: +2 | Tool: +0 | Total: 17 | Difficulty: 9 | Success
Damage: 1d8 (2) − soak 0 = 2 | Blighter sledge 1 HP 7 → 5
alf_tanner vs Blighter sledge 2 — 2d10: 5+9 | Capability: +0 | Tool: +0 | Total: 14 | Difficulty: 9 | Success
Damage: 1d6 (1) − soak 0 = 1 | Blighter sledge 2 HP 7 → 6
— exchange 3 —
pc vs Blighter sledge 1 — 2d10: 7+5 | Capability: +2 | Tool: +0 | Total: 14 | Difficulty: 9 | Success
Damage: 1d8 (5) − soak 0 = 5 | Blighter sledge 1 HP 5 → 0 — down
alf_tanner vs Blighter sledge 2 — 2d10: 5+4 | Capability: +0 | Tool: +0 | Total: 9 | Difficulty: 9 | Success
Damage: 1d6 (5) − soak 0 = 5 | Blighter sledge 2 HP 6 → 1

GM-Δ 3 ⟵ 2
  + player.fighting_style.tonight :: "nobody dies for a pub" — two down or it goes bad → out the back and down the alley
  ~ world_state.environment.town :: the Ten Bells' front windows smashed; the bar mirror broken
  + npcs.nobby_crane.state.tactics :: windows, then sledges on the door; one man sent round the back once the door held
  + world_state.pending.blighter_sledge_1 :: down in the doorway, HP 0
  + world_state.pending.blighter_sledge_2 :: HP 1, pulled back by his mates
  ~ world_state.time :: Day 7 21:03, night
```

The tables go against the door with a scream of wood on flagstones. Sal herds the dockers and the two old women out through the back, and the last you see of them is the old woman who'd been asleep, holding her gin.

The windows go first. Cudgels through the glass, all four panes, and the bar mirror behind you bursts too. Then the sledges hit the door, one, two, and on the fourth blow the oak splits around the bolt and the tables slide back a foot.

The first man through is all shoulders, hammer up for a swing he has no room for. You get the cane across his wrist and then across his ear, and when he tries to come again you put it into his throat. He goes down in the doorway and stays there. Alf, beside you, beats the second sledge man back into the street with a stool leg, slow and heavy, until the man is staggering and his mates drag him out by the coat.

Nobody's touched you. Through the broken door you can see the rest of them in the gaslight: Nobby Crane in front, bellowing, five more with cudgels behind him. They aren't running. There are still six of them standing to your four.

And then, from behind you, at the back door Sal went out of, somebody tries the latch. Then kicks it.

Mick turns white. "Tom — the back."

*[test note: the batch paused when sledge 1 fell. AT PAUSE: morale settled for the Blighters — one of their own fell, but they still outnumber 6 to 4, and their norm is "hold while they outnumber" → they hold. World around the fight: the NO, BUT man arrives at the back door now. The plan covers the front doorway and the retreat out the back, not a Blighter at the back — the way out the plan relies on. That's "something the plan doesn't cover" → the player decides (GM §5, RULES §8 AT PAUSE). The fight is one round, so this is still Round 3.]*

**▶ Player:** Davey, take the back. If he gets in, knife him. Mick, with me and Alf. We hold the front.

*[test note: two combat forms run side by side: the front doorway (PC and Alf against Nobby Crane and a cudgel man) and the back (Davey alone against the man sent round). They're separate fights, so separate batches. The back fight ran 6 exchanges to the front's 2 before each paused. The tool has no shared clock between two batches; the GM put them back in step by hand: Davey's fight ran on while the front paused, and he finished it about when the front's next pause came. The rules don't say how two fights at once are timed.]*

```text
— front —
— exchange 1 —
pc vs Nobby Crane — 2d10: 7+1 | Capability: +2 | Tool: +0 | Total: 10 | Difficulty: 9 | Success
Damage: 1d8 (2) − soak 0 = 2 | Nobby Crane HP 14 → 12
alf_tanner vs Blighter cudgel 1 — 2d10: 8+2 | Capability: +0 | Tool: +0 | Total: 10 | Difficulty: 9 | Success
Damage: 1d6 (5) − soak 0 = 5 | Blighter cudgel 1 HP 12 → 7
— exchange 2 —
pc vs Nobby Crane — 2d10: 10+3 | Capability: +2 | Tool: +0 | Total: 15 | Difficulty: 9 | Success
Damage: 1d8 (8) − soak 0 = 8 | Nobby Crane HP 12 → 4
alf_tanner vs Blighter cudgel 1 — 2d10: 3+5 | Capability: +0 | Tool: +0 | Total: 8 | Difficulty: 9 | Failure
Damage: 1d8 (1) − soak 0 = 1 | alf_tanner HP 12 → 11

— back —
davey_shaw vs Blighter at the back — 2d10: 10+6 | … | Success  (exchanges 1–6: Davey 12 → 7, the Blighter 12 → 0 — down)

— front, Nobby pulled back —
— exchange 1 —
pc vs Blighter cudgel 1 — 2d10: 5+1 | Capability: +2 | Tool: +0 | Total: 8 | Difficulty: 9 | Failure
Damage: 1d8 (1) − soak 0 = 1 | pc HP 14 → 13
alf_tanner vs Blighter cudgel 2 — 2d10: 4+2 | Capability: +0 | Tool: +0 | Total: 6 | Difficulty: 9 | Failure
Damage: 1d8 (7) − soak 0 = 7 | alf_tanner HP 11 → 4

— front, Davey in for Alf —
— exchange 1 —
pc vs Blighter cudgel 1 — 2d10: 3+10 | Capability: +2 | Tool: +0 | Total: 15 | Difficulty: 9 | Success
Damage: 1d8 (1) − soak 0 = 1 | Blighter cudgel 1 HP 7 → 6
davey_shaw vs Blighter cudgel 2 — 2d10: 1+7 | Capability: +0 | Tool: +0 | Total: 8 | Difficulty: 9 | Failure
Damage: 1d8 (8) − soak 0 = 8 | davey_shaw HP 7 → 0 — down

GM-Δ 3 (continued)
  ~ npcs.nobby_crane.state.hp :: 4
  + npcs.nobby_crane.condition.conditions.split_scalp :: blood in his eyes — harder to see in a fight
  ~ npcs.alf_tanner.state.hp :: 4
  + npcs.alf_tanner.condition.conditions.cracked_ribs :: harder to fight, lift or run
  ~ npcs.davey_shaw.state.hp :: 0
  + npcs.davey_shaw.condition.conditions.skull :: down; untreated for an hour → survival roll
  + world_state.pending.blighter_back :: down in the back passage (Davey's knife)
  ~ player.condition.hp :: 13
  ~ world_state.time :: Day 7 21:05, night
```

Davey is gone down the passage with his knife out before you finish saying it.

Nobby Crane comes through the door himself, hammer up, roaring. You meet him in the doorway. The cane catches him over the eye and the second blow opens his scalp to the bone, and suddenly Nobby is a big man who can't see for his own blood. He backs out into the street, still roaring, shoving his men forward.

From the back passage comes a crash, a yell, and a long scuffle. Then quiet. Then Davey's voice, breathless: "Got him." He comes back up the passage holding his side, his knife red.

At the front, the next two come in together. One cudgel catches your shoulder, a glancing knock. The other catches Alf full in the ribs. You hear them go. Alf folds over and backs off the door, white-faced, and Davey shoves past him to take his place, still bleeding from the fight at the back.

He lasts one swing. A cudgel takes him over the ear and Davey drops in the doorway like a sack, right at the Blighters' feet.

Out in the street, Nobby is shouting: "Get in there! Get in!" Five of them are still on their feet, one of them hurt. On your side: you, nearly untouched; Alf, holding his ribs and breathing in little gasps; Mick, with a chair leg, shaking; and Davey on the floor of the doorway, not moving, a Blighter's boot already on his coat.

*[test note: three pauses, each correct: Nobby badly hurt (leader); Alf badly hurt; Davey down. AT PAUSE each time: morale settled from the norms. Blighters: they still outnumber (5 to 3 on their feet) → they hold; Nobby's fear (going back empty-handed) keeps him there. Rooks: "break like any gang once badly outmatched"; Mick's fear is being thought a coward, and Alf holds for Tom, so they hold while Tom does. Davey down is the point the player's own retreat rule may have been reached ("two of us go down or it goes bad"): one is down, one badly hurt. That's honestly ambiguous, and getting Davey out means reaching into the doorway, so it goes to the player. Rule conflict found: GM §3 says "a fight is one round" (SAME), and also that a round CLOSEs when it "brings a new decision". The back-door choice was kept in Round 3; this one opens Round 4.]*

---

## Round 4

**▶ Player:** That's it, we go. I grab Davey by the collar and haul him back off the doorstep. Mick, shove the tables back into the gap behind me. Alf, get the back door open. Then out the back, Davey between me and Mick, down the alley.

*[test note: action form — haul Davey clear from under the cudgel man: brawling, opposition level 2, position adverse +1 (bent into the doorway, guard down), danger the cudgel man (reaches, harm → loss), cost form "inflict harm", reach full.]*

```text
ROUND 4 | Day 7 | 21:05 | the Ten Bells, Whitechapel | saved R0 · save R10

2d10: 9+2 | Capability: +2 | Tool: +0 | Total: 13
Difficulty: 11 [position +1: bending into the doorway to grab Davey, guard down] | Stakes: loss/full | Outcome: Success

GM-Δ 4 ⟵ 3
  + world_state.material_history.r4_ten_bells_lost :: the Rooks gave up the Ten Bells to Nobby Crane's crew and went out the back carrying Davey Shaw
  ~ npcs.nobby_crane.state.position :: the Ten Bells
  ~ npcs.nobby_crane.state.plan :: A-1 hold the Ten Bells for Kaylock tonight; break what's left of the bar
  ~ npcs.sal_pruitt.state.position :: her sister's on Flower and Dean Street
  ~ npcs.davey_shaw.state.position :: carried by Tom and Mick through the alley
  ~ world_state.location :: whitechapel
  ~ world_state.time :: Day 7 21:08, evening
```

You go down on one knee in the broken doorway, get both fists in Davey's collar and heave. The Blighter over him swings and you feel the cudgel go past your ear and crack the doorframe instead. Then Davey is sliding back across the flagstones and Mick is screaming as he drags a table into the gap.

Alf has the back door open. The Blighter Davey knifed is lying in the back passage, groaning, and you step over him. Davey's boots bump down the step into the yard. Behind you there's a crash as the tables go over and the Blighters pour into the Ten Bells cheering.

Nobody follows you into the alley. They came for the pub, and now they have it. Through the fog behind you, you hear the bar going to pieces.

Davey isn't waking up. There's blood in his hair and his breathing is slow and loud. A man hit like that needs a surgeon, and tonight. The nearest that takes a poor man at night without a letter is the London Hospital on Whitechapel Road, ten minutes off at a carry.

*[test note: success at full reach: Davey dragged clear, no cost. No pursuit: Nobby's plan is the pub, and with the Rooks gone the pub is his. Settled from his plan, no roll. The London Hospital is the usual answer (GM §3.5 USUAL): a real 1868 charity hospital on Whitechapel Road that took accident cases at night. Davey is down and untreated, so the survival roll comes due one hour after he fell (21:05) unless treatment stabilises him (RULES §5 DOWN).]*

---

## Round 5

**▶ Player:** London Hospital, now. Mick, take his feet. Alf, can you walk? Then walk.

```text
ROUND 5 | Day 7 | 21:08 | Whitechapel → the London Hospital | saved R0 · save R10

GM-Δ 5 ⟵ 4
  + locations.london_hospital :: the London Hospital, Whitechapel Road, zone whitechapel; porter's lodge, accident ward, night surgeons
  ~ npcs.davey_shaw.state.position :: the London Hospital, accident ward
  ~ npcs.davey_shaw.condition.conditions.skull :: cracked skull; stabilised; in hospital at least a week; no fighting
  + npcs.ezra_watts :: night porter, depth 0; asks the questions he's paid to and writes the answers down
  + world_state.pending.porter_report :: the porter's book (a man beaten about the head, brought by "friends" Tom and Alf) goes to the police on the morning round; due Day 8 morning
  ~ npcs.alf_tanner.condition.conditions.cracked_ribs :: strapped; harder to fight, lift or run for about a week
  ~ world_state.location :: london_hospital
  ~ world_state.time :: Day 7 21:25, evening
```

You carry him down the alley and out onto Wentworth Street, then the long way round to avoid Commercial Street, past shut shops and a coffee stall where nobody looks up. Alf walks bent over, one hand on the wall. Mick doesn't stop talking under his breath the whole way.

The London Hospital is a long grey front with gas lamps at the gate. The night porter, an old man named Watts, comes out of his lodge, takes one look at Davey's head and shouts for the house surgeon without asking anything at all. Then, while two orderlies carry Davey in on a board, he asks everything. Name. Address. How did it happen? Who are you?

"Fell down the stairs," Mick says.

Watts writes "beaten about the head" in his book anyway, and under it, "brought by friends, Tom Kell and Alfred Tanner." You know what that book is. In the morning a constable goes round the hospitals and reads it.

Twenty minutes later the young house surgeon comes out wiping his hands. "Cracked skull. He'll live if he lies still for a week, and he won't if he doesn't." He looks at Alf. "And you've broken ribs. Sit down before you fall down." He straps Alf up himself, tight enough that Alf grunts.

There's no charge. It's a charity hospital; the poor of Whitechapel come in off the street.

*[test note: the PC reached treatment inside the hour, so treatment stabilises Davey and no survival roll is made (RULES §5 DOWN). The porter's report comes from the usual practice (GM §3.5 USUAL): hospitals logged assault cases, and police read the books. It's written as a pending consequence with a due, so the world carries it on its own. The witness chain (RULES §15.7) starts with the porter. Span 21:08 → 21:25: nothing.]*

---

## Round 6

**▶ Player:** Mick, run to the rail yards and find Jacob. Tell him the Ten Bells is gone and Davey's in the London. Alf, you stay with Davey. I'm going back to have a look at the Ten Bells from across the street. I won't go near it.

*[test note: Mick's search is an NPC's uncertain act → `ask`: for +1 (Jacob and Evie are known to be at the yards), +1 (zone point: Mick thrives in disorder, surface −2, open act); against −1 (fog over a big yard; Jacob is scouting to stay unseen). The PC's watch is an action form: streetwise, opposition level 2, sensory favourable −1 (fog, lit windows), danger five Blighters a street away (loss, "a threat acts"), reach full.]*

```text
ROUND 6 | Day 7 | 21:25 | the London Hospital → Commercial Street | saved R0 · save R10

mick_doyle — 2d10: 2+8 | Likelihood: +1 [for: Jacob and Evie are known to be at the rail yards tonight +1; zone point: Mick thrives in disorder (surface -2), open act +1; against: night fog over a big yard; Jacob is scouting to stay unseen -1] | Total: 11 → NO, BUT

2d10: 9+8 | Capability: +2 | Tool: +0 | Total: 19
Difficulty: 9 [sensory -1: fog and the broken windows lit from inside] | Stakes: loss/full | Outcome: Success

GM-Δ 6 ⟵ 5
  ~ npcs.mick_doyle.state.position :: Whitechapel rail yards
  + world_state.pending.mick_finds_evie :: NO, BUT — Mick misses Jacob in the fog; finds Evie at the yard gate near midnight; due Day 7 23:40
  ~ npcs.alf_tanner.state.plan :: stays by Davey's bed at the London
  + player.knowledge.facts.ten_bells_now :: Nobby holds the Ten Bells with four Blighters; one on the door; two carried the hurt men toward the rail yards; a runner went the same way
  + world_state.pending.nobby_runner :: the runner reaches Kaylock's train with the news; due Day 7 22:15
  ~ npcs.rexford_kaylock.state.due :: A-1 Day 7 22:15 hears from Nobby's runner
  + npcs.nobby_crane.knowledge.facts.kell :: the Rook who split his scalp was Tom Kell, known by sight
  ~ world_state.time :: Day 7 22:00, evening
```

Mick is off down Whitechapel Road at a run before you've finished, glad to be moving.

You come back up Commercial Street on the far side and stop in the doorway of a closed pawnbroker's, opposite the Ten Bells, in the fog. Nobody looks your way. The Ten Bells is lit up like a lantern with its windows gone, and you can see straight in.

Nobby Crane sits on the end of the bar with a rag tied round his head, drinking Sal's gin from the bottle. Four Blighters are with him, one of them nursing his hand. A fifth leans in the doorway with his cudgel, a guard. While you watch, two more come out of the back carrying the sledge man between them, and the man Davey knifed comes hopping after with his arm round a third. They head north up Commercial Street, toward the rail yards. A boy in a green cap runs ahead of them.

That's Kaylock's train they're going to. And the boy is carrying the news.

Nobby looked at your face over that cane. "Kell of the Rooks" isn't a hard name to put to a face in Whitechapel.

*[test note: NO, BUT means less or later: Mick misses Jacob and finds Evie near midnight, written as a pending consequence with its own due. The Blighters carrying their hurt men home, and Nobby sending word to Kaylock, are the plain competent next steps of their side. Kaylock's due moved from "Day 8 morning" to 22:15, because a real channel (the runner) brings him the news sooner. Nobby knowing Tom's name comes from the PC's own trait ("gang name on the street"), not from invention.]*

---

## Round 7

*GM correction first. In Round 6 I had the Blighter Davey knifed hopping up the street. He was down at 0 HP and couldn't walk, so he was carried. I also had five Blighters left in the pub, which was wrong: four men left carrying the two downed ones. What you saw from the pawnbroker's doorway was **Nobby with one man**, the one with the hurt hand, on the door. Nothing else changes.*

**▶ Player:** Two of them, both hurt? I'm going back in. Cosh in my pocket, cane in my hand. Across the street fast in the fog, the doorman first before he knows it's me, then Nobby. If a third one shows up, or I get hurt bad, I'm out the back again.

*[test note: GM mistake found while planning the next roll: the narration had a 0 HP man walking (state says down), and the head count didn't add up (8 in the crew: 2 down, 3 hurt, 3 fresh). Fixed under GM §7.4: it changed nothing already resolved, so one corrected entry and a line to the player before the next round. Then: the approach (action form, no skill fits, so capability is level only; sensory favourable for fog and a doorman lit from behind; decisive reach). Decisive = he reaches the doorman unseen and gets the first blow in. NEO has no rule for striking an unaware target; v6.3 AI_RULES had one ("opposes with awareness; once the approach beats it, the strike is not rolled again"). The GM applied the first blow with the harm form and gave the fight that followed a favourable position. Then the combat form: the PC alone against the doorman (HP 1) and Nobby (HP 4).]*

```text
ROUND 7 | Day 7 | 22:00 | the Ten Bells, Whitechapel | saved R0 · save R10

2d10: 8+7 | Capability: +0 | Tool: +0 | Total: 15
Difficulty: 9 [sensory -1: fog; the doorman is lit from behind and looking into the dark] | Stakes: loss/decisive | Outcome: Success
Damage: 1d6 (5) − soak 0 = 5 | the doorman HP 6 → 1

— exchange 1 —
pc vs the doorman — 2d10: 5+7 | Capability: +2 | Tool: +0 | Total: 14 | Difficulty: 10 | Success
Damage: 1d8 (1) − soak 0 = 1 | the doorman HP 1 → 0 — down

2d10: 6+8 | Capability: +2 | Tool: +0 | Total: 16
Difficulty: 9 [sensory -1: Nobby can barely see through the blood] | Stakes: loss/full | Outcome: Success
Damage: 1d8 (3) − soak 0 = 3 | Nobby Crane HP 4 → 1

GM-Δ 7 ⟵ 6
  ~ player.knowledge.facts.ten_bells_now :: corrected: Nobby and one hurt Blighter held the pub; the knifed man was carried out
  + continuity_status.corrected.r6 :: knifed Blighter hopping at HP 0, five left in the pub → carried; two left (GM §7.4)
  + world_state.pending.ten_bells_doorman :: down in the doorway, HP 0
  ~ npcs.nobby_crane.state.hp :: 1
  ~ npcs.nobby_crane.state.status :: beaten in the back passage; yielded to Tom Kell
  ~ npcs.nobby_crane.state.plan :: stay alive; get word to Kaylock; blame the Rooks' numbers
  ~ npcs.nobby_crane.state.due :: A-1 when he is free or a Blighter finds him, tells Kaylock it was Kell
  + npcs.nobby_crane.relationships.pc.grievance.r7_beaten :: beaten twice by Tom Kell in one night, in front of his own men
  ~ player.skills.brawling.evidence :: 1
  ~ player.growth_period.credited :: [brawling]
  + world_state.pending.carriers_return :: three Blighters and the hurt sledge man come back to hold the pub as Nobby ordered; due Day 7 23:00
  ~ world_state.location :: ten_bells
  ~ world_state.time :: Day 7 22:04, evening
```

You come out of the fog at a fast walk, collar up. The man in the doorway peers out into the dark with the light behind him and sees a shape, and that's all he sees. You hit him with the cosh before he's worked out the shape is coming straight at him, and as he reels, the cane finishes it. He goes down across the threshold, over the same boards Davey lay on an hour ago.

Nobby hears it. He comes off the bar with his hammer, wiping his eyes with his sleeve, and he can't see a thing through the blood. He swings at the noise, misses by a yard, and then he does the sensible thing and runs for the back passage. You catch him halfway down it. The cane takes him across the back and he hits the wall, and when you raise it again he throws the hammer down.

"All right! All right, my son. All right." He slides down the wall with his hands up and his face a red mask. "You win the night."

The Ten Bells is yours again: a bar in pieces, every window gone, Sal's gin on the floor, one Blighter out cold in the doorway and Nobby Crane sitting in the passage with his hands up.

You got through it with one bruise on your shoulder. The fight's left you feeling sharper with your fists than you were this morning.

*[test note: the batch paused when the doorman fell. Morale settled for Nobby: alone, badly hurt, half-blind; the Blighters' norm is "break when their leader falls or the fight turns; run rather than die" → he runs. The chase is the plan's next step ("then Nobby"), so no stop. Two findings: (1) the action form only applies damage when the opposition is a recorded actor; against a level the GM runs harm by hand. (2) "Reach full" means two things: RULES §4 says the stated objective ("put him down"), RULES §5 says one hit. Here one hit left Nobby on 1 HP, still standing, so the objective wasn't met; his morale settled it (he yields). Brawling earned evidence (Nobby is a real challenge, level 3 vs the PC's 5 − 2). The span flagged Nobby with no due; given one.]*

---

## Round 8

**▶ Player:** I tie Nobby's hands with his own belt, and the doorman's too, and leave the doorman where he is. Abberline's got a bounty on Blighters up at the station board. Nobby's coming with me to Leman Street. Walk, Nobby.

*[test note: the PC knows of the bounties: Abberline's notice has been on the station board since Day 4 (his recorded move), and a Rook reads the street. The span stopped at Kaylock's 22:15 due; it doesn't reach the PC (it's on his train), so time runs on. He re-plans from what he's told: he heard the pub was taken back, not that Kell then retook it. Is Abberline at the station at 22:20? That's honestly open → `ask`: for +1 (he works late on Kaylock), against −1 (past ten). The bounty itself is Abberline's recorded trigger ("when a bounty is brought in, pays it"); 10s is inside the price list's bounty range.]*

```text
ROUND 8 | Day 7 | 22:04 | the Ten Bells → Leman Street police station | saved R0 · save R10

frederick_abberline — 2d10: 10+4 | Likelihood: +0 [for: he wants Kaylock in a cell and works late on it +1; against: past ten at night; a sergeant has a bed -1] | Total: 14 → YES

GM-Δ 8 ⟵ 7
  ~ npcs.rexford_kaylock.state.due :: A-1s heard from Nobby's runner; A-1 Day 8 morning doubles protection and hunts the Rooks' new pubs
  + npcs.rexford_kaylock.knowledge.facts.ten_bells :: the Ten Bells taken back by Nobby; two men down; a Rook called Kell (he doesn't know Kell retook it)
  + npcs.ten_bells_doorman :: unknown Blighter, depth 0; down, tied with his own belt, in the Ten Bells
  ~ npcs.nobby_crane.state.position :: Whitechapel police station (Leman Street)
  ~ npcs.nobby_crane.state.status :: in the cells, charged on Abberline's bounty notice; HP 1
  + player.knowledge.facts.bounties :: Abberline's notice names Blighter men, Nobby Crane at 10s
  ~ player.money.cash :: 13s (3s + 10s bounty)
  ~ npcs.frederick_abberline.state.due :: A-1s paid Tom's bounty on Nobby; A-1 when a bounty is brought in, pays it
  + npcs.frederick_abberline.relationships.pc :: a Rook who brought in a bounty; wary, interested; credit: brought him Nobby Crane
  ~ world_state.time :: Day 7 22:35, evening
```

Nobby walks. He has no choice; he can barely see, and every time he slows you put the end of the cane in his back. Nobody stops you on Commercial Street. Two women in a doorway watch a Rook march a Blighter boss past with his hands tied, and you know by morning half of Whitechapel will have heard.

The police station on Leman Street has a blue lamp over the door. The constable on the desk half stands up when he sees who you've brought. "That's Nobby Crane."

"I know who it is," says a voice from the back office, and Sergeant Abberline comes out with his sleeves rolled up and a pen still in his hand. He's younger than you thought, with a long serious face, and he looks at Nobby, then at you, then at the cane.

He doesn't say much. He checks the notice on the board with his finger, writes in the book, and counts ten shillings out of a tin box onto the desk. Nobby goes down to the cells calling him every name he knows. Abberline writes those down too.

Then he looks at you properly. "You're one of Frye's."

It isn't really a question.

"The Ten Bells," he says. "I had three people in here an hour ago saying the Blighters had smashed it to bits. Now you walk in with Crane." He taps the pen on the desk. "Tell your Mr Frye something for me. I'd like a word with him. Quietly. Not here."

*[test note: Abberline's request is an NPC talking to the PC. He's answered in play, and the round hands back only because the answer would commit the PC to something: carrying a message from the police to his gang boss. His want is to find honest help outside the force, so the request comes from his own record.]*

---

## Round 9

**▶ Player:** I'll tell him. Can't promise he'll come. And Sergeant, the Ten Bells. Kaylock'll send them back tonight, sure as anything. Can you put a man on it?

*[test note: a request to an NPC, honestly open → `ask`: for +1 (he wants Kaylock's men caught in the act); against −1 (police guarding a gang pub would be talked about), −1 (half his station is in Starrick's pay). Likelihood −1.]*

```text
ROUND 9 | Day 7 | 22:35 | Leman Street police station | saved R0 · save R10

frederick_abberline — 2d10: 10+6 | Likelihood: -1 [for: he wants Kaylock's men caught in the act +1; against: police guarding a gang pub would be talked about -1; half his station is in Starrick's pay -1] | Total: 15 → YES

GM-Δ 9 ⟵ 8
  + npcs.joseph_hale :: Constable Joseph Hale, depth 0, one of Abberline's honest men; plan: stand at the Ten Bells till the morning relief
  + world_state.pending.hale_at_ten_bells :: Hale reaches the Ten Bells and stands on the door till morning; due Day 7 22:55
  + rights_obligations.message_to_jacob :: promise: Tom tells Jacob that Abberline wants a quiet word, not at the station
  + active_commitments.r9 :: rights_obligations.message_to_jacob
  ~ world_state.time :: Day 7 22:45, evening
```

Abberline thinks about it long enough that you expect a no. Then he leans back into the office. "Hale!"

A big slow constable comes out buttoning his coat.

"Go and stand outside the Ten Bells on Commercial Street till the relief. If anyone comes to break the place, use your rattle and write down every face." Abberline turns back to you. "That's not a favour to the Rooks. A gang war on my patch needs a constable to see it."

Hale says "Sir" to Abberline, then, a little uncertainly, "sir" to you as well, and goes out into the fog.

"Your Mr Frye," Abberline says. "Quietly. Not here." And he goes back to his office.

*[test note: YES, AND would have been more; YES is as asked. His reason is his own (a witness for a gang war), not a gift to the PC. Hale's arrival is written as a pending consequence with its own due, so it lands at the pub whether the PC is there or not.]*

---

## Round 10

**▶ Player:** I'm going up to the rail yards to find Jacob myself and give him all of it. The back ways, not Commercial Street.

*[test note: span 22:45 → 23:45. Two pending consequences fired: Hale reaches the pub (22:55), and the carriers come back (23:00). Neither stopped the span, because pending consequences carry no zone, so the tool can't tell whether they could reach the PC. The GM judged it: the carriers come down Commercial Street and the PC takes the back ways (the player's own words, and the competent least-exposed route, GM §3.4 FILL), so they don't meet, no roll. At the pub: no crew boss, no orders, a constable on the door. They don't attack a policeman and they go back (settled from the norms). Kaylock hears at 23:30 and re-plans. Mick's NO, BUT lands at 23:40: Evie at the yard gate.]*

```text
ROUND 10 | Day 7 | 22:45 | Whitechapel rail yards, the yard gate | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ world_state.pending.hale_at_ten_bells :: done: Hale on the door from 22:55, holding the tied doorman
  ~ world_state.pending.carriers_return :: done: three Blighters and the hurt sledge man found a constable on the door, went back to the train
  + world_state.pending.kaylock_hears_constable :: due Day 7 23:30 → done: a peeler on the door; Nobby missing
  ~ npcs.rexford_kaylock.state.due :: A-1 Day 8 morning doubles protection, asks his bought constables where Nobby is, sends men to find Kell
  ~ world_state.pending.mick_finds_evie :: done: Evie came out to the yard gate at 23:40
  + npcs.evie_frye.knowledge.facts.ten_bells :: lost and retaken; Davey in the London; Nobby in the cells; Abberline wants a word with Jacob
  + npcs.evie_frye.relationships.pc :: one of Jacob's Rooks; approving, dry; credit: retook the Ten Bells and brought Abberline's message
  ~ npcs.evie_frye.state.due :: A-1 Day 8 morning tells Jacob; A-3 when beat_2 opens, the Kenway mansion
  ~ rights_obligations.message_to_jacob :: passed to Evie for Jacob
  ~ world_state.time :: Day 7 23:45, evening
```

You go up through the courts behind Wentworth Street and along Brick Lane, where the night stalls are packing up, and come out by the goods yard wall. The rail yards are black and huge in the fog, all shunting engines and the smell of hot iron, and a lamp burning somewhere in the middle on what can only be Kaylock's train.

Mick is at the yard gate stamping his feet. "Can't find him, Tom. I've been all round. Can't find anybody."

You wait. At twenty to twelve a woman steps out of the dark on the inside of the gate, where you'd have sworn there was nobody, and it's Evie Frye in a dark coat, with fog on her hat.

"Mr Doyle," she says. "You've been calling my brother's name round a Blighter railway yard for an hour. Very discreet." Then she looks at you, and at your cane, and she listens.

You tell her all of it. The Ten Bells, the doorway, Davey in the London Hospital, going back in, Nobby in Abberline's cells, the constable on the door. Abberline wanting a quiet word.

When you finish she's quiet for a moment. "You lost the pub and took it back on your own, with Nobby Crane in a cell for your trouble." The corner of her mouth moves. "Jacob is going to be unbearable about this. I'll tell him in the morning. Abberline too." She looks at the yard behind her. "Go home, Mr Kell. Kaylock knows your name now. Sleep somewhere he doesn't know."

*[test note: Evie's reaction comes from her record (dry; the Creed and knowledge) and her new credit entry. Her warning is what she would plausibly know: the runner went to Kaylock's train, which she's been watching all night. It isn't a hint of hidden state, because the PC already knows Nobby saw his face. Save due at the close of R10.]*

---

## Save R10

`save_ac_A3_R10.md`: the readable part written by the GM, the capsule built by `merge` (no base: the first save), then `validate` → **valid: true**. Merge marked one entry degraded (see finding 9). Validate's advisory list: seven depth 0–1 actors with no plan (Alf, Davey, Mick, Sal, Watts, Hale, the doorman). They're incidental and should be written `due: none (incidental)` in the next change.

---

## Findings from this run

1. **The batch pauses worked.** Each of the six pauses came at a real turning point (a fall, a badly hurt fighter, a man down), and two of them were real player decisions: the back door, and Davey down. The batch never ran past a decision.
2. **Two fights at once have no shared clock.** The front and back fights were separate batches; the back one ran 6 exchanges while the front ran 2. The GM synced them by hand.
3. **"A fight is one round" vs "a round closes on a new decision."** GM §3 says both. Mid-fight decisions don't fit either cleanly.
4. **No rule for striking an unaware target.** v6.3's AI_RULES had one; NEO lost it. The GM improvised with the harm form.
5. **"Reach full" means two things.** RULES §4: the stated objective. RULES §5: one hit. "Put him down" with one hit left Nobby standing on 1 HP.
6. **The action form applies damage only against a recorded actor.** Against a `level` opposition the GM runs the harm form by hand.
7. **"Night" in a due is 21:00 to the tool**, but the daypart table says night is 00–06. A "Day 7 night" due is ambiguous.
8. **GM-Δ flow mappings with commas break silently.** `{what: NO, BUT …}` parsed as `what: false`; NPC records lost half their fields; the tool reported nothing. Fixed in place by quoting. The same defect sits in the SCP background (`spine.end` split on a colon).
9. **Background placeholders can't be retired.** `player.skills.[ROLE …]` has no id, so merge marks the line degraded.
10. **Pending consequences carry no zone.** Span lists them but never stops for them, so whether one reaches the PC is always the GM's call (here, the carriers returning at 23:00).
11. **Whitechapel is one zone,** so every Whitechapel due "could reach the PC" (Kaylock on his train stopped the span twice). The GM has to judge every one.
12. **Span repeats ~15 untimed triggers on every call.** It's noise in the GM's working.
13. **A GM narration slip** (a 0 HP man walking, a wrong head count) was caught only because the GM went back to the state for the next roll. GM §7.4 repair worked as written.
14. **Undercurrent vs due.** A due that *is* the undercurrent's own racket could also trigger an undercurrent roll. The rules don't say it counts once.
