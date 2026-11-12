# NEO BACKGROUND TEMPLATE — v0

How to make or rework a NEO background, and the shape of one. Attach this file only when making or reworking a background; play itself uses NEO_SAVE.

A background is the world at Round 0: the setting, the people, the places, the PC, and every truth already fixed before play. Fill in what the game uses and leave out what it doesn't. Give the PC the capability, gear and connections their history supports.

```text
PARTS  0 design logic · A frame · B situation · C people · D places · E player ·
       F opening
FILE   worlds/BACKGROUND_<NAME>_NEO_v0.md
```

---

## Making a background

When the person asks for a new world, or a rework, before play:

```text
1 ASK     what they want, in their words: setting, era, tone, who the PC could be,
          what it is about, what must or must not be in it; something unclear that
          changes the whole world → ask once
2 RECORD  provenance (authored, generated, mixed) and `requested`, word for word
          (§1); requested facts are fixed like authored ones
3 DESIGN  Part 0 in its order: hidden reality (§0.1), mystery principles by the
          tool's rolls (§0.2), lenses (§0.3), story shape (§0.4), quest spines
          (§0.5); write the design_logic record
4 FILL    Parts A–F in order; each actor gets the depth the story gives them and
          every field that depth needs (§11); every important actor and pressure
          gets a plan or pace with a due that names a time of day ("Day 2 night")
5 CHECK   the tool's check form (RULES §16); fix each finding and run it again
          until ok; then read the design against §0's TEST yourself
6 SHOW    give the person the background with a short list of what you invented
          beyond `requested` (secrets, pulls, beliefs, added people and places);
          they strike or change what they like, and their word is final
7 FILE    save it in worlds/; play starts from a checked, shown background
```

---

# PART 0 — DESIGN LOGIC

## 0. Building the hidden world

```text
USE    a new background, or a rework for complex quests and stories; authored
       facts and `requested` items stay as given, and this shapes what you fill in
ORDER  1 build the hidden reality first (§0.1)
       2 let complexity grow from people with their own motives (§0.2, §0.3)
       3 shape it into storylines (§0.4) and quest spines (§0.5), then the player
         and the opening
TEST   the design gives several plausible explanations, people with their own
       motives, real connections, and consequences that run on even if the PC
       misreads everything
```

### 0.1 Hidden reality to establish

```text
D1 WORLD FACTS        what happened, in time order, including which events are
                      linked and which only look linked → §9, world_state history
D2 ACTOR STATE        each NPC and faction by depth: the want the PC can push on,
                      the fear, the line, the secret with its ordinary reason; for
                      story-turning people the pull and the false belief; a voice
                      for anyone who speaks → §11
D3 EVIDENCE           each clue: which thread it came from, what it actually
                      shows, which readings it leaves open → §9 evidence
D4 TIMELINES          what each actor does if the PC stays out of it; every step
                      has a due, so the world moves on its own → §11 state, §8
D5 CROSSINGS          where threads meet, where they stay apart, how one actor's
                      move changes another thread → §8 pressures
D6 CONSEQUENCES       what changes when the PC acts, including acting on a wrong
                      belief → §11, §8 on_step / on_fill
D7 BOUNDARIES         what can be learned, what particular NPCs know and don't →
                      §11 knowledge
SCALE                 fill what this story uses
```

### 0.2 Mystery principles

```text
COUNT   new background: tool `roll 1d5` + 4 = N principles (5–9)
PICK    new background: tool `roll 1d9` until N distinct numbers; a rework: pick
        the principles that fix what it lacks; record in design_logic
WEIGHT  new background: tool `roll 1d3` = W; roll among the picked until W distinct
        → the weighted ones; a rework: weight by need
APPLY   picked principles shape the background; weighted ones are what it is
        built around; M2 and M5 hold in every background
```

```text
M1 STRUCTURED CHAOS   any mix of independent events, connected operations,
  conspiracies, personal agendas and coincidences; some events stand alone, others
  form long chains; people shape each other's lives without knowing it; whoever
  seems behind an event may have caused it, used it, helped by accident, or just
  seen a chance; a minor figure may understand more than those involved; a victim
  may also manipulate

M2 TRUTH AND BELIEF   the background fixes what happened, what connects, and
  what each person intends, knows, believes and gets wrong; the PC builds their
  own explanation from evidence, and NPCs act on partial information too; the
  truth holds still while everyone reads it their own way

M3 THE WORLD ANSWERS ACTIONS   when the PC acts on a wrong theory, the world
  responds to what they actually did: they may succeed, fail, hurt the wrong
  person or help someone unexpected; a wrong reading is a real outcome; the
  author sets reality and consequences, and the player draws their own
  conclusions; never an NPC who appears just to explain the answer, never a
  quest to correct a mistaken theory, never events rearranged to prove the PC
  right

M4 TRUE CLUES, FALSE LINKS   each thread leaves real evidence; evidence from
  different threads overlaps in time, place, people or motive and suggests a
  wrong but convincing picture (A and B linked, A and C only look linked, D uses
  the confusion); the strongest misdirection is all true evidence read with
  missing pieces; a later find may recast an earlier scene

M5 PEOPLE, NOT CLUE BOXES   people have lives beyond the case; most hide things
  for ordinary reasons (privacy, shame, love, duty, money, fear); some are
  wrongdoers, others victims, witnesses, bystanders or opportunists, and roles
  overlap; they act from their own motives and knowledge, never to hand out
  clues or keep a mystery going

M6 COMPLEXITY FROM CROSSING   each thread makes sense alone; the complexity comes
  from how they collide: several wrongdoers with different aims, overlapping
  events, rival loyalties, coincidences that look planned, small choices with big
  results; study how stories you know make these interact, and build your own;
  put complexity where the story gains from it

M7 OPEN ENDINGS   a story can satisfy without the full truth: a confident wrong
  conclusion, one culprit caught and another missed, a conspiracy half
  uncovered, a detail that never fits; the immediate goal may be settled while the
  bigger picture stays unclear

M8 MANY ROUTES   investigate, negotiate, deceive, cooperate, withdraw, confront,
  fight: each route gets its own consequences and its own access to the truth;
  the PC can beat a threat without understanding it, and the world follows the
  route they chose

M9 THE CORE   the background is what is true; the simulation is what happens as
  people pursue their aims; the PC holds what they believe happened; the three may
  stay different; real facts, understandable motives, and no promise they form a
  simple picture
```

### 0.3 Lenses for romance, combat, factions

Use a lens where the background holds that domain, and only the patterns that fit. Record lenses in design_logic.

```text
ROMANCE   each person holds their own meaning of the relationship, so each side
  gets its own §11 relationship entry and bond; patterns: casual to one, deep to
  the other · real care, different futures · an NPC falls for the PC for reasons
  the PC doesn't see · real affection and still a no · a moment that matters to
  only one · trust growing while attraction fades; it plays out through attitude,
  bond, drives and choices

COMBAT    winning the fight and winning the situation are different; each side has
  its own objective and its own idea of winning; patterns: the opponent is
  delaying · win the fight, lose the goal · the enemy already got what they came
  for · a third party profits from the fight · the opponent was guarding
  something or acting on bad information; fights make story

FACTIONS  a faction is an official aim plus members with their own interests,
  partial information and varying loyalty; patterns: an order read differently
  down the line · two members obeying for different reasons · a subordinate
  succeeding while undermining the leader · an internal quarrel helping a rival ·
  the faction winning its goal and damaging its reason to exist
```

### 0.4 Story shape

```text
CAMPAIGN   premise and question first (§7), one line each; every storyline bears on
           the question or the PC's own life; a background that is one big quest
           takes that quest's spine as its question (§0.5)
SITUATION  write what each actor does if the PC stays out (D4): situations, with
           the scenes left to play
STORYLINE  one reality that makes sense alone (M6): its truth (§9), actors (§11),
           pressure (§8) and routes, indexed in §7
ROUTES     a case tied to a quest has 3 or more (RULES §15.6); other storylines have
           the routes their own facts give; never invent routes or connections to
           reach a count
SCALES     one main storyline over weeks or months · local storylines over days ·
           ordinary lives, which need no pressure (most storylines are ordinary
           lives)
SIGNS      each pressure stage leaves a sign someone could notice: a rumour, a
           changed place, a person acting differently
ENGINE     how work and trouble keep reaching the PC: work sources with a pace
           (§11), the main case's leads, the PC's own people
MAIN LINE  the main quest opens as a simple, ordinary job; what it grows into lives
           in its truth and its actors
OWN PEOPLE the PC has a life: a few people they share history with (family, old
           friends, a mentor, an ex), each with a bond (§11)
```

### 0.5 Quest spine

```text
SPINE      each quest has one; it belongs to the quest, so any PC role fits it
PARTS      question: one sentence · stake: why this PC cares, as stake_hooks, one
           per likely PC role · pressure: how it moves by the world's own logic ·
           end: a visible end point, which may come with the truth still unclear
SCOPE      one big quest → one spine for the background (Die Hard, Jaws) · several
           main quests → one spine each (The Witcher 3, Red Dead Redemption 2)
SOURCE     a copied or modified story → its spine, changed as far as the changes
           need · an original → generate topic options, roll among them, build
           from the result (a topic is a real fact, a mode such as comedy or dread,
           or a rule); record in design_logic
BUILD      write the spine from this world first; then compare its structure with
           reference works; a spine that would work unchanged elsewhere, or reads
           like a reference with names swapped, is rebuilt
THREADS    hang on the spine: many threads, one spine per quest
HIDDEN     the spine lives in the quest record; the player-facing hook is written
           separately from what it hides
```

---

# PART A — FRAME

## 1. Identity and provenance

```yaml
background_id:        # required; every save's background_ref points here
provenance:           # authored | generated | mixed
requested: []         # generated or mixed: what the person asked for, in their terms
design_logic:         # Part 0 only: {mystery: {rolled_n: , picked: [M#], weighted: [M#]}, spine_topic: , lenses: [romance|combat|factions]}
replaces: {}          # only for a setting with its own system: {<rules part>: <this background's rule>}
```

`authored` means the person wrote all of it, and only they change it. In a `generated` or `mixed` background, `requested` lists what the person actually asked for, in their words, fixed like authored facts; the rest becomes established as play relies on it.

`replaces`: a setting with its own system for a part of RULES (a sanity system, a magic system) names it here, and that rule is used in place of the RULES part.

## 2. Setting

```yaml
setting:
  world:
  era:
  starting_region:
  mode:                 # canon | historical | original | alternate (canon: attach the modules file)
  canon_scope:          # canon: history before the start is fixed; after it, canon's course is the actors' default plans
  allowed_deviations:   # what play may change
```

### Canon course — only when `mode: canon`

The bones of the main quest and major questlines, written as the plans of the actors who drive them: intent, with the scenes, dates and outcomes left to play. Each step needs its actors' knowledge, means and time. What this file leaves out comes from the source.

```yaml
canon_course:
  beat_<n>_<name>:
    opens:              # the event that opens it; a Day only for the opening
    quest: []           # the quest(s) that record it: blocked until it opens
    <actor_or_group>:   # what each side does in this beat, in order
  later_steps:          # optional: "as in the game — …"
  timed_plans:          # optional: plans that run on their own dates
```

## 3. Setting anchors

The anchors new material in play traces back to. Record the ones that keep generation consistent; what they leave open is developed in play (GM §7.5).

```yaml
setting_anchors:
  peoples_or_species: []
  powers_or_supernatural_rules: []
  technology: []
  institutions: []
  religions_or_beliefs: []
  economics_or_trade: []    # incl. a price list of everyday goods, services, and wages
  economy_model:            # the real economy prices follow, e.g. "English market town c. 1450, copper bit ≈ penny"
  tool_prices: standard     # standard | cheap (RULES §14)
  law_and_social_structure: []
  creatures_or_threats: []
  norms:
    law_and_outlaws: []     # whom the law protects; what people care about; what counts as cruelty here
    morale:                 # how readily each common kind of combatant breaks (RULES §8)
      kind_of_combatant:
    usual:                  # optional: where this setting's "usual" differs from the real world's
  mp_powers:                # only if the setting has MP-drawing powers (attach the modules file)
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

`norms` holds the setting's own standards, how readily each common kind of foe breaks, and what counts as usual here. Morale is settled from these; without an entry, self-preservation decides.

`undercurrent_pool` is what the hidden layer does when a contact roll comes up: `sign` is wrongness a local would misread, `brush` contact without harm, `incident` something happening to someone, `hostile` it acting against those present. Write them from the setting's own hidden things.

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
  numeric_level_xp: true            # false: attach the modules file
  flexible_item_entitlement: true
```

Every module is on unless set false here. A save keeps the setting as it is.

## 6. Presentation

```yaml
narrative_theme:
  initial: {tone: , style: }
  current: {tone: , style: }
```

A style seed: it shapes how things are told and adds no facts. Tone comes from here.

---

# PART B — THE SITUATION

## 7. Campaign premise

```yaml
premise:              # one line: who the PC is, where, and the situation they are in
question:             # one line: what play will answer; the answer is open
storylines:           # an index pointing at owners
  storyline_id:
    kind:             # main | side | ordinary_life | wrongdoer
    line:             # one line: what is really going on in it
    refs: []          # quests.<id>, locked_case_truths.<id>, active_world_pressures.<id>, npcs.<id>, factions.<id>
```

`premise` and `question` are design notes: every arc stays open. A storyline's status lives at the owners it points to. Where two storylines collide is recorded at their pressures (§8).

## 8. Quests, threads, pressures

```yaml
quests:
  quest_id:                        # a stable id; the player-facing code (A, A-1, A-B)
                                   # is designed here and given when the PC takes it on (RULES §10)
    code:                          # designed with the quest (A, B; follow-ons A-C); parts carry
                                   # A-1, A-2; the player is given it when the PC takes it on
    objective:
    source:                        # who offers or requires it
    spine: {question: , stake_hooks: {<role>: <hook>}, pressure: , end: }   # GM truth (§0.5)
    hook:                          # player-facing, written from what the player can know
    level:                         # its fixed challenge (RULES §10 LEVEL)
    status:                        # Round 0: available | blocked; in play: active |
                                   # succeeded | partly | failed | abandoned
    trigger:                       # blocked only: the event that opens it
    parts: {}                      # optional: {part_id: {code: A-1, objective: , level: }}
    routes: []                     # a case tied to it: 3 or more ways in (RULES §15.6)
    support_refs: []
    terms:                         # paid work: rights_obligations.<id>; the contract names quest: <code>
development_threads:
  thread_id: {direction: , origin: , state: , status: }

active_world_pressures:
  pressure_id:
    name:
    origin:
    state: {}
    actors: []
    trajectory:                    # the expected direction if conditions hold
    track:                         # bound to zones: one entry per zone it moves
      zone_id:
        layer:                     # surface | undercurrent
        direction:                 # destabilising (default) | stabilising
        pace:                      # every <interval> while <condition>
        due:                       # first check time
        on_step: {}                # {<step>: <what the world does when the layer reaches it>}
    clock:                         # bound to no zone (a plan, construction, research, a tally)
      {segments: , filled: 0, pace: every <interval> while <condition>, due: <first check time>,
       on_fill: , stages: {early: <segments>, late: <segments>}, signs: {early: , late: }}   # stages optional
    discovered_information: {}
```

A pressure gets a `track` when it plays out in places (a spreading cult, gang war in a ward): each advance is a mark on that zone, so the zone's stability shows its progress. It gets a `clock` when it belongs to no place (a rival's plan, a ritual's preparation, a debt paid down) or is a short emergency in hours or days. One of the two per zone.

Set `pace` so the whole span fits the process: a world-scale pressure moves in weeks or months. A zone moves at most one step a week, and a step takes 3, 5 or 6 marks. `on_step` and `on_fill` are what the world does if nobody interferes. Every stage leaves a sign someone could notice. Zero pressures is fine.

A development thread is a direction the PC is growing in, from their stated intent or history. Standing with a faction or person lives in credit and grievance (§11).

## 9. Hidden truth at Round 0 — optional

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

Write the cause first, and the evidence follows from it. A suspicion someone holds at Round 0 lives in that actor's `knowledge.suspicions` (§11). Each case tied to a quest lists its routes on the quest (§8). All of this is hidden state: it goes in the capsule.

## 10. Ending conditions — optional

```yaml
ending_conditions:
  core_conditions: []
  hidden_conditions: []
  closed: []                       # permanently unreachable
```

An open world needs none. Write them before the choices they govern.

---

# PART C — PEOPLE

## 11. Actors and factions

Order: the PC's own people → work sources → storyline actors → factions. Depth and its fields are explained in NEO_SAVE §1.

```yaml
npcs:
  npc_id:
    depth:                         # 0 | 1 | 2 | 3
    name:                          # name, job, belongs, gender, character are required;
    job:                           # write unknown where it isn't established
    belongs:
    gender:
    character:                     # what kind of person they are
    manner:                        # depth 0: how they come across, one line
    voice:                         # depth 1+: how they talk — words, rhythm, habits, what they avoid saying
    in_disorder:                   # thrives | suffers | neither
    state: {}                      # status, position (a recorded location's name), current HP/MP when below
                                   # max, nerve when it matters, plan, due, what they do if blocked
                                   # due: each move with the code of the quest step it serves and a daypart
                                   # or trigger: "A-1 Day 2 night …; A-3 Day 6 night …" (A-1s once resolved)
                                   # work source: routines: {work_source: {pace: , kinds: []}}
    drives:
      want:                        # depth 1+: the one plain thing they want
      fear:                        # depth 1+: what they dread
      line:                        # depth 2+: what they won't do; crossing it is possible, at a cost
      pull:                        # depth 3: a second want that fights the first
      loyalties: []
      values: []
    secret: {what: , why: }        # depth 2+: what they hide and their own ordinary reason
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

`attitude` is a few plain words, starting neutral at a first meeting unless the record says otherwise. `credit` is what the other did for this actor; `grievance` what this actor holds against them. `believes_identity` holds a false or partial belief about who someone is.

`bond` is what the relationship is to this side: `history` what they've been through, `means` what the other is to them, `habits` how they are together (names, banter, rituals, small care), `wants` what they want from it, `unsaid` what they feel and keep back. Fill it for the PC's own people and anyone the relationship matters to.

A work source (fixer, guild, employer, patron) carries its pace in `state.routines.work_source`, else it checks weekly.

---

# PART D — PLACES

## 12. Locations

```yaml
locations:
  location_id:
    name:
    conditions: {}
    challenge_band: {min: , max: , basis: }
    zone:                                              # a building or room: the zone it sits in
    surface: {baseline: , current: , tension: 0}       # −3..+3
    undercurrent: {baseline: , current: , tension: 0, sites: [], hours: , nature: }   # none..−3; omit if none
    cover:                                             # the actor keeping the hidden hidden; omit if none
    closed:                                            # optional: why it can't be entered, and until when
    encounters:
      hostile: []
      ordinary: []
```

A band says which causes can plausibly exist in a place; `basis` says why. `surface` is how the place behaves openly, `undercurrent` what is hidden there, both from the place itself (a town can be calm on top and deep underneath). List the setting's real threats in `encounters.hostile` (beasts, bandits, gangs, patrols) beside ordinary trouble. A building or room names its `zone`; give it its own stability only when it has its own control. Record the places the opening needs; others get their band and stability when first entered.

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
      class: NORMAL | ELITE | LEGENDARY     # ceiling
      tier: T1 | T2 | T3 | T4               # current mastery
      evidence: 0
      class_source:
      abilities: []
  traits: []
  expertise:
    established: []
    limitations: []
  growth_period: {opened: 0, credited: []}
  progression:                    # with numeric_level_xp
    system: numeric_level_xp
    state: {level: , xp: 0}
  vitality:                       # without numeric_level_xp: ordinary | seasoned | veteran | exceptional | heroic | legendary
  item_points: {rank: , basis: }  # with flexible_item_entitlement
```

Ordinary trained competence starts at T1; a higher start needs mastery in the history. `evidence` starts at 0 unless earlier learning is recorded. Level comes from recorded experience.

`item_points.rank` comes from the PC's standing and income: `outcast · commoner · working_adult · well_off · elite`; `basis` says why. The pool starts full. Ordinary possessions from the PC's history are separate.

### Condition and possessions

```yaml
  condition:
    hp:                           # current; the maximum is derived
    mp:                           # current; only with an MP-drawing skill
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
    channels: []                  # how the PC hears of the world
```

HP and MP start at the derived maximum unless the history says otherwise. `fighting_style` holds the combat habits the player has stated, in their words; leave it empty until they state some. `routines` holds recorded recurring behaviour.

## 14. Rights and obligations

```yaml
rights_obligations:
  right_id: {type: , parties: [], state: {}}   # type: owed for an earned, undelivered benefit
active_commitments: []             # references to right_ids
```

Ownership held by someone else, custody, contracts, duties, debts either way, authority and its limits. A deal's terms and status live here; quests and actors point to it.

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

The opening is this state, `player.starting_activity`, the quests available at Round 0, every important actor's first due, and the first contact the opening names (GM §7.2): play starts with the world already moving.

---

*End of NEO BACKGROUND TEMPLATE v0*
