# SAVE — AC Syndicate (combat test A2) R10

## Part A — readable

```yaml
background_ref: {id: ac_syndicate_london_v6_0}
language: en
round: {last_completed_round: 10, saved_completed_round: 10}
world_state:
  location: ten_bells
  time: {season: winter, day_index: 6, date: Day 6 (February 1868), clock_minutes: 360, daypart: morning, precision: exact}
  environment: {weather: cold fog, town: "Whitechapel at dawn; the mill whistle on Hanbury Street"}
player:
  identity: {name: Tom Kell, age: 24, origin: "Whitechapel born; docker's son", history: ["ran with the Clinkers; went Rook on Day 3"]}
  appearance: "broad, broken nose, red Rook scarf"
  archetype: Rook
  job: Rook enforcer
  belongs: [rooks]
  gender: man
  character: player-defined in play
  status: rested; at the Ten Bells
  skills:
    brawling: {class: NORMAL, tier: T2, evidence: 0, class_source: the docks and the Clinkers, abilities: []}
    streetwise: {class: NORMAL, tier: T2, evidence: 0, class_source: Whitechapel born, abilities: []}
    blades: {class: NORMAL, tier: T1, evidence: 0, class_source: street fighting, abilities: []}
  traits: ['gang name on the street — "Kell of the Rooks"']
  growth_period: {opened: 6, credited: []}
  progression: {system: numeric_level_xp, state: {level: 3, xp: 38}}
  condition: {hp: 14, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [], fatigue: rested, last_rest: "Day 5 night, the Ten Bells"}
  equipment:
    - {item_id: knuckle_duster, name: knuckle-duster, type: light weapon, condition: serviceable, tier: T1}
    - {item_id: cane, name: weighted cane, type: one-handed weapon, condition: worn, tier: T1}
    - {item_id: cosh, name: leather cosh, type: light weapon, condition: serviceable, tier: T1}
  money: {cash: 0s}
  item_points: {rank: commoner, basis: "a Rook's share and docker's pay", current: 40, max: 40}
  fighting_style: []
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
index:
  npcs:
    clara_odea: "Clara O'Dea — the urchins' leader; warmer now"
    maggie_dunn: "Maggie Dunn — Lizzie's mother; furious about the lost wage"
    grieve: "Mr Grieve — night foreman at the jute mill; saw Tom's face"
    sal_pruitt: "Sal Pruitt — let six children sleep in the back room"
    alf_tanner: "Big Alf — took the gatehouse"
    davey_shaw: "Davey Shaw — took the gatehouse"
  locations:
    jute_mill: "Starrick & Co. jute mill, Hanbury Street"
    ten_bells: "the Ten Bells"
  quests:
    Bs: "the mill children — thirty out for one night"
```

## Part B — capsule

capsule:
  save_round: 10
  delta_of: ac_syndicate_london_v6_0   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    locations.jute_mill.challenge_band :: R1: {basis: a guarded mill; the danger is the machines, max: 3, min: 1}
    locations.jute_mill.conditions.back_door :: R3: "unbolted from inside by Clara at 19:20 (R3); the stoker never saw her"
    locations.jute_mill.conditions.features :: R1: [three floors of looms and carding engines driven by one steam engine and leather belts, a gatehouse on the street with two Blighters, a coal chute into the boiler cellar off the back lane (Clara's tunnel), 'night shift: about thirty children and a foreman']
    locations.jute_mill.conditions.hazards :: R1: [belts and carding engines that take hands, 'jute dust and oil lamps: fire spreads fast']
    locations.jute_mill.name :: R1: Starrick & Co. jute mill, Hanbury Street
    locations.jute_mill.zone :: R1: whitechapel
    locations.ten_bells :: R0: {name: "the Ten Bells", zone: whitechapel, conditions: {features: ["the Rooks' pub since Day 3", "a long bar", "a back yard to the alley"]}, challenge_band: {min: 1, max: 3, basis: "a gang pub"}}
    npcs.alf_tanner.belongs :: R2: [rooks]
    npcs.alf_tanner.capability :: R2: {overall_level: 2, skills: {brawling: T1}}
    npcs.alf_tanner.character :: R2: slow-talking, steady, likes Tom
    npcs.alf_tanner.depth :: R2: 1
    npcs.alf_tanner.drives :: R2: {fear: the workhouse for his mum, want: his share and a quiet pint}
    npcs.alf_tanner.gender :: R2: man
    npcs.alf_tanner.in_disorder :: R2: thrives
    npcs.alf_tanner.job :: R2: Rook, ex-Clinker
    npcs.alf_tanner.name :: R2: Big Alf Tanner
    npcs.alf_tanner.state.due :: R2: none (incidental)
    npcs.alf_tanner.state.hp :: R4: 8
    npcs.alf_tanner.state.position :: R2: Hanbury Street
    npcs.alf_tanner.voice :: R2: few words, all of them flat
    npcs.bert_marsh :: R3: {depth: 0, name: "Bert Marsh", job: "night stoker, jute mill boiler cellar", belongs: [independent], gender: man, character: "old, deaf from the boilers", manner: "shovels and hums", in_disorder: suffers, state: {position: "Starrick & Co. jute mill, Hanbury Street", due: "none (incidental)"}}
    npcs.clara_odea.knowledge.facts.mill :: R2: "thirty kids on the night shift from seven; Grieve the foreman with his strap; two Blighters in the gatehouse; the coal chute in the back lane drops into the boiler cellar; her friend Annie lost two fingers in a carding engine last week"
    npcs.clara_odea.relationships.pc.attitude :: R9: "warmer; trusts him with one thing"
    npcs.clara_odea.relationships.pc.credit :: R5: ['came when Jacob didn''t, and took Grieve down, R4']
    npcs.clara_odea.relationships.pc.credit.r9 :: R9: "kept six of her kids out of the workhouse tonight, R8"
    npcs.clara_odea.relationships.pc.tie :: R5: the Rook who came
    npcs.clara_odea.state.due :: R8: Bs brought the six to the Ten Bells; B Day 6 morning moves them on to her own hiding places
    npcs.clara_odea.state.plan :: R5: "hide the six with nowhere from the parish and the workhouse; trade what her kids see for help"
    npcs.davey_shaw :: R2: {depth: 1, name: "Davey Shaw", job: "Rook, ex-Clinker", belongs: [rooks], gender: man, character: "wiry, mean-tempered, good with a knife", voice: "sneers and swears", drives: {want: "Blighter blood for his brother's broken arm", fear: "Kaylock's hammer men"}, in_disorder: thrives, state: {position: "Hanbury Street", due: "none (incidental)"}, capability: {overall_level: 2, skills: {blades: T1, brawling: T1}}}
    npcs.evie_frye.state.due :: R0: A-3s Day 2 morning starts Henry's records (test fixture: done); A-3 when beat_2 opens, the Kenway mansion
    npcs.frederick_abberline.state.due :: R0: A-1s Day 4 morning posted bounties (test fixture: done); A-1 when a bounty is brought in, pays it
    npcs.grieve.belongs :: R2: [templars]
    npcs.grieve.capability :: R2: {overall_level: 2}
    npcs.grieve.character :: R2: thin, tidy, carries a strap
    npcs.grieve.depth :: R2: 1
    npcs.grieve.drives :: R2: {fear: the owners docking his pay, want: the shift's quota met}
    npcs.grieve.gender :: R2: man
    npcs.grieve.in_disorder :: R2: suffers
    npcs.grieve.job :: R2: night foreman, Starrick & Co. jute mill
    npcs.grieve.knowledge.facts.tom :: R4: "a big Rook with a broken nose and a red scarf, with Clara O'Dea the urchin; took the night shift out"
    npcs.grieve.name :: R2: Mr Grieve
    npcs.grieve.state.due :: R7: B Day 6 06:00 found by the morning shift; B Day 6 09:00 reports to the mill manager, who complains to Leman Street station with Grieve's description of the Rook
    npcs.grieve.state.plan :: R2: run the night shift 19:00 to 06:00
    npcs.grieve.state.position :: R7: "Starrick & Co. jute mill, Hanbury Street (tied in the carding room)"
    npcs.grieve.state.status :: R4: "put on the floor of the carding room by Tom before he reached the alarm bell; tied with his own strap (R4)"
    npcs.grieve.voice :: R2: a schoolmaster's sneer
    npcs.henry_green.state.due :: R0: A-3 Day 8 morning works through Ethan Frye's notes with Evie at his shop
    npcs.jacob_frye.state.due :: R0: A-1 Day 6 21:00 leads the Rooks on a Blighter stronghold
    npcs.jacob_frye.state.position :: R0: Whitechapel rail yards
    npcs.maggie_dunn.belongs :: R6: [independent]
    npcs.maggie_dunn.character :: R6: worn out, fierce
    npcs.maggie_dunn.depth :: R6: 1
    npcs.maggie_dunn.drives :: R6: {fear: the workhouse, want: the rent paid}
    npcs.maggie_dunn.gender :: R6: woman
    npcs.maggie_dunn.in_disorder :: R6: suffers
    npcs.maggie_dunn.job :: R6: matchbox maker; mother of Lizzie (8), one of the night shift
    npcs.maggie_dunn.name :: R6: Maggie Dunn
    npcs.maggie_dunn.relationships.pc.attitude :: R6: furious
    npcs.maggie_dunn.relationships.pc.credit :: R6: ["gave her 3s for the lost week, R6"]
    npcs.maggie_dunn.relationships.pc.grievance :: R6: ['cost her Lizzie''s 4s a week, R6']
    npcs.maggie_dunn.relationships.pc.tie :: R6: the Rook who took her girl out of work
    npcs.maggie_dunn.state.due :: R7: B Day 6 morning goes to the mill to beg Lizzie's place back from the day foreman
    npcs.maggie_dunn.state.plan :: R7: "get Lizzie a place somewhere; tell anyone who'll listen that a Rook cost her the rent"
    npcs.maggie_dunn.state.position :: R6: Hanbury Street
    npcs.maggie_dunn.voice :: R6: shouts first, cries after
    npcs.mill_guards :: R2: {depth: 0, name: "two Blighters on the mill gate (Hoke and a lad)", job: Blighters, belongs: [blighters], gender: men, character: "bored, cold, paid by the week", manner: "smoke in the gatehouse, look out twice an hour", in_disorder: thrives, state: {position: "Starrick & Co. jute mill, Hanbury Street", due: "none (incidental)"}, capability: {overall_level: 2}}
    npcs.pip :: R1: {name: Pip, depth: 0, job: "one of Clara's runners", belongs: [independent], gender: boy, character: "about nine, barefoot, cheeky", manner: "talks while chewing, never stands still", in_disorder: neither, state: {position: "the Ten Bells", due: "none (incidental)"}}
    npcs.rexford_kaylock.state.due :: R7: A-1 Day 6 07:00 hears from Hoke that Rooks and Clara O'Dea emptied Starrick's Hanbury Street mill; A-1 Day 7 night his men start breaking Rook pubs
    npcs.sal_pruitt :: R8: {depth: 1, name: "Sal Pruitt", job: "landlady of the Ten Bells", belongs: [independent], gender: woman, character: "tough, practical; loyal to whoever keeps her windows in", voice: "barmaid's patter over a hard edge", drives: {want: "her pub standing", fear: "a fire"}, in_disorder: suffers, state: {position: "the Ten Bells", due: "none (incidental)"}}
    quests.side_mill_children.code_given :: R1: B (R1: Tom told Clara's runner the Rooks would come)
    quests.side_mill_children.status :: R9: succeeded (R9: thirty children out tonight; tomorrow the mill hires others) → shown as Bs
    world_state.material_history.xp_quest_b_the_mill_children_freed :: R9: XP paid for quest B, the mill children freed: 38
    world_state.pending.gatehouse :: R4: "R4 19:25 Alf and Davey took the gatehouse: the gate lad down (HP 0), Hoke (HP 4) yielded and sits tied in the corner"
    world_state.pending.gatehouse_found :: R7: {what: "the morning shift finds Hoke and the gate lad tied in the gatehouse; Hoke goes to Kaylock's train", cause: "the raid", due: Day 6 06:00}
    world_state.pending.mill_children :: R5: "R5 19:40 thirty children out in the back lane; twenty-four go home to their families on Clara's say; six with nowhere (no family, or a father who'd send them straight back) stay with Clara"
    world_state.pending.orphans_ten_bells :: R8: "six of the mill children sleep in the Ten Bells' back room tonight; Sal said yes (R8 ask) for the Rooks keeping her windows in"
continuity_status:
  degraded: ["R0 '- player.skills.[ROLE skills from the role table]' unreadable to merge (placeholder key); Part A holds the real skills", "R3–R6 no span was run; the evening surface roll was made late (R7) — nothing occurred"]
  corrected: ["R8: Sal Pruitt asked before her record existed in this run; recorded in the same block"]
  round0_revisions: []
  save_deferral: null
