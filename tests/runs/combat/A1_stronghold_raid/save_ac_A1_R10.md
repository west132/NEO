# SAVE — AC Syndicate (combat test A1) R10

## Part A — readable

```yaml
background_ref: {id: ac_syndicate_london_v6_0}
language: en
round: {last_completed_round: 10, saved_completed_round: 10}
world_state:
  location: london_hospital
  time: {season: winter, day_index: 6, date: Day 6 (February 1868), clock_minutes: 1395, daypart: evening, precision: exact}
  environment: {weather: thick fog, town: "Whitechapel near midnight; the cooperage yard held by the Rooks; Kaylock dead"}
player:
  identity: {name: Tom Kell, age: 24, origin: "Whitechapel born; docker's son", history: ["ran with the Clinkers; went Rook on Day 3"]}
  appearance: "broad, broken nose, red Rook scarf"
  archetype: Rook
  job: Rook enforcer
  belongs: [rooks]
  gender: man
  character: player-defined in play
  status: bruised; at the London Hospital with Alf
  skills:
    brawling: {class: NORMAL, tier: T2, evidence: 0, class_source: the docks and the Clinkers, abilities: []}
    streetwise: {class: NORMAL, tier: T2, evidence: 0, class_source: Whitechapel born, abilities: []}
    blades: {class: NORMAL, tier: T1, evidence: 0, class_source: street fighting, abilities: []}
  traits: ['gang name on the street — "Kell of the Rooks"']
  growth_period: {opened: 0, credited: []}
  progression: {system: numeric_level_xp, state: {level: 3, xp: 93}}
  condition: {hp: 14, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [], fatigue: tired, last_rest: "full night, Day 5"}
  equipment:
    - {item_id: knuckle_duster, name: knuckle-duster, type: light weapon, condition: serviceable, tier: T1}
    - {item_id: cane, name: weighted cane, type: one-handed weapon, condition: worn, tier: T1}
    - {item_id: cosh, name: leather cosh, type: light weapon, condition: serviceable, tier: T1}
  money: {cash: 11s}
  item_points: {rank: commoner, basis: "a Rook's share and docker's pay", current: 40, max: 40}
  fighting_style: ["both sides of the gate; nobody kills a man who drops his cudgel; if it turns, over the back wall (Day 6)"]
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
index:
  npcs:
    jacob_frye: "Jacob Frye — the Rooks' boss; killed Kaylock; told Tom off in front of the gang"
    alf_tanner: "Big Alf — broken collarbone, in the London"
    davey_shaw: "Davey Shaw — arm laid open, in the London"
    rigger: "Rigger — Blighter crew boss, skull fractured, in the London"
    rexford_kaylock: "Rexford Kaylock — dead in the cooperage cart gate"
  locations:
    cooperage_yard: "the Black Eagle cooperage yard — the Rooks' first stronghold"
    london_hospital: "the London Hospital"
  quests:
    A-1: "Whitechapel: who holds it — Kaylock dead; the train still the Blighters'"
```


## Part B — capsule

capsule:
  save_round: 10
  delta_of: ac_syndicate_london_v6_0   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    locations.cooperage_yard.challenge_band :: R0: {basis: a Blighter stronghold, max: 4, min: 2}
    locations.cooperage_yard.conditions.features :: R0: [a walled yard off Brick Lane behind Truman's brewery, stacked barrels, a two-storey cooperage the Blighters use as a counting house, a cart gate and a wicket door]
    locations.cooperage_yard.conditions.held_by :: R0: a Blighter crew; protection money counted there
    locations.cooperage_yard.conditions.money :: R3: "upstairs on the table: Thursday's protection takings, about £11 in coin and notes, counted into stacks"
    locations.cooperage_yard.conditions.tonight :: R2: "Rigger and one man counting upstairs at a lit window; two Blighters at a brazier in the yard; one sitting by the wicket with a cudgel; one asleep on sacks under the cooperage stairs (six in all)"
    locations.cooperage_yard.name :: R0: the Black Eagle cooperage yard, Brick Lane
    locations.cooperage_yard.zone :: R0: whitechapel
    locations.london_hospital :: R5: {name: "the London Hospital, Whitechapel Road", zone: whitechapel, conditions: {features: ["a night porter's lodge", "the accident ward", "house surgeons on night duty"]}, challenge_band: {min: 0, max: 1, basis: "a charity hospital"}}
    locations.ten_bells :: R0: {name: "the Ten Bells", zone: whitechapel, conditions: {features: ["the Rooks' pub since Day 3", "a long bar", "a back yard to the alley"]}, challenge_band: {min: 1, max: 3, basis: "a gang pub"}}
    locations.whitechapel.undercurrent.tension :: R9: 3 (R9: Kaylock killed, a decisive act +2, lasting; Whitechapel's lieutenant dead)
    npcs.alf_tanner.belongs :: R0: [rooks]
    npcs.alf_tanner.capability :: R0: {overall_level: 2, skills: {brawling: T1}}
    npcs.alf_tanner.character :: R0: slow-talking, steady, likes Tom
    npcs.alf_tanner.condition.conditions.collarbone.condition :: R5: broken collarbone
    npcs.alf_tanner.condition.conditions.collarbone.effect :: R5: strapped; can't lift his left arm; no fighting for a week
    npcs.alf_tanner.condition.conditions.collarbone.source :: R5: body
    npcs.alf_tanner.depth :: R0: 1
    npcs.alf_tanner.drives :: R0: {fear: the workhouse for his mum, want: his share and a quiet pint}
    npcs.alf_tanner.gender :: R0: man
    npcs.alf_tanner.in_disorder :: R0: thrives
    npcs.alf_tanner.job :: R0: Rook, ex-Clinker
    npcs.alf_tanner.name :: R0: Big Alf Tanner
    npcs.alf_tanner.state.due :: R0: none (incidental)
    npcs.alf_tanner.state.hp :: R3: 4
    npcs.alf_tanner.state.plan :: R6: "with Shem, sit by Rigger's bed in the London; nobody takes him out (Tom's order)"
    npcs.alf_tanner.state.position :: R5: the London Hospital
    npcs.alf_tanner.voice :: R0: few words, all of them flat
    npcs.clara_odea.state.due :: R0: Bs Day 5 afternoon sent a runner to Jacob (test fixture: done); B when the Rooks answer, shows them the mill
    npcs.crawford_starrick.state.due :: R10: A-1 Day 7 morning hears by wire that Kaylock is dead and the first stronghold fell; orders his lieutenants to crush the new gang
    npcs.davey_shaw.belongs :: R0: [rooks]
    npcs.davey_shaw.capability :: R0: {overall_level: 2, skills: {blades: T1, brawling: T1}}
    npcs.davey_shaw.character :: R0: wiry, mean-tempered, good with a knife
    npcs.davey_shaw.depth :: R0: 1
    npcs.davey_shaw.drives :: R0: {fear: Kaylock's hammer men, want: Blighter blood for his brother's broken arm}
    npcs.davey_shaw.gender :: R0: man
    npcs.davey_shaw.in_disorder :: R0: thrives
    npcs.davey_shaw.job :: R0: Rook, ex-Clinker
    npcs.davey_shaw.name :: R0: Davey Shaw
    npcs.davey_shaw.state.due :: R0: none (incidental)
    npcs.davey_shaw.state.hp :: R8: 2
    npcs.davey_shaw.state.position :: R10: the London Hospital (walked in with Tom)
    npcs.davey_shaw.voice :: R0: sneers and swears
    npcs.evie_frye.state.due :: R0: A-3s Day 2 morning starts Henry's records (test fixture: done); A-3 when beat_2 opens, the Kenway mansion
    npcs.frederick_abberline.state.due :: R0: A-1s Day 4 morning posted bounties (test fixture: done); A-1 when a bounty is brought in, pays it
    npcs.henry_green.state.due :: R0: A-3 Day 8 morning works through Ethan Frye's notes with Evie at his shop
    npcs.jacob_frye.knowledge.facts.cooperage :: R1: Clara's urchins counted six Blighters on weeknights at the cooperage yard, a crew boss called Rigger, and the protection money counted upstairs on Fridays; tonight is a Thursday
    npcs.jacob_frye.relationships.pc :: R4: {tie: "his Rook", attitude: "pleased, cocky", credit: ["scouted the yard and saw the gun, R2", "first through the wicket, R3"]}
    npcs.jacob_frye.state.carried.revolver :: R3: "Rigger's cheap revolver, four rounds (one fired into the floor as Jacob took it)"
    npcs.jacob_frye.state.carried.rooks_chest :: R10: "£5 10s, half of Rigger's takings, for the Rooks' chest"
    npcs.jacob_frye.state.due :: R9: A-1s killed Kaylock; A-1 Day 7 morning takes Kaylock's train with the Rooks before the Blighters regroup
    npcs.jacob_frye.state.plan :: R4: "A-1 hold the cooperage yard tonight as the Rooks' first stronghold; send for every Rook in Whitechapel; split the money: half to the Rooks' chest, half to tonight's men"
    npcs.jacob_frye.state.plan.next :: R0: A-1 take the first Blighter stronghold in Whitechapel (the cooperage yard), to start the Rooks' push on the borough
    npcs.jacob_frye.state.tactics :: R1: Jacob over the back wall and through the cooperage; Tom's party in at the wicket door when he whistles; nobody touches the money till the Blighters are out
    npcs.rexford_kaylock.knowledge.facts.cooperage :: R5: "the Rooks took the cooperage and Rigger; Jacob Frye with a revolver at the window (the runners, 21:45)"
    npcs.rexford_kaylock.state.due :: R9: none (dead)
    npcs.rexford_kaylock.state.hp :: R8: 0
    npcs.rexford_kaylock.state.plan :: R5: "A-1 retake the cooperage yard tonight with the train crew, himself at the front; never backs down in front of his men"
    npcs.rexford_kaylock.state.position :: R7: Brick Lane, outside the cooperage cart gate
    npcs.rexford_kaylock.state.status :: R9: dead — killed by Jacob Frye with a kukri in the cooperage cart gate, helpless, Day 6 22:40 (R9)
    npcs.rigger.belongs :: R2: [blighters]
    npcs.rigger.capability :: R2: {overall_level: 3, skills: {brawling: T1, firearms: T1}}
    npcs.rigger.carried :: R2: a cheap revolver (bow-class 1d8 per shot), five rounds
    npcs.rigger.character :: R2: careful, sour, a counter of coins
    npcs.rigger.condition.conditions.down.condition :: R5: fractured skull
    npcs.rigger.condition.conditions.down.effect :: R5: stabilised by the house surgeon at 21:55; in hospital at least a week
    npcs.rigger.condition.conditions.down.source :: R5: body
    npcs.rigger.depth :: R2: 1
    npcs.rigger.drives :: R2: {fear: being short when Kaylock counts, want: the money counted right and sent up to Kaylock}
    npcs.rigger.gender :: R2: man
    npcs.rigger.in_disorder :: R2: thrives
    npcs.rigger.job :: R2: Blighter crew boss at the cooperage yard
    npcs.rigger.name :: R2: Rigger (Sam Riggs)
    npcs.rigger.state.due :: R2: A-1 Day 7 morning sends the takings to Kaylock's train
    npcs.rigger.state.hp :: R3: 0
    npcs.rigger.state.plan :: R2: count Thursday's takings; send them to the train Friday
    npcs.rigger.state.position :: R5: the London Hospital, accident ward
    npcs.rigger.state.status :: R5: in the London Hospital under the name the Rooks gave (R5)
    npcs.rigger.voice :: R2: short, flat, swears quietly
    npcs.rook_crew_a1.belongs :: R1: [rooks]
    npcs.rook_crew_a1.capability :: R1: {overall_level: 1}
    npcs.rook_crew_a1.character :: R1: ex-Clinkers and dockers
    npcs.rook_crew_a1.depth :: R1: 0
    npcs.rook_crew_a1.gender :: R1: men
    npcs.rook_crew_a1.in_disorder :: R1: thrives
    npcs.rook_crew_a1.job :: R1: Rooks
    npcs.rook_crew_a1.manner :: R1: loud, nervy, eager
    npcs.rook_crew_a1.name :: R1: three more Rooks from the Brick Lane end (Fitch, Lenny, Old Shem)
    npcs.rook_crew_a1.state.due :: R1: none (incidental)
    npcs.rook_crew_a1.state.position :: R1: the Ten Bells
    npcs.rook_crew_a1.state.split :: R6: "Shem stays at the London with Alf; Lenny back with Tom; Fitch at the yard"
    npcs.rooks_reinforcements.belongs :: R6: [rooks]
    npcs.rooks_reinforcements.capability :: R6: {overall_level: 1}
    npcs.rooks_reinforcements.character :: R6: dockers, carters, a couple of lads
    npcs.rooks_reinforcements.depth :: R6: 0
    npcs.rooks_reinforcements.gender :: R6: men
    npcs.rooks_reinforcements.in_disorder :: R6: thrives
    npcs.rooks_reinforcements.job :: R6: Rooks
    npcs.rooks_reinforcements.manner :: R6: half drunk on the promise of beer
    npcs.rooks_reinforcements.name :: R6: eight Rooks from the Ten Bells and the Brick Lane end
    npcs.rooks_reinforcements.state.due :: R6: none (incidental)
    npcs.rooks_reinforcements.state.hurt :: R8: "Rook 3 down (HP 0); Rooks 1, 8, Fitch, Lenny badly hurt; the rest bruised"
    npcs.rooks_reinforcements.state.position :: R6: the Black Eagle cooperage yard, Brick Lane
    quests.tq_whitechapel.code_given :: R9: A-1 (R1: Tom joined Jacob's raid without reservation — given late, R9, GM slip)
    quests.tq_whitechapel.status :: R9: active
    world_state.material_history.r3_cooperage :: R3: "R3 Day 6 21:25 the Rooks took the Black Eagle cooperage yard: Jacob over the back wall and up the stairs, Tom's party through the wicket; Rigger down, three Blighters yielded, two fled over the back wall"
    world_state.material_history.r9_jacob_remark :: R9: "NO, AND (R9 ask): Jacob told Tom off in front of the Rooks for arguing for Kaylock — a remark; no grievance, the relationship moves only on a material event"
    world_state.material_history.r9_kaylock :: R9: "Day 6 22:40 Rexford Kaylock killed by Jacob Frye in the cooperage cart gate — not on his train as in the game"
    world_state.material_history.xp_kaylock_s_crew_beaten_at_the_cart_gate_r8 :: R9: XP paid for Kaylock's crew beaten at the cart gate (R8): 55
    world_state.material_history.xp_the_cooperage_yard_taken_r3 :: R9: XP paid for the cooperage yard taken (R3): 38 (paid late, R9 — GM slip)
    world_state.pending.blighter_prisoners :: R10: "seven Blighters tied in the cooperage yard (three from R3, four from R8); Jacob means to turn them loose at dawn without their boots"
    world_state.pending.blighters_fled :: R5: "done 21:45: the two reached Kaylock's train"
    world_state.pending.blighters_fled_2 :: R10: "done 22:50: the three reached the train; with Kaylock dead the train crew argue about who leads; one goes to wire Starrick's office"
    world_state.pending.cooperage_prisoners :: R3: "the wicket man (HP 5), the counter (HP 12) and brazier man 2 (HP 1, knife-cut) yielded; sitting against the barrels under Rooks' eyes"
    world_state.pending.kaylock_attack :: R7: {what: "Kaylock and twelve of the train crew (level 2; cudgels, two sledges, lanterns) come down Brick Lane to the cart gate", cause: "Kaylock's A-1 Day 6 22:30 move", due: Day 6 22:30}
    world_state.pending.rook_runners :: R6: "done 22:00: YES (R6 ask) — eight more Rooks turned out at the yard, level 1–2, cudgels and knives; with Jacob, Tom, Davey, Lenny, Fitch: thirteen"
    world_state.pending.yard_fight :: R8: "R8 Day 6 22:35: Kaylock's crew broke the cart gate and were caught between the Rooks; six Blighters down (Blighters 1, 4, 5, 6, 11 and Kaylock); when Kaylock fell the rest broke — four hurt ones yielded, three ran up Brick Lane"
  retired:
    npcs.rexford_kaylock.condition.conditions.down :: dead
continuity_status:
  degraded: ["R0 '- player.skills.[ROLE skills from the role table]' unreadable to merge (placeholder key); the player block in Part A holds the real skills"]
  corrected: ["R9: quest A-1 made active late (should have been R1); XP for R3 and R8 paid late at R9; Jacob's NO, AND first written as a grievance, corrected to a remark before showing"]
  round0_revisions: []
  save_deferral: null
