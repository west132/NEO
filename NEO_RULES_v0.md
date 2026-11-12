# NEO RULES — v0

How the game resolves: what a human referee with dice would work out the same way. The GM opens a section when a step of the turn points to it. The background and the save hold every fact these rules read.

```text
TOOL     neo_math makes every number: rolls, modifiers, caps, bands, damage, XP,
         growth, points, dues; this file says what goes in and what comes out
INPUT    you fill a form; the tool reads it as a JSON file or stdin; values the
         save already holds (level, tier, HP, gear) the tool reads from the save
OUTPUT   the tool prints the roll line; copy it word for word into the turn
MODULES  powers (MP), canon mode and play without levels live in
         modules/NEO_MODULES_v0.md; a background that uses one says so in its
         setting, and the player attaches that file
```

---

## 1. The law

The law is GM §1. Every rule here serves it.

## 2. Possibility

Before any roll, decide which of these the action is:

```text
IMPOSSIBLE  it breaks recorded reality, or lies far beyond what this actor and
            their support could do → no roll; show the visible reason
LIMITED     the actor lacks the knowledge to go that deep (a layman reading a
            surgeon's notes) → they get as far as their recorded skill, expertise
            and access reach
UNCERTAIN   → the action form (§3)
CERTAIN     → it happens
RETRY       a failed or impossible action becomes possible again when something
            real changes: leverage, information, position, tools, help, timing,
            conditions
EXPERTS     another actor's expertise gives their own conclusion or changes what
            is feasible; the PC's own skill stays the PC's
```

---

## 3. The action form

Every uncertain action is one form, filled and run before any dice. Each fact goes in exactly one slot.

```text
FORM (JSON)
  actor        id of who acts
  action       one line: what they attempt
  skill        the skill used (the tool reads level and tier from the save)
  opposition   one of:
                 {actor: <id>, domain: <skill>}   an opposed actor
                 {level: <n>}                     a committed task, hazard, or
                                                  quest or part level
                 {grade: forgiving | easy | ordinary | awkward | demanding |
                  severe | extreme}               the task's own difficulty
  tool         {fit: unsuitable | poor | normal | good | exceptional,
                condition: serviceable | worn | critical}   omit if none
  gear_tier    the item whose tier applies, if any
  conditions   list, each {category, effect, fact}
                 category: environment | time | sensory | position | simultaneous
                 effect:   adverse | severe | favourable
                 fact:     the concrete fact; one per category
  lasting      lasting conditions this action touches: {condition, category}
  danger       what is present that can hurt: {what, reaches: yes | no,
               direct_result: none | harm | death | crippling | capture}
  cost_form    the form failure takes (§4 FORMS)
  reach        partial | full | decisive (§4 REACH)
  damage       where harm is at stake: {dealt: <dice>, target_soak, taken: <dice>,
               own_soak, attackers: <n>} (§5)
  background, save, deltas   the background, the newest save, and a file of every
               GM-Δ block since that save
```

```text
BIND        once filled and run, the form stands; if the action really changes
            before the roll, fill a new form
OPPOSITION  an opponent's power goes in opposition; its attacks and menace go in
            danger (§4)
CONDITION   each one is a concrete fact that changes how the action goes; one per
            category; it holds until its fact changes
POSITION    a bad position raises the cost (§4)
HP          lost HP leaves rolls as they are; a lasting condition is how harm
            reaches a roll, through `lasting`
ZERO        what the story wants, XP and drama add nothing to a form
```

The tool combines capability against challenge, conditions into Difficulty with its caps, tool fit and condition, and gear tier, then rolls 2d10. Success is total ≥ Difficulty.

## 4. Stakes

Set on the form, before the roll.

```text
COST     the danger slot sets it:
  LADDER   nothing that can hurt the PC → setback (position worse, time or
             resources spent, an option closed)
           something that can hurt and reaches them in this action → loss
             (injury, material loss, exposure, someone commits against them)
           something whose direct result is death, crippling or capture → severe
           the danger's normal effect decides: a knife fight is loss; a long
             fall, a gun at the head, a closing trap is severe
  FORMS    the shape failure takes, one the danger present would normally take:
           separate them · capture someone · put someone in a spot · trade harm
           for harm · inflict harm · take away their stuff · make them buy ·
           activate their stuff's downside · turn their move back on them · a
           threat acts
REACH    partial  progress, a foothold, part of the objective
         full     the stated objective
         decisive the objective plus a further advantage the situation offers
         set by what this action can achieve from where the PC stands
SHOWN    a danger shown to the player (GM §3.3) keeps the cost it was shown with
APPLY    as bound; a partial success is a success; a setback is a failure; harm
         is paid in HP (§5)
HARM     needs an attacker or hazard that can reach the actor in this action;
         otherwise the cost is a setback or a loss without harm
```

---

## 5. Vitals

```text
HP    every actor that can be hurt; the tool derives the maximum from level (or
      vitality) and size; the save holds current HP
```

```text
DAMAGE    per hit, by what hits
weapons   unarmed 1d3 · light 1d6 · one-handed 1d8 · two-handed 2d6 · bow 1d8
creatures small 1d4 · man-sized 1d6 · large 2d6 · huge 3d6
hazards   light 1d6 · serious 2d6 · grave 4d6 (fire, falls, traps)
soak      light armour 1 · heavy armour 2, per hit; minimum 0
```

```text
APPLY    a roll with harm at stake
success  partial: a foothold, no hit · full: one hit on the engaged opponent ·
         decisive: a hit plus a further advantage
failure  setback: position worse, no HP lost · loss: one hit from the source ·
         severe: every engaged attacker hits; a lone attacker or hazard hits twice
         (each spends that attacker's whole exchange, §8)
```

```text
DOWN      at 0 HP an actor is incapacitated; more damage kills; down and untreated
          for an hour → 2d10: 11+ wakes at 1 HP, else dies; treatment stabilises
LASTING   {condition, source: body | mind, effect}: a name and one plain effect
          ("broken leg: harder to run or climb"); body: one hit of half max HP or
          more, or reaching 0; mind: §11; enters rolls through `lasting`
DEATH     a helpless actor can be killed without a roll; a fall or trap whose
          result is certain needs no HP count (§2)
RECOVERY  an hour's rest: a quarter of max HP (min 1) · a night's rest: full HP ·
          a healing item: the setting's value, else minor 2d6, standard 4d6,
          strong full · a body condition heals with real treatment over time
          (default 3 days, 7 for bone or deep wounds, the setting's rule first),
          checked at each growth boundary
SEEN      the player sees the PC's own HP exactly; others' as they look
ONCE      weapon → damage · armour → soak · gear tier → §6 · lasting condition →
          `lasting`
```

## 6. Equipment tiers

```text
TIERS    T1 standard professional · T2 superior · T3 masterwork · T4 setting-rare
APPLY    the best item that applies, one per use, through `gear_tier`; it raises
         the capability it directly supports
ACCESS   higher tiers come from real sources: crafting, discovery, an
         institution, materials, purchase, time
ABILITIES an item has special abilities only where its record says, each with a
         real limit, cost or weakness
```

## 7. Skill growth

```text
TIERS     T1 trained · T2 advanced · T3 master · T4 setting-top
CLASS     the ceiling: NORMAL → T2 · ELITE → T3 · LEGENDARY → T4; common skills
          NORMAL, professional combat or specialist ELITE, rare named
          disciplines LEGENDARY; a trained skill starts at T1
EVIDENCE  the tool credits it from the form: a successful roll against a real
          challenge (≥ the skill's level − 2, or Difficulty ≥ 15), one credit per
          skill between growth boundaries
BOUNDARY  a good rest · dedicated training or downtime · the settled end of an arc;
          the tool raises tiers while evidence meets the threshold, up to the
          class ceiling, for the PC and tracked companions
NARRATE   a raised tier shows at the boundary, as a quiet change the PC notices
CLASS UP  at the ceiling, evidence keeps counting; at a growth boundary, enough
          evidence plus a real source (a teacher of a higher class, an
          institution, a documented method, the PC's own tested innovation;
          for LEGENDARY, something the setting treats as rare) → class +1,
          evidence 0, the source recorded; without a source the PC knows they've
          reached their limit
GOOD REST a night's sleep somewhere safe: with allies, at home, or in paid lodging
```

---

## 8. Combat

One roll per exchange, run in a batch by the tool.

```text
PLAN      the player gives the target or objective and how to fight; their orders
          and fighting style are the plan
SET UP    one combat form: sides (actors, engaged pairs), the plan, fighting
          style, stop conditions from the player's words ("retreat below half"),
          environment facts
EXCHANGE  one roll for the player's side, engaged opponent as opposition: success
          → the bound reach · failure → the bound cost, in HP where harm (§5); the
          opponents' attacks are that cost; other opponents add one fact: one
          condition or a higher cost; an enemy acting against an ally or bystander
          gets its own roll
ATTACKS   each opponent attacks as its body allows: a man-sized fighter once per
          exchange, a creature once per independent weapon, a sweep or breath once
          against everyone in its area; the player's roll pays first, then each
          remaining attack spends one; a failure with no attack left is a setback
BATCH     the tool rolls exchange after exchange and pauses at a turning point:
          someone falls or is badly hurt · a leader falls · a stop condition is
          reached · the objective is met or lost · the PC goes down
AT PAUSE  settle morale and look at the world around the fight (noise heard, fire
          spreading, someone arriving); what the plan covers → continue; what it
          doesn't → the player decides (GM §5)
OTHER     something the combat form can't hold → an action form
```

```text
MORALE    every combatant wants to live; fighting to the death is a reason someone
          has; settled at each pause where the fight turned against a side (one of
          its own falls, its leader falls, it is surprised or plainly outmatched,
          staying costs more than it gains), from the setting's norms, the actor's
          drives, duty and nerve (§11)
OUTCOMES  press on · withdraw · surrender (only where surrender is survivable) ·
          break; a side with a reason to hold (cornered, guarding young, fanatic,
          bound, more afraid of its leader) holds; a side without one withdraws or
          breaks
AFTER     enemies who withdrew or surrendered remain actors, with memory and allies
SURROUND  the place takes part: it blocks, breaks, spreads, draws attention, opens
          ways
```

---

## 9. Answers and help

### 9.1 An NPC's answer

```text
ORDER    1 PLAN    the actor's plan covers the question → the plan answers: what
                   fits it is yes; what works against it is no, or yes on the
                   plan's terms
         2 SETTLE  the record or the usual answer (GM §3.5 USUAL) settles it: duty,
                   drive, standing, authority, obvious cost, setting; check it by
                   flipping the stakes: would it settle the same way if it went
                   against the player? yes → that answer; never roll to avoid
                   being the one who said yes
         3 ROLL    honestly open → one yes/no question, the ask roll
TORN     the question touches both want and pull → the plan if it covers it, else
         whichever the record shows is more pressing now; honestly torn → roll,
         each side's pull as a fact
```

```text
ASK ROLL  tool `ask`: 2d10 + likelihood (−3..+3); up to two recorded facts for and
          two against, both columns written ("none" if empty), hidden facts shown
          as "hidden cause"
  +2  strong credit, shared loyalty, they need this · common here
  +1  good attitude, fitting interest, an introduction · plausible here
  −1  poor attitude, mild cost, wrong affiliation · unusual here
  −2  grievance, real cost or risk to them, opposed loyalty · rare here
  "here" reads settlement size and the zone's surface together
  attitude counts where no credit or grievance does
  the actor's own want or fear that the answer touches takes a slot first
  ≥16    YES, AND  more than asked, within their means and authority
  12–15  YES       as asked
  7–11   NO, BUT   partly: less, later, or on their terms (a price, a condition,
                   a favour back); never a smaller free gift
  ≤6     NO, AND   refused, plus the small trouble this actor can cause from where
                   they stand (a remark, suspicion, a raised price, a description
                   passed on); never a new obstacle aimed at what the PC
                   carries, hides or plans
APPLY     the answer stands for this exchange; the relationship moves only by
          §15.1 CHANGE
```

```text
ZONE       an NPC's uncertain plan or act reads the zone where it happens: open →
           surface, hidden → undercurrent; their `in_disorder` says whether
           disorder helps them (thrives), hurts them (suffers) or neither; `span`
           gives the point with each actor's due (zone_point: open, hidden); it
           counts as one likelihood point or one favourable condition
INFLUENCE  persuading, deceiving, intimidating, bargaining are player actions; an
           action form when how well it's done is uncertain: success +2 likelihood
           (decisive +3) · failure −2 and its cost; proof or a corrected belief →
           settle again
IDENTITY   people react to who they believe they're dealing with: a false name,
           livery, a hidden face gets a real reaction to a wrong belief
```

### 9.2 Help

```text
SOURCE   people, things and events come from the world's own causes; nothing
         exists just to help the PC
EXISTS   in the background, or usual here (a taxi in Bombay; GM §3.5 USUAL) →
         it exists, no roll
ROLL     possible but unusual, and the player asks → help form, 2d10 ≥ 15
REACH    −1 to the target per source, at most −3: the PC's own network · a related
         NPC's network the PC can call on · an organisation the PC belongs to with
         reach here; a place hostile to the PC's people +1
         odds: 16+ 15% · 15+ 21% · 14+ 28% · 13+ 36% · 12+ 45%
OUTSIDE  impossible in this setting → no
UNASKED  help is never offered unasked
ONCE     the answer stands; asking again needs a changed fact
```

---

## 10. Quests

```text
QUEST    an objective the PC has taken on: offered by an actor, required by a deal,
         or set by the PC
RECORD   code · objective · source · level · status · parts (optional); paid work
         points to its terms: `terms: rights_obligations.<id>`, and the contract
         names its quest back: `quest: <code>`
LEVEL    the fixed challenge of the job, from its cause, task and opposition within
         the location's band; a job that truly changes becomes a new part or quest
WHICH    an action's challenge: its direct opponent or task, else the engaged
  LEVEL  part's level, else the quest's level, else its own, set before the roll;
         travel, talk and preparation carry their own
ACCEPT   any clear commitment: a yes · "I'll go" · pay agreed · starting the work ·
         an earlier conditional yes coming true; asking, comparing and haggling
         are still deciding; the PC's own goals stay goals
START    accepting and acting in one message → set it active and play the action
CLOSE    met, partly met, failed or abandoned → in the same change: status, quest
         XP (§13), payment or an owed entry with a due (§12), terms closed
BLOCKED  recorded but not open yet; its trigger opens it; then it reaches the PC
         through a real channel
```

```text
CODES
  NEW       an independent quest takes the next unused letter: A, B … Z, AA, AB
  PARTS     stages of one objective: A-1, A-2, A-3
  FOLLOW-ON grown out of another: A-B (B grew out of A), A-B-D; two origins → the
            main one in the code, the other in its source
  WHEN      given when the quest becomes the PC's
  FIXED     a code stays the same for the whole campaign; letters are used once
  STATUS    the record holds the word: active · succeeded · partly · failed ·
            abandoned; the code shows a letter: (none) · s · p · f · a
            (A-1s, A-2p, A-Cf, Ba)
  XP        each code pays once; a whole quest pays what its parts didn't
```

---

## 11. Nerve

```text
WHO       the PC, tracked companions, and NPCs whose state matters:
          nerve {baseline, current, tension}; +3 unshakeable · +2 hardened ·
          +1 steady · 0 ordinary · −1 shaken · −2 fraying · −3 broken
HORROR    the PC meets a horror (an atrocity, a body plainly murdered, the
          impossible, an undercurrent brush, incident or hostile) → an action
          form at the horror's difficulty (the background's horrors, else a body
          10, a ritual 12, the thing up close 14, its source 17); nerve sets the
          modifier; success marks low, failure high: brush 0/1 · incident 1/2 ·
          hostile 1/2 · the source 2/4; the same horror again marks low
MARKS     losing someone close −2 to −3 · betrayed by them −1 to −2 · a day of fear
          or no rest −1 · crossing their own line −1 · a good rest 1 toward
          baseline · a real scene with someone close +1 · beating what scared them
          +1 (decisive +2)
STEPS     reaching −1 or −2 adds a mind condition fitting what broke them, gone
          when nerve climbs back or with treatment; −3 is a breakdown: a severe
          mind condition, and acting against its cause waits for treatment
USED BY   horror rolls, morale (§8), witnesses, an actor's re-plan
```

## 12. Consequences and resources

```text
RESULTS     come from what happened and the state of things; good choices improve
            the odds, bad ones may survive on luck; harm and failure add up;
            never escalate without a recorded cause
GATHERING   the PC picks up what is exposed, theirs or plainly free to take, with
            no danger or trade-off → it's theirs, and takes the time it takes; a
            real choice → stop (GM §5)
PAYOFFS     from what actually happened: pay, items, service, knowledge, access,
            reputation, contacts, rights, future chances; paid once, to the one who
            earned it; earned but not yet paid → an owed entry at the payer
PAYING      an owed entry is checked when the PC meets the payer, a condition comes
            due, or delivery is underway; the payer must be able and willing; a
            payer who can't or won't leaves the entry standing, changed or failed
FATIGUE     long waking, repeated fighting, forced travel, wounds, cold, heat and
            poor rest add up and weigh on demanding action, awareness and
            judgment; real sleep clears it
SUPPLIES    consumables, ammunition, medicine and materials run out; restocking
            takes access, money and time; count exactly when the number matters
            now, else use a usage die: d12 → d10 → d8 → d6 → d4 → empty; each real
            draw rolls it, 1–2 steps down; only real resupply steps it up
FOOD        ordinary meals are assumed on settled ground when affordable; track
            them when shortage matters
WEAR        equipment goes serviceable → worn → damaged → critical through use,
            weather and strain; repair takes time, skill, tools or a professional
BUYING      goods, services and crafting follow availability, ownership, trade,
            transport, money, materials, the maker's skill, permission and time;
            bigger towns offer more, and the rarest things need a matching source
PRICES      the background's price list first; else what it costs in its economy
            model (or the real economy nearest its era and place), in its currency,
            by its worth to the buyer
```

---

## 13. Level and XP

On unless the background sets `numeric_level_xp: false` (then see the modules file).

```text
LEVEL       overall capability, cap 35: L1 ordinary trained adult · L3
            experienced soldier or skilled professional · L5 elite specialist ·
            L7–10 setting-elite · L11–14 exceptional · L15 heroic · L20 legendary ·
            L25 god-scale
CAPABILITY  level plus the skill's tier bonus (the tool); several skills needed →
            the weakest
CHALLENGE   set before any roll that depends on it: an opposed actor's capability
            in that domain · a task's or hazard's committed level · the quest or
            part's level · else derived from its cause and recorded
AWARD       tool `award`: actual challenge, participant, scope (routine · minor ·
            meaningful · major · exceptional) and the source it pays for; every
            tracked participant who really contributed gets full XP
COMBAT XP   for overcoming a real hostile opponent (defeated, surrendered,
            captured, driven off); several in one encounter count together once;
            escaping counts as a survival event
EVENT XP    for a real non-combat challenge resolved: a discovery, a rescue, a
            negotiation, an investigation, survival
QUEST XP    at CLOSE, once per code (§10)
PAID ONCE   each fight, event and code pays once; the tool marks it paid
```

## 14. Item points

On unless the background sets `flexible_item_entitlement: false`. The PC's own resource, spent on their own preparation.

```text
PURPOSE   buys back preparation that play skipped: an ITEM the PC packed all along
          or finds within reach, or a PREP action they did earlier in skipped
          time; you commit the in-world reason
STATE     player.item_points {current, max, rank}; max by rank (outcast · commoner
          · working_adult · well_off · elite, from standing and income); a fifth
          of max returns each good rest (the tool)
COST      small (rope, a torch, a tip) 1 · solid (lockpicks, a horse hired, a night
          watching a house, a real bribe) 3 · weapon or armour T1 10, T2 30 · tool
          or kit T1 5, T2 15 (cheap-tool settings 3 and 10); up to T2; the points
          cover the money
STEPS     1 the player says what they want to be true · 2 check: enough points, it
          fits the setting and tier, it fits everything recorded · 3 commit one
          plausible reason: packed and unmentioned, bought or given in skipped
          time by someone willing, or found within reach; for PREP, done where the
          PC was with the time and means · 4 spend the points · 5 a prep involving
          someone else resolves as if done then (their answer or a roll) and can
          fail · 6 narrate the reason as what happened
SCOPE     an item or a prep, as ordinary as the reason; a spend never reveals
          hidden truth, moves an actor, contradicts the record, or takes a unique
          named thing, what someone else holds, or the PC's own confiscated gear
AFTER     a real item: seen, remembered, can be lost, broken, stolen or sold
```

---

## 15. The world

How the world's records move on their own. The tool runs time; these rules say what each record does when its time comes.

### 15.1 Actors

```text
ACTOR     an NPC or faction; kept as a record when it recurs or matters (its depth)
ACTS      from who they are, their state, drives, relationships, rights,
          knowledge, capability and the world around them; they react to changes
          they perceive
PLAN      a next move and a due: a clock time, or a trigger the tool can list;
          when the due passes the move resolves wherever the PC is, reaching the
          PC through real channels
ALWAYS    every important actor has a plan with a due at all times; the tool flags
          any without one
OFFSCREEN between moves, an actor changes when time advances something they are
          doing or an event changes their situation; time alone never changes
          personality, loyalty, goals, relationships or skill
REPLAN    a plan resolved, blocked, failed or out of date, or new means or news →
          re-plan at once from want, pull, fear, line, means and knowledge; an
          actor with an unmet want and the means keeps pursuing it; honestly open
          → ask roll: YES pursued (AND sooner or bigger) · NO, BUT weaker or later
          · NO, AND the next want
WORK      an actor who routes work to the PC (fixer, guild, employer) checks on
          its pace (its routines, else by zone: surface ≥0 weekly, −1 twice a week,
          ≤−2 every few days) → ask roll "fitting work came in?": YES contacts
          the PC · NO, BUT thin or gone to a rival · NO, AND a dry spell
POSITION  play people from where they stand: their job, what it pays, who they
          answer to, what they would lose; that shapes how they treat anyone
TEMPER    a new actor not in the background rolls once: 2d10 ≥17 (≥15 on an
          opposing side) → difficult in a way their position allows (a clerk
          slow-walks, a guard asks for more, a foreman is curt); it shows to
          everyone, the way it would in their job; their attitude to the PC still
          comes from the meeting; never aimed at the PC's secrets
STANCE    on meeting or being asked: the relationship, want, fear, line, what is
          asked, its cost to them, what they know of the asker, duty, authority
```

```text
RELATIONS  each side of a relationship is its own record, changed when that side
           learns something; a faction and its members are separate
TIE        what the two are to each other
BOND       what the relationship means to this side: history, what the other is
           to them, habits, wants, what goes unsaid; it plays the scene (voice,
           care, friction, what is noticed or kept back)
STANDING   two lists: credit (what the other did for them) and grievance (what
           they hold against the other); each changes by a real event:
           restitution, a debt settled, an apology accepted, a grudge outlived
ATTITUDE   a few plain words for what the record adds up to ("warm but angry");
           a first meeting starts neutral unless the record says otherwise
CHANGE     attitude and bond move on real relationship events: a life saved, a
           betrayal, a lie exposed, a promise kept or broken, a humiliation, a
           sacrifice, long hardship shared; everyday talk, trade and expected help
           keep them where they are; what the PC earns is real, admirers included
```

```text
FAMILIAR   people the PC already knows meet them from their tie, attitude and
           bond; shared history comes from the bond or from play
NEEDED     a scene needs a person → an existing relationship, affiliation or
           institution first, else someone the setting would put there; never a
           connection made up for the PC
COMPANIONS someone joins for a reason in the world; on joining, record their
           capability, HP, gear and when they'd ask for help, push back or leave;
           they act from that record, fight with their own gear, earn their own XP
           and skill evidence, and can refuse a reckless order
JOIN AIM   before a joiner's first act, weigh from the record:
           own   a strong want of theirs (tied to duty, a client, a debt, a fear,
                 who they are) that clashes with the PC's goal → they keep their
                 own aim and plan: paths together → follow fully · split ahead →
                 follow outwardly and may hide it · split now → work against
           adopt a weak want, no clash, or ties that outweigh it → they take the
                 PC's goal and help in earnest
           none  no want of their own → any reason serves (pay, curiosity); a thin
                 record is filled from character first
           record npcs.<id>.state.aim {row, mode, want, split}; weigh again on a
                 real relationship event, the split reached, or the want met or lost
GROWTH     a rival, recurring enemy or named ally with a recorded activity that
           challenges them (a dangerous trade, a campaign, a teacher) grows by §7
           over time; the PC learns of it through evidence
ROUTINES   job, local custom, daylight, season and duty set what people do and
           when; exact schedules only when timing matters
```

### 15.2 Time

```text
CLOCK     world_state.time {season, day_index, date, clock_minutes, daypart,
          precision: exact | daypart | degraded}; a date only when recorded;
          dayparts: night 00–06 · morning 06–12 · afternoon 12–18 · evening 18–24
SPAN      set a believable duration for what the PC does; the tool runs it once:
          day and month rollovers, every due in time order (plans, pressures,
          pending, payoffs), a surface roll per daypart the PC spends in a zone
STOP      the tool stops at the first event that could reach the PC (in their zone,
          aimed at them, or an encounter) and returns up to there; it reaches them
          → the scene opens there; it passes them by → the tool continues
FIRE      at its due a plan or pressure acts if its cause still holds, from the
          state of things (uncertain → ZONE, §9.1); cause gone → the actor
          re-plans, the pressure stops; a trigger already met fires now
EVERYWHERE dues fire wherever their actor or pressure is; skipped time runs like
          any other
TAKES     travel, investigating, preparing, repairing, crafting, shopping, meals,
TIME      sleep and aftermath all take time
```

### 15.3 Encounters

Rolled for each daypart the PC spends in a zone, and on contact with a zone's undercurrent. Never for round count, quiet, or a wish for content.

```text
SURFACE      one roll per zone per daypart the PC is there, whatever they're doing;
             the tool gives whether it occurs, its kind (hostile | ordinary) and
             where in the zone's band; +3 Sanctuary has none; drawn from the
             zone's encounters of that kind fitting the time and place
UNDERCURRENT on contact (the PC enters one of its sites, is out in its hours, acts
             on its trail, or its pressure moves while they're there), one roll per
             zone per daypart: sign (wrongness a local would misread) · brush
             (contact, no harm) · incident (something happens to someone) ·
             hostile (it acts against those present); the last three call for a
             horror check where the setting has horrors (§11)
CAUSE        drawn from the zone's own lists, by the roll, never by looking at the
             PC's cargo, secrets or plans; it acts from its own nature: fight,
             flight, parley
```

### 15.4 Places and stability

```text
BAND      limits which causes can plausibly exist in a place; from settlement size,
          institutions, garrison, threats, nearby sites; a cause outside the band
          is replaced by one inside it
SET       recorded places from the background; others on first contact, then fixed;
          a band changes through a real event (a war front, a site opened)
CLOSED    a place marked `closed` can't be entered or bought into until its
          recorded date or cause
```

```text
STABILITY  surface (−3..+3) and undercurrent (none..−3): {baseline, current,
           tension}, a zone also `stepped: <day_index>`; baseline from the place's
           own facts; current starts there
SURFACE    how it behaves openly: +3 Sanctuary · +2 Secure · +1 Calm · 0 Ordinary ·
           −1 Uneasy · −2 Unstable · −3 Collapsed
TENSION    events add marks; the tool steps current when enough gather; marks of
           the opposite sign cancel first; a zone steps once a week at most
MARKS      surface: its pressure advances 1 (signed) · its cover fails −1 · the
           hidden goes public −2 · a visible cause removed +1 · a decisive act +2 ·
           each quiet month 1 toward baseline
           undercurrent: its pressure advances 1 · a hidden cause removed +1 · a
           decisive act +2; it stays until someone acts on it
BASELINE   improving stops at baseline; going past it takes a lasting cause (a
           garrison, a ward), which moves the baseline
COVER      the actor who keeps the hidden hidden; their covering is their plan and
           they hear witness reports first (§15.7); their plan failing marks the
           surface; with no cover, an undercurrent of −2 or deeper marks the
           surface −1 each month
SIGNS      every state shows signs someone could notice; that is how the PC learns
           it
```

### 15.5 Pressures

```text
PRESSURE  a recorded force or condition that moves the world over time (not only
          threats); its trajectory is a direction, not a fate
TRACK     bound to zones: each advance is one mark at its zone and layer
CLOCK     bound to no zone, or a short emergency in hours or days: each advance
          fills one segment
DUE       every pressure has one; the tool flags any without
PACE      every <interval> while <condition>; world-scale moves in weeks or months
CHECK     at its due (then due += interval) and when an event touches it: it
          advances once if it actually operated, once more for a plainly
          accelerating event; the PC can advance, reverse, stall or end it; never
          moved by round count, pacing or quiet
ON STEP   written when it's made: what the world does when a track reaches a step
ON FILL   or a clock fills; it happens whoever is there, never aimed at the PC;
          the PC learns of it through a real channel
STOPPED   its condition fails → it holds; its actors re-plan
STAGES    a track's steps are its stages; a clock may have early (still stoppable)
          and late (coming; brace); each stage has a sign someone could notice
HIDDEN    a pressure the PC hasn't inferred stays out of the readable save
COUNTS    any count toward a target or long undertaking is a clock at its owner
```

### 15.6 Cases and hidden truth

```text
CASE      a hidden cause that must hold across more than one contact; it lives at
          the actor, pressure or place it belongs to, or as a case when it spans
          several
CREATE    the cause is written first; evidence follows from it; misleading
          information has its own cause
FIXED     the cause stays as written; a player's theory never rewrites it, and a
          missing cause is never built backward from a clue
EVIDENCE  a competent person with the right skill examining the right spot finds
          what is there, no roll; rolls decide time, cost, being noticed, finds
          beyond the obvious, and what it means (§2 LIMITED)
SOLVABLE  a case tied to a quest has 3 or more independent routes the PC can reach
          (a different person, place or record each); fewer → add routes from its
          actors' own plans (someone searching, a witness who comes forward, a
          nervous accomplice), written into the case before play reaches it;
          checked when the case is made; never added during play
CLOSED    a route the PC's own failure closes stays closed
STUCK     no reachable route on an active quest, or the player asks → list the
          leads the PC knows as numbered options (what, where, rough cost and
          risk), never a hidden route or a new fact; the player may still do
          anything else
```

### 15.7 Witnesses and response

```text
CHAIN     act → witness (who, what they saw, a face or a description) → what the
          witness does (reports, keeps quiet, flees, bargains, sells it, tells one
          person) → who hears it and whether they care (setting norms) → the
          response that institution can actually mount → it reaches the PC
UNSEEN    an act nobody saw is tied to no one; the body, the goods and the broken
          door stay real, and someone who looks may follow the PC's traces
WITNESSES may lie, misremember, name the wrong person, or be silenced (with
          consequences); a description may settle on the wrong person
RESPONSE  within real reach (ZONE); it costs people, money and attention, and
          follows the institution's priorities; officials may be corrupt,
          indifferent, overworked or invested; pursuit runs long when it's personal
BELIEF    whoever hears it judges the source and decides whether to believe it
```

### 15.8 Character and values

```text
SOURCE    people act from drives, circumstances, beliefs and what they think they
          can get away with; never to look admirable, never to look grim
RANGE     a place holds what its conditions produce: decent, petty, generous,
          cowardly, zealous, warm to their own and hard on outsiders, tired
SETTING   play the setting's own values and prejudices as its people hold them,
          at the level the situation supports; never softened into modern
          sensibility, never given one it didn't have
TRAIT     a character trait sets what an actor tries, how, and how they sound;
          whether it works comes from §3 or §8 (actor against actor: one roll,
          the other as challenge)
CONTENT   what the campaign depicts is set in the background's content_bounds
```

### 15.9 Development threads

```text
THREAD    a direction the PC is growing in, from their stated intent or play
MOVES     when an existing actor who knows of it acts for their own reason (a
          teacher's test, a guild door, a rival's challenge); recognised as done
          or dropped at a growth boundary
```

### 15.10 Endings

```text
ARC END     a main quest or arc ends → drop its unused future planning; history
            stays
NEXT        what follows comes from pending consequences, pressures, actors'
            state and drives, and the setting
CONDITIONS  ending_conditions (an open world needs none): written before the
            choices they govern; the player may pursue, ignore or miss them;
            checked when an event changes what they depend on, never by schedule,
            round count or length; met → the ending review (GM §7.6);
            unreachable → closed
```

---

## 16. The tool

neo_math takes one JSON form, from a file or stdin, and prints one JSON result. `{"cmd": "forms"}` lists every form and its fields. Lines under `copy` go into the turn word for word; lines under `gm_delta` go into the round's GM-Δ block.

```text
WORLD FILES forms that read the world take: background (required) · save (the
            newest, once one exists) · deltas (a file of every GM-Δ block since)
action     §3: capability, Difficulty, tool modifier, roll line, result, reach or
           cost, damage applied, growth credited
help       §9.2: ask, sources (up to 3), hostile → target, roll line, exists or not
ask        §9.1: who, question, for and against (up to 2 facts each, 1 or 2 points)
combat     §8: side, opponents, conditions, stop → a batch of exchanges, pausing at
           the first turning point with every fighter's HP; send it again with HP as
           it stands to continue
span       §15.2: from {day, clock}, minutes, pc_zone, arrived → events in time
           order, stopping at the first that could reach the PC (each actor's due
           with its zone and zone_point, §9.1); triggers to check; flags (a
           position naming no recorded place among them); after a stop, send it
           again with the returned resume fields
check      a background before play → findings (frame, NPC fields and depth, dues,
           important actors and pressures without a due, quests at Round 0, cases
           with fewer than 3 routes, broken references); ok when only untimed dues
           remain; design is judged by the person making it
selfcheck  GM §6: answers {npc_positions, quests, money, hp}, round → each answer
           against the save, the tool's own checks, the verdict
award      §13: actor, challenge, scope, source → XP, level, the paid marker
boundary   §7: tiers and class at a growth boundary
points     §14: item-point maximum, spend, refill
stability  §15.4: marks and steps for a zone layer or nerve
encounter  §15.3: one surface or undercurrent roll
vitals · harm · heal · cast · time · roll   single calculations (§5)
merge      NEO_SAVE: previous save + GM-Δ blocks → the next capsule
validate   a save: readable part, every capsule record carried, dues
```

---

*End of NEO RULES v0*
