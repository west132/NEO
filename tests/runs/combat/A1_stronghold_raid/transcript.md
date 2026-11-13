# Combat test A1 — AC Syndicate: taking the cooperage yard (armed raid)

Test of the NEO play set on the `design-tripod` branch, with `worlds/BACKGROUND_AC_SYNDICATE_NEO_v0.md` and the modules file (canon mode). The stand-in player is Claude. Every roll, time step and save comes from the tool. *[test note: …]* is outside the game.

**Test start (fixture):** Day 6, 18:00, the Ten Bells. Same PC as A3 (Tom Kell, Rook). Dues before Day 6 are marked done as the canon course has them. Jacob's next move is set from his plan ("take the first Blighter stronghold"): `A-1 Day 6 21:00 leads the Rooks on the Blighter stronghold in the Black Eagle cooperage yard, Brick Lane`. The cooperage yard is developed as a location (the background lists "Blighter strongholds" as Whitechapel activity, with no specific place). This also lines up with `rooks_rising.whitechapel`, due Day 7, whose advance is "a stronghold, a street, a mill".

**Scene:** armed raid.

*[test note: first span from Day 6 18:00, PC zone the Ten Bells. Its first run **didn't stop at Jacob's 21:00 due** and ran to 23:00. The Ten Bells record was written in GM-Δ as JSON (`"zone": "whitechapel"`), and the tool finds a building's zone with a pattern that only matches YAML flow (`zone: whitechapel`). So it didn't know the PC was in Whitechapel, couldn't tell the due could reach them, and processed straight past it. Rewritten in YAML flow, the span stopped at 21:00 as it should. This is the failure §3 describes: a processing run passing a decision point. Here the cause was a silent format mismatch, and nothing flagged it.]*

---

## Round 0

Tom Kell, Rook, as in A3: brawling T2, streetwise T2, blades T1; cane, cosh, knuckle-duster; 3s; HP 14.

18:00, Day 6, the Ten Bells. Evening surface roll: nothing. The evening passes in a line: pints, shove-ha'penny, Alf and Davey arguing about nothing.

---

## Round 1

**▶ Player:** (at nine, when Jacob comes in) What's the job, boss?

```text
ROUND 1 | Day 6 | 21:00 | the Ten Bells, Whitechapel | saved R0 · save R10

GM-Δ 1 ⟵ 0
  + npcs.rook_crew_a1 :: three more Rooks (Fitch, Lenny, Old Shem), depth 0, level 1
  + npcs.jacob_frye.knowledge.facts.cooperage :: Clara's urchins: six Blighters on weeknights, crew boss Rigger, protection money counted upstairs on Fridays; tonight is a Thursday
  + npcs.jacob_frye.state.tactics :: Jacob over the back wall and through the cooperage; Tom's party in at the wicket door at his whistle; nobody touches the money till the Blighters are out
  ~ world_state.time :: Day 6 21:00, evening
```

Jacob Frye comes in out of the fog at nine with three more Rooks behind him, slaps the bar and grins at the room like he owns it, which, since Tuesday, he does.

"Coats on, gentlemen. We're going to church." He drops onto the bench beside you. "The Black Eagle cooperage, Brick Lane. Kaylock's lot count their protection money there. Clara's little horrors say six on a weeknight, and a fellow called Rigger in charge. It's Thursday." He holds up a finger. "I go over the back wall. When I whistle, Tom, you bring Alf and Davey and these three through the wicket door in the cart gate, and we squeeze them between us. Nobody touches the money till the Blighters are gone. Questions?"

Seven Rooks and Jacob against six Blighters in their own yard. The wicket is a man-sized door in a big cart gate. It's narrow, and the first one through it will be the first one hit.

*[test note: Jacob's due fired and reaches the PC: his plan needs the Ten Bells Rooks. Jacob's briefing is his record (acts first, brash, funny) plus his knowledge, developed from Clara's network and her Day 5 runner to him. The player has a real choice: go first through the wicket, send someone else, or change the plan.]*

---

## Round 2

**▶ Player:** I'll go through the wicket first, Alf right behind me. Davey, you've got the knife: stay by the gate and take anyone who runs for it. But give me ten minutes first, boss. I want to look over that wall before we go.

*[test note: action form: streetwise, opposition level 2 (the yard's watch), sensory favourable (fog, the yard lit by a brazier). Danger: being seen means the Blighters are ready. Nothing can hurt him on the wall, so the cost is a setback. Reach full: a clear count.]*

```text
ROUND 2 | Day 6 | 21:00 | Brick Lane, the brewery wall | saved R0 · save R10

2d10: 5+5 | Capability: +2 | Tool: +0 | Total: 12
Difficulty: 9 [sensory -1: fog and the yard lit by a brazier] | Stakes: setback/full | Outcome: Success

GM-Δ 2 ⟵ 1
  + npcs.rigger :: Rigger (Sam Riggs), Blighter crew boss, depth 1, level 3; a cheap revolver, five rounds
  + locations.cooperage_yard.conditions.tonight :: two at the brazier, one on the wicket, one asleep under the stairs, Rigger and one upstairs counting
  + player.knowledge.facts.cooperage :: the same, and Rigger's revolver
  ~ world_state.time :: Day 6 21:15, evening
```

Jacob shrugs. "Ten minutes. Then I'm going over whether you're back or not."

You go up the side of Truman's brewery where the drays stand, onto a barrel and up to the top of the wall, with the fog for cover. The cooperage yard below is lit by one brazier. Two Blighters stand at it, warming their hands and laughing. One sits on a crate by the wicket with a cudgel across his knees. Another is asleep on sacks under the cooperage stairs. Upstairs a window is lit, and through it you see two men at a table with money in stacks. One of them stands up to stretch, and his coat swings open on a revolver on his belt. That'll be Rigger.

Six. Not seven, not twelve. And one gun.

*[test note: success at full reach = the true picture. The truth (six men, one revolver) was developed now and recorded before it was shown, consistent with Clara's count ("six on a weeknight"). The revolver is the one danger the plan didn't know about. It's shown to the player before the fight, so they can choose with it in view (RULES §4 SHOWN).]*

---

## Round 3

**▶ Player:** Back to Jacob. Six of them, and Rigger upstairs has a gun. So you go over the back and straight up the cooperage stairs for Rigger before he can get to that window, boss. When you're on the stairs you whistle, and I take the wicket man. Alf, Fitch and Lenny take the brazier pair, and the sleeper too if he wakes. Davey and Shem hold the gate. If Rigger starts shooting, everyone gets behind the barrels.

*[test note: Jacob's answer is settled from his record. He goes for the dangerous man himself (acts first, loyal to his people) and likes the plan. Two batches run at once: upstairs (Jacob against Rigger and the counter) and the yard (the PC, Alf, Fitch and Lenny against the wicket man, the two at the brazier and the sleeper). Both get a favourable position (caught from two sides; Jacob up the back stairs before Rigger reaches the window). Then a third, short one at the gate (Davey against a runner).]*

```text
ROUND 3 | Day 6 | 21:15 | the Black Eagle cooperage yard, Brick Lane | saved R0 · save R10

— upstairs —
— exchange 1 —
jacob_frye vs Rigger — 2d10: 4+7 | Capability: +4 | Tool: +0 | Total: 15 | Difficulty: 10 | Success
Damage: 1d6 (4) − soak 0 = 4 | Rigger HP 14 → 10
  … exchanges 2–4: all Jacob's; Rigger 10 → 3 …
— exchange 5 —
jacob_frye vs Rigger — 2d10: 7+5 | Capability: +4 | Tool: +0 | Total: 16 | Difficulty: 10 | Success
Damage: 1d6 (3) − soak 0 = 3 | Rigger HP 3 → 0 — down

— the yard —
— exchange 1 —
pc vs the wicket man — 2d10: 5+10 | Capability: +2 | Tool: +0 | Total: 17 | Difficulty: 9 | Success
Damage: 1d8 (7) − soak 0 = 7 | the wicket man HP 12 → 5
alf_tanner vs brazier man 1 — 2d10: 2+5 | Capability: +0 | Tool: +0 | Total: 7 | Difficulty: 9 | Failure
Damage: 1d8 (8) − soak 0 = 8 | alf_tanner HP 12 → 4
Fitch vs brazier man 2 — 2d10: 1+9 | Capability: +0 | Tool: +0 | Total: 10 | Difficulty: 9 | Success
Damage: 1d6 (5) − soak 0 = 5 | brazier man 2 HP 12 → 7
Lenny vs the sleeper — 2d10: 5+10 | Capability: +0 | Tool: +0 | Total: 15 | Difficulty: 9 | Success
Damage: 1d6 (1) − soak 0 = 1 | the sleeper HP 12 → 11

— the gate —
davey_shaw vs brazier man 2 — 2d10: 5+8 | … | Success → HP 7 → 6
davey_shaw vs brazier man 2 — 2d10: 10+4 | … | Success → HP 6 → 1

GM-Δ 3 ⟵ 2
  + world_state.material_history.r3_cooperage :: the Rooks took the cooperage yard; Rigger down, three yielded, two fled over the back wall
  ~ npcs.rigger.state.hp :: 0 (down on the stairs; untreated by 22:25 → survival roll)
  + world_state.pending.cooperage_prisoners :: the wicket man, the counter, brazier man 2
  + world_state.pending.blighters_fled :: two run for Kaylock's train with the news; due Day 6 21:45
  ~ npcs.alf_tanner.state.hp :: 4
  + npcs.alf_tanner.condition.conditions.collarbone :: broken collarbone; can't lift his left arm; no fighting for a week
  + npcs.jacob_frye.state.carried.revolver :: Rigger's revolver, four rounds
  + locations.cooperage_yard.conditions.money :: upstairs: Thursday's takings, about £11, counted into stacks
  ~ world_state.time :: Day 6 21:25, evening
```

Jacob's whistle comes from inside the cooperage, and you go through the wicket.

The man on the crate is half up, cudgel coming round, when your cane takes him across the face. He sits back down hard and stays there, bleeding into his hands. Beside you Alf goes for the bigger of the two brazier men and walks straight into his cudgel. You hear the bone go in his shoulder. Fitch catches the other one across the back of the neck, and Lenny jumps on the sleeper as he comes up off the sacks.

Upstairs there's a single shot, a lot of shouting, furniture going over, and then Jacob's head out of the lit window with a revolver in his hand. "Your Rigger's having a lie-down, lads! Who's next?"

That ends it. The Blighters in the yard look at each other. The bleeding one on the crate puts his hands up. The big one who broke Alf's shoulder and the sleeper go up the barrels and over the back wall into the brewery yard. The last one runs for the cart gate and finds Davey there with his knife. Two cuts later he's sitting against the gate with his hands up too, and Shem is holding his collar.

Upstairs, the counter has his hands on his head. Rigger is lying on the stairs, not moving.

Alf is sitting on a barrel, grey in the face, holding his arm against his chest.

*[test note: three batches with no shared clock again (upstairs 5 exchanges, the yard 1, the gate 2). The GM put them in order by hand. In the yard the batch paused after one exchange on two "badly hurt" results. AT PAUSE: Rigger's fall reached the yard (Jacob at the window), and the Blighters' norm is "break when their leader falls" → they break. Each man's choice was settled from his own position: hurt and cornered → yields; free → runs. That's morale, not dice. Jacob used 1d6 here when his record gives him blades and a hidden blade (1d8). GM slip, noted; it changed only how long the fight upstairs took. The fight in the yard needed no player stop: Alf's injury and the runners were covered by the plan ("Davey and Shem hold the gate"). Now the fight is over, and the aftermath is the player's.]*

---

## Round 4

**▶ Player:** Davey, tie the three of them back to back. I'm going up to Rigger. I'll bind his head with his own scarf; alive, he's worth something to Abberline. Jacob, two of them got over the wall. They'll be at Kaylock's train in ten minutes and he'll come with everything he's got. Do we take the money and go, or hold?

*[test note: binding a head wound with no first-aid skill: action form, no skill (absolute grade basic, −2), opposition the task's own grade "awkward" (13), no danger to the PC (cost: setback), reach full = stabilised. Jacob's answer is settled from his record: "hold or go" against his want ("his gang strong") and his character (acts first) → hold, no roll.]*

```text
ROUND 4 | Day 6 | 21:25 | the cooperage yard | saved R0 · save R10

2d10: 10+1 | Capability: -2 | Tool: +0 | Total: 9
Difficulty: 13 | Stakes: setback/full | Outcome: Failure

GM-Δ 4 ⟵ 3
  ~ npcs.jacob_frye.state.plan :: A-1 hold the cooperage tonight as the Rooks' first stronghold; send for every Rook in Whitechapel; split the money: half to the chest, half to tonight's men
  ~ npcs.jacob_frye.state.due :: A-1s took the yard; A-1 Day 6 22:00 the Rooks he sent for start arriving
  + npcs.jacob_frye.relationships.pc :: his Rook; pleased, cocky; credit: scouted the gun; first through the wicket
  + world_state.pending.rook_runners :: Fitch runs for Rooks; due Day 6 22:00
  ~ npcs.rigger.condition.conditions.down :: the binding failed; untreated by 22:25 → survival roll
  ~ world_state.time :: Day 6 21:35, evening
```

Rigger is lying on the stairs with his head split above the ear. You wrap his scarf round it and pull it tight, and in a minute it's soaked through and blood is running down the back of his neck again. You're a docker, not a surgeon. His breathing is slow and noisy.

Jacob is counting money into his hat. "Hold, of course," he says, as if you'd asked whether the Thames was wet. "Take a man's house and then run off with his purse? That's what thieves do. We're a gang." He tips the coins into a sack. "Fitch! Run to the Ten Bells and the Brick Lane end. Every Rook who can stand, here, now. Tell them there's beer." Fitch goes. Jacob grins at you. "Good eye on that gun, Tom. And you were first through that door."

He glances at Alf on his barrel. "Alf's done for tonight. And that one," he nods at Rigger, "is either going to the hospital or the churchyard. Your call. I've got a yard to hold."

*[test note: the failed binding is a setback: time spent and Rigger still bleeding. The survival roll stays due at 22:25 (an hour after he went down) unless real treatment reaches him. Jacob gives the Rigger decision to the PC in his own words. That's his character (careless of anything that isn't the fight), not the GM offering a choice.]*

---

## Round 5

**▶ Player:** Shem, Lenny, carry Rigger. Alf, walk with me. London Hospital, then I come straight back.

*[test note: the stronghold taken is a resolved event in the borough → a mark on Whitechapel's undercurrent (a hidden cause removed +1, lasting, per the background's own Borough control box and RULES §15.4). The tool's stability form: tension 0 → +1, no step yet. The span 21:35 → 21:52 crossed the fled Blighters' due (21:45, Kaylock's train). It doesn't reach the PC, so the GM settles Kaylock's answer from his record: his line "never backs down in front of his men" and his want "Whitechapel" → he retakes it tonight, himself at the front. Starrick's recorded trigger ("when the first stronghold falls") gets its due: tomorrow morning, by wire.]*

```text
ROUND 5 | Day 6 | 21:35 | Brick Lane → the London Hospital | saved R0 · save R10

Undercurrent -2 (depth -2) · tension 0 +1 → +1

GM-Δ 5 ⟵ 4
  ~ locations.whitechapel.undercurrent.tension :: 1 (a stronghold taken, lasting)
  ~ world_state.pending.blighters_fled :: done 21:45: the two reached Kaylock's train
  ~ npcs.rexford_kaylock.state.plan :: A-1 retake the cooperage tonight with the train crew, himself at the front
  ~ npcs.rexford_kaylock.state.due :: A-1 Day 6 22:30 hits the cooperage yard with the train crew; A-1 Day 7 night breaks Rook pubs
  ~ npcs.crawford_starrick.state.due :: A-1 Day 7 morning hears by wire that the first stronghold fell; orders his lieutenants to crush the new gang
  + locations.london_hospital :: the London Hospital, Whitechapel Road
  ~ npcs.rigger.state.position :: the London Hospital, accident ward
  ~ npcs.rigger.condition.conditions.down :: fractured skull; stabilised 21:55; in hospital at least a week
  ~ npcs.alf_tanner.condition.conditions.collarbone :: strapped; no fighting for a week
  ~ world_state.time :: Day 6 21:55, evening
```

Shem and Lenny take Rigger by the arms and legs, cursing, and you walk Alf by his good side. Down Brick Lane, across Wentworth Street, out onto Whitechapel Road. Nobody stops a party of Rooks carrying a bleeding man. People step into doorways to let you by.

The night porter at the London Hospital shouts for the house surgeon at the sight of Rigger's head and asks his questions after. You give him "Sam Riggs, fell in a brewery yard" and he writes it down without believing a word. Ten minutes later the surgeon comes out. Fractured skull: he'll live if he lies still. Alf's collarbone is broken; the surgeon straps it and tells him a week. Alf says nothing at all, which for Alf is complaining.

Leaving him there means leaving Rigger there too, with only a porter between him and the door.

*[test note: real treatment reached Rigger inside the hour, so he's stabilised and no survival roll is made. The PC's "I come straight back" stands as his order; leaving Rigger unguarded is the world as it is, said in one line, not a stop.]*

---

## Round 6

**▶ Player:** Shem, you stay here with Alf. Nobody takes Rigger out of that bed. Lenny, with me, back to the yard. And when we get there, boss, two lads up on the brewery wall watching Brick Lane both ways. Kaylock'll come, and I want to see him coming.

*[test note: did the Rooks answer Fitch's call? `ask`: for +1 (a won fight and free beer in Jacob's name), +1 (zone point: the Rooks thrive, surface −2, open act); against −1 (the Rooks are three days old). The span stopped at Jacob's 22:00 due (the Rooks arriving); it doesn't reach the PC, who is on the Whitechapel Road, so time runs on.]*

```text
ROUND 6 | Day 6 | 21:55 | the London Hospital → the cooperage yard | saved R0 · save R10

rooks — 2d10: 7+5 | Likelihood: +1 [for: a won fight and free beer, in Jacob's name +1; zone point: the Rooks thrive in disorder (surface -2), open act +1; against: the Rooks are three days old; most are still Clinkers at heart -1] | Total: 13 → YES

GM-Δ 6 ⟵ 5
  ~ npcs.alf_tanner.state.plan :: with Shem, sit by Rigger's bed; nobody takes him out
  + npcs.rook_crew_a1.state.split :: Shem at the London; Lenny with Tom; Fitch at the yard
  ~ world_state.pending.rook_runners :: done 22:00: eight more Rooks turned out; thirteen in the yard with Jacob
  ~ npcs.jacob_frye.state.due :: A-1s the Rooks arrived; A-1 when Kaylock comes, meets him at the cart gate
  + npcs.rooks_reinforcements :: eight Rooks, depth 0, level 1
  + player.routines.tonight :: two Rooks on the brewery wall watching Brick Lane
  ~ world_state.location :: cooperage_yard
  ~ world_state.time :: Day 6 22:12, evening
```

The cooperage yard has filled up while you were gone. Eight more Rooks, dockers and carters, a couple of lads who look about fifteen, standing round the brazier drinking Blighter beer out of Blighter mugs. The three prisoners sit tied back to back against the barrels, looking at their boots.

Jacob is on the cooperage steps with the revolver in his belt and a mug in his hand. He likes the wall idea. "Look at that, a man who thinks. Oi, you two, up on the wall. If you see green, shout."

Thirteen Rooks in the yard, counting you. Jacob has a revolver with four rounds in it. The cart gate is shut and barred, the wicket bolted. The fog is getting thicker.

*[test note: YES = as asked: eight came. The yard's defence follows Jacob's character (he likes the idea) and the player's suggestion.]*

---

## Round 7

**▶ Player:** I have a mug of their beer and wait by the gate. Keep the lads off the beer till it's over.

```text
ROUND 7 | Day 6 | 22:12 | the cooperage yard | saved R0 · save R10

GM-Δ 7 ⟵ 6
  + world_state.pending.kaylock_attack :: Kaylock and twelve of the train crew (level 2; cudgels, two sledges, lanterns) come down Brick Lane to the cart gate; due Day 6 22:30
  ~ npcs.rexford_kaylock.state.position :: Brick Lane, outside the cooperage cart gate
  ~ world_state.time :: Day 6 22:30, evening
```

Eighteen minutes. The lads grumble about the beer and drink it anyway, slower.

Then the boy on the wall shouts. "Green! Green coming! Loads of 'em!"

From the top of the barrels you can see them: lanterns bobbing down Brick Lane in the fog, a dozen at least, two sledges on shoulders. At the front, a big man in a long coat with a railwayman's cap, laughing loudly at something. You've never seen Rexford Kaylock up close, but you know him. Everyone in Whitechapel does.

"Frye!" he bellows at the gate. "You're in my yard!"

Thirteen of them, then, and Kaylock himself. Thirteen of you. The gate is barred and they have sledges. The back wall goes over into the brewery, if it comes to that.

Jacob jumps down from the steps grinning like Christmas.

*[test note: the span stopped at Kaylock's 22:30 move; it reaches the PC. The lookout (the player's suggestion) sees them coming → the PC's side acts first, the danger shown: numbers, sledges, Kaylock, the back wall as a way out. The crew size came from Kaylock's record ("a train full of Blighters, T1–T2"), developed and recorded before it was shown.]*

---

## Round 8

**▶ Player:** Let them break the gate. Jacob on the cooperage steps with the gun, half of us behind the barrels on the left of the gate, half on the right. When they come through, they come through in a crush, and we hit them from both sides. I'm by the gate. Nobody kills a man who drops his cudgel. If it turns against us, over the back wall into the brewery.

*[test note: one combat form: 13 a side. Ours: the PC, Jacob, Davey, Lenny, Fitch, eight Rooks at level 1. Theirs: Kaylock (level 4, leader) and twelve Blighters (level 2). Position favourable (the crush in the gate, hit from both sides). The tool made the pairings itself by list order: it put the PC on Kaylock and Jacob on a common Blighter. The plan said nothing about who takes Kaylock, so the order the GM typed decided the most important match-up of the night. The batch paused **4 times in 4 exchanges**: with 26 fighters someone is "badly hurt" in almost every exchange. Three of those pauses needed nothing (morale held, no world change); the GM re-sent the form. Davey (HP 2) pulled out of the line at the second pause on his own judgment. Full log: fight_log_part1.txt and fight_log_part2.txt.]*

```text
ROUND 8 | Day 6 | 22:30 | the cooperage yard, the cart gate | saved R0 · save R10

— exchange 1 —
pc vs Rexford Kaylock — 2d10: 6+6 | Capability: +0 | Tool: +0 | Total: 12 | Difficulty: 9 | Success
Damage: 1d8 (5) − soak 0 = 5 | Rexford Kaylock HP 16 → 11
jacob_frye vs Blighter 1 — 2d10: 6+8 | Capability: +4 | Tool: +0 | Total: 18 | Difficulty: 9 | Success
  … 11 more lines; pause: Blighter 7 badly hurt; Rook 8 badly hurt …
— exchanges 2–3 —
pc vs Rexford Kaylock — 2d10: 9+2 | … | Success | Kaylock HP 11 → 9
pc vs Rexford Kaylock — 2d10: 9+4 | … | Success | Kaylock HP 9 → 6
Rook 8 vs Rexford Kaylock — 2d10: 3+9 | Capability: -2 | … | Success | Kaylock HP 6 → 3
  … pauses: Lenny, Fitch, Rook 3 badly hurt; Davey badly hurt; Blighter 11 falls …
— exchange 4 —
pc vs Rexford Kaylock — 2d10: 9+7 | Capability: +0 | Tool: +0 | Total: 16 | Difficulty: 9 | Success
Damage: 1d8 (1) − soak 0 = 1 | Rexford Kaylock HP 3 → 2
Rook 6 vs Rexford Kaylock — 2d10: 10+2 | Capability: -2 | Tool: +0 | Total: 10 | Difficulty: 9 | Success
Damage: 1d6 (4) − soak 0 = 4 | Rexford Kaylock HP 2 → 0 — down
  … Blighters 1, 4, 5, 6 down; Rook 3 down …
>>> PAUSE: their leader Rexford Kaylock falls

GM-Δ 8 ⟵ 7
  + player.fighting_style.yard :: both sides of the gate; nobody kills a man who drops his cudgel; if it turns, over the back wall
  ~ npcs.rexford_kaylock.state.hp :: 0 (down in the cart gate; helpless; untreated by 23:35 → survival roll)
  + world_state.pending.yard_fight :: six Blighters down incl. Kaylock; four yielded, three ran
  + world_state.pending.blighters_fled_2 :: three run for the train; due Day 6 22:50
  ~ npcs.davey_shaw.state.hp :: 2
  + npcs.rooks_reinforcements.state.hurt :: Rook 3 down; Rooks 1, 8, Fitch, Lenny badly hurt
  ~ npcs.jacob_frye.state.due :: A-1 Day 6 22:40 walks to Kaylock with his blade out
  ~ world_state.time :: Day 6 22:38, evening
```

The sledges take the cart gate off its bar on the sixth blow, and the Blighters come through it in a shouting mass with Kaylock at the front, too many at once for the space, straight into the Rooks on both sides.

You get to Kaylock first because you're nearest. He's big and slow and laughing, and he hits like a dray horse when he connects. He doesn't connect. Your cane opens his cheek, then his scalp, and every time he swings you aren't there. Around you it's a brawl in fog and lantern light: Davey stabbing and cursing until a cudgel lays his arm open and he staggers back out of it; Fitch and Lenny going down on one knee and getting up again; Jacob in the middle with a kukri, laughing as loudly as Kaylock.

Kaylock goes down between you and a Rook called Old Shem's nephew, who hits him over the head with a barrel stave while he's still swaying from your cane.

When Kaylock falls, the fight goes out of the Blighters all at once. Three of them run back out through the broken gate and up Brick Lane. Four throw down their cudgels and sit down on the cobbles with their hands up. Five more are lying in the yard. One Rook is down too, and half of you are bleeding.

You've got a bruise, maybe two. Nobody really landed on you.

Kaylock lies on his back in the gate with his eyes open, breathing, not moving. Jacob walks over to him, wiping the kukri on his sleeve. He doesn't put it away.

*[test note: AT PAUSE: the leader falls → the Blighters break (their norm). Each one's choice was settled from his position: the hurt ones yield, the free ones run. Kaylock is helpless, and RULES §5 lets a helpless actor be killed without a roll. Jacob's next move comes from his record and the canon course: Jacob kills Kaylock in the game, as a Templar-backed lieutenant. The PC is standing there, and the player's own rule was "nobody kills a man who drops his cudgel". That makes this a real decision → hand back. Canon note: in the game Kaylock dies on his train during the gang war, after the borough's grip breaks. Here he falls on Day 6 at a stronghold. Canon mode lets play change the course; the beat's actors adapt.]*

---

## Round 9

**▶ Player:** Jacob, wait. He's down, he's done. Alive he's worth more. Abberline's got a bounty on him, and every Blighter in Whitechapel sees Kaylock in a cell instead of a martyr.

*[test note: is Jacob's choice settled by his record? Flip test: would the record decide it the same way if it went the other way for the player? Jacob is an Assassin and Kaylock is the Templar-backed lieutenant he came to London to kill, but Jacob also acts on his gang's interest, so it's honestly open. INFLUENCE first: persuading him is a player action. The PC has no persuasion skill (level only, 3) against Jacob (leadership, 9) → −4. Then the `ask`. The PC has credit tonight (+1); against him: Kaylock is the man Jacob came to kill (−2), and the influence roll's failure (−2, RULES §9.1 INFLUENCE).]*

```text
ROUND 9 | Day 6 | 22:38 | the cooperage yard | saved R0 · save R10

2d10: 4+5 | Capability: -4 | Tool: +0 | Total: 5
Difficulty: 10 | Stakes: setback/full | Outcome: Failure

jacob_frye — 2d10: 3+3 | Likelihood: -3 [for: Tom has credit with him tonight (the gun, the wicket) +1; against: Kaylock is Starrick's lieutenant, the man he came to London to kill -2; Tom's argument fell flat (influence failure) -2] | Total: 3 → NO, AND

Undercurrent -2 (depth -2) · tension +1 +2 → +3
XP +38 (the cooperage yard taken (R3)) → level 3, 38 XP
XP +55 (Kaylock's crew beaten at the cart gate (R8)) → level 3, 93 XP

GM-Δ 9 ⟵ 8
  ~ player.progression.state :: {level: 3, xp: 93}
  + world_state.material_history.xp_… :: the cooperage yard taken (R3): 38 · Kaylock's crew beaten (R8): 55
  + quests.tq_whitechapel.code_given :: A-1 (R1; given late, R9)
  ~ quests.tq_whitechapel.status :: active
  ~ npcs.rexford_kaylock.state.status :: dead — killed by Jacob Frye with a kukri in the cart gate, helpless
  + world_state.material_history.r9_jacob_remark :: NO, AND: Jacob told Tom off in front of the Rooks
  ~ npcs.jacob_frye.state.due :: A-1s killed Kaylock; A-1 Day 7 morning takes Kaylock's train before the Blighters regroup
  ~ locations.whitechapel.undercurrent.tension :: 3 (Kaylock killed: a decisive act +2, lasting)
  + world_state.material_history.r9_kaylock :: Kaylock killed in the cooperage gate, not on his train as in the game
  ~ world_state.time :: Day 6 22:45, evening
```

Jacob hears you out. Then he crouches by Kaylock and looks at him for a moment.

"Abberline's cells have a back door, Tom. They all do. Starrick owns the key." He says it quietly, and then the kukri goes in under Kaylock's ribs, once, and Kaylock lets out a breath and doesn't take another.

Jacob stands up and looks round at the yard: at the Rooks, at the four Blighters sitting with their hands up, at you. "And next time you want to tell me my business," he says, loud enough for everyone, "do it where the whole gang can't hear you." Then he grins, because Jacob always grins. "Good fight, though. Beer's on Rexford."

Nobody laughs much. A few of the Rooks look at you. A few look at Kaylock.

You feel the night in your shoulders: two fights, a stronghold, the man who ran Whitechapel dead in the gate.

*[test note: NO, AND = refused, plus the smallest trouble this actor can make: a public telling-off. It goes in the history, not as a grievance, because the relationship moves only on a material event (RULES §15.1 CHANGE). The GM first wrote it as a grievance, then corrected it before showing the block. Two GM slips found while closing the fight. (1) Quest A-1 was never made active when the PC joined the raid in R1 ("starting the work without reservation" is acceptance, RULES §10). (2) XP was not paid at R3 or R8, though GM §3.6 AFTERMATH says "a fight won → RULES §13 XP". Both paid now with a note. The turn's checklist was there, and it was skipped twice under the weight of combat processing. Kaylock dead is a decisive act in Whitechapel (the background's Borough control box): +2, lasting; the undercurrent's tension is now +3, two short of a step.]*

---

## Round 10

**▶ Player:** I take my share and walk Davey and the other hurt lads down to the London Hospital. I sit with Alf a while.

```text
ROUND 10 | Day 6 | 22:45 | the cooperage yard → the London Hospital | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ player.money.cash :: 11s (3s + 8s share)
  + npcs.jacob_frye.state.carried.rooks_chest :: £5 10s for the Rooks' chest
  ~ world_state.pending.blighters_fled_2 :: done 22:50: the train crew argue about who leads; one goes to wire Starrick's office
  ~ npcs.crawford_starrick.state.due :: A-1 Day 7 morning hears Kaylock is dead and the first stronghold fell; orders his lieutenants to crush the new gang
  + world_state.pending.blighter_prisoners :: seven Blighters tied in the yard; Jacob means to turn them loose at dawn without their boots
  ~ world_state.location :: london_hospital
  ~ world_state.time :: Day 6 23:15, evening
```

Jacob splits the money on the cooperage steps like a man handing out Christmas presents: half into a sack for "the Rooks' war chest", half into thirteen piles. Yours comes to eight shillings. More than a docker makes in three days.

You take Davey and the two worst of the others down Brick Lane to the London Hospital. Watts the porter sees you coming and goes to wake the house surgeon without a word.

Alf is awake in the ward with his arm strapped across his chest. Rigger is three beds down with his head bandaged, snoring.

"Heard shouting," Alf says.

You tell him. Kaylock dead in the gate. The cooperage is the Rooks'. The Blighters on the train will be fighting over who's boss by now.

Alf thinks about it for a long time. "Kaylock," he says at last. "Well." And then: "Jacob kill him?"

You nod.

Alf looks at the ceiling. "He'd have killed us," he says, and closes his eyes.

*[test note: span 22:45 → 23:15 crossed the fled Blighters' due (22:50, at the train). It doesn't reach the PC; the GM settles what happens there: with no leader, they argue and one wires Starrick. Starrick's due now carries Kaylock's death too. The share is the split Jacob announced (half the £11 among thirteen men ≈ 8s each), close to the background's real 1868 wages. Save due at the close of R10.]*

---

## Save R10

`save_ac_A1_R10.md`: merge (first save) → valid; validate → **valid: true**, no advisory items. While assembling it, a script error left the readable part out of the file, and **validate still said valid: true** (finding 8). The readable part was then added and the file validated again.

---

## Findings from this run

1. **The JSON-vs-YAML zone bug made the span run past a decision.** A building recorded as JSON in GM-Δ hid the PC's zone from the tool, and the span ran straight past Jacob's 21:00 move. Nothing warned. That's the §3 failure, from a processing gap.
2. **The tool picks who fights whom by list order.** The PC got Kaylock because the GM typed him first. The plan never said who takes the leader.
3. **Mass fights pause on nearly every exchange** (4 pauses in 4 exchanges at 13 a side), because some fighter is always "badly hurt". Most pauses needed nothing. Pausing on *any* badly hurt fighter is too fine-grained for a crowd; a pause on the PC, named allies, leaders and falls would cover it.
4. **The checklist slipped under combat load.** Quest A-1 wasn't activated when the PC joined the raid, and XP wasn't paid after either fight. GM §3.6 AFTERMATH lists both; the GM caught them at R9. The tool could flag both (a won combat form with no award since; actions on a quest's objective while it isn't active). That's processing.
5. **Allies' weapons.** The GM typed Jacob's damage as 1d6 instead of his record's blade. The combat form takes damage per fighter from the GM, not from the record.
6. **The influence rule worked:** persuasion failure −2, then an ask at −3 → NO, AND. The world went against the player and stayed in character, with no GM mercy and no GM cruelty.
7. **Canon drift is handled by the rules:** Kaylock died on Day 6 in a yard instead of on his train. The canon course's actors now have to adapt (Jacob takes the train tomorrow). Nothing in the rules broke.
8. **validate passed a save with no readable part at all.** It checks the capsule and lints the readable part, but never checks that the readable part exists.
9. Same as A3: the placeholder-key degraded line, and pending consequences with no zone.
