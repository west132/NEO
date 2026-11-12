# NEO test run: SCP Class of '99, 10 rounds

This is a test of the play set on `scp-neo` (GM, RULES, SAVE, the tool, and `worlds/BACKGROUND_SCP_OMEGA99_NEO_v0.md` with the modules file for canon mode). The GM follows the files as written. The player is a **stand-in** who sets the open fields and plays Sam West. Every roll, time step and save comes from `neo_math_v0.py`.

Player turns are marked **▶ Player**. Everything else is the GM's turn as the player would see it. Notes in *[test note: …]* are mine, outside the game.

---

## Round 0: setup

**▶ Player:** Load NEO with the SCP background. Given name Sam, 26 (born January 2000), man. Three years as a patrol officer in Columbus, Ohio before the Foundation. Tall, lean, short black hair. My sidearm is a Glock 19; I call it Patience.

> Play your character as a real person. I treat your character as a real person, and the world as a real place with its own logic.

**SCP** is a shared-fiction world where a secret organisation, the **SCP Foundation**, finds things that break the laws of nature (**anomalies**), locks them away, and keeps the public from ever knowing. Its motto is *Secure. Contain. Protect.* On paper it is a dull WHO programme, the "Special Containment Programme".

**Sam West.** A week ago you finished the Foundation's field-agent academy: law, cover identities, amnestic protocol, firearms, first aid, containment basics. Before that you were three years on patrol in Columbus, until a call where something impossible happened and you kept your head. Everyone else on that call was given an amnestic (a drug that erases memories). They kept you.

You're a **field agent**: the Foundation's eyes and ears, who confirms an anomaly and calls in the people who contain it. You hold **Level 2** clearance, which governs what you may *know*, not your rank. Today is Day 1 of a 90-day probation. You're posted to **Site-19** as liaison to **MTF Omega-99**, "Class of '99", a small mobile task force that takes the Foundation's low-priority weird jobs worldwide. Your handler and partner is Agent Rosa Delgado. You've heard the unit's joke already: anyone born before 2000 claims they secretly saved the world in 1999 and swore never to tell, and makes fun of everyone who wasn't there. You were born in January 2000.

You carry Patience with 45 rounds, Foundation ID with WHO credentials and a spare cover badge, and a field kit (radio, gloves, evidence bags, torch, two doses of Class-A amnestic). You have $1,200; first pay comes on Day 30. Field investigation, firearms, cover and persuasion, first aid: all academy-fresh (T1). HP 12.

```text
GM-Δ 0
  ~ player.identity.name :: Sam West
  ~ player.identity.age :: 26 (born January 2000)
  ~ player.identity.origin :: United States; recruited after three years as a patrol officer in Columbus, Ohio
  ~ player.appearance :: tall, lean, short black hair, a police-academy posture he hasn't shaken
  ~ player.gender :: man
  ~ player.equipment.west_sidearm.name :: Glock 19 he calls "Patience"
  ~ player.item_points.current :: 60
  ~ player.item_points.max :: 60
  ~ player.condition.hp :: 12
  + player.knowledge.facts.first_meeting :: Rosa's message: she meets West at dorm C, 08:30 Day 1
```

07:30, Day 1, early spring: cold and clear outside. You come in through the dorm block C entrance with one bag. Somewhere above you the PA is reading a memo in a voice with no feelings at all: *"…reminding all personnel that the cafeteria's no-feeding-the-anomalies policy applies to all anomalies, including those that ask nicely."*

Your room assignment says **C-14**. Rosa Delgado's message from last night said she'd meet you here at 08:30.

*[test note: span from Day 1 07:30 at site19. Morning surface roll: 6, nothing. It stops at Rosa's A-1 08:30 due, zone point {open 0, hidden 0}. The player acts before that, so Round 1 opens on the player's action (GM §7.2 OPEN).]*

---

## Round 1

**▶ Player:** I find C-14, knock once, and go in.

```text
ROUND 1 | Day 1 | 07:30 | Site-19, dorm block C | saved R0 · save R10

GM-Δ 1 ⟵ 0
  ~ world_state.time :: Day 1 07:50, morning
  ~ npcs.leo_brandt.relationships.pc.bond.history :: met R1 in C-14; gave West the bottom bunk and the lore
  ~ npcs.leo_brandt.state.position :: Site-19 containment wing, day shift
  + player.knowledge.facts.roommate :: Leo Brandt, junior containment technician, C-14; born '98, claims he was "there" in 1999
```

C-14 is a two-person room with a bunk bed, two lockers, a desk under a window that looks at a wall, and a mini-fridge held shut with a zip tie. A man of about your age is sitting on the top bunk lacing a work boot, a grey Site-19 technician's jumpsuit tied round his waist by the arms.

"New roommate!" he says. "Quick question, very important. What year were you born?"

"January 2000."

His face lights up. "Oh, buddy. Oh no. Ninety-eight." He puts a hand on his heart. "I was *there*. We don't talk about it." He sticks the hand out. "Leo Brandt. Containment tech, junior, which means I hold the clipboard while someone else holds the thing." He drops down from the bunk. "You get the bottom. The top one creaks; I've zip-tied it twice and it's still winning."

He talks while he finishes the second boot. The 1999 joke, he explains, is the unit's whole personality: anyone born before 2000, even on New Year's Eve 1999, was "there", "handled it" and signed a secret oath, and gets to rub it in to anyone who wasn't. "Nobody can say what 'it' was. That's the joke. If you ask, they say 'you're welcome.' Rosa started half of it. Don't ask Rosa. She'll say 'you're welcome.'"

At ten to eight he grabs a lanyard off the hook. "Shift's at eight. Cafeteria's down the stairs and left; it's free, and the eggs are better than they look. Cards tonight, if you want. I'm terrible. Bring nothing you'd miss." He's out the door.

The room is yours for forty minutes. Rosa said 08:30.

---

## Round 2

**▶ Player:** I unpack, get a coffee from the cafeteria, and I'm back outside C-14 by 08:25.

*[test note: a FAST stretch, told in prose. Span 07:50 → 08:30: no new surface roll (the morning was already rolled), Rosa's due fires at 08:30 in the PC's zone.]*

```text
ROUND 2 | Day 1 | 08:30 | Site-19, dorm block C | saved R0 · save R10

GM-Δ 2 ⟵ 1
  ~ quests.probation.status :: active (R2, West reported for duty; code A given)
  ~ quests.orientation_week.status :: active (R2, Rosa set it; code A-1 given)
  ~ npcs.rosa_delgado.state.due :: A-1s Day 1 08:30 meets West at dorm C; A-1 Day 5 first real assignment
  ~ npcs.rosa_delgado.relationships.pc.bond.history :: met R2; walked West round the cleared wings
  + player.knowledge.facts.wings :: cleared at Level 2: dorm C, cafeteria, Omega-99 office, gym, archive front desk; containment wings by assignment only
  + player.knowledge.facts.omega99 :: met Dima Volkov (office) and the commander's 10:00 welcome talk is today
  ~ world_state.time :: Day 1 09:55, morning
  ~ world_state.location :: site19 (Omega-99 office)
```

The bag's unpacked, the cafeteria coffee is better than the Columbus precinct's, and at 08:30 exactly a woman in a grey suit comes up the stairs two at a time: mid-thirties, dark hair pulled back, a travel mug in one hand and a folder in the other.

"West." She looks you over the way a sergeant would, and then she smiles, and it's a real one. "Rosa Delgado. I'm your handler, your partner, and for the next ninety days the person who signs everything you do." She checks the coffee in your hand. "You found the cafeteria on your own. You're welcome."

**▶ Player:** "Morning. So: is it true you saved the world in 1999?"

Rosa doesn't miss a beat. "Signed the oath. Can't talk about it." She sips. "You're welcome."

Then the folder comes out. **This week is orientation**, and she reads it to you like a list she wrote at midnight: settle into the dorm (done; Leo's a sweetheart, don't let him fix anything of yours with zip ties), learn the cafeteria, walk every wing you're cleared for, file your first Form MU-2 "so you learn what paperwork feels like when it's fun", a sparring session with Dima, and "survive the 1999 thing, which you have already started doing badly." Day 5, if you're still standing, she gives you a real job.

**Quests:**

- **A: Probation.** Ninety days, a field board reading your file at the end. Day 90 is a review, not an ending.
- **A-1: Orientation week.** Settle in at Site-19, through to the end of Day 5 and your first real assignment.

The tour takes ninety minutes. Site-19 is fluorescent corridors and heavy doors that sigh when they shut. Your Level 2 card opens dorm C, the cafeteria, the gym, the front desk of the archive, and the **Omega-99 office**: four desks, a whiteboard with a betting pool on it ("HOW WILL IT GO WRONG — WK 10"), and a kettle with "PROPERTY OF THE CLASS OF '99" written on it in marker. Everything past the containment-wing doors needs an assignment; your card just beeps sadly at them.

In the office, a very large man is reading a binder labelled *Safe-class trivia, vol. 3*. He stands up, and keeps standing up. "Dima," he says gently, and shakes your hand like he's holding a bird. "You will spar with me this week. I will be careful. Mostly." Rosa tells you the commander gives new people a welcome talk at ten, in here, and that the commander was born in 1985 and "is very tired of the joke, so do it once, not twice."

It's five to ten. Rosa refills her mug from the Class of '99 kettle.

---

## Round 3

**▶ Player:** I sit up straight for the commander. I won't do the joke. I'll ask her what the unit needs most from a rookie.

*[test note: Lindqvist's A-1 10:00 due fired in the PC's zone. After this block her due holds only the uncoded Day 75 move; span 10:00–10:30 shows nothing more and no flag.]*

```text
ROUND 3 | Day 1 | 10:00 | Site-19, Omega-99 office | saved R0 · save R10

GM-Δ 3 ⟵ 2
  ~ npcs.commander_lindqvist.state.due :: A-1s Day 1 10:00 welcome talk; Day 75 transfer decision
  + npcs.commander_lindqvist.relationships.pc :: {tie: commander and probationer, attitude: neutral, measuring}
  + player.knowledge.facts.commander :: Lindqvist wants reports filed on time, nobody hurt, and results that keep the unit funded
  ~ world_state.time :: Day 1 10:30, morning
```

Commander Beatrice Lindqvist comes in at ten on the dot with a coffee from the cafeteria, not the kettle. She's early forties, blonde hair going grey at the temples, reading glasses pushed up on her head. She looks at Rosa's mug, then at the kettle, then at you.

"West. Welcome to Omega-99. You'll hear we're the odd-jobs unit. We are. Every job a bigger MTF thinks is beneath them comes here, and we do it properly, on a budget that wouldn't run a food truck." She sits on the edge of a desk. "Three rules. File your report the day you get back. Don't get hurt. Don't make me explain anything to the Site Director that I didn't know about first."

**▶ Player:** "What does the unit need most from a rookie, ma'am?"

She considers it for a moment, which you suspect is a compliment. "Reports that tell me what happened, not what you wish happened. People who ask when they don't know. And results I can put in a budget meeting." She glances at the whiteboard pool. "Not that."

Dima, behind her, says helpfully, "And coffee for the Class of—"

"Dima." She doesn't turn round. "I was born in 1985. I was *fourteen*. I did not save the world. I sat my geography exam." She stands, and gives you a short nod. "Rosa has you this week. Day 5 she gives you something real. Don't get hurt before then; it's a lot of paperwork."

She leaves. Rosa waits till the door shuts. "That went well. She asked you nothing back. That's the good sign."

The rest of the day is yours: the MU-2 form, the gym, the archive desk, lunch.

---

## Round 4

**▶ Player:** After lunch I fill in an MU-2 for SCP-294: one cup of plain black coffee. I hand it in at the archive desk. Then I spend the afternoon at the site range getting Patience zeroed, and I'm back in C-14 for cards at seven.

```text
ROUND 4 | Day 1 | 12:30 | Site-19, archive front desk | saved R0 · save R10

GM-Δ 4 ⟵ 3
  + world_state.pending_consequences.mu2_west :: Form MU-2 filed R4 Day 1 for SCP-294, one cup of black coffee; approved and booked Day 2 (1d3 → 1), 15:00 slot
  + player.knowledge.facts.mu2 :: filed for an SCP-294 coffee; RAISA's desk says 1–3 days
  ~ world_state.time :: Day 1 19:00, evening
  ~ world_state.location :: site19 (dorm C, C-14)
```

**SCP-294** is a coffee machine that pours any liquid you name. It's Euclid-class, which (Rosa told you on the tour) means "not sure what it'll do", not "dangerous". Staff may book it for ordinary drinks only, and the drink gets tested first.

Form MU-2 is four pages. Page three asks you to "describe the expected morale outcome in 50 words or fewer". You write *a good cup of coffee* and leave forty-five words blank. The clerk at the archive desk (RAISA, the records people) stamps it without reading page three. "One to three days. Rookie forms go fast; nobody's used up their month in March."

The range is in the basement, cold and loud. Patience was shooting a hair left. By four she isn't.

At seven you're back in C-14. Leo has a deck of cards, two packets of instant noodles, and a kettle he has definitely not had approved.

---

## Round 5

**▶ Player:** Cards, for matchsticks. I ask him how long he's been here and what the containment side is like. Then bed.

```text
ROUND 5 | Day 1 | 19:00 | Site-19, dorm C, C-14 | saved R0 · save R10

GM-Δ 5 ⟵ 4
  ~ npcs.leo_brandt.relationships.pc.bond.habits :: cards for matchsticks and late noodles (R5); Leo lost every hand cheerfully
  + player.knowledge.facts.leo :: two years at Site-19; works the Safe-storage wing; from Allentown; calls his mum Sundays
  + world_state.material_history.d2_131 :: Day 2 00:10 SCP-131-A and -B out of their pen, wandering dorm C's corridor (ordinary site alert; PA call)
  ~ world_state.time :: Day 2 00:10, night
```

Leo is exactly as bad as he said. He bets matchsticks on pairs of threes and grins every time he loses. In between hands he tells you he's been at Site-19 two years, came from Allentown, calls his mum on Sundays, and works the Safe-storage wing: "Shelves. Very boring shelves. If something on a shelf ever gets exciting, I've had a bad day." He fixes the wobbly desk leg with a zip tie while he talks, without looking.

You're asleep by eleven.

At ten past midnight the PA wakes you, in the same voice that read the cafeteria memo:

*"Attention dorm block C. SCP-131-A and SCP-131-B are outside containment in your corridor. Both instances are harmless. Do not feed them. Do not take them to bed. A handler is on the way. That is all."*

Leo groans from the top bunk. "Eye pods. Ugh. They'll sit outside the door and look at it all night."

**SCP-131** is two little teardrop-shaped creatures, each about knee-high, with one big eye and a wheel where a foot would be. They follow people around like puppies. You can book them as a staff perk, for company while you file reports.

Through the gap under the door: a soft whirr of little wheels, going up and down the corridor. Then it stops, right outside C-14.

---

## Round 6

**▶ Player:** I open the door a crack and look. If they're just sitting there, I sit on the floor in the doorway with them till the handler comes, and then I go back to sleep.

*[test note: two surface rolls came up "encounter, ordinary" (00:00 and 06:00), drawn from Site-19's own ordinary list: a loose Safe item in a corridor (top of the band) and a jammed door (low). The handler is new, so a temper roll was made: 2d10 16, under 17, not difficult. Gus's untimed Day 2 due ("meets West fixing the dorm C door") is next; the tool would put it at 08:00.]*

```text
ROUND 6 | Day 2 | 00:10 | Site-19, dorm C, C-14 | saved R0 · save R10

GM-Δ 6 ⟵ 5
  + npcs.marcus_ojo :: {depth: 0, name: Marcus Ojo, job: night-shift animal handler, Safe wing, manner: yawning and polite; shakes a box of cereal to call the pods, position: Site-19 Safe wing}
  ~ world_state.material_history.d2_131 :: Day 2 00:10–00:30 SCP-131-A and -B loose in dorm C; West kept them company at C-14's door until Ojo collected them; no harm
  + world_state.material_history.d2_door :: Day 2 06:00 C-14's door lock jammed (old lock); found when West and Leo tried to leave at 07:40
  ~ world_state.time :: Day 2 07:40, morning
```

Two of them, right on the threshold: smooth, pale, teardrop-shaped, each with one enormous eye. When the door opens they both roll back an inch and look up at you. Then they look at each other. Then they roll forward again until they're touching your bare feet.

You sit down in the doorway. They settle either side of you like dogs that have decided you're theirs.

At half past midnight a man in a Site-19 handler's fleece comes down the corridor shaking a box of cereal like a maraca. "Sorry, sorry. Marcus Ojo, Safe wing. They figured out the pen latch again." He yawns enormously. The pods leave you at once for the cereal. "Don't take it personally. They'd leave their own mother for Cheerios." He herds them off down the corridor, a small procession of whirring wheels.

You sleep till seven.

At 07:40 Leo, dressed, lanyard on, turns the handle of C-14's door. It turns. The door doesn't move. He tries again, harder. The lock has seized: the bolt's stuck halfway out, and the door's wedged in its frame.

"No," Leo says to the door. "Not today. I'm on at eight." He looks at you. "I've got zip ties, a butter knife and a bad attitude. You?"

---

## Round 7

**▶ Player:** I'm not taking a butter knife to a Foundation lock on Day 2. I radio maintenance and say we're locked in C-14.

```text
ROUND 7 | Day 2 | 07:42 | Site-19, dorm C, C-14 | saved R0 · save R10

GM-Δ 7 ⟵ 6
  ~ world_state.material_history.d2_door :: C-14's lock seized Day 2; Gus freed it 08:00 with a kick and graphite; new lock cylinder ordered
  ~ npcs.gus_pembroke.state.due :: Day 6 morning back through dorm C to fit C-14's new lock cylinder
  + npcs.gus_pembroke.relationships.pc :: {tie: the maintenance man who let him out, attitude: friendly, bond: {history: met R7 through a jammed door; told the 173 story}}
  + player.knowledge.facts.gus :: Gus Pembroke, 71, maintenance and archive porter; retired field agent; knows every door that sticks
  ~ npcs.leo_brandt.state.position :: Site-19 Safe-storage wing, day shift (five minutes late)
  ~ world_state.time :: Day 2 08:15, morning
```

The radio crackles. A slow, unhurried voice: "C-14. Bolt's stuck halfway, isn't it. That lock's older than both of you put together. Don't touch it. On my way."

Leo sits on his bunk with his head in his hands and watches the clock go to 07:58.

At eight there's a shuffle of feet outside, a pause, and then a single, precise kick, low, by the lock. Something inside the door goes *clunk*. A squirt of something, a smell of graphite, and the door swings open.

The man on the other side is in his seventies, in grey maintenance coveralls, with a can of lock lubricant in one hand. He looks at Leo. "Go on, son. Tell them Gus held you up." Leo goes, at a run.

Gus looks at you, and the lock, and you again. "You're the new one. West." He works the bolt back and forth, listening to it like a doctor. "This cylinder's done. I'll get a new one in. Few days." He doesn't seem in any hurry to leave. "First thing they teach you here, nobody tells you, is the doors. Doors are what keep everything where it is. You know about one-seven-three?"

**SCP-173** is the most famous anomaly in the Foundation: a concrete statue that moves when nobody's looking at it. Old-timers' cafeteria stories, mostly, and not a job you'll ever be sent on.

"Three of us in the cell for the cleaning," Gus says. "Rule is you don't blink, or you say 'blinking' first so the others keep looking. I was twenty-six. Fella next to me sneezed." He puts the lubricant back in his pocket. "We're all still here. But I never did trust a door since." He pats the frame and starts off down the corridor, slow. "Ask nicely, I know where everything is. Most things."

---

## Round 8

**▶ Player:** Day 2: archive desk in the morning, reading whatever Level 2 lets me see of Omega-99's closed jobs, to learn how they write things up. My coffee at three if it's approved. Quiet evening.

*[test note: span Day 2 08:15 → Day 3 08:00. The noon surface roll came up "encounter, ordinary, low of band": a lockdown drill, from Site-19's list. The order covers it (the PC follows a drill), so there's no hand-back. Four more rolls, nothing. It stops at Priya's untimed Day 3 due (08:00). GM slip found: the R4 MU-2 booking was written as one line with no `due:` field, so span never listed it. It still resolved at its booked time because the player's order went there.]*

```text
ROUND 8 | Day 2 | 08:15 | Site-19, archive front desk | saved R0 · save R10

GM-Δ 8 ⟵ 7
  + world_state.material_history.d2_drill :: Day 2 12:10–12:25 site lockdown drill; West sat it out at the archive front desk
  + player.knowledge.facts.reports :: read the Level 2 versions of Omega-99's closed reports; knows the house format (summary, rules observed, addendum)
  − world_state.pending_consequences.mu2_west :: used Day 2 15:00; one cup of black coffee from SCP-294, tested first
  + player.knowledge.facts.scp294 :: SCP-294 poured a perfect black coffee; one MU-2 used this month
  ~ world_state.time :: Day 3 08:00, morning
  ~ world_state.location :: site19 (dorm C)
```

RAISA's reading room is three carrels and a sign that says THINK BEFORE YOU REQUEST. At Level 2, Omega-99's closed reports come with so many black bars they look like barcodes. What survives teaches you the house style: a two-line summary, the rules the anomaly was seen to follow, what was done, and an **addendum**, the notes added after the fact, where the people who were there say what they'd do differently. Half the addenda are signed *T. Reyes-Hart* and run longer than the reports.

At ten past twelve the lights go amber and the PA says, *"Lockdown drill. Remain where you are. This is a drill. Remain where you are."* You remain where you are, with the clerk, who eats her sandwich through it. Fifteen minutes later the lights go white again.

A memo is in your inbox by one: *MU-2 APPROVED. SCP-294. 15:00. Test chamber 2. One (1) beverage.*

At three a researcher with a clipboard watches you say "a cup of black coffee" to what looks like an old office vending machine. A paper cup drops, fills, stops. She dips a test strip, waits, reads it, and nods. It's the best coffee you've ever had. You wrote *a good cup of coffee* on page three, and that's what it was.

The evening is cards and noodles with Leo, who's in a good mood and loses again. You sleep well.

Day 3, eight o'clock. There's a knock at C-14: a woman in an Omega-99 windbreaker with grease on one sleeve and a set of van keys round her finger.

---

## Round 9

**▶ Player:** Sure, show me the van. Then the gym till lunch, and lunch in the cafeteria at noon.

*[test note: Priya's untimed due fired at 08:00. She's depth 1 with no tie to a quest or to the PC's standing, so after it she gets `due: none`; nothing flags. Span from 09:00: the noon surface roll came up "encounter, hostile, top + rare of band", and Site-19's hostile list has one entry: "a loose Safe item turns briefly nasty". GM §7.5 says canon first, so I checked the SCP Wiki for a Safe item that fits. SCP-504 "Critical Tomatoes" is Safe, launches at whoever tells a bad joke, and its canon page notes it once got into a cafeteria kitchen. Its cause is written hidden in the block. The joker is new, so a temper roll was made: 13, not difficult. The tomato's hit uses the light-hazard damage (1d6) and rolled 6: Kevin drops from 10 HP to 4, which is over half his max, so he takes a lasting condition.]*

```text
ROUND 9 | Day 3 | 08:00 | Site-19, Omega-99 van bay | saved R0 · save R10

GM-Δ 9 ⟵ 8
  ~ npcs.priya_raman.state.due :: none (showed West the van R9)
  + npcs.priya_raman.relationships.pc :: {tie: unit colleague, attitude: friendly, bond: {history: showed West the van R9}}
  + player.knowledge.facts.van :: Omega-99's van: nets, crates, capture poles, Priya's cage-building kit; rifles are drawn from the armoury per op
  + world_state.material_history.d3_504 :: hidden cause — a crate of SCP-504 fruit from the botany wing's soundproof grow room went to the kitchen loading dock on a mixed pallet Day 3 morning; a kitchen hand put about twenty whole ripe tomatoes on the salad bar at 11:30
  + npcs.kevin_hale :: {depth: 0, name: Kevin Hale, job: logistics clerk, manner: loud, laughs at his own jokes, position: Site-19 cafeteria}
  + npcs.kevin_hale.state.condition :: hp 4 of 10; broken nose (hard to breathe, dazed) — hit by a tomato at 12:05 after telling the 1999 joke
  ~ world_state.time :: Day 3 12:05, afternoon
  ~ world_state.location :: site19 (cafeteria)
```

"Priya Raman. Containment. I build the boxes." She's talking before you've finished saying good morning, walking you down to the van bay at speed. The Omega-99 van is a white Ford Transit with a WHO decal and a dent nobody has filled in. She throws open the back doors: nets on hooks, three collapsible crates, two capture poles, a cargo box of what looks like plumbing and is "a cage, if you know what you're doing", and a clipboard with an inventory form she clearly hates. "Rifles and tranqs come from the armoury per op; you sign them out, you sign them back, you sign the form that says you signed them back." She taps the dent. "That's from a goose. It's in the pool on the whiteboard as 'Goose (2)'. Don't ask about Goose (1)."

You spend the rest of the morning in the gym. No sign of Dima; his whiteboard slot says *TOMORROW: WEST*.

At noon the cafeteria is full and loud. You've got a tray and a seat near the salad bar when a man at the next table, logistics badge, big voice, leans over to a nervous young woman in a lab coat: "Relax, it's your first week. Whatever goes wrong, the Class of '99 already handled it." He spreads his hands. "You're welcome."

*Crack.*

Something red crosses the room faster than you can follow it, from the salad bar, and hits him full in the face. He goes over backwards off the bench. There's a wet red spatter across the wall behind him: tomato, mostly. Some of it is blood. He's sitting up holding his face, eyes streaming, breathing through his mouth. His nose is plainly broken.

For a second the whole cafeteria is completely silent.

On the salad bar, in a steel tray between the lettuce and the croutons, sit about twenty whole, ripe, perfectly ordinary-looking tomatoes. There's a gap at the front of the tray, the size of one tomato.

Someone near the coffee urn says, slowly, "Did that tomato just—" and stops.

You don't know what this is. You know what you saw: a joke, then a tomato off that tray, aimed at the man who told it. Sixty people are in the room, the joker is bleeding, and nobody's moving yet.

---

## Round 10

**▶ Player:** I stand up and say it loud and flat, no smile: "Nobody say anything funny. Nobody. Everyone get up slowly and go out by the far doors. Leave the trays." Then I go to the man with the broken nose, get him sitting forward and pinch the bridge, and radio site security: "Possible anomaly, cafeteria salad bar, the tomatoes. One injured. It goes for jokes."

*[test note: the action form for clearing the room is `cover_and_persuasion`, ordinary grade, with an adverse environment (a shocked crowd). The danger can't reach the PC (it targets jokers), so the cost is a setback in the form "a threat acts" (a nervous joke and another launch). It rolled exactly 11 against 11: success, full reach. First aid on a broken nose and a radio call are certain for a trained field agent, so neither was rolled. Two new people, two temper rolls: 11 and 9, neither difficult. Event XP from the tool: challenge 3 (top of Site-19's band), minor scope, +19.]*

```text
ROUND 10 | Day 3 | 12:05 | Site-19, cafeteria | saved R0 · save R10

GM-Δ 10 ⟵ 9
  + npcs.dana_price :: {depth: 0, name: Officer Dana Price, job: Site-19 security officer, manner: brisk, chews gum, position: Site-19 cafeteria}
  + npcs.ines_okafor :: {depth: 0, name: Dr. Inés Okafor, job: botany wing researcher, manner: mortified and precise; wears a radio mask, position: Site-19 botany wing}
  ~ world_state.material_history.d3_504 :: cafeteria cleared 12:06–12:12 with no further launches; Okafor took the tray in a sound-proofed crate 12:30; cafeteria sealed for an hour; the hidden pallet mix-up still unreported to West
  ~ npcs.kevin_hale.state.position :: Site-19 infirmary (broken nose set)
  + npcs.kevin_hale.relationships.pc :: {tie: the rookie who held his nose together, attitude: grateful, credit: [first aid R10]}
  + rights_obligations.probation.file.r10 :: Day 3 cafeteria, SCP-504 loose on the salad bar: West cleared the room without further injury, gave first aid, called it in (good)
  + player.knowledge.facts.scp504 :: SCP-504, "Critical Tomatoes", Safe: a ripe, detached tomato launches at whoever makes a bad joke in earshot; each fruit once
  + player.knowledge.facts.report_due :: incident report on the cafeteria owed today (Lindqvist: the day it happens)
  ~ player.progression.state :: {level: 2, xp: 19}
  + world_state.material_history.xp_event_d3_504_cafeteria :: XP paid for event.d3_504_cafeteria: 19
  ~ world_state.time :: Day 3 12:40, afternoon
```

**2d10: 2+9 | Capability: +0 | Tool: +0 | Total: 11**
**Difficulty: 11 [environment +1: sixty people in one room, shocked, some starting to laugh nervously] | Stakes: setback/full | Outcome: Success**

It's the police voice from Columbus, the one for car wrecks, and it works. A laugh starts somewhere by the windows and dies. Chairs scrape. Sixty people put their trays down and file out of the far doors without a word, like the end of a very strange church service. Nobody says anything funny. The lab-coat rookie who was the joke's audience goes past you white as paper.

The man with the broken nose is Kevin, from Logistics; his badge says so. You get him sitting forward, head down, pinch below the bridge, tell him to breathe through his mouth. He tries to say something that starts "Well, at least—" and you say "*Don't,*" and he doesn't.

Security is there in four minutes: Officer Dana Price, gum, radio, a look at the tray and a look at you. "It goes for jokes?" she says. "Great. Nobody tell my sergeant." She takes Kevin to the infirmary herself.

At half past twelve a researcher arrives from the botany wing in a full-face radio mask, carrying a padded crate with a soundproof lid. Dr. Inés Okafor looks at the tray the way you'd look at your own dog on a neighbour's lawn. Her voice comes out of a speaker on her chest.

"SCP-504. *Critical Tomatoes.* Safe-class: lock it in a room and it stays. A ripe tomato off the vine launches itself at whoever makes a bad joke within earshot. Each fruit goes once. Speed depends on how bad the joke is." She lifts the tray into the crate without a word, very carefully, and closes the lid. "These shouldn't be here. They don't leave my grow room. I'll find out how they did."

The cafeteria is sealed for an hour, and the kitchen staff are asked a lot of questions. You have an incident report to write, today, because the commander said so.

On your way out, Officer Price stops chewing for a moment. "Clean work, rookie." Then she starts again.

---

## After Round 10: the save

The save is due: R10 reaches T = 10 (GM §6). It was built by the tool from the background and GM-Δ 0–10, and checked by `validate` before play would go on.

```text
merge     GM-Δ 0–10 → 31 records, 1 retired, 37 player/time entries left for the readable part
validate  valid: true · overdue none · actors_without_plan: dana_price, ines_okafor, kevin_hale, marcus_ojo
```

The full save is `save_scp_R10.md`.

**Where the world stands at R10 (hidden from the player):**

- Leo's first call, `L Day 3 a late-night call`, is set for Day 3 at 21:00, tonight.
- Dima's sparring session is Day 4 at 08:00.
- Rosa's `A-1 Day 5 first real assignment` is still open.
- Gus comes back for the lock on Day 6 morning.
- Darrow's squeeze clock is due on Day 8.

---

## Findings

### What worked

1. **Opening.** Span from 07:30 stopped at Rosa's 08:30 due. The player acted first, so Round 1 opened on that action. No hook was invented.
2. **Move codes.** Rosa's and Lindqvist's A-1 moves each took the `s` letter (`A-1s`) and stopped firing. Lindqvist's uncoded Day 75 move stayed in place. Neither span nor validate flagged anything.
3. **Untimed dues.** Gus and Priya landed at 08:00, which suits both of them. Leo's "late-night" wording puts his call at 21:00 Day 3.
4. **Encounters.** Every encounter came from Site-19's own lists. Four of the ten rolls hit: the eye pods, the jammed door, the drill, and the hostile Safe item.
5. **The hostile Safe item.** It was filled from canon (SCP-504, checked on the wiki, whose page says it once got into a cafeteria kitchen). It was not made up for drama.
6. **Hand-backs.** The drill and the jammed door were handled under the player's order. There were hand-backs only at the door (a real choice: force it or call it in) and at the tomatoes.
7. **The save.** Merge and validate passed.

### GM slips (rules were clear, I wrote it wrong)

8. **R4: the MU-2 booking had no `due:` field.** It was written as one line in `world_state.pending_consequences`, so span never listed it. It resolved only because the player went at 15:00. Validate doesn't flag a pending consequence with no due either; it checks only pressures.
9. **R10 erased the hidden cause.** `~ world_state.material_history.d3_504` replaced the R9 hidden cause (the SCP-504 crate sent to the kitchen on a mixed pallet) with the outcome. The save no longer holds the cause. Under RULES §15.6 it should have been its own case, `+ locked_case_truths.cafeteria_504 {cause: …}`. The fix is one `~` in the next block.
10. **Depth-0 people were written with `position:` at the top of the record**, not under `state.position`. Kevin now has both: `npcs.kevin_hale.position` says the cafeteria and `npcs.kevin_hale.state.position` says the infirmary. Nothing flagged it.

### Tool problems

11. **Merge turns an unquoted comma into a junk key.** Kevin's record holds `manner: loud, laughs at his own jokes`. A field inside it changed in the same block, so merge split the record field by field, and the comma made a key `npcs.kevin_hale.laughs at his own jokes` with no value, silently. Dana's and Marcus's records carry the same kind of comma and will break the same way the first time a field inside them changes. Merge should flag a key with spaces and no value.
12. **validate's `actors_without_plan` lists depth-0 people.** Under SAVE §1 only important actors need a plan. Dana, Inés and Marcus are noise.
13. **Merge leaves 37 player and time entries for a hand-built Part A, and nothing checks them.** One example is `player.equipment.west_sidearm.name` inside a list. Validate doesn't compare Part A against the blocks, so a dropped change would pass unseen.

### A design question for you

14. **Kevin is "important" now.** He holds a credit to the PC, and by SAVE §1 IMPORTANT any credit, grievance or bond makes an actor important. That means he must have a plan and a due. Is that meant for a passer-by who's grateful once, or should IMPORTANT start at depth 1 or above?
