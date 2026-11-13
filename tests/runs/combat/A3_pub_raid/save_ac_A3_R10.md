# SAVE — AC Syndicate (combat test A3) R10

## Part A — readable

```yaml
background_ref: {id: ac_syndicate_london_v6_0}
language: en
round:
  last_completed_round: 10
  saved_completed_round: 10
world_state:
  location: whitechapel
  time: {season: winter, day_index: 7, date: Day 7 (February 1868), clock_minutes: 1425, daypart: evening, precision: exact}
  environment: {weather: cold fog, coal smoke, a thin rain, town: Whitechapel near midnight; the Ten Bells smashed, a constable on its door}
player:
  identity:
    name: Tom Kell
    age: 24
    origin: Whitechapel born; docker's son; worked the London Docks from fourteen
    history: [ran with the Clinkers; went Rook on Day 3 when Jacob Frye took the Clinkers' pub]
  appearance: broad, broken nose, red scarf of the Rooks, docker's hands
  archetype: Rook
  job: Rook enforcer
  belongs: [rooks]
  gender: man
  character: player-defined in play
  status: bruised shoulder; near midnight at the rail-yard gate
  skills:
    brawling: {class: NORMAL, tier: T2, evidence: 1, class_source: the docks and the Clinkers, abilities: []}
    streetwise: {class: NORMAL, tier: T2, evidence: 0, class_source: Whitechapel born, abilities: []}
    blades: {class: NORMAL, tier: T1, evidence: 0, class_source: street fighting, abilities: []}
  traits: ['gang name on the street — "Kell of the Rooks"']
  expertise: {established: [Whitechapel streets, pubs and fences, the docks], limitations: [no Assassin training, no letters beyond his name]}
  growth_period: {opened: 0, credited: [brawling]}
  progression: {system: numeric_level_xp, state: {level: 3, xp: 0}}
  condition: {hp: 13, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [], fatigue: tired, last_rest: full night, Day 6}
  equipment:
    - {item_id: knuckle_duster, name: knuckle-duster, type: light weapon, capability_domain: brawling, condition: serviceable, tier: T1}
    - {item_id: cane, name: weighted cane, type: one-handed weapon, capability_domain: brawling, condition: worn, tier: T1}
    - {item_id: cosh, name: leather cosh, type: light weapon, capability_domain: brawling, condition: serviceable, tier: T1}
    - {item_id: working_clothes, name: coat, boots and cap, type: clothing, condition: worn, tier: T1}
  money: {cash: 13s}
  item_points: {rank: commoner, basis: a Rook's share and docker's pay, current: 40, max: 40}
  fighting_style: ['nobody dies for a pub: two down or it goes bad → out the back (Day 7, the Ten Bells)']
  knowledge:
    facts:
      london: the Blighters own Whitechapel and Starrick owns the Blighters
      role: Jacob Frye runs the Rooks
      bounties: Abberline's notice names Blighter men
    channels: [the street, the papers, the Rooks]
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
narrative_theme: {initial: swaggering, adventurous, sharp-tongued; Victorian grime and wit, current: same}
index:
  npcs:
    jacob_frye: "Jacob Frye — the Rooks' boss; out at the rail yards tonight"
    evie_frye: "Evie Frye — Jacob's sister; told everything at the yard gate"
    frederick_abberline: "Sergeant Abberline — paid the bounty on Nobby; wants a quiet word with Jacob"
    alf_tanner: "Big Alf — ribs strapped, by Davey's bed"
    davey_shaw: "Davey Shaw — cracked skull, in the London Hospital"
    mick_doyle: "Mick Doyle — with Tom at the yard gate"
    sal_pruitt: "Sal Pruitt — fled to her sister's"
    nobby_crane: "Nobby Crane — Blighter crew boss; in Abberline's cells"
    joseph_hale: "Constable Hale — on the Ten Bells door"
    rexford_kaylock: "Rexford Kaylock — the Blighters' boss in Whitechapel"
  locations:
    ten_bells: "the Ten Bells — smashed, retaken, a constable on the door"
    london_hospital: "the London Hospital — Davey and Alf"
  rights_obligations:
    message_to_jacob: "promise to Abberline — passed to Evie for Jacob"
```

## Part B — capsule

capsule:
  save_round: 10
  delta_of: ac_syndicate_london_v6_0   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    active_commitments.r9 :: R9: rights_obligations.message_to_jacob
    continuity_status.corrected.r6 :: R7: "R6 narration had the knifed Blighter hopping at HP 0 and five Blighters left in the pub; fixed: he was carried; two left in the pub (GM §7.4)"
    locations.london_hospital :: R5: {"name": "the London Hospital, Whitechapel Road", "zone": "whitechapel", "conditions": {"features": ["a night porter's lodge", "the accident ward", "house surgeons on night duty"]}, "challenge_band": {"min": 0, "max": 1, "basis": "a charity hospital"}}
    locations.ten_bells :: R0: {"name": "the Ten Bells", "zone": "whitechapel", "conditions": {"features": ["the Rooks' pub since Day 3", "a long bar", "a back yard to the alley"]}, "challenge_band": {"min": 1, "max": 3, "basis": "a gang pub"}}
    npcs.alf_tanner.belongs :: R1: [rooks]
    npcs.alf_tanner.capability :: R1: {overall_level: 2, skills: {brawling: T1}}
    npcs.alf_tanner.character :: R1: slow-talking, steady, likes Tom
    npcs.alf_tanner.condition.conditions.cracked_ribs.condition :: R5: cracked ribs
    npcs.alf_tanner.condition.conditions.cracked_ribs.effect :: R5: strapped; harder to fight, lift or run for about a week
    npcs.alf_tanner.condition.conditions.cracked_ribs.source :: R5: body
    npcs.alf_tanner.depth :: R1: 1
    npcs.alf_tanner.drives :: R1: {fear: the workhouse for his mum, want: his share and a quiet pint}
    npcs.alf_tanner.gender :: R1: man
    npcs.alf_tanner.in_disorder :: R1: thrives
    npcs.alf_tanner.job :: R1: Rook, ex-Clinker
    npcs.alf_tanner.knowledge.facts.orders :: R1: Jacob's orders: hold the Ten Bells tonight, nobody goes looking for trouble; he and Evie are at the rail yards
    npcs.alf_tanner.name :: R1: Big Alf Tanner
    npcs.alf_tanner.state.hp :: R3: 4
    npcs.alf_tanner.state.plan :: R6: stays by Davey's bed at the London
    npcs.alf_tanner.state.position :: R5: the London Hospital
    npcs.alf_tanner.voice :: R1: few words, all of them flat
    npcs.clara_odea.state.due :: R0: Bs Day 5 afternoon sent a runner to Jacob (test fixture: done); B when the Rooks answer, shows them the mill
    npcs.davey_shaw.belongs :: R1: [rooks]
    npcs.davey_shaw.capability :: R1: {overall_level: 2, skills: {blades: T1, brawling: T1}}
    npcs.davey_shaw.character :: R1: wiry, mean-tempered, good with a knife
    npcs.davey_shaw.condition.conditions.skull.condition :: R5: cracked skull
    npcs.davey_shaw.condition.conditions.skull.effect :: R5: stabilised by the house surgeon; in hospital at least a week; no fighting
    npcs.davey_shaw.condition.conditions.skull.source :: R5: body
    npcs.davey_shaw.depth :: R1: 1
    npcs.davey_shaw.drives :: R1: {fear: Kaylock's hammer men, want: Blighter blood for his brother's broken arm}
    npcs.davey_shaw.gender :: R1: man
    npcs.davey_shaw.in_disorder :: R1: thrives
    npcs.davey_shaw.job :: R1: Rook, ex-Clinker
    npcs.davey_shaw.name :: R1: Davey Shaw
    npcs.davey_shaw.state.hp :: R3: 0
    npcs.davey_shaw.state.position :: R5: the London Hospital, accident ward
    npcs.davey_shaw.voice :: R1: sneers and swears
    npcs.evie_frye.knowledge.facts.ten_bells :: R10: R10 from Tom and Mick: the Ten Bells lost and retaken; Davey in the London; Nobby Crane in Abberline's cells; Abberline wants a quiet word with Jacob
    npcs.evie_frye.relationships.pc :: R10: {"tie": "one of Jacob's Rooks", "attitude": "approving, dry", "credit": ["retook the Ten Bells alone and brought her Abberline's message, R10"]}
    npcs.evie_frye.state.due :: R10: A-1 Day 8 morning tells Jacob about the Ten Bells and Abberline; A-3 when beat_2 opens, the Kenway mansion
    npcs.ezra_watts :: R5: {"depth": 0, "name": "Ezra Watts", "job": "night porter, London Hospital", "belongs": ["independent"], "gender": "man", "character": "tired, careful, seen it all", "manner": "asks the questions he's paid to and writes the answers down", "in_disorder": "suffers", "state": {"position": "the London Hospital"}}
    npcs.frederick_abberline.relationships.pc :: R8: {"tie": "a Rook who brought in a bounty", "attitude": "wary, interested", "credit": ["brought him Nobby Crane, R8"]}
    npcs.frederick_abberline.state.due :: R8: A-1s paid Tom Kell's bounty on Nobby Crane (R8); A-1 when a bounty is brought in, pays it
    npcs.henry_green.state.due :: R2: A-3 Day 8 morning works through Ethan Frye's notes with Evie at his shop
    npcs.jacob_frye.state.due :: R0: A-1 Day 8 evening hits the Blighters' rail-yard stronghold with every Rook he can find
    npcs.jacob_frye.state.plan.next :: R0: A-1 scouting Kaylock's rail-yard stronghold with Evie tonight
    npcs.jacob_frye.state.position :: R0: Whitechapel rail yards
    npcs.joseph_hale.belongs :: R9: [metropolitan_police]
    npcs.joseph_hale.character :: R9: big, slow, honest
    npcs.joseph_hale.depth :: R9: 0
    npcs.joseph_hale.gender :: R9: man
    npcs.joseph_hale.in_disorder :: R9: suffers
    npcs.joseph_hale.job :: R9: constable, H Division, one of Abberline's honest men
    npcs.joseph_hale.manner :: R9: rattle on his belt, says sir to everyone
    npcs.joseph_hale.name :: R9: Joseph Hale
    npcs.joseph_hale.state.plan :: R9: stand at the Ten Bells till the morning relief, Abberline's order (R9)
    npcs.joseph_hale.state.position :: R10: the Ten Bells
    npcs.mick_doyle.belongs :: R1: [rooks]
    npcs.mick_doyle.capability :: R1: {overall_level: 1, skills: {brawling: T1}}
    npcs.mick_doyle.character :: R1: 17, quick, eager, scared and hiding it
    npcs.mick_doyle.depth :: R1: 1
    npcs.mick_doyle.drives :: R1: {fear: being thought a coward, want: to be somebody in the Rooks}
    npcs.mick_doyle.gender :: R1: man
    npcs.mick_doyle.in_disorder :: R1: thrives
    npcs.mick_doyle.job :: R1: Rook, the youngest
    npcs.mick_doyle.name :: R1: Mick Doyle
    npcs.mick_doyle.state.plan :: R6: find Jacob at the rail yards; tell him the Ten Bells is lost and Davey is in the London
    npcs.mick_doyle.state.position :: R10: Whitechapel rail yards, the yard gate
    npcs.mick_doyle.voice :: R1: too loud, too fast
    npcs.nobby_crane.belongs :: R2: [blighters]
    npcs.nobby_crane.capability :: R2: {overall_level: 3, skills: {brawling: T2}}
    npcs.nobby_crane.character :: R2: big, loud, proud of his hammer
    npcs.nobby_crane.condition.conditions.split_scalp :: R3: {"condition": "scalp split by a cane", "source": "body", "effect": "blood in his eyes: harder to see in a fight"}
    npcs.nobby_crane.depth :: R2: 1
    npcs.nobby_crane.drives :: R2: {fear: going back to the train empty-handed, want: the Ten Bells back by morning for Kaylock}
    npcs.nobby_crane.gender :: R2: man
    npcs.nobby_crane.in_disorder :: R2: thrives
    npcs.nobby_crane.job :: R2: Blighter crew boss under Kaylock
    npcs.nobby_crane.knowledge.facts.kell :: R6: the Rook who split his scalp with a cane was Tom Kell — "Kell of the Rooks" is known by sight on the street (R4)
    npcs.nobby_crane.name :: R2: Nobby Crane
    npcs.nobby_crane.relationships.pc.grievance.r7_beaten :: R7: beaten twice by Tom Kell in one night, in front of his own men (R4, R7)
    npcs.nobby_crane.state.due :: R7: A-1 when he is free or a Blighter finds him, tells Kaylock it was Kell
    npcs.nobby_crane.state.hp :: R7: 1
    npcs.nobby_crane.state.plan :: R7: "stay alive; get word to Kaylock; blame the Rooks' numbers"
    npcs.nobby_crane.state.position :: R8: Whitechapel police station (Leman Street)
    npcs.nobby_crane.state.status :: R8: in the cells, charged by Sergeant Abberline on his bounty notice; HP 1
    npcs.nobby_crane.state.tactics :: R3: windows first, sledges on the door; NO, BUT: no men sent round the back at first, one sent when the door held (R3 ask)
    npcs.nobby_crane.voice :: R2: bellows; calls everyone "my son"
    npcs.rexford_kaylock.knowledge.facts.ten_bells :: R10: a peeler on the Ten Bells door; Nobby missing; a Rook called Kell (23:30)
    npcs.rexford_kaylock.state.due :: R10: A-1 Day 8 morning doubles protection on every Whitechapel street, asks his bought constables where Nobby is, and sends men to find Kell
    npcs.sal_pruitt.belongs :: R1: [independent]
    npcs.sal_pruitt.character :: R1: tough, practical; loyal to whoever keeps her windows in
    npcs.sal_pruitt.depth :: R1: 1
    npcs.sal_pruitt.drives :: R1: {fear: a fire, want: her pub standing}
    npcs.sal_pruitt.gender :: R1: woman
    npcs.sal_pruitt.in_disorder :: R1: suffers
    npcs.sal_pruitt.job :: R1: landlady of the Ten Bells
    npcs.sal_pruitt.name :: R1: Sal Pruitt
    npcs.sal_pruitt.state.position :: R4: Whitechapel, her sister's on Flower and Dean Street (fled out the back)
    npcs.sal_pruitt.voice :: R1: barmaid's patter over a hard edge
    npcs.ten_bells_doorman.belongs :: R8: [blighters]
    npcs.ten_bells_doorman.character :: R8: a hired cudgel
    npcs.ten_bells_doorman.depth :: R8: 0
    npcs.ten_bells_doorman.gender :: R8: man
    npcs.ten_bells_doorman.in_disorder :: R8: thrives
    npcs.ten_bells_doorman.job :: R8: Blighter
    npcs.ten_bells_doorman.manner :: R8: out cold
    npcs.ten_bells_doorman.name :: R8: unknown Blighter (the Ten Bells doorman)
    npcs.ten_bells_doorman.state.hp :: R8: 0
    npcs.ten_bells_doorman.state.position :: R8: the Ten Bells
    npcs.ten_bells_doorman.state.status :: R10: tied, held by Constable Hale
    rights_obligations.message_to_jacob.parties :: R10: [pc, frederick_abberline]
    rights_obligations.message_to_jacob.state :: R10: {status: 'passed to Evie for Jacob, R10', terms: 'Tom tells Jacob Frye that Abberline wants a quiet word, not at the station'}
    rights_obligations.message_to_jacob.type :: R10: promise
    world_state.material_history.r4_ten_bells_lost :: R4: R4 Day 7 21:06 the Rooks gave up the Ten Bells to Nobby Crane's crew and went out the back carrying Davey Shaw
    world_state.pending.blighter_back :: R3: the Blighter sent round the back, down in the back passage, HP 0 (Davey's knife)
    world_state.pending.blighter_cudgel_1 :: R3: HP 6 (R3)
    world_state.pending.blighter_sledge_1 :: R3: down in the Ten Bells doorway, HP 0 (R3)
    world_state.pending.blighter_sledge_2 :: R3: hurt, HP 1, pulled back by his mates (R3)
    world_state.pending.carriers_return :: R10: "done: at 23:00 three Blighters and the hurt sledge man found a constable on the Ten Bells door; with no crew boss and no orders they shouted, didn't touch him, and went back toward the train"
    world_state.pending.hale_at_ten_bells :: R10: "done: Hale on the Ten Bells door from 22:55; found the tied doorman and is holding him"
    world_state.pending.kaylock_hears_constable :: R10: "done 23:30: Kaylock heard of the constable and that Nobby is missing"
    world_state.pending.mick_finds_evie :: R10: "done: at 23:40 Evie came out to the yard gate; Mick and Tom told her"
    world_state.pending.nobby_runner :: R8: "done: the runner reached the train at 22:15"
    world_state.pending.porter_report :: R5: {what: "the porter's book records a man brought in beaten about the head by friends Tom Kell and Alfred Tanner; the book goes to the police on the morning round", cause: "hospital practice with assault cases", due: Day 8 morning}
    world_state.pending.ten_bells_raid :: R2: {what: "Nobby Crane and seven Blighters (level 2: two sledgehammers, five cudgels) march on the Ten Bells", cause: "Kaylock's A-1 Day 7 night order", due: Day 7 21:00}
  retired:
    world_state.pending.ten_bells_doorman :: now a record of his own (npcs.ten_bells_doorman)
continuity_status:
  degraded: ["R0 '- player.skills.[ROLE skills from the role table]' could not be read by merge: the background's placeholder key has no id; the player block in Part A holds the real skills"]
  corrected: ["R6: knifed Blighter hopping at HP 0, five left in the pub → carried; two left (GM §7.4)"]
  round0_revisions: []
  save_deferral: null
