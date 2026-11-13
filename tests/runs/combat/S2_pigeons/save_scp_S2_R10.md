# SAVE — SCP Class of '99 (combat test S2) R10

## Part A — readable

```yaml
background_ref: {id: scp_class_of_99_v5_2}
language: en
round: {last_completed_round: 10, saved_completed_round: 10}
world_state:
  location: oneida_lake
  time: {season: early spring, day_index: 7, date: '2026-03-08', clock_minutes: 390, daypart: morning, precision: exact}
  environment: {weather: grey, still, cold over the lake}
player:
  identity: {name: Sam West, age: 26 (born January 2000), origin: "United States; three years a patrol officer in Columbus, Ohio", history: ["recruited after an impossible call; finished the field-agent academy last week"]}
  appearance: "tall, lean, short black hair; a fresh stitched cut on the left cheek"
  archetype: field agent (probationary)
  job: Foundation field agent, Level 2, liaison to MTF Omega-99
  belongs: [foundation, mtf_omega_99]
  gender: man
  character: player-defined in play
  status: rested; Day 7 of probation
  skills:
    field_investigation: {class: NORMAL, tier: T1, evidence: 0, class_source: academy training, abilities: []}
    firearms: {class: NORMAL, tier: T1, evidence: 1, class_source: academy and prior service, abilities: []}
    cover_and_persuasion: {class: NORMAL, tier: T1, evidence: 1, class_source: academy cover-identity training, abilities: []}
    first_aid: {class: NORMAL, tier: T1, evidence: 0, class_source: academy, abilities: []}
  growth_period: {opened: 7, credited: []}
  progression: {system: numeric_level_xp, state: {level: 2, xp: 44}}
  condition: {hp: 12, nerve: {baseline: 1, current: 1, tension: 0}, conditions: [{condition: "beak cut across the left cheek, stitched", source: body, effect: "none on rolls"}], fatigue: rested, last_rest: "Day 6 night, with allies"}
  equipment:
    - {item_id: west_sidearm, name: 'Glock 19 he calls "Patience"', type: t1_pistol, capability_domain: firearms, condition: serviceable, tier: T1}
    - {item_id: vest, name: issued soft vest, type: t1_vest, condition: serviceable, tier: T1}
    - {item_id: net_launcher, name: issued net launcher (no nets left), type: t1_net_launcher, condition: serviceable, tier: T1}
    - {item_id: field_kit, name: "field kit (radio, gloves, evidence bags, torch, one dose Class-A amnestic left)", type: kit, condition: serviceable, tier: T1}
  item_points: {rank: working_adult, current: 60, max: 60}
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
index:
  npcs:
    rosa_delgado: "Rosa Delgado — handler; benched West after the fight"
    ada_okafor: "Sgt Ada Okafor, Gamma-119 — approving"
    jenna_kowalski: "Jenna Kowalski — sanctuary volunteer; amnesticised, remembers nothing"
  locations:
    oneida_lake: "Oneida Lake shore and the raptor sanctuary — the pigeons are gone"
  quests:
    A: "probation — Day 7 of 90"
    A-1s: "orientation week — done"
    Hs: "the Oneida Lake pigeons — 101 birds bagged"
```

## Part B — capsule

capsule:
  save_round: 10
  delta_of: scp_class_of_99_v5_2   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    active_world_pressures.pigeon_breakout.clock.due :: R9: none (stopped R9)
    active_world_pressures.pigeon_breakout.clock.filled :: R7: 1 (R7 20:00 check: two instances still free and recombining)
    active_world_pressures.pigeon_breakout.clock.opened :: R0: Day 6 08:00 (the team arrived; checks every 12 hours from 20:00)
    active_world_pressures.pigeon_breakout.state.current :: R9: stopped (R9): every instance and fragment accounted for — 41 + 22 + 38 birds bagged; count to be confirmed at dawn
    npcs.ada_okafor.belongs :: R0: [foundation, mtf_gamma_119]
    npcs.ada_okafor.capability :: R0: {overall_level: 5, skills: {containment: T2, firearms: T2}}
    npcs.ada_okafor.character :: R0: calm, birder's patience, hates waste
    npcs.ada_okafor.depth :: R0: 1
    npcs.ada_okafor.drives :: R0: {fear: a hawk-mix hatching on her watch, want: every instance and fragment accounted for}
    npcs.ada_okafor.gender :: R0: woman
    npcs.ada_okafor.in_disorder :: R0: suffers
    npcs.ada_okafor.job :: R0: MTF Gamma-119 team lead
    npcs.ada_okafor.name :: R0: Sergeant Ada Okafor
    npcs.ada_okafor.relationships.pc :: R8: {tie: "Omega-99's rookie on loan", attitude: "approving", credit: ["netted an instance alone (R5)", "the roost idea (R8)"]}
    npcs.ada_okafor.state.due :: R10: Hs Day 7 05:30 counted and handed the bags to the Site-19 courier; none (her part done; Gamma-119 returns to base)
    npcs.ada_okafor.state.plan :: R0: H sweep the shore and the sanctuary at dusk; net the fragments, tranquillise the large ones
    npcs.ada_okafor.state.position :: R0: Oneida Lake shore and a raptor sanctuary, New York
    npcs.ada_okafor.voice :: R0: quiet, exact, counts things out loud
    npcs.commander_lindqvist.state.due :: R0: A-1s Day 1 10:00 welcome talk (test fixture: done); Day 75 transfer decision
    npcs.dmitri_volkov.state.due :: R0: none (incidental; Day 4 sparring done — test fixture)
    npcs.gamma_team :: R0: {depth: 0, name: "Cole and Ruiz, MTF Gamma-119", job: "operatives", belongs: [foundation, mtf_gamma_119], gender: men, character: "veterans, bored by birds until they aren't", manner: "radio chatter and gum", in_disorder: suffers, state: {position: "Oneida Lake shore and a raptor sanctuary, New York", due: "none (incidental)"}, capability: {overall_level: 4, skills: {firearms: T2}}, carried: "tranquilliser rifles (sedate by dose and size, not HP), net guns"}
    npcs.gus_pembroke.state.due :: R0: Day 8 morning fixes the Omega-99 office door and tells West a story about it
    npcs.jenna_kowalski.belongs :: R1: [independent]
    npcs.jenna_kowalski.capability :: R1: {overall_level: 2, skills: {animal_care: T2}}
    npcs.jenna_kowalski.character :: R1: 50s, tough, talks to the hawks by name
    npcs.jenna_kowalski.depth :: R1: 1
    npcs.jenna_kowalski.drives :: R1: {fear: the barn owl getting sick again, want: the birds fed and safe}
    npcs.jenna_kowalski.gender :: R1: woman
    npcs.jenna_kowalski.in_disorder :: R1: suffers
    npcs.jenna_kowalski.job :: R1: volunteer at the raptor sanctuary
    npcs.jenna_kowalski.knowledge.beliefs.vests :: R1: "the men in vests are from the state wildlife office, about bird flu (the cover story)"
    npcs.jenna_kowalski.name :: R1: Jenna Kowalski
    npcs.jenna_kowalski.relationships.pc.attitude :: R6: neutral
    npcs.jenna_kowalski.relationships.pc.tie :: R6: none she remembers
    npcs.jenna_kowalski.state.due :: R10: Hs Day 7 06:00 fed the raptors; no memory of last night; Day 8 06:00 feeds the raptors again (her routine)
    npcs.jenna_kowalski.state.plan :: R6: "drives home 'tired'; feeds the birds at six tomorrow as usual"
    npcs.jenna_kowalski.state.position :: R4: Oneida Lake shore and a raptor sanctuary, New York
    npcs.jenna_kowalski.voice :: R1: brisk, upstate, no patience for men in vests
    npcs.leo_brandt.state.due :: R0: Ls Day 3 a late-night call (West slept through it — test fixture); L Day 12 skips cards night; L Day 29 copies the list if not helped
    npcs.priya_raman.state.due :: R0: none (incidental; Day 3 showed West the van — test fixture: done)
    npcs.rosa_delgado.relationships.pc.credit.r5 :: R7: "held the net alone with a cut face till she got there (R5)"
    npcs.rosa_delgado.state.due :: R3: Hs Day 6 evening worked the dusk sweep with West at the aviaries; A Day 10 next assignment
    npcs.rosa_delgado.state.plan :: R7: "H keep West at the truck with the bag and the radio; he's hurt"
    npcs.rosa_delgado.state.position :: R0: Oneida Lake shore and a raptor sanctuary, New York
    npcs.tomas_reyes_hart.state.due :: R0: none (incidental; Day 5 report template — test fixture: done)
    quests.orientation_week.status :: R0: succeeded (test fixture: the first week done)
    quests.pest_control.status :: R9: succeeded (R9) → shown as Hs
    quests.probation.status :: R0: active
    world_state.material_history.xp_quest_h_the_oneida_lake_pigeons :: R9: XP paid for quest H, the Oneida Lake pigeons: 44
    world_state.pending.amnestic_jenna :: R6: "R6 18:40 West gave Jenna Kowalski a Class-A amnestic in tea, with Rosa's say-so (Foundation witness protocol); logged for the incident report"
    world_state.pending.instance_1_captured :: R5: "R5 18:23 West netted the first instance point-blank; it burst into about forty pigeons inside the net and the net held them all (YES, R5)"
    world_state.pending.instance_fight :: R4: "R4 18:21 the instance came off the aviary roof onto West; he shot twice at arm's length and missed both; HP 5"
    world_state.pending.instance_to_sanctuary :: R3: {what: "an SCP-3683 instance (turkey-sized, level 4, man-sized for harm, bursts into pigeons when cornered or killed) lands on the red-tail's aviary", cause: "Gamma-119's sweep flushed it toward the sanctuary (NO, AND, R3)", due: Day 6 18:20}
  retired:
    npcs.jenna_kowalski.knowledge.facts.pigeons :: "amnesticised (R6): Class-A in thermos tea; she loses the last two hours"
continuity_status:
  degraded: []
  corrected: ["R3: Okafor's ask left out the zone point (−1); outcome unchanged", "R9: XP first typed 58 instead of the tool's 44; fixed before showing", "R10: Jenna's depth first lowered to 0; depth never goes down; removed"]
  round0_revisions: []
  save_deferral: null
