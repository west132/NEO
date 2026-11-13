# SAVE — SCP Class of '99 (combat test S1) R10

## Part A — readable

```yaml
background_ref: {id: scp_class_of_99_v5_2}
language: en
round: {last_completed_round: 10, saved_completed_round: 10}
world_state:
  location: site19
  time: {season: early spring, day_index: 14, date: '2026-03-15', clock_minutes: 1435, daypart: evening, precision: exact}
  environment: {weather: cold, clear}
player:
  identity: {name: Sam West, age: 26 (born January 2000), origin: "United States; three years a patrol officer in Columbus, Ohio", history: ["recruited after an impossible call; academy; Site-19 probation"]}
  appearance: "tall, lean, short black hair"
  archetype: field agent (probationary)
  job: Foundation field agent, Level 2, liaison to MTF Omega-99
  belongs: [foundation, mtf_omega_99]
  gender: man
  character: player-defined in play
  status: bruised ribs; Day 14 of probation
  skills:
    field_investigation: {class: NORMAL, tier: T1, evidence: 0, class_source: academy training, abilities: []}
    firearms: {class: NORMAL, tier: T1, evidence: 0, class_source: academy and prior service, abilities: []}
    cover_and_persuasion: {class: NORMAL, tier: T1, evidence: 0, class_source: academy cover-identity training, abilities: []}
    first_aid: {class: NORMAL, tier: T1, evidence: 0, class_source: academy, abilities: []}
  growth_period: {opened: 0, credited: []}
  progression: {system: numeric_level_xp, state: {level: 2, xp: 50}}
  condition: {hp: 10, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [], fatigue: tired, last_rest: "Day 13 night"}
  equipment:
    - {item_id: west_sidearm, name: 'Glock 19 he calls "Patience"', type: t1_pistol, capability_domain: firearms, condition: serviceable, tier: T1}
    - {item_id: vest, name: issued soft vest, type: t1_vest, condition: serviceable, tier: T1}
    - {item_id: field_kit, name: "field kit (radio, gloves, evidence bags, torch, two doses Class-A amnestic)", type: kit, condition: serviceable, tier: T1}
  item_points: {rank: working_adult, current: 60, max: 60}
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
index:
  npcs:
    rosa_delgado: "Rosa Delgado — handler; noticed he holstered"
    leo_brandt: "Leo Brandt — roommate; the debt cancelled; sees the Commander at ten"
    felix_darrow: "Felix Darrow — MC&D junior, disowned, detained"
    dmitri_volkov: "Dima — first through the door"
  locations:
    trenton_storage: "Darrow's storage unit, Trenton — raided"
    site19: "Site-19"
  quests:
    A: "probation — Day 14 of 90"
    Ls: "Darrow's list — Darrow exposed, Leo's debt gone"
```

## Part B — capsule

capsule:
  save_round: 10
  delta_of: scp_class_of_99_v5_2   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    active_world_pressures.darrow_scheme.clock.due :: R8: none (stopped R8)
    active_world_pressures.darrow_scheme.clock.filled :: R0: 1
    active_world_pressures.darrow_scheme.state.current :: R8: stopped R8: Darrow detained and disowned; the debt cancelled
    locked_case_truths.darrow_case.evidence.laptop :: R6: "Darrow's laptop: emails to Pinnacle Recovery LLC's bank and to Brice; a draft memo to MC&D acquisitions he never sent; no MC&D sign-off anywhere — he is acting on his own"
    locked_case_truths.darrow_case.evidence.table_list :: R6: "a printed schedule of the Site-19 disposal contractor's truck runs (public bids), with Thursday 26 March circled; no item list yet — Leo never gave one"
    npcs.commander_lindqvist.state.due :: R10: Day 15 10:00 sees Leo Brandt about the debt and the broker; Day 75 transfer decision
    npcs.darrow_muscle.belongs :: R0: [mcd]
    npcs.darrow_muscle.capability :: R0: {overall_level: 3, skills: {firearms: T2}}
    npcs.darrow_muscle.carried :: R0: pistols each (one-handed class, 1d8 per shot)
    npcs.darrow_muscle.character :: R0: professionals; paid, not loyal
    npcs.darrow_muscle.depth :: R0: 1
    npcs.darrow_muscle.drives :: R0: {fear: a federal charge, want: the pay without the trouble}
    npcs.darrow_muscle.gender :: R0: men
    npcs.darrow_muscle.in_disorder :: R0: thrives
    npcs.darrow_muscle.job :: R0: ex-security, hired by the job
    npcs.darrow_muscle.name :: R0: Brice and Pell, Darrow's hired men
    npcs.darrow_muscle.state.due :: R2: Ls Day 14 19:30 at the unit with Darrow; none (incidental) after
    npcs.darrow_muscle.state.plan :: R0: L meet Darrow Thursdays; plan the disposal-truck hit
    npcs.darrow_muscle.state.position :: R0: Darrow's storage unit, Trenton, New Jersey
    npcs.darrow_muscle.state.status :: R9: "R9 Brice and Pell handed to Site-19 security with Darrow; held for questioning; amnestic and release after (Lindqvist)"
    npcs.darrow_muscle.voice :: R0: short, flat, ex-army
    npcs.dmitri_volkov.state.due :: R0: none (incidental; sparring done — test fixture)
    npcs.dmitri_volkov.state.plan :: R0: "L first through the door on the raid"
    npcs.dmitri_volkov.state.position :: R0: Darrow's storage unit, Trenton, New Jersey
    npcs.felix_darrow.state.due :: R8: L Day 15 morning questioned at Site-19, then handed back to MC&D under amnestic (Lindqvist's order)
    npcs.felix_darrow.state.plan :: R8: "keep his head down; get out of this without a record"
    npcs.felix_darrow.state.position :: R5: Darrow's storage unit, Trenton, New Jersey
    npcs.felix_darrow.state.status :: R8: "disowned by MC&D (R8); detained by the Foundation for questioning; signed Pinnacle's release of Leo's debt"
    npcs.felix_darrow.state.tonight :: R2: "inside unit C-17 with the roll-up door half open, a folding table, a laptop and a list of Site-19 disposal dates on it; Brice and Pell with him"
    npcs.felix_darrow.state.tonight_after :: R7: "R7 shown the unsent memo and told the Foundation is calling MC&D tonight: his fear (MC&D's seniors learning) is touched; settled — he starts bargaining before MC&D can answer"
    npcs.gus_pembroke.state.due :: R0: Day 16 morning fixes the Omega-99 office door and tells West a story about it
    npcs.leo_brandt.relationships.pc.attitude :: R10: "grateful, ashamed, owes him"
    npcs.leo_brandt.relationships.pc.credit.r10 :: R10: "West reported it properly and got the debt cancelled (R8–R10)"
    npcs.leo_brandt.state.due :: R10: Ls when Darrow is dealt with, waited up in C-14 (R10); L Day 15 10:00 sees Commander Lindqvist about his conduct
    npcs.leo_brandt.state.status :: R10: "the debt cancelled (R8); the Commander will see him in the morning"
    npcs.priya_raman.state.due :: R0: none (incidental; showed West the van — test fixture)
    npcs.ray_dumont.belongs :: R1: [independent]
    npcs.ray_dumont.character :: R1: bored, careful about his job
    npcs.ray_dumont.depth :: R1: 0
    npcs.ray_dumont.gender :: R1: man
    npcs.ray_dumont.in_disorder :: R1: suffers
    npcs.ray_dumont.job :: R1: night manager, Trenton self-storage
    npcs.ray_dumont.knowledge.facts.van :: R1: "a WHO public-health team watching for a gas leak in Row C; he's to keep quiet and stay in his office (West, R1)"
    npcs.ray_dumont.manner :: R1: flashlight in your face, clipboard in the other hand
    npcs.ray_dumont.name :: R1: Ray Dumont
    npcs.ray_dumont.state :: R1: {due: none (incidental), position: 'Darrow''s storage unit, Trenton, New Jersey'}
    npcs.rosa_delgado.relationships.pc.credit.r4 :: R9: "holstered and tackled an unarmed man instead of shooting (R4)"
    npcs.rosa_delgado.state.due :: R0: L Day 14 19:30 leads the raid on the storage unit; A Day 20 next assignment
    npcs.rosa_delgado.state.position :: R9: Site-19 Omega-99 office
    npcs.tomas_reyes_hart.state.due :: R0: none (incidental; report template given — test fixture)
    quests.darrows_list.route_taken :: R0: report it properly; raid the storage unit with Omega-99 (Lindqvist authorised Day 14)
    quests.darrows_list.status :: R8: succeeded (R8: Darrow exposed; Leo safe) → shown as Ls
    quests.orientation_week.status :: R0: succeeded (test fixture: the first week done)
    quests.probation.status :: R0: active
    rights_obligations.leo_debt :: R8: {type: "debt", parties: ["leo_brandt", "felix_darrow"], state: {status: "cancelled R8 — Pinnacle Recovery LLC's signed release, in Rosa's case"}}
    world_state.material_history.xp_quest_l_darrow_s_list :: R8: XP paid for quest L, Darrow's list: 50
    world_state.pending.brice :: R4: "R4 19:41 West holstered and tackled Brice under the roll-up door; they went down on the asphalt; Dima came out and sat on Brice; Brice gave up (HP 8)"
    world_state.pending.lindqvist_calls_mcd :: R8: "done 21:00: MC&D's liaison says no associate named Darrow was authorised for anything; they will 'review his employment'; the Foundation may keep him for questioning"
    world_state.pending.raid_entry :: R3: "R3 19:40 Dima went under the roll-up door shouting Federal agents, Rosa behind him; NO, BUT (ask): neither man drew — Pell put his hands up; Brice dropped his gun and ran for the door, where West stands"
  retired:
    npcs.felix_darrow.state.offer :: accepted in part by Lindqvist: the debt release and the laptop; no promise about what MC&D is told
continuity_status:
  degraded: []
  corrected: []
  round0_revisions: []
  save_deferral: null
