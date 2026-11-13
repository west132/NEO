# Combat test A2 — AC Syndicate: the night shift at the jute mill (the "creature" scene)

Test of the NEO play set on the `design-tripod` branch, with the AC Syndicate background and the modules file. The stand-in player is Claude; every roll and time step comes from the tool.

**Same scene, two worlds: the gap.** SCP's scene 2 is a creature fight (SCP-3683 pigeons). AC Syndicate 1868 has no creatures: its `creatures_or_threats` lists Blighters, Templar agents, constables, thieves, river gangs, **factory machinery, runaway carriages, fire, disease**. The nearest equal is a **non-human danger**, so this run puts a hazard where SCP has a beast. It's the background's own side quest `side_mill_children` (B), opened by Clara's recorded Day 5 runner. Inventing a guard dog or a rat swarm to match SCP would have been the GM making content to fit a test.

**Test start (fixture):** Day 5, 11:40, the Ten Bells; Tom Kell, Rook, as in A3. Dues before Day 5 marked done.

---

## Round 1

*[test note: span from 11:40 (arrived): the morning surface roll came up nothing, and it stopped at Clara's B "Day 5 afternoon" (the tool reads "afternoon" as 12:00). It reaches the PC: the runner is sent to "whoever is fighting the Blighters", and that's the Rooks' pub.]*

At noon a barefoot boy of about nine comes into the Ten Bells looking for Jacob Frye, and finds you instead.

**▶ Player:** Jacob's out. I'm Rooks. What's Clara want?

```text
ROUND 1 | Day 5 | 12:00 | the Ten Bells, Whitechapel | saved R0 · save R10

GM-Δ 1 ⟵ 0
  + npcs.pip :: Pip, one of Clara's runners, depth 0
  ~ npcs.clara_odea.state.due :: Bs sent Pip (Jacob out; Tom took it); B Day 5 18:00 meets the Rooks at the mill wall on Hanbury Street
  + quests.side_mill_children.code_given :: B
  ~ quests.side_mill_children.status :: active
  + locations.jute_mill :: Starrick & Co. jute mill, Hanbury Street: looms and carding engines on belts; a gatehouse; Clara's coal chute; night shift of about thirty children; jute dust and oil lamps
  ~ world_state.time :: Day 5 12:10, afternoon
```

"Clara says the Rooks says they fight the Blighters," the boy says, chewing something. "So there's a mill on Hanbury Street. Starrick's. Kids work it all night. She wants 'em out. Says come to the back wall at six and she'll show you how."

**Code B**: *the mill children.* You tell him the Rooks will come. He's gone before you finish the sentence.

*[test note: the PC took it on, so the quest gets its code (RULES §10). The span flagged Pip as "important with no due": the quest line named him, so he counted as a quest actor. Correct: an incidental can't be named in a quest. The line was reworded.]*

---

## Round 2

**▶ Player:** I find Alf and Davey and we're at the back wall on Hanbury Street at six. Not Jacob's job, ours.

```text
ROUND 2 | Day 5 | 12:10 | Hanbury Street, behind the jute mill | saved R0 · save R10

GM-Δ 2 ⟵ 1
  + npcs.alf_tanner :: Big Alf, depth 1 · + npcs.davey_shaw :: Davey Shaw, depth 1
  + npcs.mill_guards :: two Blighters on the mill gate, depth 0, level 2
  + npcs.grieve :: Mr Grieve, night foreman, depth 1; plan: run the night shift 19:00–06:00
  + npcs.clara_odea.knowledge.facts.mill :: thirty kids from seven; Grieve and his strap; two Blighters in the gatehouse; the coal chute into the boiler cellar; Annie lost two fingers last week
  ~ world_state.time :: Day 5 18:00, evening
```

At six it's dark already. Clara O'Dea is sitting on the wall like a cat. Eleven, maybe, in a man's coat cut down, with eyes that have already counted your weapons.

"Three of you," she says. "Jacob Frye said he'd beat the whole of London and he sends three." But she climbs down. "Night shift's thirty kids from seven o'clock. Grieve's the foreman; he's got a strap. Two Blighters in the gatehouse on the street side, smoking. Round the back there's a coal chute drops into the boiler cellar. I got in that way twice." She looks at the dark windows. "My friend Annie lost two fingers in a carding engine last week. Grieve docked her for the blood on the jute."

What's in a mill at night is machines: steam, belts that take hands, dust, oil lamps. And thirty children in the middle of it all.

*[test note: span 12:10 → 18:00 stopped at Clara's 18:00 meeting, which reaches the PC. The mill's people were developed from the location's conditions and Clara's knowledge, and recorded before they were shown. The danger here is the machinery, shown as plainly as a beast would be.]*

---

## Round 3

**▶ Player:** We wait till the shift's started and the street's quiet. Then Clara and me go down the chute. Alf, Davey: round the front to the gatehouse. When you hear the back door go, sit on those two Blighters, and quietly.

*[test note: Possibility (RULES §2) before any roll. A coal chute is a hatch made for sacks of coal, and the location says Clara has used it twice. A broad docker's shoulders don't fit through a 14-inch hatch. That's impossible for Tom, not a roll, and it's shown before he tries, as the visible reason. The player re-plans in the same round (clarifying stays in its round). Clara's slip past the stoker is her own uncertain act: action form with actor clara_odea, stealth T2, sensory favourable (boiler roar, dark); danger: the stoker raises the alarm (capture → severe, cost form "capture someone").]*

```text
ROUND 3 | Day 5 | 18:00 | the back lane, Hanbury Street | saved R0 · save R10

clara_odea — 2d10: 9+1 | Capability: +2 | Tool: +0 | Total: 12
Difficulty: 9 [sensory -1: the boiler roar and the dark of the cellar] | Stakes: severe/full | Outcome: Success

GM-Δ 3 ⟵ 2
  + npcs.bert_marsh :: the night stoker, depth 0; old, deaf from the boilers
  + locations.jute_mill.conditions.back_door :: unbolted from inside by Clara at 19:20
  + player.knowledge.facts.chute :: a 14-inch hatch: Clara fits; Tom doesn't
  ~ world_state.time :: Day 5 19:20, evening
```

At seven the mill wakes up: a whistle, then the steam engine coughing into life, then the noise of the looms coming through the walls like a storm. A line of children goes in through the street gate, small and silent, and the gate shuts behind them.

Clara shows you the chute: an iron hatch in the back lane, the size of a big book. You'd get one shoulder in it. Clara looks at you and doesn't bother to say anything.

**▶ Player:** All right. You go down, Clara. Open the back door from inside and I'll come in that way.

She drops into the hatch feet first and is gone. You wait in the dark by a back door that looks as if it hasn't been opened in years. Five minutes. Ten. Then the bolt scrapes on the inside and the door opens an inch, and Clara's face is there, black with coal. "Old Bert never even turned round," she whispers. "Deaf as a post. Come on."

---

## Round 4

**▶ Player:** Up to the kids. Clara takes them down the back stairs and out the back. If Grieve goes for the bell, he's mine.

*[test note: the gatehouse is the PC's people in a fight he isn't at → played out by its own combat form (Alf and Davey against Hoke and the gate lad, position favourable: the door opens on men sitting down). It paused when the lad fell; morale was settled: Hoke, alone and hurt against two, yields. Inside: Grieve goes for the alarm bell (his plan and fear: the shift's quota, the owners). Action form: get between him and the bell. Position adverse +1 (the rope hangs between two carding engines). The danger is the machinery itself: the oil lamp on the carding frame over loose jute, with thirty children in the room. Cost form "a threat acts" (the lamp goes over). That cost was bound and shown before the roll.]*

```text
ROUND 4 | Day 5 | 19:20 | the jute mill, the carding room | saved R0 · save R10

— the gatehouse —
alf_tanner vs Hoke — 2d10: 9+8 | … | Success | Hoke HP 12 → 7
davey_shaw vs the gate lad — 2d10: 2+9 | … | Success | the gate lad HP 10 → 6
alf_tanner vs Hoke — 2d10: 5+1 | … | Failure | alf_tanner HP 12 → 8
davey_shaw vs the gate lad — 2d10: 9+7 | … | Success | HP 6 → 3
alf_tanner vs Hoke — 2d10: 1+8 | … | Success | Hoke HP 7 → 4
davey_shaw vs the gate lad — 2d10: 1+7 | … | Success | the gate lad HP 3 → 0 — down

— the carding room —
2d10: 4+6 | Capability: +2 | Tool: +0 | Total: 12
Difficulty: 11 [position +1: the bell rope hangs between two carding engines; little room to move] | Stakes: loss/full | Outcome: Success

GM-Δ 4 ⟵ 3
  + world_state.pending.gatehouse :: Alf and Davey took the gatehouse; the lad down, Hoke yielded and tied
  ~ npcs.alf_tanner.state.hp :: 8
  ~ npcs.grieve.state.status :: put on the floor before he reached the bell; tied with his own strap
  + npcs.grieve.knowledge.facts.tom :: a big Rook with a broken nose and a red scarf, with Clara O'Dea; took the night shift out
  ~ world_state.time :: Day 5 19:30, evening
```

The carding room is a long hot hall full of noise. Iron engines with combs the size of cartwheels, leather belts slapping up to the shafts on the ceiling, oil lamps on hooks, and fluff in the air like snow. Thirty children feed jute into the machines. The smallest are sweeping underneath them while they run.

Clara goes down the line tugging sleeves, and the children look at her and then at you, and start to stop.

Mr Grieve sees it from the end of the hall. He doesn't come for you. He goes for the bell rope that hangs between two carding engines, with a lamp swinging on its hook right above the loose jute.

You get there first, just. You take him round the middle and put him on the floor between the machines, away from the lamp, and his strap goes skidding under a carding engine. You tie his hands with the strap's own buckle end, and he swears at you in a schoolmaster's voice the whole time.

Down the back stairs, the children are already going out the door into the lane in a silent line, Clara at the front.

*[test note: success at full reach: Grieve down, no cost. **The hazard never acted.** In this scene the machinery could only reach anyone through a failed roll's bound cost, and the roll succeeded. A beast acts on its own every exchange; a hazard here only waits. RULES has no "a hazard acts on its own clock" rule (fire spreading, a belt snapping) unless something sets it off. That's a real difference between the two worlds' scene 2.]*

---

## Round 5

**▶ Player:** Out in the lane, I count them. Clara, where do they go now?

```text
ROUND 5 | Day 5 | 19:30 | the back lane, Hanbury Street | saved R0 · save R10

GM-Δ 5 ⟵ 4
  + world_state.pending.mill_children :: thirty out; twenty-four go home on Clara's say; six with nowhere stay with her
  ~ npcs.clara_odea.state.plan :: hide the six from the parish and the workhouse; trade what her kids see for help
  ~ npcs.clara_odea.state.due :: B Day 5 21:00 brings the six to wherever the Rooks say
  + npcs.clara_odea.relationships.pc :: the Rook who came; suspicious, a little impressed; credit: came when Jacob didn't
  ~ world_state.time :: Day 5 19:45, evening
```

Thirty children in a lane in the fog, coal smoke and jute fluff on all of them. Clara looks at you as if you've asked something stupid.

"Home, most of 'em. They've got mums." She starts sending them off in twos and threes with older ones. "These lot haven't." Six of them, the smallest. "No mum, or a dad who'd send 'em back to Grieve tomorrow with a clip round the ear. If the parish gets 'em, it's the workhouse." She says the word like it's a disease.

*[test note: real 1868 logic (GM §3.5 USUAL): most child mill hands lived at home and their families needed the wage. Freeing them isn't the end of it. Clara's answer comes from her record and her fear (the workhouse).]*

---

## Round 6

**▶ Player:** All right, the six come with us. And who's that woman shouting?

```text
ROUND 6 | Day 5 | 19:45 | the back lane | saved R0 · save R10

GM-Δ 6 ⟵ 5
  + npcs.maggie_dunn :: Maggie Dunn, matchbox maker, mother of Lizzie (8), depth 1
  + npcs.maggie_dunn.relationships.pc :: furious; grievance: cost her Lizzie's 4s a week
  ~ player.money.cash :: 0s (gave Maggie Dunn his 3s)
  ~ npcs.maggie_dunn.relationships.pc.credit :: gave her 3s for the lost week
  ~ world_state.time :: Day 5 20:00, evening
```

A woman is coming down the lane with a girl by the wrist, the girl one of the night shift. "Who did this? Who's took them out?" She sees your red scarf. "You. That's four shillings a week, that is. That's our rent. Who's paying Lizzie's four shillings when Grieve won't have her back?"

Lizzie is crying. So is Maggie Dunn, by the end of it, though she shouts the whole way through.

**▶ Player:** I give her the three shillings I've got. It's all I have. Tell her there's other work, not Grieve's.

She takes it. She doesn't thank you. "That's a week," she says. "What about next week?" And she goes, with Lizzie.

*[test note: one of the 24 families, developed at first meeting. Her grievance is a real cost the PC's act caused (lost wages), recorded at the weight of a real cost. The money was the player's choice, so it's credit for her, and the grievance stays: credit and grievance never cancel (RULES §15.1 STANDING). This is the "win the fight, lose the goal" pattern from the background template's combat lens, coming from ordinary life rather than from an enemy.]*

---

## Round 7

**▶ Player:** Grieve stays tied in the carding room for the morning shift to find. Hoke and the lad stay tied in the gatehouse. We go.

```text
ROUND 7 | Day 5 | 20:00 | the jute mill → Whitechapel | saved R0 · save R10

GM-Δ 7 ⟵ 6
  ~ npcs.grieve.state.due :: B Day 6 06:00 found by the morning shift; B Day 6 09:00 reports to the mill manager, who complains to Leman Street with Grieve's description of the Rook
  + world_state.pending.gatehouse_found :: the morning shift finds Hoke; Hoke goes to Kaylock's train; due Day 6 06:00
  ~ npcs.rexford_kaylock.state.due :: A-1 Day 6 07:00 hears the Rooks and Clara emptied Starrick's mill; A-1 Day 7 night breaks Rook pubs
  ~ npcs.maggie_dunn.state.due :: B Day 6 morning goes to beg Lizzie's place back
  ~ world_state.time :: Day 5 20:15, evening
```

You leave the mill's engine thumping away with nobody feeding it. Grieve is still swearing on the carding-room floor.

*[test note: the witness chain (RULES §15.7) is written now, as dues: Grieve saw the PC's face and scarf → the mill manager → a complaint to the half-bought station. Hoke → Kaylock. Each lands on its own time; nothing reaches the PC tonight. **GM slip found here:** no span had run since Round 2, so the evening surface roll was missed. The span stopped at Clara's 18:00 due, and the evening roll at that same minute was never made after it. Run now from 18:00 with arrived: nothing. Pending consequences carry no zone, as in A3. Maggie Dunn has a grievance, so she's important and got a due (the tool flagged her).]*

---

## Round 8

**▶ Player:** The six come to the Ten Bells. Sal, they need the back room tonight. Just tonight.

*[test note: `ask`: for +1 (the Rooks keep her windows in now); against −1 (six children in a pub is trouble with the parish and the police) → 2d10 10+3 = 13 → YES.]*

```text
ROUND 8 | Day 5 | 20:15 | the Ten Bells | saved R0 · save R10

sal_pruitt — 2d10: 10+3 | Likelihood: +0 [for: the Rooks keep her windows in now +1; against: six children in a pub is trouble with the parish and the police -1] | Total: 13 → YES

GM-Δ 8 ⟵ 7
  + npcs.sal_pruitt :: Sal Pruitt, landlady, depth 1
  + world_state.pending.orphans_ten_bells :: six children in the back room tonight
  ~ npcs.clara_odea.state.due :: Bs brought them; B Day 6 morning moves them on to her own hiding places
  ~ world_state.time :: Day 5 21:00, evening
```

Sal looks at the six of them in her doorway, black with coal and jute, and puts her hands on her hips. "Just tonight." She gets them bread and dripping and puts them in the back room on sacks by the stove, and then she shouts at the dockers for swearing in front of them.

*[test note: Sal was asked before her record existed in this run (the `ask` form took "sal_pruitt" without complaint). GM order slip: she was recorded after the roll in the same block. The tool doesn't check that `who` is a recorded actor.]*

---

## Round 9

**▶ Player:** Clara. Tonight was your job, and we did it. What's it worth to the Rooks?

```text
ROUND 9 | Day 5 | 21:00 | the Ten Bells | saved R0 · save R10

XP +38 (quest B, the mill children freed) → level 3, 38 XP

GM-Δ 9 ⟵ 8
  + player.knowledge.facts.clara_trade :: the Blighters count protection money at the Black Eagle cooperage yard on Brick Lane; six on weeknights; a crew boss called Rigger
  + npcs.clara_odea.relationships.pc.credit.r9 :: kept six of her kids out of the workhouse tonight
  ~ npcs.clara_odea.relationships.pc.attitude :: warmer; trusts him with one thing
  ~ player.progression.state :: {level: 3, xp: 38}
  ~ quests.side_mill_children.status :: succeeded → Bs
  ~ world_state.time :: Day 5 21:30, evening
```

Clara sits on the end of the bar with her feet dangling and eats Sal's bread. "You came. Jacob Frye talks and talks." She wipes her mouth. "All right. The Blighters count their protection money in the cooperage yard behind the Black Eagle on Brick Lane. Six of them on a weeknight. A boss called Rigger. That's worth something to your Jacob, ain't it?"

**Code B: done.** Thirty children are out of the mill tonight. By tomorrow Grieve will have thirty more.

*[test note: quest XP paid at the quest's level (3, meaningful), once. Clara's trade is her record ("trade what her kids see for help"), and its content matches what A1's fixture had Jacob learn from her. It isn't a hint: the PC earned it, and the background lists strongholds as Whitechapel activity. Quest closes as succeeded: its end was "children freed, still working, or moved elsewhere", and the end is freed, for tonight.]*

---

## Round 10

**▶ Player:** I sleep in the Ten Bells tonight, on the bench by the door. Somebody should.

```text
ROUND 10 | Day 5 | 21:30 | the Ten Bells | saved R0 · save R10

GM-Δ 10 ⟵ 9
  ~ player.condition.hp :: 14 (a night's rest: full)
  ~ player.condition.last_rest :: Day 5 night, the Ten Bells bench (good rest: with allies, at his pub)
  ~ player.growth_period :: {opened: 6, credited: []} (growth boundary at the good rest: no evidence, no tier change)
  ~ world_state.time :: Day 6 06:00, morning
```

You sleep badly on a hard bench and wake at six with the fire out, the six children asleep in a heap by the stove, and the mill whistle going on Hanbury Street as if nothing happened.

*[test note: a good rest (with allies, at his pub, RULES §7 GOOD REST) → full HP, a growth boundary (no evidence banked, so no change), item points already full. The span for the night is in the save notes below; it stopped at 06:00 at the gatehouse discovery, which doesn't reach the PC. Save due at the close of R10.]*

---

## Save R10

`save_ac_A2_R10.md`: merge (first save) → valid; validate → **valid: true**. The night's span (21:30 → 06:00): the day rollover (nerve day marks: none due, the PC is at baseline and rested), the night surface roll (nothing), and a stop at Clara's 06:00 move, which reaches the PC and opens the next scene after the save. Flag: Maggie Dunn's position "Hanbury Street" names no recorded location.

---

## Findings from this run

1. **The "same scene" doesn't exist in this world.** AC 1868 has no creatures. The fair equal was a hazard scene drawn from the background's own threats. A test plan written for one world doesn't carry to another; each world's own list of threats has to drive its scenes.
2. **A hazard has no clock of its own.** The machinery only acts through a failed roll's bound cost. A beast acts every exchange, but a fire, a belt or a boiler waits for the PC to fail. That may be right (no invented drama), but it makes hazard scenes quieter than creature scenes for the same danger level. The rules don't say whether a hazard already in play (a lamp over jute) can act on its own.
3. **The possibility gate worked:** the coal chute was impossible for a broad docker, so there was no roll and the visible reason was shown, and the player re-planned.
4. **Ordinary-life consequences came from the world's own logic** (the families need the wage), with no rule written for it. That's the GM §3.5 USUAL question doing its job.
5. **Missed spans:** the GM ran no span for four rounds while the scene was busy, and the evening surface roll was only made late. A span that stops at a due on a daypart boundary doesn't make that daypart's roll when it resumes; the GM has to pass `arrived`.
6. **The `ask` form doesn't check that `who` is recorded,** so Sal was asked before she existed in this run.
7. **The important-actor flag worked twice:** Pip (named in a quest line) and Maggie (a grievance). Each forced a real plan.
