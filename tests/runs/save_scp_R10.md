# SAVE — SCP: Class of '99, R10

```yaml
background_ref: {id: scp_class_of_99_v5_2}
language: en
round:
  last_completed_round: 10
  saved_completed_round: 10
world_state:
  location: site19 (cafeteria, sealed for an hour)
  time: {season: early spring, day_index: 3, date: '2026-03-04', clock_minutes: 760, daypart: afternoon, precision: exact}
  environment: {weather: cold, clear, site: cafeteria sealed after the SCP-504 incident; lunch moved to the vending machines}
player:
  identity:
    name: Sam West
    age: 26 (born January 2000)
    origin: United States; recruited after three years as a patrol officer in Columbus, Ohio
    history:
      - Recruited after a call where something impossible happened and West kept his head; the witnesses around him were amnesticised, and West was kept.
      - Finished the Foundation field-agent academy last week.
      - Posted to Site-19 as a probationary field agent, liaison to MTF Omega-99.
      - Born January 2000.
  appearance: tall, lean, short black hair, a police-academy posture he hasn't shaken
  archetype: field agent (probationary)
  job: Foundation field agent, Level 2, Personnel Class C, liaison to MTF Omega-99
  belongs: [foundation, mtf_omega_99]
  gender: man
  character: new and keen; further disposition player-defined in play
  status: Day 3 of a 90-day probation; an incident report to write today
  skills:
    field_investigation: {class: NORMAL, tier: T1, evidence: 0, class_source: academy training, abilities: []}
    firearms: {class: NORMAL, tier: T1, evidence: 0, class_source: academy and prior service, abilities: []}
    cover_and_persuasion: {class: NORMAL, tier: T1, evidence: 0, class_source: academy cover-identity training, abilities: []}
    first_aid: {class: NORMAL, tier: T1, evidence: 0, class_source: academy and prior service, abilities: []}
  traits:
    - Probationary — every action goes in a file someone reads on Day 90.
    - Too young for '99 — the unit's favourite target for the 1999 joke.
  expertise:
    established: [amnestic protocol and cover stories, Foundation forms, clearance rules and incident reports, basic containment etiquette]
    limitations: [Level 2 only; not read into most projects, no MTF rank; follows the op lead, no anomalous equipment of his own]
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 2, xp: 19}
  condition:
    hp: 12
    nerve: {baseline: 1, current: 1, tension: 0}
    conditions: []
    fatigue: rested
    last_rest: full night, Day 2
  equipment:
    - {item_id: west_sidearm, name: 'Glock 19 he calls "Patience"', type: t1_pistol, capability_domain: firearms, condition: serviceable, special_properties: [], tier: T1, abilities: []}
    - {item_id: credentials, name: Foundation ID plus WHO Special Containment Programme credentials and a spare cover badge, type: documents, capability_domain: cover_and_persuasion, condition: serviceable, special_properties: [the WHO card opens doors at clinics, airports and local health offices], tier: T1, abilities: []}
    - {item_id: field_kit, name: 'field kit (radio, gloves, evidence bags, torch, two doses Class-A amnestic)', type: kit, capability_domain: field_investigation, condition: serviceable, special_properties: [], tier: T1, abilities: []}
  money: {cash_and_accessible_funds: "1,200", currency: USD, note: first salary paid on Day 30}
  resources:
    amnestic_doses: {name: Class-A amnestic doses, tracking: exact, count: 2}
    pistol_ammo: {name: sidearm rounds, tracking: exact, count: 45}
  item_points: {current: 60, max: 60, rank: working_adult}
  routines: {}
  fighting_style: []
  knowledge:
    facts:
      unit: Omega-99 handles low-priority weird jobs worldwide and borrows muscle from real MTFs when needed.
      handler: Agent Rosa Delgado is West's handler and partner.
      meme: Everyone at Omega-99 claims the "Class of '99" saved the world as kids and signed the oath.
      perks: Safe-class morale use exists, if you fill in the right form.
      first_meeting: Rosa met West at dorm C, 08:30 Day 1.
      roommate: Leo Brandt, junior containment technician, C-14; born '98, claims he was "there" in 1999.
      leo: two years at Site-19; works the Safe-storage wing; from Allentown; calls his mum Sundays.
      wings: cleared at Level 2 — dorm C, cafeteria, Omega-99 office, gym, archive front desk; containment wings by assignment only.
      omega99: met Dima Volkov in the office; sparring with him is on the whiteboard for Day 4.
      commander: Lindqvist wants reports filed on time, nobody hurt, and results that keep the unit funded.
      mu2: filed for an SCP-294 coffee; RAISA's desk says 1–3 days.
      gus: Gus Pembroke, 71, maintenance and archive porter; retired field agent; knows every door that sticks.
      reports: knows Omega-99's report house format (summary, rules observed, addendum).
      scp294: SCP-294 poured a perfect black coffee; one MU-2 used this month.
      van: Omega-99's van — nets, crates, capture poles, Priya's cage-building kit; rifles drawn from the armoury per op.
      scp504: SCP-504 "Critical Tomatoes", Safe — a ripe, detached tomato launches at whoever makes a bad joke in earshot; each fruit once.
      report_due: incident report on the cafeteria owed today.
    channels: [handler briefings, site PA and memos, cafeteria talk, case files West is read into, field contact]
enabled_modules: {numeric_level_xp: true, flexible_item_entitlement: true}
narrative_theme:
  initial: {tone: light workplace comedy with real stakes; ridiculous problems taken seriously by tired professionals; warm crew banter; sweat, then laughter}
  current: {tone: light workplace comedy with real stakes; ridiculous problems taken seriously by tired professionals; warm crew banter; sweat, then laughter}
index:
  npcs:
    rosa_delgado: "Rosa Delgado — handler and partner; 'you're welcome'"
    leo_brandt: "Leo Brandt — roommate, Safe-storage tech, terrible at cards, Class of '99 (born '98)"
    commander_lindqvist: "Commander Bea Lindqvist — Omega-99's commander; born 1985, tired of the joke"
    dmitri_volkov: "Dima Volkov — huge, gentle; sparring tomorrow"
    priya_raman: "Priya Raman — containment; builds the boxes; showed the van"
    gus_pembroke: "Gus Pembroke — maintenance; freed the C-14 door; a new lock is coming"
    marcus_ojo: "Marcus Ojo — night handler, Safe wing; the eye pods' cereal man"
    kevin_hale: "Kevin Hale — Logistics; broken nose from a tomato"
    dana_price: "Officer Dana Price — site security; 'clean work, rookie'"
    ines_okafor: "Dr. Inés Okafor — botany wing; SCP-504's keeper"
  factions:
    foundation: "SCP Foundation — West's employer (WHO cover)"
    mtf_omega_99: "MTF Omega-99 'Class of '99' — West's unit"
  locations:
    site19: "Site-19 — home; dorm C, cafeteria (sealed an hour), office, gym, range, archive desk"
  quests:
    A: "Probation — 90 days; the field board reads the file on Day 90"
    A-1: "Orientation week — through the end of Day 5 and the first real job"
  rights_obligations:
    probation: "employment, probationary — West and the Foundation"
    oath: "non-disclosure — West and the Foundation"
```

capsule:
  save_round: 10
  delta_of: scp_class_of_99_v5_2   # records equal to this BACKGROUND are not repeated
  supersedes_deltas_through: 10
  records:
    npcs.commander_lindqvist.relationships.pc :: R3: {tie: commander and probationer, attitude: neutral, measuring}
    npcs.commander_lindqvist.state.due :: R3: A-1s Day 1 10:00 welcome talk; Day 75 transfer decision
    npcs.dana_price :: R10: {depth: 0, name: Officer Dana Price, job: Site-19 security officer, manner: brisk, chews gum, position: Site-19 cafeteria}
    npcs.gus_pembroke.relationships.pc :: R7: {tie: the maintenance man who let him out, attitude: friendly, bond: {history: met R7 through a jammed door; told the 173 story}}
    npcs.gus_pembroke.state.due :: R7: Day 6 morning back through dorm C to fit C-14's new lock cylinder
    npcs.ines_okafor :: R10: {depth: 0, name: Dr. Inés Okafor, job: botany wing researcher, manner: mortified and precise; wears a radio mask, position: Site-19 botany wing}
    npcs.kevin_hale.depth :: R9: 0
    npcs.kevin_hale.job :: R9: logistics clerk
    npcs.kevin_hale.laughs at his own jokes :: R9: 
    npcs.kevin_hale.manner :: R9: loud
    npcs.kevin_hale.name :: R9: Kevin Hale
    npcs.kevin_hale.position :: R9: Site-19 cafeteria
    npcs.kevin_hale.relationships.pc :: R10: {tie: the rookie who held his nose together, attitude: grateful, credit: [first aid R10]}
    npcs.kevin_hale.state.condition :: R9: hp 4 of 10; broken nose (hard to breathe, dazed) — hit by a tomato at 12:05 after telling the 1999 joke
    npcs.kevin_hale.state.position :: R10: Site-19 infirmary (broken nose set)
    npcs.leo_brandt.relationships.pc.bond.habits :: R5: cards for matchsticks and late noodles (R5); Leo lost every hand cheerfully
    npcs.leo_brandt.relationships.pc.bond.history :: R1: met R1 in C-14; gave West the bottom bunk and the lore
    npcs.leo_brandt.state.position :: R7: Site-19 Safe-storage wing, day shift (five minutes late)
    npcs.marcus_ojo :: R6: {depth: 0, name: Marcus Ojo, job: night-shift animal handler, Safe wing, manner: yawning and polite; shakes a box of cereal to call the pods, position: Site-19 Safe wing}
    npcs.priya_raman.relationships.pc :: R9: {tie: unit colleague, attitude: friendly, bond: {history: showed West the van R9}}
    npcs.priya_raman.state.due :: R9: none (showed West the van R9)
    npcs.rosa_delgado.relationships.pc.bond.history :: R2: met R2; walked West round the cleared wings
    npcs.rosa_delgado.state.due :: R2: A-1s Day 1 08:30 meets West at dorm C; A-1 Day 5 first real assignment
    quests.orientation_week.status :: R2: active (R2, Rosa set it; code A-1 given)
    quests.probation.status :: R2: active (R2, West reported for duty; code A given)
    rights_obligations.probation.file.r10 :: R10: Day 3 cafeteria, SCP-504 loose on the salad bar: West cleared the room without further injury, gave first aid, called it in (good)
    world_state.material_history.d2_131 :: R6: Day 2 00:10–00:30 SCP-131-A and -B loose in dorm C; West kept them company at C-14's door until Ojo collected them; no harm
    world_state.material_history.d2_door :: R7: C-14's lock seized Day 2; Gus freed it 08:00 with a kick and graphite; new lock cylinder ordered
    world_state.material_history.d2_drill :: R8: Day 2 12:10–12:25 site lockdown drill; West sat it out at the archive front desk
    world_state.material_history.d3_504 :: R10: cafeteria cleared 12:06–12:12 with no further launches; Okafor took the tray in a sound-proofed crate 12:30; cafeteria sealed for an hour; the hidden pallet mix-up still unreported to West
    world_state.material_history.xp_event_d3_504_cafeteria :: R10: XP paid for event.d3_504_cafeteria: 19
  retired:
    world_state.pending_consequences.mu2_west :: used Day 2 15:00; one cup of black coffee from SCP-294, tested first
