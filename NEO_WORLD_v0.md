# NEO WORLD — v0

What exists. Two files share this one schema:

- **BACKGROUND** — the world at Round 0: the setting, the people, the places, the PC, and every truth already fixed before play. Once play begins it is history; it never changes.
- **SAVE** — the same world later: a readable part for the player, plus a capsule of every record that now differs from the BACKGROUND (§18). The BACKGROUND supplies the rest on load, so both travel together.

Field names are the same in both, so nothing is translated between them. Fill in only what the game uses. Never create an empty category to satisfy the template, and never grant unstated capability, gear, or connections because they might be useful later.

```text
PARTS  0 design logic · A frame · B situation · C people · D places · E player ·
  F opening · G records and changes · H the save
BUILD  generating a background, or reworking one for complex quests and stories:
  the procedure is GM §7.1; Part 0 runs before Parts B–C
READ   the GM reads facts only from here (BACKGROUND + newest SAVE + the GM-Δ blocks
  since); never from memory of earlier turns
```

---

# PART 0 — DESIGN LOGIC

## 0. Generating or reworking a background

```text
USE  generating a background, or reworking one for complex quests/stories;
  authored facts and `requested` items stay fixed: this shapes only what the
  GM fills in
ORDER  1 build the hidden reality first (§0.1)
  2 let complexity emerge from independently motivated actors (§0.2, §0.3)
  never start by deciding how many twists, conspiracies, or false leads the PC
  must meet
  3 shape it into storylines (§0.4) and quest spines (§0.5), then the player and
  the opening
TEST  the design yields several plausible explanations, independently motivated
  NPCs, genuine connections, and consequences that continue even if the PC
  misunderstands everything; false connections are required only when M4 is
  picked (§0.2 APPLY), else only where they arise naturally
```

### 0.1 Hidden reality to establish

```text
D1 WORLD FACTS  what happened, in time order, incl. genuine causal links and
  which events are NOT linked → §9 cause/prior_events, §15 material_history
D2 ACTOR STATE  each NPC/faction: objectives, knowledge, beliefs, false beliefs,
  secrets, resources, current plan → §11, written by depth: the want the PC can
  push on, the fear, the line they won't cross, the secret with its own ordinary
  reason; for those the story turns on, the pull that fights the want and the
  belief that isn't true; and a voice for anyone who speaks
D3 EVIDENCE PROVENANCE  each clue: the thread it came from, what it actually
  establishes, which readings it does NOT establish → §9 evidence
  check per clue: evidence | objectively true | plausible reading
D4 INDEPENDENT TIMELINES  what each actor does if the PC never intervenes; every
  step carries a due, so the world never freezes around the PC → §11 state,
  §8 track or clock
D5 INTERACTION POINTS  where threads can collide, where they stay separate, how
  one actor's move changes another thread → §8 pressures (actors, trajectory)
D6 CONSEQUENCES  what changes when the PC acts, incl. acting on a wrong belief
  → §11 state (if blocked), §8 on_step / on_fill
D7 INFORMATION BOUNDARIES  what may be revealed, what particular NPCs do not know,
  what must not be invented as established history → §11 knowledge, §15 hidden
LIMIT  D1–D7 are the information a complex background needs to simulate
  consistently, not seven more systems for every story; fill only what it uses
```

### 0.2 Mystery principles

```text
COUNT  new background: tool `roll 1d5` + 4 = N (5–9) principles
PICK  new background: tool `roll 1d9` until N distinct numbers → M#; never
  pick by habit · reworking an existing background: no dice; pick the
  principles that fix what it lacks · record in §1 design_logic
WEIGHT  new background: tool `roll 1d3` = W (1–3); roll among the picked until
  W distinct → weighted M#; reworking: weight by need · record in §1 design_logic
APPLY  picked = applied meaningfully, not merely mentioned; weighted = the
  background is built around them; unpicked may appear naturally, never as
  extra requirements
FLOOR  M2 objective truth and M5 independent motives hold in every background
  whatever is picked: the pick sets emphasis, never which part of objective
  reality or world consistency may be skipped
LOW N  never compensate with more conspiracies, false leads, connections, twists
```

```text
M1 STRUCTURED CHAOS — no mandatory pattern
  world may hold any mix: independent events, connected operations, large
    conspiracies, personal agendas, coincidences, opportunistic interventions
  no master conspiracy required; a large conspiracy equally valid
  some events wholly unrelated; others form long cause-and-effect chains
  a connection may be unintentional: two people may shape each other's lives
    without knowing the other exists
  whoever appears behind events may have created them, exploited them,
    contributed by accident, or only seen an opportunity others missed
  an insignificant NPC may understand part of the situation better than those
    involved and make a small intervention for personal gain
  a victim may manipulate events, exploit assumptions, hide an agenda, or cause
    further consequences; victim in one situation ≠ whole role in the world
  no predetermined pattern of conspiracy, innocence, guilt, or interconnectedness
  chaos ≠ arbitrary: independently motivated people and events interact, producing
    consequences nobody intended or fully understands

M2 OBJECTIVE TRUTH vs SUBJECTIVE BELIEF
  background fixes: what happened; which events/operations connect and which do
    not; each NPC's motives, actions, knowledge, beliefs, misunderstandings; what
    each intends, knows of the wider situation, merely assumes; which
    consequences have occurred and which remain possible
  PC has none of it by default: finds evidence in play, builds own explanation —
    correct, partly correct, joins separate events, misses a real link, or unresolved
  NPCs also act on incomplete information: misread events, misjudge people, act
    on false assumptions, or see a pattern without its significance
  truth stays fixed; no character is required to understand it correctly

M3 NO AUTHORIAL CORRECTION
  a mistaken theory never triggers a quest to uncover the truth
  no NPC appears merely to explain the correct answer
  the world never rearranges events to validate the PC's assumptions
  PC acts on a wrong belief → world responds to the action and its actual consequences
  PC may succeed, fail, harm the wrong person, help an unexpected beneficiary, or
    reach the objective for reasons they misunderstand
  wrong interpretation = legitimate outcome, never a failed puzzle state
  author controls established reality and consequences, never what the player
    must conclude

M4 EVIDENCE COLLISION — true clues, false connections
  each thread has genuine facts and evidence from its own events
  evidence from different threads may overlap in time, place, people, objects, or
    apparent motive → a convincing explanation that is wrong
  e.g. A and B genuinely connected; A and C unrelated despite matching evidence;
    D exploits the A/C confusion without causing either
  an NPC may lie for a personal reason unrelated to the main investigation
  a suspicious action may be ordinary; an innocent-looking one may hide a real offence
  strongest misdirection uses no fabricated evidence: real evidence read through
    incomplete understanding (TRUE A + TRUE B + TRUE C, never TRUE A + fake clues
    + final reveal)
  a later discovery may recast an earlier scene, show apparent accomplices never
    knew each other, or show the blamed person only took advantage
  the player may be right on individual facts, wrong on how they relate

M5 NPCs AS INDEPENDENT ACTORS, NOT MYSTERY CONTAINERS
  lives, priorities, relationships beyond the PC's investigation
  most NPCs need no secret, crime, or betrayal to justify existing
  concealment is often ordinary: privacy, shame, love, family duty, promises,
    money, fear of being misunderstood
  some genuine wrongdoers; others victims, witnesses, bystanders, opportunists,
    people caught in circumstances they do not understand
  roles overlap: a victim deceives, a wrongdoer helps sincerely, a bystander
    becomes decisive through one small intervention
  a clever NPC may exploit events they did not create, redirecting a thread,
    intensifying a conflict, or causing consequences far beyond their intent
  cleverness, information, and importance are unequal
  behaviour follows actual motives and knowledge, never a need to provide clues
    or sustain the mystery
  not everyone suspicious · not everyone innocent · not everyone secretly connected

M6 COMPLEXITY THROUGH INTERACTION, NOT MANDATORY LORE
  each thread understandable alone; their interactions may become very complicated
  sources: several genuine wrongdoers with different objectives · independent
    events overlapping in time and place · partial conspiracies, competing
    factions, conflicting loyalty chains · victims, witnesses, bystanders deciding
    unexpectedly · opportunists exploiting what they did not create · coincidences
    resembling coordination · NPCs acting on different versions of the truth ·
    small decisions with unforeseen consequences
  a thread needs no elaborate history to have complicated consequences
  may draw on novels, films, games, written stories: study how their characters,
    motives, evidence, and events interact; never just borrow a familiar
    conspiracy structure
  not maximum complexity everywhere: complexity where the story benefits

M7 DRAMATIC IRONY AND UNRESOLVED OUTCOMES
  the full truth is not needed for a satisfying story
  the PC may: hold a confident wrong conclusion and live by it · catch one
    wrongdoer and miss another · uncover a real conspiracy only partly · see
    someone escape suspicion through a convincing alternative explanation · keep
    a leftover detail that contradicts their theory, never explained · meet a
    late reveal that recasts an earlier scene without invalidating what they found
  unresolved ≠ missing content: limited knowledge, unfinished events, a world
    continuing beyond the PC's understanding
  an ending may settle the immediate objective while the larger situation stays
    misunderstood or incomplete

M8 MULTIPLE ROUTES THROUGH THE SITUATION
  investigation is not the only valid approach: investigate, negotiate, deceive,
    cooperate, withdraw, confront, fight
  each approach yields different consequences and different access to information
  combat never turns into an investigation quest afterwards: the PC may beat the
    threat without understanding the wider situation, destroy a chance to learn,
    or solve the immediate problem while other threads continue
  the world responds to what the PC does; never forces a play style back onto the
    intended mystery path

M9 CORE PHILOSOPHY
  background = what is true · simulation = what happens as independent actors
    pursue their objectives · PC = what they believe happened; the three may stay
    different
  design question: can a believable world of independently motivated people,
    genuine connections, unrelated events, deliberate conspiracies, coincidences,
    and unexpected interventions leave the player to build an explanation from
    incomplete truths?
  the answer must not depend on one mastermind, many conspirators, or none
  defining quality: structured chaos — real facts, understandable motives, no
    guarantee they form a simple, complete, or correctly understood picture
```

### 0.3 Lenses for romance, combat, factions

```text
ROOT  as in M2: separate the shared event from each party's own reading of it
WHEN  a lens applies only where the background holds that domain; its patterns
  are options — use those that fit, never all; record lenses in §1 design_logic
```

```text
ROMANCE — two people live different love stories
  a relationship is not one progress bar shared by two people: each holds their
    own meaning of it → keep each direction in its own §11 relationships entry
    (its own bond); never mirror one side onto the other
  patterns: one sees it as casual, the other as meaningful · real care, incompatible
    futures · an NPC falls for the PC for reasons the PC does not understand · an
    NPC rejects the PC despite genuine affection · a moment meaningful to one is
    ordinary to the other · one dimension improves while another deteriorates
    (trust grows while attraction fades)
  yields unexpected romance, misunderstanding, incompatible desires, relationships
    that never resolve neatly
  there is no romance rule: it plays out through attitude, bond, drives,
    and the actor's own choices

COMBAT — winning the fight ≠ winning the situation
  a fight is one event inside the world, not an isolated victory/defeat encounter
  each participant has their own objective and own meaning of winning → §11
    state (plan), drives
  patterns: the opponent is delaying, not trying to defeat · win the fight, lose
    the objective · a defeated enemy achieved their goal before the fight began ·
    combatants define winning differently · a third party exploits the fight
    without joining it · the opponent was protecting something, pursuing an
    unrelated aim, or acting on incomplete information
  physical outcome never decides strategic outcome; each participant judges the
    same fight separately
  combat creates story, not only resolves obstacles

FACTIONS — nobody controls the organisation as completely as they think
  faction = official objective (§11 factions drives) + members with their own
    interests, incomplete information, varying loyalty (§11 npcs, belongs)
  an organisation is not a single character: its actual behaviour emerges from
    people who may agree on the objective and disagree on everything else
  patterns: a leader's order is interpreted differently by subordinates · two
    members follow the same order for different reasons · a subordinate achieves
    the objective while undermining the leader · an internal dispute accidentally
    benefits a rival · the faction succeeds at its stated goal while damaging the
    reason it exists
  yields political intrigue, faction war, betrayal that arise organically
```

### 0.4 Story shape

```text
CAMPAIGN  premise + question (§7) first: what this campaign is about, one line
  each; every storyline bears on the question or on the PC's own life; one that
  touches neither is cut; background is 1 big quest → question = its spine (§0.5)
SITUATION, NOT PLOT  write what each actor does if the PC never acts (D4); never
  a sequence of scenes the PC must walk through
STORYLINE  one reality, understandable alone (M6): its truth (§9), its actors (§11),
  its pressure (§8), its routes; indexed in §7
ROUTES  a case tied to a quest: ≥3 (RULES §15.6 SOLVABLE) · other storylines:
  whatever routes their own facts give, no minimum; never invent routes or
  connections to reach a count
SCALES  one main storyline: slow, weeks to months · local storylines: days ·
  ordinary lives: no pressure needed (M5: most storylines are ordinary lives)
VISIBLE STEPS  each pressure stage leaves a sign someone in the world could notice
  (a rumour, a changed place, a person acting differently): a track through its
  zone's signs (RULES §15.4 SIGNS), a clock through its stages (RULES §15.5)
STORY ENGINE  how work and trouble keep reaching the PC: work sources with a pace
  (§11), the main case's leads, the PC's own people
MAIN LINE  the main quest (§8) opens as a simple, ordinary job; what it opens into
  lives in its truth and actors, never in pre-written segments
OWN PEOPLE  the PC has a life, not only contacts: a few people they share history
  with (family, old friends, a mentor, an ex), each with a bond (§11)
```

### 0.5 Quest spine

```text
SPINE  every quest the PC enters has exactly 1 spine; PC role stays free: the
  spine attaches to the quest, never the PC
PARTS  question: 1 question or goal statable in one sentence
  stake: why this PC cares → stake_hooks, one per likely PC role; GM attaches
    the fitting hook when the PC enters the quest
  pressure: moves by the world's own logic (D4); never an imposed timer or countdown
  end: visible end point; done may arrive with the truth still unclear (M7)
SCOPE  background is 1 big quest → 1 spine for the whole background (Die Hard,
  Jaws) · main + side main quests → each quest its own spine (The Witcher 3,
  Red Dead Redemption 2)
SOURCE  copied/modified story → take that story's spine; change it only as far as
  the modifications require · original → generate topic options on the spot,
  tool roll among them, build the spine from the result; topic = a real fact,
  a mode (tone: comedy, dread, …), or a rule · record in §1 design_logic
BUILD  write the spine from this background's own world first; only then check
  it against the reference works for structure; references show structure only:
  never reuse their plot, characters, setting, or spine
TRANSPLANT  works unchanged in another setting, or reads like a reference with
  names swapped → discard, build again
THREADS  hang on the spine, never replace it: many threads, 1 spine per quest
HIDDEN  spine lives in the quest record (§8); the player-facing hook is written
  separately and never reveals locked truth
```

---

# PART A — FRAME

## 1. Identity and provenance

```yaml
background_id:        # required; every save's background_ref points here
provenance:           # authored | generated | mixed
requested: []         # generated or mixed: what the person asked for, in their terms
design_logic:         # Part 0 only: {mystery: {rolled_n: , picked: [M#], weighted: [M#]}, spine_topic: , lenses: [romance|combat|factions]}
chapter:              # campaigns played in chapters only: {campaign: , n: , previous: <background_id or none>, end: }
replaces: {}          # only for a setting with its own system: {<rules part>: <this background's rule>}
```

`authored` means the person wrote all of it: every fact is theirs and only they change it. In a `generated` or `mixed` background, `requested` lists what the person actually asked for — those facts are fixed like authored ones. Everything else was filled in by the GM and is provisional until play establishes it. Record requests as the person gave them; do not widen them.

`chapter.end` is where this chapter breaks (a day, an arrival, a quest's close). A chapter N+1 background is written from the previous chapter's final state: its carried records are established Round 0, only its new content is provisional, and the previous chapter's closed business sits in `world_state.material_history` as `chN:` lines.

`replaces`: a setting with its own system for a part of RULES (a sanity system, a magic system) names it here; that rule replaces the RULES part, never runs beside it.

## 2. Setting

```yaml
setting:
  world:
  era:
  starting_region:
  mode:                 # canon | historical | original | alternate
  canon_scope:          # canon: history before the start is fixed; after it, canon's
                        # main course is the actors' default plans (Canon course)
  allowed_deviations:   # what play may change; no canon outcome is protected
```

### Canon course — only when `mode: canon`

The bones of the main quest and major questlines, written as the plans of the actors who drive them: settled intent, not scenes, dates, or outcomes. Each step needs its actors' knowledge, means, and time; play can delay, divert, or end any of them. Anything this file leaves out comes from the game or source itself.

```yaml
canon_course:
  beat_<n>_<name>:
    opens:              # the event that opens it ("beat_1 closed", "the Rooks hold 2 boroughs"); a Day only for the opening
    quest: []           # the quest(s) that record it: blocked until it opens, closed when they close
    <actor_or_group>:   # what each side does in this beat, in order
  later_steps:          # optional: "as in the game — …"
  timed_plans:          # optional: plans that run on their own dates whatever else happens
```

## 3. Setting anchors

Record only the anchors needed to stop incompatible generation. Every new setting element in play must trace back to one of these, to recorded canon, or to in-world development (I3); what none of them settles is developed by GM §7.5.

```yaml
setting_anchors:
  peoples_or_species: []
  powers_or_supernatural_rules: []
  technology: []
  institutions: []
  religions_or_beliefs: []
  economics_or_trade: []    # incl. a price list of everyday goods, services, and wages
  economy_model:            # real economy that prices off the list follow, e.g. "English market town c. 1450, copper bit ≈ penny"
  tool_prices: standard     # standard | cheap: cheap where the setting runs on tools and kits (RULES §14)
  law_and_social_structure: []
  creatures_or_threats: []
  norms:
    law_and_outlaws: []     # whom the law protects; what people care about; what counts as cruelty here
    morale:                 # how readily each common kind of combatant breaks (RULES §8)
      kind_of_combatant:
    usual:                  # optional: where this setting's "usual" differs from the real world's (e.g. movie logic: police bribable, nobody official arrives in time)
  mp_powers:                # only if the setting has MP-drawing powers (RULES §5)
    draws_mp: []
    recovery:               # fast | slow | rest_only
    notes:
  horrors: []               # optional: {what: , base: , marks: <low>/<high>} (RULES §11)
  undercurrent_pool:        # only if the setting has a hidden layer
    sign: []
    brush: []
    incident: []
    hostile: []
```

`norms` holds the setting's own standards where they differ from a generic modern sense of right, how readily each common kind of foe breaks, and what counts as usual here. Morale is settled from these, never rolled; without an entry, self-preservation decides.

`tool_prices: cheap` makes item-point tools and kits cheaper where the setting runs on them; weapons and armour cost the same everywhere.

`undercurrent_pool` is what the hidden layer does when a contact roll comes up, by result: `sign` is wrongness a local would misread, `brush` is contact without harm, `incident` is something happening to someone, `hostile` is it acting against those present. Write them from the setting's own hidden things, never generic monsters.

### Calibration notes — optional

```yaml
skill_tiers:          {T1: , T2: , T3: , T4: }
class_sources:        {ELITE: , LEGENDARY: }
equipment_tiers:      {T1: , T2: , T3: , T4: }
weapon_and_armour_classes: {}
```

## 4. What this campaign depicts

```yaml
content_bounds:
  depicts: []
  excludes: []
  notes:
```

## 5. Modules

```yaml
enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true
```

Every module is on unless set false here; turn one off only when the campaign does without it. A save preserves the setting and never changes it.

## 6. Presentation

```yaml
narrative_theme:
  initial: {tone: , style: }
  current: {tone: , style: }
```

A style seed only: it never adds facts, and the initial theme never regenerates on reload. Tone comes from here, never from the GM's mood.

---

# PART B — THE SITUATION

## 7. Campaign premise

```yaml
premise:              # one line: who the PC is, where, and the situation they are in
question:             # one line: what play will answer; never a promised outcome
storylines:           # index only, never an owner
  storyline_id:
    kind:             # main | side | ordinary_life | wrongdoer
    line:             # one line: what is really going on in it
    refs: []          # owner paths: quests.<id>, locked_case_truths.<id>,
                      # active_world_pressures.<id>, npcs.<id>, factions.<id>
```

`premise` and `question` are design notes, not facts and not a content promise: no arc is protected. A storyline's status lives at the owners it points to and never in this index, which play never changes. Each storyline keeps its own cause-and-effect line; where two collide is recorded at the pressures (§8 actors, trajectory), never by merging them here.

## 8. Quests, threads, pressures

```yaml
quests:
  quest_id:                        # a stable id; the player-facing code (A, A-1, A-B)
                                   # is given only when the PC takes it on (RULES §10)
    objective:
    source:                        # who offers or requires it
    spine: {question: , stake_hooks: {<role>: <hook>}, pressure: , end: }   # GM truth (§0.5)
    hook:                          # player-facing; never reveals locked truth
    level:                         # its fixed challenge (RULES §10 LEVEL)
    status:                        # Round 0: available | blocked; in play: active |
                                   # succeeded | partly | failed | abandoned
    trigger:                       # blocked only: the event that opens it
    parts: {}                      # optional: {part_id: {objective: , level: }}
    routes: []                     # a case tied to it: ≥3 ways in (RULES §15.6)
    support_refs: []
development_threads:
  thread_id: {direction: , origin: , state: , status: }   # a player-development direction

active_world_pressures:
  pressure_id:
    name:
    origin:
    state: {}
    actors: []
    trajectory:                    # expected direction if conditions continue, not a locked future
    track:                         # bound to zones: one entry per zone it moves
      zone_id:
        layer:                     # surface | undercurrent
        direction:                 # destabilising (default) | stabilising
        pace:                      # every <interval> while <condition>
        due:                       # first check time; a pressure always has one
        on_step: {}                # {<step>: <what the world does when the layer reaches it>}
    clock:                         # bound to no zone (a plan, construction, research, a tally)
      {segments: , filled: 0, pace: every <interval> while <condition>, due: <first check time>,
       on_fill: , stages: {early: <segments>, late: <segments>}, signs: {early: , late: }}   # stages optional
    discovered_information: {}
```

A pressure gets a `track` when it plays out in places (a spreading cult, a weakening seal, gang war in a ward): each advance is one mark on that zone's tension, so the zone's stability is its progress, and `on_step` says what happens when the layer reaches a step. It gets a `clock` when it is bound to no place (a rival's plan, a ritual's preparation, a debt paid down), or when it is a short emergency paced in hours or days, faster than a zone can move. A count toward a target is a clock at the owner that wants it, not a separate record. Never both a track and a clock for one zone.

Set `pace` so the whole span fits the process: a world-scale pressure moves in weeks or months, never one advance a night. A zone moves at most one step a week and a step needs 3, 5, or 6 marks. `on_step` and `on_fill` are what the world does if nobody interferes, never an event aimed at the player. Every stage leaves a sign someone in the world could notice. Zero pressures is valid.

A development thread is a direction the player's character is growing in, from explicit intent or recorded history. Setting lore, perks, rumours and other flavour are not threads. A score kept on a faction or deal is not a record either: standing lives in each actor's credit and grievance (§11).

## 9. Hidden truth at Round 0 — optional

A campaign that begins with something already true and unknown records it here. It is hidden state from the first round: it belongs in the capsule, never in the readable save.

```yaml
locked_case_truths:
  case_id:
    cause:
    prior_events: []
    state: {}
    evidence: {}
    trajectory:
    discovered_information: {}
```

A suspicion someone holds at Round 0 lives in that actor's `knowledge.suspicions` (§11).

Commit the cause here and the evidence follows from it. Never write evidence whose cause is left to be decided later. Each case tied to a quest lists its routes on the quest (§8).

## 10. Ending conditions — optional

```yaml
ending_conditions:
  core_conditions: []
  hidden_conditions: []
  closed: []                       # permanently unreachable
```

Open-world play needs none. A chapter's `chapter.end` is one of these. Committed before the decisions they govern, never rewritten after player choices.

---

# PART C — PEOPLE

## 11. Actors and factions

Order: the PC's own people → work sources → storyline actors → factions.

### Depth

Every NPC has a depth. It sets which fields they carry; never how much they matter to the story.

```text
0 PASSER-BY      name, job, one manner line; not recorded unless play makes them
                 matter
1 REGULAR        + want, fear, voice
2 SUPPORTING     + line, an ordinary secret, ties (relationships, bond)
3 STORY-TURNING  + pull, belief; plan and due; knowledge
UP     an NPC rises when the record shows they matter more: a tie with the PC, a
       role in a quest, pressure or case, a deal; new fields are developed once
       (GM §7.5), then fixed
NEVER  moves down; a dead or departed NPC keeps the record (witnesses, grudges and
       knowledge outlast them)
START  the BACKGROUND sets each NPC's depth; an NPC first met in play starts at 0,
       or 1 if they will clearly be seen again
IMPORTANT  (must always have a due) read from the newest save, never from the
       BACKGROUND alone: a relationship with the PC (credit, grievance, bond), a
       role in a quest, pressure or case, or a deal with the PC
```

```yaml
npcs:
  npc_id:
    depth:                         # 0 | 1 | 2 | 3
    name:                          # name, job, belongs, gender, character are required;
    job:                           # use unknown where it is not established
    belongs:
    gender:
    character:                     # personality: what kind of person they are
    manner:                        # depth 0: how they come across, one line
    voice:                         # depth 1+: how they talk — words, rhythm, habits, what they avoid saying
    in_disorder:                   # thrives | suffers | neither (RULES §9.1 ZONE)
    state: {}                      # status, position, current HP/MP when below max, nerve when it
                                   # matters, plan, due (a time or a trigger), what they do if blocked
                                   # work source: routines: {work_source: {pace: , kinds: []}}
                                   # joined the PC: aim: {row: own | adopt | none, mode, want, split}
    drives:
      want:                        # depth 1+: the one plain thing they want; what the PC can push on
      fear:                        # depth 1+: what they dread
      line:                        # depth 2+: what they won't do; crossing it is possible, at a cost
      pull:                        # depth 3: a second want that fights the first; both can't be had
      loyalties: []
      values: []
    secret: {what: , why: }        # depth 2+: what they hide and their own ordinary reason
                                   # (privacy, shame, love, money, fear); usually not the case at hand
    relationships:
      toward_id: {tie: , attitude: , credit: [], grievance: [], believes_identity: ,
        bond: {history: , means: , habits: , wants: , unsaid: }}
    knowledge:
      facts: {}
      beliefs: {}                  # depth 3: what they believe that isn't true
      channels: []
      suspicions: {}               # {description, concerns_act, attached_to}
    capability: {}
    discovered_information: {}

factions:
  faction_id:
    name:
    role:
    in_disorder:
    state: {}
    drives: {}
    relationships: {}
    knowledge: {facts: {}, channels: []}
    capability: {}
    discovered_information: {}
```

`in_disorder` says how a zone's disorder bears on this actor's plans: `thrives` for those who work against order (gangs, smugglers, predators, cults), `suffers` for those who rely on it (watch, courts, merchants, healers, guild offices), `neither` for the mixed or indifferent. It is the actor's relation to order, never a judgement of good or bad. Write `position` as a recorded location's name where the actor is at one, so the tool can find the zone.

`character` is who they are; `voice` is how they sound. Keep them apart: a line of personality is played as behaviour, a line of voice as speech. A character from a source (a game, a film, history) is played as that source made them: voice, manner, competence.

`want` is kept plain: complexity lives in `pull`, `beliefs`, `secret` and `line`, not in a tangled want. `secret.why` is recorded before any lie that protects it: an NPC lies, evades or over-helps only for a recorded reason, never to make or keep a mystery.

`attitude` is a few plain words; a first meeting starts neutral unless state says otherwise, never friendly by default. `credit` is what the other party did for this actor; `grievance` is what this actor holds against them. `believes_identity` holds a false or partial belief about who someone is. A canon actor's canon plan goes in `canon_course`, not here.

`bond` is what the relationship is to this actor, this side only, never mirrored onto the other: `history` what they have been through together, `means` what the other is to them, `habits` how they are together (names, banter, rituals, small care), `wants` what they want from it, `unsaid` what they feel or hide and do not say. Fill it for the PC's own people and anyone the relationship matters to. A familiar actor meets the PC from it, never as a stranger; it plays the scene and never counts in dice.

A `due` is a clock time, or a trigger written as an event ("when …") the tool can list (RULES §15.1 PLAN, ALWAYS). A work source (fixer, guild, employer, patron) carries its `pace` in `state.routines.work_source`, else it is checked weekly.

---

# PART D — PLACES

## 12. Locations

```yaml
locations:
  location_id:
    name:
    conditions: {}
    challenge_band: {min: , max: , basis: }
    zone:                                              # a building or room: the zone it sits in; then no stability of its own
    surface: {baseline: , current: , tension: 0}       # −3..+3; stepped is set in play
    undercurrent: {baseline: , current: , tension: 0, sites: [], hours: , nature: }   # none..−3; omit if none
    cover:                                             # actor id holding the surface over the hidden; omit if none
    closed:                                            # optional: why it can't be entered and until when
    encounters:                                        # what the surface roll draws from here
      hostile: []
      ordinary: []
```

A band constrains what causes can plausibly exist in a place; its `basis` says why. `surface` is how the place behaves openly, `undercurrent` what is hidden there; both baselines come from the place itself, never from the genre — an SCP town is calm on top and deep underneath. List the setting's real threats in `encounters.hostile` (beasts, bandits, gangs, patrols) beside ordinary trouble, never only the harmless kind. A building or room names its `zone` and carries no stability of its own; give one its own stability only when it has its own control. Record only places the opening actually needs; a place first entered in play gets its band and stability then.

---

# PART E — PLAYER

## 13. Player

```yaml
player:
  identity:
    name:
    age:
    origin:
    history: []
  appearance:
  archetype:
  job:
  belongs: []
  gender:
  character:
  status:
  starting_activity:
```

### Capability

```yaml
  skills:
    skill_id:
      class: NORMAL | ELITE | LEGENDARY     # advancement ceiling
      tier: T1 | T2 | T3 | T4               # current mastery
      evidence: 0
      class_source:
      abilities: []
  traits: []
  expertise:
    established: []
    limitations: []
  growth_period: {opened: 0, credited: []}
  progression:                    # when numeric_level_xp is enabled
    system: numeric_level_xp
    state: {level: , xp: 0}
  vitality:                       # only when numeric_level_xp is disabled:
                                  # ordinary | seasoned | veteran | exceptional | heroic | legendary
  item_points: {rank: , basis: }  # when flexible_item_entitlement is enabled
```

`class` is the ceiling, `tier` is where they are now. Trained but unremarkable competence starts at T1; a higher start needs mastery evidence in the history. `evidence` starts at 0 unless prior qualifying learning is actually recorded. Level comes from recorded experience, and the history must support it.

`item_points` is required when `flexible_item_entitlement` is on. `rank` comes from the PC's social standing and income, never from level: `outcast · commoner · working_adult · well_off · elite`; `basis` says why in a few words. The pool starts full; the tool derives `current` and `max` from `rank`. Reasonable background possessions are separate and never consume it.

### Condition and possessions

```yaml
  condition:
    hp:                           # current; the maximum is derived
    mp:                           # current; omit if no MP-drawing skill
    conditions: []                # lasting: {condition: , source: body | mind, effect: }
    nerve: {baseline: , current: , tension: 0}   # −3..+3 from history
    fatigue:
    last_rest:
  equipment:
    - item_id:
      name:
      type:
      capability_domain:
      condition: serviceable | worn | damaged | critical
      special_properties: []      # incl. downsides
      tier:                       # T1..T4
      abilities: []
  money:
  resources:
    resource_id: {name: , tracking: exact | usage_die, count: , usage_die: }
  routines: {}
  fighting_style: []
  knowledge:
    facts: {}
    channels: []                  # how the PC hears of the world: the GM tells what comes through these (GM §3.1 WORD)
```

`hp` and `mp` start at the derived maximum unless the history says otherwise. A lasting condition is a name and one plain effect ("broken leg: harder to run or climb"). `fighting_style` holds combat habits the player has stated for this character, in their words — what a resource is kept for, how a fight opens, how a danger is tested, where allies stand. Leave it empty if they have stated none; only the player adds or changes it. `routines` holds only recorded in-world recurring behaviour. `channels` are how this character actually receives information.

## 14. Rights and obligations

```yaml
rights_obligations:
  right_id: {type: , parties: [], state: {}}   # type: owed for an earned, undelivered benefit
active_commitments: []             # references to right_ids only
```

Ownership held by someone else, custody, contracts, duties, debts owed either way, authority and its limits. A deal's terms and status live only here; quests and actors point to it.

---

# PART F — OPENING

## 15. World state

```yaml
world_state:
  location:
  time:
    season:
    day_index: 0
    date:
    clock_minutes:
    daypart:
    precision: exact | daypart | degraded
  environment: {}
  material_history: []
  pending: {}                    # caused, delayed consequences with no better owner: {what, cause, due}
  unowned_facts:
    visible: []
    hidden: []
  glossary: {}                   # optional, per language: {zh_hans: {<id>: <English> = <form>}}
```

The opening is this state, `player.starting_activity` (§13), the quests available at Round 0 (§8), and every important actor's first due (§11): play starts with the world already moving.

---

# PART G — RECORDS AND CHANGES

## 16. Who owns what

Every material fact has exactly one owner (I1).

```text
actor_core  identity, role/job, affiliation, gender, character, voice, manner,
  depth, in_disorder
actor_state  status, condition (lasting conditions, nerve), current HP/MP, position,
  resources, carried equipment, current plan, due, routines, aim; the player's
  fighting_style and item_points
drives  want, pull, fear, line, loyalties, values
secret  what an actor hides and why
relationships  directional per target: tie, attitude, standing (credit, grievance
  separate), bond, believed identity
rights_obligations  ownership/claims, authority, contracts, duties, permissions,
  owed entries; a deal's terms and status live only here
knowledge  known facts, beliefs, provenance, channels, suspicions not yet attached
  to a person
capability  skills, traits, expertise, vitality, biological and setting limits
progression  overall level and XP, when enabled
quests  objective, source, code, level, status, parts, quest XP paid
development_threads  unfinished player-development directions
locked_case_truths  committed case cause, evidence, state with no better owner
active_world_pressures  persistent world conditions and forces
locations  identity, conditions, challenge band, stability (surface, undercurrent),
  cover, encounters, closed
ending_conditions  conditions that end a scenario or chapter
narrative_theme  style only
world_state  time, environment, material history, pending consequences,
  otherwise-unowned facts, glossary
continuity_status  degradation, corrections, Round-0 revisions, save deferral
```

```text
FILING  who holds it? → npcs.<id> · factions.<id>
  where is it?  → locations.<id>
  neither  → world_state.material_history
  another owner only when its row names exactly this
OMIT  empty categories; nesting allowed, ownership single-source
INDEXES  active_commitments, storylines = reference indexes;
  discovered_information = visibility projection; none is an owner
DERIVED  stance, risk, opportunity, access, feasibility, severity, payoff
  eligibility: computed from owners each time; stored only if the result is
  material state
```

## 17. GM-Δ: how a change is written

```text
EXISTS  a fact exists only once written (a GM-Δ entry or the capsule); until then
  it never influences resolution, decisions, evidence, or narration (I2, I3)
BLOCK   one per round, at the top of the turn before any prose (GM §3.6), holding
  every change since the last block, visible or hidden, plain text; header names
  the previous block's round (first after a save names the save's round);
  no change → `GM-Δ <round> none`; a missing block = a gap
ENTRY   <op> <id> :: <content>
id      <owner>.<record id>.<field>, e.g. npcs.<id>.state.position; owner by FILING
        (§16); name the field; ~ on a whole record kept only as a dated note
+       new path; a new record may be one line holding its whole content
~       new value of that field
−       no longer holds; content = why
RULES   one fact, one record, one line per entry; never re-emit unchanged state;
        content: who, why, what evidence exists where; not the reveal or the scene
        one new id per credit or grievance; one ~ per field
RETIRE  only what can no longer matter: dead with no remaining witness, knowledge,
        or consequence · resolved case · solved puzzle · completed quest with XP
        and payoffs cleared; never for quietness: a witness, identity belief,
        grievance, debt, or actor with unknown position stays
GAPS    an empty, cut-off or unreadable entry, or a round with no block → its
        content marked degraded (I12); never rebuilt from narration; a cause never
        written was never committed; if its evidence was shown, commit a cause
        from the world as it stood before (motive, means, opportunity then),
        never from the clue or a player theory; none supported → unknown,
        degraded
```

```text
EXAMPLES
~ npcs.mags_pell.relationships.pc.credit :: [killed the boar; gave her a leg]
  → + npcs.mags_pell.relationships.pc.credit.hind_leg :: gave her a boar leg (R37)
~ npcs.marlene_osgood.state :: {position: …, plan: …, due: …}
  → one ~ per field: …state.position · …state.plan · …state.due
− npcs.harl :: quiet lately → keep: RETIRE never for quietness
+ quests.lab_theft.code :: B (R12, PC agreed to help Meera)
~ quests.lab_theft.status :: active
~ quests.lab_theft.status :: succeeded (R31, Ravi confessed) → shown as Bs
```

---

# PART H — THE SAVE

A save is a projection of the world now. Every field is canonical state or an explicitly derived convenience that cannot create or strengthen anything. Save-only world facts are forbidden.

```text
TWO PARTS  A readable (written by the GM at save time) · B capsule (built by the
  tool); the same completed round, the same stable ids, never the same field twice
BUILT    the tool merges the previous save (none for the first) with every GM-Δ
  block since, copied from the turns (RULES §16 save)
TIMING   GM §6
```

## 18. Part A — readable

Never place an undiscovered cause, hidden actor state, a secret trajectory, a hidden layer's tension or an undiscovered clock the player has not inferred, a hidden ending condition, a quest spine, or internal reasoning in this part.

```yaml
background_ref: {id: }           # BACKGROUND background_id; from chapter 2 on, that chapter's
language:                        # game language, e.g. en, zh_hans
profile: full                    # full | lite: output length only
round:
  last_completed_round:
  saved_completed_round:
world_state:
  location:
  time: {season: , day_index: , date: , clock_minutes: , daypart: , precision: }
  environment: {}
player:                          # the §13 player block, as it stands now
enabled_modules: {}              # as the BACKGROUND set them; never changed
narrative_theme: {initial: , current: }
index:                           # one line per record the player knows of; display only
  npcs:            {npc_id: "<name> — <what the player knows, a few words>"}
  factions:        {faction_id: "<name> — <role>"}
  locations:       {location_id: "<name> — <the state the player has observed>"}
  quests:          {<code + status letter>: "<objective> — <how it stands>"}   # e.g. A-2p: "read the throne — half"
  development_threads: {thread_id: "<direction> — <status>"}
  rights_obligations: {right_id: "<type> — <parties>"}
  active_world_pressures: {pressure_id: "<name> — <what the player has seen>"}
```

`evidence` is live state: below the ceiling it pays for tiers, at the ceiling it accumulates toward a class raise. `growth_period.credited` enforces one evidence credit per skill per period across saves. `hp` and `mp` are current values only; maximums are derived and never saved. `resources` holds actual resources only — never a policy flag. A usage die is saved at its current size; it never resets on load. `routines` holds only recorded in-world recurring behaviour; never a diagnostic, a display, an output preference, an obligation, a quest, or an inferred habit. `item_points`: `current` is the unspent reserve; `max` comes from `rank`.

The index never lists a record the player has not met or learned of. Quest levels, tracks and clocks appear in it only where an in-world source made them visible to the player.

## 19. Part B — capsule

```yaml
capsule:
  save_round:
  delta_of:                          # background_id; records equal to it are left out
  supersedes_deltas_through:         # last GM-Δ round folded into this capsule
  records:                           # one line each, plain text: <id> :: <content>
    npcs.hadvar :: {"name": "Hadvar", ...}
    npcs.hadvar.state.position :: R112: Riverwood
  retired:                           # ids dropped by a − entry; BACKGROUND paths stay listed
    <id> :: <reason>
continuity_status:
  degraded: []                       # what is known, what was lost
  corrected: []                      # player corrections and repaired GM errors, with the round
  round0_revisions: []               # {field, was, now, reason, round}
  save_deferral: null                # null | one_round
```

**Records are field paths.** An id may name a whole record (`npcs.hadvar`) or one field under it (`npcs.hadvar.state.position`). The tool stamps what it writes with its round (`R112: …`); where records disagree about a detail, the later round wins, and an unstamped record is older than any stamped one. A whole record is never overwritten: a change aimed at it is appended as a dated note. A record reading `no longer holds — <reason>` cancels that detail.

**Survival.** Every record of the previous capsule appears here verbatim, changed only by the GM-Δ blocks, appears under `retired` with its reason, or is left out because it equals the BACKGROUND. The tool guarantees this; a missing id makes the save invalid. A GM-Δ round missing between the previous save and this one is reported as a gap: list what that round committed under `continuity_status.degraded` rather than rebuilding it from narration.

`round0_revisions` override the BACKGROUND for their field on load. `save_deferral` is set only by the continue-unsaved choice and cleared at the next round close.

## Contract

- Both parts represent the same authoritative completed round, with the same stable ids, and never hold the same field.
- The save does not carry the setting. The BACKGROUND holds `setting`, `setting_anchors`, and `content_bounds`, and must travel with the save.
- Part A exposes only established player-visible information.
- Derived convenience fields never create, strengthen, or override state.
- Missing noncritical detail is marked degraded and the save stays valid. A continuation-critical gap makes the save invalid until repaired from authoritative evidence.

---

*End of NEO WORLD v0*
