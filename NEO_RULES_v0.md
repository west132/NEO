# NEO RULES — v0

How the game resolves: what a human referee with dice would work out the same way. The GM (NEO_GM) calls a section when its flow step needs it; WORLD holds every fact these rules read.

```text
TOOL     neo_math owns every number: rolls, modifiers, caps, bands, damage, XP,
         growth, points, dues; this file never restates its maths
INPUT    the GM fills a form; the tool reads it as a JSON file or stdin, never as
         command-line text; values the save already holds (level, tier, HP, gear)
         are read by the tool from the save, never typed by the GM
OUTPUT   the tool prints the roll line; the GM copies it verbatim, never retypes
NO TOOL  without a code tool there is no roll; the GM says so and stops
FORMAT   terse rules; tags (§x, In) are references, never restated
```

---

## 1. The law

The law is GM §1. Tags I1–I12 in this file cite it.

## 2. Possibility

```text
violates recorded reality  → IMPOSSIBLE
far beyond plausible capability/support  → IMPOSSIBLE
domain gate blocks required knowledge  → LIMITED or IMPOSSIBLE at that depth
uncertain  → ROLL
otherwise  → DETERMINISTIC
IMPOSSIBLE  no roll, no lowered difficulty; show only the visible reason
RETRY  repetition never makes it possible; needs changed leverage, information,
  position, tools, assistance, timing, or conditions (I10, I11)
DOMAIN GATE capability never replaces missing knowledge; interpretation depth ≤
  recorded skill/expertise/access; another actor's expertise changes
  feasibility or gives their own conclusion, never the player's capability
```

---

## 3. The action form

Every uncertain action is one form. One slot per thing: a fact goes in exactly one slot (I8).

```text
FORM (JSON)
  actor        id of who acts
  action       one line, what they attempt
  skill        skill exercised (tool reads level and tier from the save)
  opposition   one of:
                 {actor: <id>, domain: <skill>}   an opposed actor (tool reads
                                                  its capability)
                 {level: <n>}                     a committed task, hazard or
                                                  quest/segment level
                 {grade: forgiving | easy | ordinary | awkward | demanding |
                  severe | extreme}               no numeric challenge: the task's
                                                  own difficulty
  tool         {fit: unsuitable | poor | normal | good | exceptional,
                condition: serviceable | worn | critical}   omit if none
  gear_tier    the item whose tier applies, if any (tool reads its tier)
  conditions   list, each: {category, effect, fact}
                 category: environment | time | sensory | position | simultaneous
                 effect:   adverse | severe | favourable
                 fact:     the concrete state fact; one per category
  lasting      lasting conditions this action touches, each: {condition, category}
               — the category it hampers; counts once, in a category nothing else
               uses; the tool checks it is recorded on the actor
  danger       what is present that can hurt: {what, reaches: yes | no,
               direct_result: none | harm | death | crippling | capture}
  cost_form    §4 FORMS: the form failure takes, one the danger would normally take
  reach        partial | full | decisive (§4 REACH)
  damage       where harm is at stake: {dealt: <dice>, target_soak, taken: <dice>,
               own_soak, attackers: <n>} (§5 DAMAGE); the tool applies the hit
  lite         true for the one-line roll format
  capability_grade  only without numeric progression: deficient | basic |
               competent | advanced | exceptional
  background, save, deltas   the world files: the BACKGROUND, the newest save, a file
               of every GM-Δ block since that save
```

```text
BIND     the form is filled and the tool run before any dice; immutable after;
         the action materially changes before the roll → new form
CHALLENGE the opposed actor's or task's power goes in opposition only; its attacks
         and menace are the danger (§4), never also a condition (I8)
CONDITION nonzero needs a concrete state fact that independently changes execution
         and is counted nowhere else; a category counts once; keeps its value until
         its fact changes; never raised to enable skill growth
POSITION a bad position raises the cost, never also a condition (I8)
HP LOSS  changes no roll; only a lasting condition reaches rolls, through `lasting`
NEVER    narrative importance, desired outcome, XP hunger, drama → 0
DICE     genuine randomness only (I10); no critical-success tier
```

The tool combines: capability against challenge into the capability modifier, the conditions into Difficulty with its caps, tool fit and condition into the tool modifier, the gear tier into effective capability, then rolls 2d10. Success ⟺ total ≥ Difficulty. (Bands, caps and clamps: neo_math.)

## 4. Stakes

```text
COST     set by the danger slot, never chosen:
  LADDER   nothing that can hurt the PC → setback (position worsens, time or
             resources spent, an option closes)
           something that can hurt and reaches them in this action → loss
             (injury, material loss, exposure, another actor commits against
             them)
           its direct result is death, crippling or capture → severe
           a danger's normal effect decides: a knife fight → loss; a long fall,
             a gun at the head, a closing trap → severe
  FORMS    the form a failure takes, one the danger present would normally take:
           separate them · capture someone · put someone in a spot · trade harm
           for harm · inflict harm · take away their stuff · make them buy ·
           activate their stuff's downside · turn their move back on them · a
           threat acts; the ladder sets how bad, the form how it looks
REACH    partial  progress, foothold, part of the objective
         full     the stated objective
         decisive objective + a further advantage the situation offers
         set by what this action can achieve from here, never by drama
SHOWN    GM §5.3; a shown danger is never reduced, refused quietly, or its cost
         lowered after
APPLY    bound stakes as written; success-partial ≠ failure; failure-setback is
         still failure (I11); physical harm paid in HP (§5)
HP NEEDS an attacker or hazard that can reach the actor in the chosen action; else
         setback or loss without harm
```

---

## 5. Vitals

```text
HP   every actor that can be hurt
MP   actor with a power the setting draws from a pool
MAX  derived by the tool from overall level (or vitality), size, and best
     MP-drawing skill's tier; never stored; current HP/MP in actor state
```

```text
DAMAGE per hit, set by what hits, never by result
weapons  unarmed 1d3 · light 1d6 · one-handed 1d8 · two-handed 2d6 · bow 1d8
creatures  small 1d4 · man-sized 1d6 · large 2d6 · huge 3d6
hazards  light 1d6 · serious 2d6 · grave 4d6  fire, falls, traps, breath
powers  T1 1d8 · T2 2d6 · T3 3d6 · T4 4d6  damage or HP restored
soak  light armour 1 · heavy armour 2  per hit; minimum 0
```

```text
APPLY a roll with harm at stake
success  partial  foothold, no hit
  full  one hit on the engaged opponent
  decisive  hit + further advantage
failure  setback  position worsens, no HP lost
  loss  one hit from the source (engaged attacker or hazard)
  severe  every engaged attacker hits; lone attacker/hazard hits twice
  (spends each attacker's whole exchange, §8)
```

```text
STATES
HP > 0  no effect on rolls
HP 0  down: incapacitated; further damage kills
LASTING  {condition, source: body | mind, effect} — a name and one plain effect
  ("broken leg: harder to run or climb"); body: one hit ≥ ½ max HP, or reaching 0;
  mind: §11; enters rolls only through the form's `lasting` slot, applied once by
  the tool
down untreated 1 hour → 2d10: 11+ wakes at 1 HP, else dies; treatment/healing first
  stabilises
OTHER DEATH  helpless actor killable without a roll; certain fatal failure needs no
  HP (§2); crippling and capture stay severe costs
```

```text
RECOVERY
1 hour rest  ¼ max HP (round down, min 1)
a night's rest  full HP
healing item  setting's value; default minor 2d6 · standard 4d6 · strong full
body condition  never by rest; checked at each growth boundary; removed as its own
  transition (I7) after real treatment (healer, restoration power, strong
  healing item, tended rest) for its time: default 3 days · 7 bone/deep ·
  setting's own rule (BACKGROUND/canon) wins
MP  BACKGROUND mp_powers.recovery: fast = full after ~10 min out of danger ·
  slow = ¼/hour rest, full on a night · rest_only = full on a night
CASTING  cost by the power's tier (tool), paid on cast whether it works or not; no
  power above caster's tier; not enough MP → no cast; BACKGROUND mp_powers names
  MP powers; others follow their setting rule
VISIBILITY  player sees own HP/MP exactly; others only as observable (I5, I9)
COUNT ONCE  weapon → damage only · armour → soak only · gear tier → §6 ·
  HP loss changes no roll · lasting conditions are harm's only way to rolls (I8)
```

## 6. Equipment tiers

```text
SCOPE  improves only directly supported capability; external to personal mastery
TIERS  T1 standard professional | T2 superior | T3 exceptional/masterwork |
  T4 setting-rare/artifact-scale
APPLY  the strongest applicable item, one per use, through the form's gear_tier
  slot; never rewrites level; never also tool fit (I8); boost values: tool
ABILITIES  only where design and source record them; limited effect with real
  condition, limit, cost, weakness, or range; adds no capability levels
T4 AUTHORITY only if concept and setting support it; bounded, counterable; never above
  superior recorded law/authority
LIMITS  never grants unrelated expertise or skill tier; higher tiers need rare,
  plausible access (crafting, discovery, institution, materials, transfer,
  cost, time)
```

## 7. Skill growth

```text
class ceiling  NORMAL → T2 | ELITE → T3 | LEGENDARY → T4
tier  T1 trained/specialised | T2 advanced | T3 master | T4 setting-top
default class  common/general NORMAL | professional combat/magic/specialist ELITE |
  rare named discipline LEGENDARY
start  unspecified trained skill T1; higher needs explicit mastery evidence
QUALIFIES  the tool decides from the form, and credits evidence itself:
  a successful, materially distinct roll; the skill bound before dice; numeric
  challenge ≥ personal skill level − 2, or
  Difficulty ≥ 15
LIMITS  failure 0 · each bound skill once per roll · never incidental skills ·
  never another actor via this roll · routine/easy/deterministic use and time
  never advance · training only via a distinct challenge · gear and tool fit never
  change eligibility · Difficulty never raised for growth
PERIOD  one credit per skill between growth boundaries; the tool keeps the list
BOUNDARY  good rest · dedicated training/downtime · settled aftermath of a resolved
  arc; never ordinary time passing or a lull mid-scene; the tool raises tiers
  while evidence meets the threshold, up to the class ceiling, for every tracked
  actor (player + tracked companions)
OVERFLOW  carries while another tier remains; at the ceiling keeps counting toward
  a class raise
NARRATE  a raised tier at the boundary, as a quiet noticed change; never mid-action
```

```text
CLASS RAISE
CEILING  evidence keeps counting at the ceiling; experience alone never breaks it
SOURCE  (≥1, materially involved while the evidence accrued): a teacher whose class
  is above the actor's · an institution/tradition teaching at that level · a
  documented method the actor can access · the actor's own recorded innovation
  tested under real challenge · LEGENDARY only: a source the setting treats as
  rare (named tradition, transformative event, discipline few reach)
RAISE  at a growth boundary, at the ceiling: evidence meets the class threshold
  (tool) AND a valid source → class +1, evidence 0, record the source (history
  only; never counts for the next raise)
NO SOURCE  evidence keeps accruing, nothing happens; in play, the character knows
  they've hit their limit
UNREACHABLE source (unwilling master, rival guild's method) = a genuine obstacle
LEGENDARY  only where the setting has a rare source; else ELITE is the end
ABILITIES  T1 none · T2 ≤1 recorded · T3 2–3 · T4 (LEGENDARY) one narrow mastery or
  authority effect; must follow skill, setting, learning history
```

---

## 8. Combat

One roll per exchange, run in a batch by the tool.

```text
PLAN      the player gives target/objective and how to fight; fight orders +
          fighting style are the plan
SET UP    the GM fills one combat form: sides (actors, engaged pairs), the plan,
          fighting style, stop conditions from the player's words ("retreat below
          half"), environment facts
EXCHANGE  one roll for the player's side (an action form), engaged opponent as
          opposition; success → bound reach, no cost; failure → bound cost, HP
          where harm (§5); opponents' attacks ARE that cost, never separate rolls
          vs the player; other opponents = one fact: one condition OR a higher
          cost, never both, never extra rolls (I8); an enemy acting against an
          ally or bystander → its own roll
ATTACK    per exchange per opponent, as its body/weapons allow: man-sized fighter
  BUDGET  1; creature 1 per independent weapon; reach limits targets; a sweep or
          breath = one attack hitting each target in its area; the player's roll
          resolves first and pays its bound cost; every other attack spends one
          from what remains; failure with no attack left or out of reach →
          setback, not harm
BATCH     the tool rolls exchange after exchange and applies damage; it pauses at
          a turning point: someone falls or is badly hurt · a leader falls · the PC
          reaches a stop condition from the plan or style · the objective is met or
          made impossible · the PC goes down
AT PAUSE  the GM settles morale (below) and checks the world around the fight
          (noise heard, fire spreading, someone arriving); nothing the plan doesn't
          cover → the tool continues; something it doesn't → the player decides
          (GM §7)
UNCOVERED a case the form can't hold → an action form, never an invented mechanic
```

```text
MORALE  combatants have their own survival; to the death is a specific choice, not
  the default
SOURCE  setting norms (BACKGROUND norms) → actor drives, obligations, discipline,
  knowledge (I5), nerve (§11)
CHECK  at each pause where the fight turned against a side: one of its own
  falls/badly hurt · leader falls · surprised or plainly outmatched · retreat
  threatened · staying costs more than it gains
SETTLED  never rolled; no recorded reason to hold (cornered, guarding young/lair,
  fanatic, undead, bound, leader feared more than the enemy) → the losing side
  withdraws or breaks; can't safely surrender → runs if it can; surrender only
  from a break, only where survivable; holds until the situation materially
  changes
press on  objective/obligation still outweighs the cost
withdraw  disengages under own power, taking what it can
surrender  break where surrender is survivable: yields instead of running
break  cohesion fails; flight, panic
AFTER  withdrawn/surrendered enemies remain actors with memory, allies, future
ENVIRON  causally active: can block, break, spread, attract attention, open options
```

---

## 9. Answers and help

### 9.1 An NPC's answer

```text
ORDER    1 PLAN    the actor's plan touches the question → the plan decides, no
                   roll: fits it → yes; works against it → no, or only on the plan's
                   terms; a plan with a condition → the condition decides
         2 SETTLE  the record or the usual answer (GM §5.5 USUAL) settles it (duty,
                   drive, standing, authority, obvious cost, recorded fact,
                   setting) → that way, for or against the player, no roll; test:
                   would it settle the same way if the outcome flipped for the
                   player? no → open; never rolled to avoid being the one who said
                   yes
         3 ROLL    honestly open: one yes/no question, the ask roll
TORN     the question touches both the actor's want and pull → plan if it covers
         it; else what the record shows is more pressing now; honestly torn → ROLL,
         each side's pull as its fact
```

```text
ASK ROLL  tool `ask`: 2d10 + likelihood, clamp −3..+3; each point a recorded fact,
  visible or hidden (shown as "hidden cause"); both columns written ("none" if
  empty); ≤2 facts per column; both from the same record at the same specificity
  +2  strong credit, shared loyalty, they need this · common here
  +1  good attitude, fitting interest, introduction · plausible here
  −1  poor attitude, mild cost, wrong affiliation · unusual here
  −2  grievance, real cost/risk to them, opposed loyalty · rare here
  +2  canon mode: canon records this outcome, causes unchanged by play
  "here" = settlement size and the zone's surface, read together; an actor's own
  plan or act reads ZONE instead, never both
  attitude counts ±1 only where no credit/grievance entry counts (I8)
  the asked actor's own want or fear the answer touches takes a column slot
  first, at record weight
  ≥16  YES, AND  more than asked, within means and authority
  12–15  YES  as asked
  7–11  NO, BUT  partly: less, later, or on their terms (price, condition, favour
  back); never a smaller free gift
  ≤6  NO, AND  refused + smallest trouble from this actor's state and reach,
  proportionate (remark, suspicion, raised price, description passed on);
  never a new obstacle aimed at what the player carries, hides, plans (I6)
APPLY  the answer stands; narration never moves it; YES within means/authority;
  cost to them already in likelihood; sets this exchange, not the relationship
```

```text
ZONE  an actor's uncertain plan or act (never the PC's own) reads the zone where it
  happens: open act → surface · hidden act → undercurrent; in_disorder: thrives ·
  suffers · neither; points by zone step: tool; counts once: one likelihood point,
  or one condition in an action form (favourable at most), never both, never
  beside "here" (I8); surface −3: an institution's response cannot reach the zone
INFLUENCE  persuade/deceive/intimidate/bargain = player action; an action form only
  when how well it's done is uncertain; plain ask → no roll; feeds the answer,
  never replaces it: success +2 likelihood (decisive +3) · failure −2 + its bound
  cost · changed fact (proof, corrected belief) → SETTLE again; takes one column
  slot; a failure's bound cost may leave one grievance or belief, which later
  counts instead of −2, never beside it (I8)
IDENTITY  actors react to who they believe they deal with (I5): a false name,
  livery, concealed face, misattributed reputation → a real reaction to a wrong
  belief
```

### 9.2 Help

```text
NOTHING  a person, thing or event exists only from the world's own causes, never
         to help the PC
EXISTS   designed by the WORLD, or usual here (a taxi in Bombay; GM §5.5 USUAL) →
         exists, no roll
ROLL     possible but not usual, and the player asks → 2d10 ≥ 15
REACH    −1 to the target per source, each once, at most −3: the PC's own network ·
         a related NPC's network the PC can actually call on · an organisation the
         PC belongs to with reach here; a place hostile to the PC's people +1;
         the GM names the sources on a help form, the tool applies them
         odds: 16+ 15% · 15+ 21% · 14+ 28% · 13+ 36% · 12+ 45%
NO       impossible in this setting; never offered unasked
ONCE     a roll's answer is fixed; asking again needs a changed fact (I10)
```

---

## 10. Quests

```text
QUEST    an objective the PC has taken on: offered by an actor, required by a deal,
         or set by the PC; not intent, a pressure, or a case truth
RECORD   code · objective · source · level (for XP) · status · parts (optional)
         · terms at rights_obligations when paid (the quest points to them)
LEVEL    the fixed challenge of the undertaking, from its committed cause, task and
         opposition inside the location's band; player level, pay, pacing, XP
         appetite, roll, outcome → 0; immutable: a transformed challenge → a new
         part or quest
WHICH    an action's challenge: 1 its direct opponent/task · 2 the engaged part's
  LEVEL  level · 3 the quest's level · 4 its own, derived and bound before the roll;
         travel, talk, preparation, scouting, support don't inherit a quest level
ACCEPT   any clear commitment: explicit take/accept · a direct commitment ("I'll
         go") · pay agreed in talk or contract · starting the work without
         reservation · a prior conditional acceptance now true
NOT      asking, checking, comparing, negotiating without commitment; the PC's own
         stated goals are not quests
ON       set active before travel or work; acceptance + first action in one input
  ACCEPT → execute, no confirmation
CLOSE    objective met, partly met, failed, or abandoned → in the same change:
         status letter · quest XP (§13) · payment, else an owed entry with a due
         (§12) · terms closed
BLOCKED  a quest recorded but not yet open; its trigger opens it; the tool lists it
         at each time call; met → available, reaching the PC only by a real
         channel, or active if the PC is already in it
```

```text
CODES
  NEW       an independent quest takes the next unused letter: A, B, C … Z, AA, AB
  PARTS     stages of the same objective: A-1, A-2, A-3; no parts → just A
  FOLLOW-ON a case that grew out of another takes a new letter after its origin:
            A-B (B grew out of A); A-B-D (D grew out of A-B); two origins → the
            main one in the code, the other in its source line
  UNIQUE    the last letter is unique in the campaign, never reused
  WHEN      given when the quest becomes the PC's, never at design time
  FIXED     codes never change; carried across chapters
  STATUS    the record holds the word: active · succeeded · partly · failed ·
            abandoned; wherever the code is shown it carries the letter: (none)
            active · s · p · f · a (A-1s, A-2p, A-Cf, Ba)
  XP        each code pays once; a whole quest pays only what its parts didn't
```

---

## 11. Nerve

TRIGGER: horror witnessed (atrocity, a body plainly murdered, the impossible) · undercurrent brush, incident, or hostile · loss, betrayal, a day of fear, or a good rest, for someone tracked · an NPC pushed past their line.

```text
WHO  PC, tracked companions, NPCs whose state matters (witness, rival, cultist):
  condition.nerve {baseline, current, tension}; +3 unshakeable · +2 hardened ·
  +1 steady · 0 ordinary · −1 shaken · −2 fraying · −3 broken
HORROR  an action form with the horror's difficulty (BACKGROUND horrors, else a
  body 10 · a ritual 12 · the thing up close 14 · the source 17; ordinary violence
  never); nerve sets the capability modifier (tool); success low marks, failure
  high: brush 0/1 · incident 1/2 · hostile 1/2 · the source 2/4; the same horror
  again → low; 2+ marks at once → mind condition until a good rest
MARKS  horror as rolled · losing someone with a bond −2 to −3 · betrayed by one −1
  to −2 · a day of fear or no rest −1 · crossing their own line −1 · a good
  rest 1 toward baseline · a real scene with a bond +1 · a win over what scared
  them +1, decisive +2 · treatment by its own rule
STEPS  reaching −1 or −2 adds a lasting mind condition (§5) fitting what broke them,
  gone when nerve climbs out of that step or by treatment; −3 breakdown: severe
  mind condition, demanding action against its trigger infeasible until treated;
  BACKGROUND may make −3 an ending path
READ BY  morale (§8), witnesses, an actor's re-plan
COUNT ONCE  nerve's modifier only on horror checks; elsewhere it acts through its
  conditions (I8)
```

## 12. Consequences and resources

```text
CONSEQUENCE  transitions from the resolved event + state, no fixed penalty list; good
  decisions improve odds, not guarantee; bad ones may survive on luck; damage
  and failure accumulate; no escalation without a recorded cause
RECOVERY  collect routinely only if: material exposed, collection possible, ownership
  permits, taking is routine or reclaims player property, no real danger/
  legal/time/capacity/preservation tradeoff → update natural owner, consume
  material time; never auto-take disputed/owned/protected goods; never
  teleport bulk; real choice → stop (GM §7); once collected, canonical (no
  repeated commands)
PAYOFFS  derive from actual outcome + canonical sources; filter by ownership,
  authority, access, causality; apply once at natural owner; earned but
  undelivered → owed entry at the payer; any form (payment, items, service,
  knowledge, access, reputation, contacts, rights, future opportunity); 0
  valid; cash doesn't suppress others; never paid twice (I8); desire/quest status
  alone never create reward; training/access grant no counters or tiers;
  books/records grant possession/access; expertise only via real learning
DISCHARGE  an owed entry needs payer ability + willingness, contact/channel, met
  conditions; check on meeting the payer, a condition coming due, or a
  delivery underway; deliver once at owner, clear (I7); payer
  can't/won't → entry stays, changes, or fails (state, not error; I11)
FATIGUE  endurance shifts limits, not infinite unless recorded; wakefulness,
  repeated fighting, forced travel, wounds, toxins, cold or heat, poor rest
  accumulate fatigue → impair demanding action, awareness, recovery,
  judgement; substantial sleep reduces it; short rest never erases major
  sleep debt; stop only when rest vs continue is a real decision
FOOD/WATER  ordinary intake assumed in settled travel when affordable/available; track
  when shortage, cost, deprivation, wilderness matters
EQUIPMENT  serviceable → worn → damaged → critical/unusable; use, weather, neglect,
  strain worsen; maintenance preserves; real damage needs time, skill, tools,
  materials, or a professional; never silent repair
SUPPLIES  consumables, ammunition, medicine, preparations, repair materials finite;
  resupply needs a recorded process, access, materials/cost, time
TRACK  exact when the number matters now (arrows in a fight, specific antidote
  doses, last charges) · usage die for bulk (rations, oil, common ammo,
  bandages, feed, rope, reagents)
USAGE DIE  d12 → d10 → d8 → d6 → d4 → empty; material draw (real quantity: a day's
  travel, a night's light, a fight, treating a wound) → roll current die;
  1–2 → step down; below d4 → exhausted; incidental use doesn't draw; never
  resets or refills itself (not even "a kit"); rises only by real resupply;
  d4 visible to the handler; player learns the same way (I5)
ACQUISITION  items, services, crafting follow availability, ownership/authority,
  institutions/trade, location/transport, money/exchange, materials, provider
  capability, permission, time; settlement size and surface shift likelihood/variety,
  not a hard cap; ordinary work → appropriate source; superior → matching
  recorded capability; rarest → exceptional recorded source; a remote
  specialist may qualify; a metropolis guarantees nothing
  exception: an item point spend needs no merchant, channel, travel, time (§14)
PRICES  a price, wage, fee, or payment the BACKGROUND price list doesn't give →
  what it costs in BACKGROUND economy_model (none → the real economy nearest the
  setting's era and place), in the setting's currency, by its value to the
  buyer (quantity, quality, risk); quest level, pacing, player level → 0; a
  setting's own money rule wins
COSTS  track practical condition wherever it can affect play; never erase a real
  cost by omission
```

---

## 13. Level and XP

On unless the BACKGROUND sets `numeric_level_xp: false`.

```text
STATE  progression: {system: numeric_level_xp, state: {level, xp}}
CAP  35, persisted overall level only; domain capability may exceed it
LEVEL  overall capability scale, not universal knowledge; no actor reads another's level
CALIBRATION L1 ordinary trained adult · L3 experienced soldier/skilled professional ·
  L5 elite mundane specialist · L7–10 setting-elite/superhuman where the
  archetype supports it · L11–14 exceptional supernatural/high-end mortal ·
  L15 heroic major figure · L20 legendary, world-class · L25 god-scale · L35 max
CAPABILITY  actor capability = overall level + the relevant skill's tier bonus
  (tool); transient, may exceed 35, never rewrites level; several necessary skills
  → most limiting; incidental skills never lower it; no tracked skill → level only
  where archetype/trait/expertise records the domain
CHALLENGE  fixed before any dependent roll: 1 opposed actor → its same-domain
  capability (a new material actor commits capability first) · 2 persistent
  task/hazard/device/cause → its committed level · 3 directly applicable
  quest/part → its committed level · 4 one-off task → derive from cause truth,
  bind before the roll; recurring → commit at its owner; never inferred after from
  roll, result, performance, desired difficulty, payment
OFF  without numeric progression: capability is the actor's absolute domain grade
  (tool scale); the engaged opponent's power is the base Difficulty, its attacks
  stay the danger
```

```text
AWARD  tool `xp`: the GM gives the actual challenge, the participant, and the scope
  (routine · minor · meaningful · major · exceptional); the tool owns the formula,
  gap multipliers, rounding, and level table
NOT A POOL  every materially contributing tracked participant gets full XP; never
  divided by party size; no XP for untracked actors
APPLY  a source naming one resolved scope by id (a quest code, else one event or
  encounter id in material_history); that scope not already paid; level 35 → xp 0;
  level-ups carried; output the XP change and level before the scene closes
ONLY  no other rule changes XP
COMBAT XP  material participation vs a valid hostile opponent materially overcome
  (defeated, surrendered, captured, forced to retreat, durably neutralised);
  each enemy's challenge from canonical capability first; several enemies in
  one encounter: vs level at encounter start, summed once; mainly escape →
  one survival scope (event XP) on aggregate challenge; none for harmless
  targets, allies, farming, duplicate exploits
EVENT XP  material, independently resolved non-combat challenge, discovery, rescue,
  negotiation, investigation, survival problem; scope not already paid; none
  for time, farming, re-describing
QUEST XP  each code pays once at CLOSE, vs its level; a part (A-1) pays for
  itself; the whole quest (A) pays only what its parts didn't; combat, event and
  quest XP never double-pay (I8)
```

## 14. Item points

On unless the BACKGROUND sets `flexible_item_entitlement: false`. Not help from the world (GM §5.5 HELP): the PC spends their own limited resource on their own preparation.

```text
PURPOSE  buys back preparation play skipped (a GM fast-forward, a step the player
  did not think of in time): an ITEM the PC packed all along or finds within reach
  in the scene, or a PREP action the PC did earlier in skipped time; the GM
  commits the in-world reason; buys the coincidence, never something from
  nothing (I3)
STATE  player.item_points {current, max, rank}; integers ≥ 0; not money, XP,
  capability, loot; a spend covers the money cost (no money spent)
MAX  by rank, from social standing and income: outcast · commoner · working_adult ·
  well_off · elite (tool); changes only when rank or income changes in play
REFILL  each good rest: a fifth of max, never above max (tool)
COST  small item or prep (rope, torch, a tip) 1 · solid item or prep (lockpicks,
  horse hire, a night's watch on a house, a real bribe) 3 · weapon or armour
  T1 10 · T2 30 · tool or kit T1 5 · T2 15 · BACKGROUND tool_prices: cheap → tool
  or kit T1 3 · T2 10 · above T2 never; an item with no tier = small or solid
```

```text
1 PLAYER  says what they want true; a player action
2 CHECK  current ≥ cost · setting-valid at that tier · not yet established ·
  contradicts nothing recorded
3 SOURCE  commit one plausible in-world reason before narration (I2):
  ITEM carried/packed, never mentioned · bought or given in skipped time by an
  actor whose drives and knowledge allow it · found within reach (body, pack,
  shelf, crate, cache already at the location)
  PREP done in skipped time where the PC was, with the time and means to do it
  built only from provisional detail (unobserved, relied on by nothing); possible
  is enough
4 APPLY  item_points.current −= cost once; the item is the player's; reason at its
  owner (I7)
5 RESOLVE  a prep involving another actor resolves as if done then: that actor's
  answer (§9.1) or a roll; it can fail; the points stay spent
6 RENDER  narrate the reason as what happened; continue
LIMITS  never contradicts recorded state (searched pack, property shown absent) ·
  never reveals hidden truth, moves an actor, takes recorded property, or makes a
  debt, obligation, or relationship beyond what the prep itself would · never a
  unique named artifact, something someone else holds, or the player's own
  confiscated gear · none valid → spend fails, costs 0, commits nothing
ACTOR  named in the reason remembers it; nothing else about them changes
WHERE  on the person: in hand now · within reach: reaching is ordinary, contested →
  an action form · combat: declared with the objective → available from the next
  exchange
TIME  the spend takes none; reaching and using take what they take
AFTER  established fact; real and visible; perceived and remembered (I5);
  legality and usability resolve normally; grants the item or prep, never the
  opportunity, permission, or immunity; can be lost, broken, stolen, sold; never
  back into points
```

---

## 15. The world

How the world's records move on their own. The tool runs time; these rules say what each record does when its time comes.

### 15.1 Actors

```text
ACTOR  NPC or faction; a persistent record only if it recurs or matters (WORLD §11
  DEPTH); incidental → interaction state only; populate material fields
action = f(identity/role, state, drives, relationships, rights, knowledge, capability,
  world state)
REACT  to material perceived change; decide independently from own state (I5, I6)
PLAN  next move + due: a clock time, or a trigger the tool can list (an event with a
  committed time, a channel the actor watches; a cycle like a tide needs its
  schedule as a world fact); else not a plan; due passes → the move resolves
  wherever the PC is, reaching them only by real channels (I5); recurring → next
  due set
ALWAYS  every important actor (WORLD §11 IMPORTANT) has a plan with a due at every moment;
  given when the record is created, imported, or becomes important; the tool flags
  any without one at each time call
OFFSCREEN  otherwise moves only when elapsed time advances a recorded activity,
  pressure, or obligation, or a material event changed its state, knowledge,
  relationships, rights, risk, opportunity; time alone never changes
  personality, loyalty, goals, relationships, skill
REPLAN  plan resolved, blocked, failed, obsolete, or undated, or the actor gains new
  means or a channel opens to it → re-plan at once, from want, pull, fear, line,
  means, knowledge (I5); never idle while a want is unmet and means exist; the
  record open between fitting moves → ask roll: YES pursued (AND sooner/bigger) ·
  NO, BUT weaker/later · NO, AND the next want
WORK SOURCE  role routes work to the PC (fixer, guild, employer, patron) → routine,
  pace from its state.routines, else by its zone's surface: ≥0 weekly · −1 twice
  weekly · ≤−2 every few days; ask roll "fitting work came in?" → YES contacts
  the PC · NO, BUT thin or went to a rival · NO, AND dry spell
TEMPER  a new actor not in the BACKGROUND, once: 2d10 ≥17 (≥15 opposing side) →
  a difficult character fitting the role (rude, greedy, petty, bully…); permanent;
  shown to all, never aimed at the PC's secrets (I6); attitude still from meeting
STANCE  on meeting or being asked, from: existing relationship, want, fear, line,
  what is asked, its cost to them, what they know of the asker, obligation,
  authority
```

```text
RELATION  per relationship, directional, each side its own, never mirrored;
  faction ≠ members; a side changes only when its actor learns (I5)
TIE  what the two are to each other; changes only when that fact does
BOND  what the relationship is to this actor, where it matters: history · means ·
  habits · wants · unsaid; plays the scene: voice, care, friction, what is noticed
  or kept back; feeds stance; never a likelihood point or roll modifier (I8)
STANDING  two records, never one scale: credit (what they know this person did for
  or with them) · grievance (what they hold against this person); no cancelling;
  only a real event (restitution, debt settled, apology accepted, grudge
  outliving cause) reduces either, as its own transition (I7); records the OTHER's
  acts; what an actor did for someone → their own state/knowledge (feels owed) or
  rights_obligations (real debt)
ATTITUDE  current disposition in plain words, mixed where recorded ("warm but
  angry"); what the record amounts to, never replacing credit/grievance; a new
  relationship from first meeting, else neutral
CHANGE  attitude and bond change only on a material relationship event (life saved,
  betrayal, lie exposed, promise kept/broken, humiliation, sacrifice, long shared
  hardship); greetings, trade, routine talk, expected help → no change; never
  recomputed on appearance; warmth and hostility earned, never granted; can fail,
  sour, cool, persist; what the PC earns, they get: an admirer earned is real
```

```text
NPC GROWTH  §7 applies; only tracked actors (rivals, recurring enemies, named
  allies); trigger: a recorded activity exposing them to qualifying challenge
  (dangerous trade, active campaign, committed teacher); never time alone or the
  PC's progress (I6); resolved per elapsed period; stops when the activity stops;
  learning stays; the PC learns of it only through evidence (I5, I9)
ROUTINES  job + local custom + daylight/season + obligations + circumstances; work,
  meals, rest, sleep; continuous services in shifts; emergencies break routine;
  exact schedules only when timing is material
FAMILIARITY  Round-0 relationships are imported before the first round; familiar
  actors meet from tie, attitude, bond, never as strangers; shared history only
  from bond or play, never invented; a scene needs a person → an existing
  relationship, affiliation or institution first, else a setting-valid actor;
  never a connection manufactured for the PC
CANON MODE  mode: canon → canon is the default course; canon actors follow its plans
  (BACKGROUND canon_course, else the source) unless play changed their causes:
  settled, never rolled; attempts resolve normally (§3, §8); +2 in answers (§9.1);
  gaps filled from canon; content fits around canon, never replaces a canon actor,
  location or event; a beat never moves the PC; its actors pursue it with their
  means; it can pass without the PC
COMPANIONS  joining or leaving needs causal support; no auto-joining; solo stays
  valid; on joining, committed before the first material action (I2): identity,
  capability (level if numeric), current HP, equipment + consumables (exact or
  usage die), risk drives (caution, pride, when they ask for help, when they
  withdraw); act from that record: own gear by own judgement; may ask for help,
  propose retreat, refuse a reckless order; the PC's property stays the PC's;
  earn XP and skill evidence from their own rolls, in the same pass as the PC
JOIN AIM  an actor joins the PC's undertaking (companion, partner, hire, ally):
  before its first act, weigh from the record, never by default:
  want  its own, at record weight: strong = tied to an obligation, client, debt,
    fear, identity · weak = a preference
  clash  with the PC's goal now, on this path, not in principle
  ties  bond, credit, grievance as recorded (STANDING); never from friendliness
  → own  strong want that clashes or will: want and plan stay its own; mode:
    paths together → follows fully · split ahead → follows outwardly, keeps and
    may hide the aim · split now → works against
  → adopt  weak want, no clash, or recorded ties outweigh it: takes the PC's goal,
    helps in earnest
  → none  no want of its own: any reason follows (pay, curiosity, nowhere better);
    a thin record is filled from character first, never read as none
  record  npcs.<id>.state.aim {row, mode, want, split}; own: plan = its own next
    move with a due, split = a registered trigger; never "follow/help the PC"
  weigh again only on a material relationship event (CHANGE), the split reached,
    or the want met or lost; never per scene
```

### 15.2 Time

```text
world_state.time = {season, day_index, date, clock_minutes, daypart,
  precision: exact | daypart | degraded}
date  only when recorded; else day_index; never invented
clock  clock_minutes 0..1439 when known, else daypart
daypart  night 00–06 · morning 06–12 · afternoon 12–18 · evening 18–24
lost  precision degraded, reason in continuity_status, until an unambiguous
  in-world anchor (I12)
SPAN  the GM sets a believable duration for the PC's action; the tool runs it once:
  day rollover (nerve day marks), month rollover (every 30 days: monthly stability
  marks), every due ≤ the new time in time order (plans §15.1, pressures §15.5,
  pending and payoffs §12), one surface roll per daypart the PC spends in a zone
STOP  the tool stops at the first event that could reach the PC (in the PC's zone,
  aimed at the PC, or a surface or undercurrent encounter) and returns only up to
  it; the GM judges: it reaches the PC → time stops there, the scene opens; it
  doesn't → the tool continues; the GM never sees past a stop
FIRE  at its due a plan or pressure acts if its cause still holds: resolve from
  state, outcome uncertain → ZONE (§9.1); cause gone → an actor re-plans (§15.1), a
  pressure is stopped (§15.5); a trigger is checked against what has happened:
  met, even earlier unnoticed → fires now, from current state
EVERYWHERE  a due fires wherever its actor or pressure is, reaching the PC only by
  real channels (I5); a skipped stretch runs like any other; skipping never jumps a
  due
COSTS TIME  travel, investigation, preparation, repair, crafting, shopping, meals,
  sleep, aftermath (nonzero); preparation ≠ rest; urgency constrains delay
```

### 15.3 Encounters

TRIGGER: each daypart the PC spends in a zone (surface) · contact with a zone's undercurrent. Never: round count, idleness, quiet, wish for content.

```text
SURFACE  one roll per zone per daypart the PC spends there; an active quest, job,
  or travel to it never cancels it; the tool gives occurs, kind (hostile |
  ordinary), and where in the band (low · middle · top · top + a rare cause the
  band allows); +3 Sanctuary never rolls
  POOL  the zone's encounters of the rolled kind fitting time and location; none of
  that kind → the other; empty → nothing
UNDERCURRENT  on contact: the PC enters one of its sites · is out during its hours ·
  acts on its trail · its pressure advances while the PC is there; one roll per
  zone per daypart; the tool gives occurs and the result:
  sign  wrongness a local would misread
  brush  contact without harm → horror check (§11)
  incident  something happens to someone → horror check
  hostile  it acts against those present (§8) → horror check
  POOL  BACKGROUND undercurrent_pool, by result
ELSE  nothing happens
CAUSE  chosen from the pool without looking at the PC's cargo, secrets, plans;
  committed before its evidence (I2); acts from its own nature: fight, flight,
  parley; a quest only if a bounded undertaking exists (§10)
```

### 15.4 Places and stability

```text
BAND  limits which causes can plausibly exist in a place; produces no number
ORDER  cause from anchors within band → commit → derive its level from the cause →
  check in band; outside → fix the cause, never clamp (I2, I3)
DERIVE  from settlement size, institutions, garrison, threats, frontier proximity,
  known sites; the PC's level or party strength → 0
AUTHOR  BACKGROUND for recorded locations; else derived and committed on first
  contact; then stable; changes only by a causal world event (war front, site
  opened)
LIMIT  bounds locally generated opportunities; never rewrites a recorded actor
CLOSED  a location with `closed`: no entry, no fighting or bribing through, no detail
  of its cause beyond what is public; lifts only on its recorded date or cause
```

```text
STABILITY  surface (−3..+3), undercurrent (none..−3), nerve (−3..+3, §11):
  {baseline, current, tension}, a zone layer also `stepped: <day_index>`;
  baseline = what it normally is, from recorded facts (a zone: the facts behind its
  band, never the PC's level; a person: their history); current starts at
  baseline; unset → derived and committed on first contact
TENSION  events add marks; the tool steps current when the boundary's marks are
  reached (more marks for the outer steps); marks past it stay in tension; a mark
  against tension's sign cancels first
BASELINE  an act that improves a layer stops at its baseline; past it takes a
  lasting cause (garrison posted, ward built, breach that never closes), which
  moves baseline; worsening has no baseline limit
ZONES  one step per zone layer per week (`stepped` records the day), extra marks
  wait in tension; a building or room names its zone and uses it; a location with
  its own control (keep, vault) may be its own zone
SURFACE  how the zone behaves openly: +3 Sanctuary · +2 Secure · +1 Calm ·
  0 Ordinary · −1 Uneasy · −2 Unstable · −3 Collapsed
  marks: its pressure advances 1, signed by direction (§15.5) · its cover fails −1 ·
  the hidden goes public −2 · a visible cause removed +1 · a decisive act +2 ·
  each month no pressure touched it, 1 toward baseline
UNDERCURRENT  what is hidden there: none · −1 · −2 · −3
  marks: its pressure advances 1, signed by direction · a hidden cause removed +1 ·
  a decisive act +2; never heals with time
COVER  an actor (an agency, a city office, plain denial); its covering is its plan;
  first receiver of witness reports of the hidden (§15.7); its plan failing →
  surface marks; no cover → undercurrent −2 or deeper takes surface −1 each month
SIGNS  each state shows signs someone could notice; the PC learns it from them (I5)
```

### 15.5 Pressures

```text
PRESSURE  a recorded persistent condition or force that matters (not only threats);
  0..n; moves by world time and events; effects stay with natural owners;
  trajectory = expected direction, not locked
TRACK  a pressure bound to a zone moves that zone, no counter of its own; several
  zones → one track each
CLOCK  a pressure bound to no zone, or a short emergency paced in hours or days,
  faster than a zone can move; a clock adds no zone marks
DUE  every pressure always has one, like an important actor (§15.1 ALWAYS)
PACE  every <interval> while <condition>: how often it can really advance + what
  must hold; world-scale moves in weeks or months, never nightly; none → every
  rest/downtime period
CHECK  at its due (then due += interval) and when a resolved event touched it:
  advances once if it actually operated (not if its actors stopped, are absent, out
  of resources, or had no opportunity); a plainly accelerating event may advance
  one extra; the PC may advance, reverse, stall, destroy; never round count,
  pacing, quiet
ADVANCE  track: one mark at its zone and layer, signed by direction (zone weekly
  limit) · clock: fill one segment
ON STEP / ON FILL  committed at creation: the world's action if nobody interferes;
  never aimed at the PC (I2, I6); track: fires when its layer reaches that step ·
  clock: fires on the last segment; happens present or not; the PC learns of it
  through a real channel (I5)
STOPPED  condition fails → holds; its actors re-plan; a new plan may open a new
  pressure
STAGES  track: the layer's steps are its stages, each with signs · clock: optional
  early (its actors can still be stopped) → late (it will happen; brace) → fill,
  one sign per stage someone could notice
HIDDEN  unless the PC has observed enough to infer it; never show a hidden layer's
  tension or an undiscovered clock's segments (I9)
REUSE  clock shape for any count toward a target and any long undertaking, at its
  owner
```

### 15.6 Cases and hidden truth

```text
TRIGGER  a hidden cause is committed that must hold across more than one future
  contact
OWNER  an actor did it → the actor · a pressure → the pressure · one location fact →
  the location · spans several owners → a case; references owners, copies nothing
  (I1)
CREATE  cause committed and written first; never an empty shell
LIMITS  player theory never rewrites a pre-contact cause; misleading information
  needs its own cause; no path to discovery → stays undiscovered; a missing prior
  cause is never built backward (I2, I12)
EVIDENCE  baseline: competent + relevant skill + examining the right spot → found,
  no roll; uncertain only: time, cost, noticed/traces, beyond-baseline finds,
  meaning; interpretation gated by §2; all other failure stays possible (I11)
SOLVABLE  a case tied to a quest needs ≥3 independent routes the PC can reach from
  where they stand (different person, location, or record); routes through one
  shared door, record, person, or access the PC lacks count as one; fewer than 3
  → add routes from its actors' own plans (someone searching, a witness who comes
  forward, a nervous accomplice, a client who calls), committed in the case before
  play reaches it; never added during play (I3)
CHECK  at creation, and before a quest attaches to it; never in play
LIMIT  routes the PC's own failures close stay closed (I11); governs how cases are
  built, never a lead, hint, or rescue after creation or after a failure
STUCK  no reachable route left on an active quest, or the player asks → the known
  leads as numbered options (what, where, rough cost/risk); never a hidden route or
  new fact (I9); a menu, not a limit: free wording stays a normal action
```

### 15.7 Witnesses and response

```text
CHAIN  act → witness (who, what they saw, a recognised person or only a
  description) → witness acts (report, stay silent, flee, bargain, sell, act alone,
  tell one) → receiver, and whether they care (setting norms) → the response the
  institution can actually mount (reach, resources, priorities) → the PC meets it
  when it arrives
NO WITNESS  no attribution; the act and its physical consequences stay real (body,
  goods, door); linking needs the chain (I2, I5); a trace the PC left can still be
  found by someone who looks (a detective working the scene)
VALID  silencing a witness (with consequences); a witness lies, misremembers, names
  the wrong person
PARTIAL  recognition attaches to a description in the holder's knowledge
  (suspicions), may settle on the wrong person
RESPONSE  within actual reach (ZONE); costs people, money, attention; follows its
  own priorities, not severity; officials may be corrupt, indifferent, overworked,
  invested; pursuit may stop when costly or run long when personal
BELIEF  a receiver judges the source and chooses to believe it or not
```

### 15.8 Character and values

```text
SOURCE  behaviour = drives + circumstances + beliefs + what they think they can get
  away with; never to look admirable, never to look grim
RANGE  a settlement holds what its conditions produce: decent, petty, generous,
  cowardly, zealous, warm to own and vicious to outsiders, tired
NEVER  better or worse than the situation supports · soften a recorded setting into
  modern sensibility · import one it never had
CULTURE  recorded prejudices, loyalties, superstitions, hierarchies, cruelties
  belong to the actors and cultures holding them
TRAIT  a character line sets what an actor tries, how, and its voice; never whether
  it works: uncertain → §3 or §8, actor vs actor = one roll, the other as challenge;
  comic luck colours a result, never makes it
CONTENT  what the campaign depicts is set once in the BACKGROUND; never improvised
  per scene or narrowed in play
```

### 15.9 Development threads

```text
THREAD  a persistent unfinished development direction of the PC, from explicit
  intent or recorded play
NOT  a quest, pressure, content promise, autonomous arc
DERIVE  requirements, paths, trainers, resources, contacts from canonical sources;
  not stored
TIME  never advances it unless a recorded actor or pressure acts on it
READ BY  an existing actor who knows the direction and has their own reason
  (teacher's test, guild door, rival challenge, patron's favour), by REACT and PLAN
LIMIT  supplies no actor, opportunity, resource (I3, I5); none who knows and cares →
  nothing, however long
CLOSE  advances only by its own valid transitions; completed/abandoned recognised at
  a growth boundary
```

### 15.10 Endings

```text
ARC END  a main quest or bounded arc ends or changes beyond recognition → discard
  unused future planning (not history)
NEXT  only from pending consequences, pressures, actor state and drives, or ordinary
  setting-anchored generation; dead or removed actors, resolved causes, failed
  prerequisites stay invalid; no escalation because content ended
CONDITIONS  ending_conditions; 0..n, an open world needs none; chapter.end is one;
  committed before the decisions they govern, never rewritten after player
  choices; outcomes the player may pursue, ignore, miss (I6, I11); hidden ones
  natural and discoverable; the full set revealed at the end
CHECK  only when a resolved event changed state a condition depends on; never on
  schedule, round count, or length; met → ending review (GM §10.6); permanently
  unreachable → closed for good; none left → ends in that state, no new ending
```

---

## 16. The tool

neo_math takes one JSON form, from a file or stdin, and prints one JSON result. `{"cmd": "forms"}` lists every form and its fields. Lines under `copy` go into the turn verbatim; lines under `gm_delta` go into the round's GM-Δ block.

```text
WORLD FILES  forms that read the world take: background (required) · save (the
             newest, once one exists) · deltas (a file of every GM-Δ block since
             that save)
action     §3: capability, Difficulty, tool modifier, roll line, result, reach or
           cost, damage applied, growth credited when it qualifies (§7)
help       §9.2: ask, sources (≤3), hostile → target, roll line, exists or not
ask        §9.1: who, question, for and against (≤2 facts each, 1 or 2 points)
combat     §8: side, opponents, conditions, stop → exchanges in a batch, pausing
           at the first turning point with every fighter's HP; send it again with
           the HP as it stands to continue
span       §15.2: from {day, clock}, minutes, pc_zone, arrived → events in time
           order (dues, day and month rollovers, encounter rolls), stopping at the
           first that could reach the PC; triggers to check; flags (an important
           actor or a pressure with no due, a malformed quest code); after a stop,
           send it again with the returned resume fields
selfcheck  GM §8: answers {npc_positions, quests, money, hp}, round → each answer
           against the save, the tool's own checks, the verdict; positions are
           answered with the location's recorded name
award      §13: actor, challenge, scope, source → XP, level, the paid marker
boundary   §7: tiers and class at a growth boundary
points     §14: item-point maximum, spend, refill
stability  §15.4: marks and steps for a zone layer or nerve
encounter  §15.3: one surface or undercurrent roll
vitals · harm · heal · cast · time · roll   single calculations (§5)
merge      WORLD §19: previous save + GM-Δ blocks → the next capsule
validate   a save: readable, capsule survival against the previous save, dues
flatten    GM §10.6: BACKGROUND + final save → one world, records open or closed
```

---

*End of NEO RULES v0*
