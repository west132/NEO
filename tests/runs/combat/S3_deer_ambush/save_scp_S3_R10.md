# SAVE — SCP Class of '99 (combat test S3) R10

## Part A — readable

```yaml
background_ref: {id: scp_class_of_99_v5_2}
language: en
round: {last_completed_round: 10, saved_completed_round: 10}
world_state:
  location: pine_barrens
  time: {season: early spring, day_index: 13, date: '2026-03-14', clock_minutes: 420, daypart: morning, precision: exact}
  environment: {weather: cold, bright, pine smell}
player:
  identity: {name: Sam West, age: 26 (born January 2000), origin: "United States; three years a patrol officer in Columbus, Ohio", history: ["recruited after an impossible call; academy; Site-19 probation"]}
  appearance: "tall, lean, short black hair; moves carefully"
  archetype: field agent (probationary)
  job: Foundation field agent, Level 2, liaison to MTF Omega-99
  belongs: [foundation, mtf_omega_99]
  gender: man
  character: player-defined in play
  status: rested; ribs strapped; Day 13 of probation
  skills:
    field_investigation: {class: NORMAL, tier: T1, evidence: 1, class_source: academy training, abilities: []}
    firearms: {class: NORMAL, tier: T1, evidence: 0, class_source: academy and prior service, abilities: []}
    cover_and_persuasion: {class: NORMAL, tier: T1, evidence: 0, class_source: academy cover-identity training, abilities: []}
    first_aid: {class: NORMAL, tier: T1, evidence: 0, class_source: academy, abilities: []}
  growth_period: {opened: 13, credited: []}
  progression: {system: numeric_level_xp, state: {level: 2, xp: 32}}
  condition: {hp: 12, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [{condition: "two cracked ribs, strapped", source: body, effect: "hard to breathe; harder to run, climb or aim steady; heals in about a week with rest"}], fatigue: rested, last_rest: "Day 12 night, the Cedar Run motel"}
  equipment:
    - {item_id: west_sidearm, name: 'Glock 19 he calls "Patience"', type: t1_pistol, capability_domain: firearms, condition: serviceable, tier: T1}
    - {item_id: vest, name: issued soft vest, type: t1_vest, condition: serviceable, tier: T1}
    - {item_id: tranq_rifle, name: "issued tranquilliser rifle, two darts left", type: t1_tranq_rifle, condition: serviceable, tier: T1}
    - {item_id: field_kit, name: "field kit (radio, gloves, evidence bags, torch, two doses Class-A amnestic)", type: kit, condition: serviceable, tier: T1}
  item_points: {rank: working_adult, current: 60, max: 60}
  fighting_style: ["they're trying to kill us: pistols, shoot to stop them (Day 12, the deer)"]
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
index:
  npcs:
    rosa_delgado: "Rosa Delgado — handler; shot a buck off West"
    marisol_vega: "Agent Vega, NJ team — 'adequate'"
    stag_cell_leader_east: "Twelve-Point — the cell leader; escaped to the bogs"
  locations:
    cedar_run_curve: "the Cedar Run curve, Route 9 — the corridor broken"
    pine_barrens: "the New Jersey pine barrens"
  quests:
    A: "probation — Day 13 of 90"
    K: "the deer network — under way"
    K-2p: "the cell leader's corridor — broken; the leader escaped"
```

## Part B — capsule

capsule:
  save_round: 10
  delta_of: scp_class_of_99_v5_2   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    active_world_pressures.stag_network.state.marks :: R0: "Day 10 check advanced once (test fixture): pine barrens undercurrent tension −1"
    active_world_pressures.stag_network.track.pine_barrens.due :: R0: Day 15
    locations.cedar_run_curve :: R1: {name: "the Cedar Run curve, Route 9", zone: pine_barrens, conditions: {features: ["a two-lane highway bending through pines", "a sand pull-off", "evening rush traffic both ways", "a deer crossing sign full of buckshot"]}, challenge_band: {min: 3, max: 6, basis: "coordinated deer attacks on cars"}}
    locations.pine_barrens.undercurrent.tension :: R0: -1
    locked_case_truths.stag_case.state.tonight :: R2: "R2 the cell at the Cedar Run curve: two scout does on the far shoulder watching traffic; in the pines behind them Twelve-Point and five attacker bucks, waiting for the scouts' signal at the 18:15 rush peak"
    npcs.commander_lindqvist.state.due :: R0: A-1s Day 1 10:00 welcome talk (test fixture: done); Day 75 transfer decision
    npcs.dmitri_volkov.state.due :: R0: none (incidental; sparring done — test fixture)
    npcs.gus_pembroke.state.due :: R0: Day 16 morning fixes the Omega-99 office door and tells West a story about it
    npcs.leo_brandt.state.due :: R10: Ls Day 3 a late-night call; Ls Day 12 skipped cards night (West away in New Jersey; nobody noticed); L Day 29 copies the list if not helped
    npcs.marisol_vega.belongs :: R0: [foundation, foundation_nj_team]
    npcs.marisol_vega.capability :: R0: {overall_level: 5, skills: {field_investigation: T2, firearms: T2}}
    npcs.marisol_vega.character :: R0: dry, tired of deer, by-the-book on Ethics rules
    npcs.marisol_vega.depth :: R0: 1
    npcs.marisol_vega.drives :: R0: {fear: an Ethics Committee review, want: the network broken with no civilian hurt}
    npcs.marisol_vega.gender :: R0: woman
    npcs.marisol_vega.in_disorder :: R0: suffers
    npcs.marisol_vega.job :: R0: Foundation New Jersey team lead
    npcs.marisol_vega.name :: R0: Agent Marisol Vega
    npcs.marisol_vega.relationships.pc :: R8: {tie: "Omega-99's rookie on loan", attitude: "approving, dry", credit: ["spotted the cell before the rush (R2)", "chose to stop shooting and bring them in alive (R7)"]}
    npcs.marisol_vega.state.due :: R8: K-1s road watch; K-2p Day 12 19:40 took the three captured bucks into the van (the cell leader and two attackers escaped to the bogs); K-3 Day 15 evening watches the network's next corridor
    npcs.marisol_vega.state.plan :: R4: "K-2 follow the retreat with West, Delgado, Hollis and Diaz; capture where she can; she stays on the road with the van"
    npcs.marisol_vega.state.position :: R0: New Jersey pine barrens near Cedar Run
    npcs.marisol_vega.voice :: R0: flat Jersey deadpan
    npcs.nj_agents :: R4: {depth: 0, name: "Hollis and Diaz, Foundation NJ team", job: field agents, belongs: [foundation, foundation_nj_team], gender: men, character: "Jersey locals, deer-weary", manner: "chew gum, swear at pines", in_disorder: suffers, state: {position: "New Jersey pine barrens near Cedar Run", due: "none (incidental)"}, capability: {overall_level: 3, skills: {firearms: T1}}, carried: "pistols and one tranquilliser rifle between them"}
    npcs.priya_raman.state.due :: R0: none (incidental; showed West the van — test fixture)
    npcs.rosa_delgado.state.due :: R0: K Day 12 evening road watch on Route 9 with the NJ team; A Day 20 next assignment
    npcs.rosa_delgado.state.plan :: R6: "K get West out of the pines; capture the three downed bucks alive for Vega"
    npcs.rosa_delgado.state.position :: R0: New Jersey pine barrens near Cedar Run
    npcs.stag_cell_east_attackers.belongs :: R2: [scp_4968_c]
    npcs.stag_cell_east_attackers.capability :: R2: {overall_level: 2}
    npcs.stag_cell_east_attackers.character :: R2: commit and rarely survive
    npcs.stag_cell_east_attackers.depth :: R2: 0
    npcs.stag_cell_east_attackers.gender :: R2: male
    npcs.stag_cell_east_attackers.in_disorder :: R2: thrives
    npcs.stag_cell_east_attackers.job :: R2: the cell's rammers
    npcs.stag_cell_east_attackers.manner :: R2: stand too still in the trees
    npcs.stag_cell_east_attackers.name :: R2: five SCP-4968-B attacker bucks
    npcs.stag_cell_east_attackers.state.due :: R6: K-2 when the cell regroups at the bogs, the two left rejoin Twelve-Point
    npcs.stag_cell_east_attackers.state.position :: R2: New Jersey pine barrens near Cedar Run
    npcs.stag_cell_east_attackers.state.status :: R7: "three captured alive (R7): darted while down, wounds packed by Hollis and Diaz from the field kits (treatment — stabilised), legs hobbled; two still free with Twelve-Point"
    npcs.stag_cell_east_scouts :: R2: {depth: 0, name: "two scout does", job: "the cell's road watch", belongs: [scp_4968_c], gender: female, character: "flee and warn", manner: "heads up, ears turning to every engine", in_disorder: thrives, state: {position: "New Jersey pine barrens near Cedar Run", due: "K-1 Day 12 18:15 signal the rush"}, capability: {overall_level: 1}}
    npcs.stag_cell_leader_east.state.due :: R3: K-2f Day 12 18:15 the Route 9 hit (called off: seen and shot at, R3); K-2 Day 12 18:30 leads the cell back through the pines toward the bogs
    npcs.stag_cell_leader_east.state.plan :: R3: "withdraw the cell to the bogs; move the attack corridor away from the Cedar Run curve"
    npcs.stag_coordinator.state.due :: R0: Day 10 visited the new cell (test fixture: done); Day 15 evening next visit (cycle every 5 days)
    npcs.tomas_reyes_hart.state.due :: R0: none (incidental; report template given — test fixture)
    quests.buck_stops_here.parts.cell_leader.status :: R8: partly (R8: the Cedar Run corridor broken, three attackers captured; Twelve-Point escaped) → shown as K-2p
    quests.buck_stops_here.status :: R0: active (test fixture: Rosa assigned it Day 11; code K given; K-1 scouts and road watch under way)
    quests.orientation_week.status :: R0: succeeded (test fixture: the first week done)
    quests.probation.status :: R0: active
    world_state.material_history.r10_night :: R10: "R10 the night at the motel: a ranger stopped a bogged car on the sand road at midnight (the ordinary encounter; it passed West by); nerve day marks for Day 12: a day of fear −1 and a good rest +1 → no change"
    world_state.material_history.xp_the_three_attacker_bucks_beaten_in_the_scrub_oak_r5_r6 :: R6: XP paid for the three attacker bucks beaten in the scrub oak (R5–R6): 32
    world_state.pending.incident_report :: R9: "R9 Vega's incident report: three SCP-4968-B captured alive, two agents hurt, no civilian contact; Ethics will read the shoot decision"
    world_state.pending.network_warned :: R3: {what: "NO, AND (R3): the scouts carry it back — the network learns the Cedar Run curve is watched; the coordinator will move the next attack corridor", cause: "the missed dart", due: Day 15 evening}
    world_state.pending.pines_ambush :: R4: "R4 18:40: the track went cold in a stand of scrub oak; three attacker bucks came out of the dark at the pursuers; one hit West in the side (HP 12 → 7)"
    world_state.pending.pines_fight :: R5: "R5 18:41 first exchange in the scrub oak: West hit again (HP 2); Rosa and Hollis hit two bucks hard; Diaz knocked down and up again (HP 9)"
    world_state.pending.pines_fight_end :: R6: "R6 18:43: Rosa shot the buck off West; West rolled clear and stayed down; Rosa, Hollis and Diaz put all three attacker bucks down (HP 0) in two more exchanges"
continuity_status:
  degraded: ["R4–R6 no span was run during the fight; Twelve-Point's 18:30 move written as happened by its own logic (R8)"]
  corrected: ["R1: the GM passed arrived for a move inside the same zone, so the afternoon surface roll was made twice (both nothing)"]
  round0_revisions: []
  save_deferral: null
