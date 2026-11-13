# NEO SAVE — v0

How the world is kept during play. Two files hold it together:

- **The background**: the world at Round 0. Once play begins it is history and stays as written.
- **The save**: the same world later. A readable part for the player, plus a capsule of every record that now differs from the background. The background fills in the rest on load, so the two always travel together.

Both use the same field names. The GM reads every fact from the background, the newest save, and the GM-Δ blocks since.

The full background schema, and how to make a new background, is in `templates/BACKGROUND_TEMPLATE_NEO_v0.md` on GitHub (https://github.com/west132/NEO). It is attached only when making or reworking a background.

---

## 1. Reading a background in play

```text
PROVENANCE  authored: the person wrote all of it, and only they change it ·
            generated or mixed: `requested` lists what they asked for, fixed like
            authored; the rest becomes established as play relies on it
REPLACES    a setting with its own system for a part of RULES names it in
            `replaces`; that rule is used in place of the RULES part
NORMS       setting_anchors.norms: the setting's own standards, how readily each
            kind of combatant breaks, and where "usual" differs from the real world
DEPTH       every NPC has one, setting the fields they carry:
            0 passer-by      name, job, one manner line
            1 regular        + want, fear, voice
            2 supporting     + line, an ordinary secret, ties
            3 story-turning  + pull, belief; plan and due; knowledge
            an NPC rises when play shows they matter more (a tie with the PC, a
            role in a quest, pressure or case, a deal); new fields are developed
            once (GM §7.5), then fixed; a dead or departed NPC keeps the record;
            someone first met in play starts at 0, or 1 if they'll be seen again
IMPORTANT   read from the newest save: an actor with a relationship to the PC
            (credit, grievance, bond), a role in a quest, pressure or case, or a
            deal with the PC; an important actor always has a plan and a due
DUE         a clock time with a daypart, or a trigger written as an event ("when …")
            the tool can list; a due with several moves starts each with the code of
            the quest or part it serves: `A-1 Day 2 night …; A-3 Day 6 night …`; a move
            that has resolved gets its status letter after the code (`A-1s …`) and
            stops firing; when no open move is left, the actor re-plans
CHARACTER   who they are, played as behaviour · VOICE how they sound, played as
            speech · a character from a source is played as the source made them
WANT        kept plain: what the PC can push on; the complexity lives in pull,
            beliefs, secret and line; `secret.why` is their own ordinary reason for
            hiding it, and the reason for any lie that protects it
IN_DISORDER thrives (works against order) · suffers (relies on it) · neither
POSITION    an actor's or the PC's position names a recorded location, so the tool
            finds the zone; someone going somewhere unrecorded that play will use
            (a lodging, a hideout) → develop the place once for the world's own
            reason (GM §7.5) and record it: + locations.<id> :: {name, zone, …}
CHANNELS    player.knowledge.channels: how the PC hears of the world (GM §3.1 WORD)
STYLE       player.fighting_style: the player's own combat habits, in their words;
            only the player changes them
THEME       narrative_theme: the tone and style the GM narrates in
```

---

## 2. Who owns what

Every fact has one home. A GM-Δ entry names it.

```text
actor_core          identity, job, affiliation, gender, character, voice, manner,
                    depth, in_disorder
actor_state         status, condition (lasting conditions, nerve), current HP/MP,
                    position, resources, carried gear, plan, due, routines, aim;
                    the player's fighting_style and item_points
drives              want, pull, fear, line, loyalties, values
secret              what an actor hides and why
relationships       per target, each side its own: tie, attitude, credit,
                    grievance, bond, believed identity
rights_obligations  ownership, authority, contracts, duties, permissions, owed
                    entries; a deal's terms and status live here
knowledge           facts, beliefs, sources, channels, suspicions not yet attached
                    to a person
capability          skills, traits, expertise, vitality, limits
progression         level and XP
quests              objective, source, code, level, status, parts, quest XP paid
development_threads the PC's growth directions
locked_case_truths  a case's cause, evidence and state
active_world_pressures  forces and conditions that move the world
locations           identity, conditions, band, stability, cover, encounters, closed
ending_conditions   what ends the campaign
narrative_theme     style
world_state         time, environment, material history, pending consequences,
                    facts with no other home, glossary
continuity_status   what is unknown, corrections, Round-0 revisions, save deferral
```

```text
FILING   who holds it? → npcs.<id> · factions.<id>
         where is it? → locations.<id>
         neither → world_state.material_history
INDEXES  active_commitments and storylines point at owners;
         discovered_information is what the player has seen of a record
DERIVED  stance, risk, access, feasibility, payoff eligibility: worked out from the
         owners each time
```

---

## 3. GM-Δ: how a change is written

```text
EXISTS  a fact takes part in play once it is written (a GM-Δ entry or the capsule)
BLOCK   one per round, at the top of the turn before the prose (GM §3.6), holding
        every change since the last block, seen or hidden, in plain text; its
        header names the previous block's round (the first after a save names the
        save's round); no change → `GM-Δ <round> none`
ENTRY   <op> <id> :: <content>
id      <owner>.<record id>.<field>, e.g. npcs.<id>.state.position
+       a new path; a new record may be one line holding its whole content
~       the new value of that field
−       it no longer holds; the content says why
LINES   one fact per entry; one new id per credit or grievance; one ~ per field;
        content says who, why, and where the evidence is
RETIRE  for what can no longer matter: someone dead with no witness, knowledge or
        consequence left · a solved case · a finished quest with XP and payoffs
        settled; a witness, a belief about identity, a grievance, a debt, or an
        actor whose whereabouts are unknown stays
GAPS    an unreadable entry, or a round with no block → mark its content unknown
        under continuity_status.degraded; a cause that was shown as evidence but
        never written is committed from the world as it stood before (motive,
        means, opportunity then); with nothing to support it, it stays unknown
```

```text
EXAMPLES
+ npcs.mags_pell.relationships.pc.credit.hind_leg :: gave her a boar leg (R37)
~ npcs.marlene_osgood.state.position :: the mill
~ npcs.marlene_osgood.state.due :: Day 4 evening
+ quests.lab_theft.code :: B (R12, PC agreed to help Meera)
~ quests.lab_theft.status :: active
~ quests.lab_theft.status :: succeeded (R31, Ravi confessed) → shown as Bs
```

---

## 4. The save

A save is the world as it stands at one completed round, in two parts with the same stable ids. The tool builds it by merging the previous save (none for the first) with every GM-Δ block since, copied from the turns (RULES §16). When to save: GM §6.

### 4.1 Part A — readable

What the player knows. Hidden causes, hidden actor state, secret trajectories, a hidden layer's tension, clocks the player hasn't inferred, hidden ending conditions, quest spines and the GM's reasoning all live in the capsule.

```yaml
background_ref: {id: }           # the background's background_id
language:                        # game language, e.g. en, zh_hans
round:
  last_completed_round:
  saved_completed_round:
world_state:
  location:
  time: {season: , day_index: , date: , clock_minutes: , daypart: , precision: }
  environment: {}
player:                          # the player block as it stands now
enabled_modules: {}              # as the background set them
narrative_theme: {initial: , current: }
index:                           # one line per record the player knows of
  npcs:            {npc_id: "<name> — <what the player knows, a few words>"}
  factions:        {faction_id: "<name> — <role>"}
  locations:       {location_id: "<name> — <the state the player has observed>"}
  quests:          {<code + status letter>: "<objective> — <how it stands>"}   # e.g. A-2p: "read the throne — half"
  development_threads: {thread_id: "<direction> — <status>"}
  rights_obligations: {right_id: "<type> — <parties>"}
  active_world_pressures: {pressure_id: "<name> — <what the player has seen>"}
```

HP and MP are saved as current values; the tool derives maximums. A usage die is saved at its current size. `item_points.current` is the unspent reserve. The index lists what the player has met or learned of; quest levels, tracks and clocks appear where something in the world showed them.

### 4.2 Part B — capsule

```yaml
capsule:
  save_round:
  delta_of:                          # background_id; records equal to it are left out
  supersedes_deltas_through:         # last GM-Δ round folded in
  records:                           # one line each: <id> :: <content>
    npcs.hadvar :: {"name": "Hadvar", ...}
    npcs.hadvar.state.position :: R112: Riverwood
  retired:                           # ids dropped by a − entry
    <id> :: <reason>
continuity_status:
  degraded: []                       # what is known, what was lost
  corrected: []                      # repaired GM mistakes and player corrections, with the round
  round0_revisions: []               # {field, was, now, reason, round}
  save_deferral: null                # null | one_round
```

**Records are field paths.** An id names a whole record (`npcs.hadvar`) or one field (`npcs.hadvar.state.position`). The tool stamps each record with its round (`R112: …`); where two disagree, the later round wins, and an unstamped record counts as oldest. A change to a whole record is appended as a dated note. `no longer holds — <reason>` cancels that detail.

**Carried forward.** Every record of the previous capsule appears here as it was, changed by the GM-Δ blocks since, or listed under `retired` with its reason, or left out because it now equals the background. The tool checks this; a missing id makes the save invalid. A missing GM-Δ round is listed under `continuity_status.degraded`.

`round0_revisions` override the background on load. `save_deferral` is set by the continue-unsaved choice and cleared at the next round close.

### 4.3 Together

- Both parts describe the same completed round with the same ids, and each field lives in one part.
- The background carries `setting`, `setting_anchors` and `content_bounds`, so it travels with every save.
- Part A shows only what the player has established.
- A missing minor detail is marked unknown and the save stays valid; a gap that play needs makes it invalid until real evidence repairs it.

---

*End of NEO SAVE v0*
