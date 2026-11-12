# Neo — Design record (v0)

The design behind Neo, the next form of the engine. Records decisions only; no rules text yet.

```text
STATUS  AGREED   the person confirmed it
        PROPOSED Claude's recommendation, not yet confirmed
        OPEN     undecided
SCOPE   Neo lives in neo/ only; v6.3 files (claude/, written background/) are never
        edited for Neo work
VERSION Neo starts at v0, apart from the 6.x line
```

---

## 1. Why Neo

```text
AGREED  the engine is a long instruction set read by an AI, not a machine running code;
        the AI interprets, skips, and leans toward pleasing the player
AGREED  the engine can do better with fewer rules and a better flow; one person
        pushes it as far as it goes
AGREED  rules that push against the AI's pull to please the player stay, however
        good models get
AGREED  tone comes from the background (or player-picked), never from the AI's mood
```

## 2. Core ideas (carried from v6.3, unchanged)

```text
WORLD    the world doesn't revolve around the player: things can be found, avoided,
         changed, missed, or lost for good; nothing is guaranteed to reach the PC;
         no storyline is protected
CAUSE    any hidden cause is decided before anything depends on it
STATE    narration can't change the state; text describes what is already true
```

Any Neo rule that goes against one of these loses.

## 3. Three layers

```text
AGREED  RULES     how the game behaves: dice, checks, combat, HP, XP, prices;
                  the Python tool lives here; maths lives in the tool only, never
                  repeated in rule text
AGREED  WORLD     what exists: fixed history and truths, people, places, tone,
                  everything the narrative draws on
AGREED  AI GM     how to run the game: the flow, when to stop, how to narrate,
                  how to fill gaps
AGREED  sorting test: RULES = what a human referee with dice would compute the
        same way; AI GM = judgment, flow, voice
AGREED  live state (the save) belongs to WORLD: the background is the world at
        Round 0, the save is the same world later; save format in WORLD, the
        saving procedure in AI GM
AGREED  AI GM describes the GM's job; a past mistake goes in only if the job
        description doesn't already cover it (guard against AI_RULES regrowth)
AGREED  the job description is a standard GM summary, built from established GM
        agendas and principles (see §3a)
```

## 3a. The GM's job

Built from Apocalypse World's GM agenda and principles, kept where they fit Neo and
replaced where they carry the pleasing bias.

Read from the fuller explanations, not the headings (Nov 11). All kept; each is
written as what it actually means, with the Neo source it draws from.

```text
AGREED (Nov 11)
AGENDA
  make the world seem real          consistent, concrete, lived-in
  make the PC's life not boring     what the world does reaches the PC through real
                                    channels and is shown; dull stretches are cut
                                    (enter late, leave early); nothing is invented
                                    to fill a quiet stretch
  play to find out what happens     no outcome steered toward
PRINCIPLES
  address the characters            narrate what the PC perceives (POV check)
  misdirect / never name the move   the effect is real and shown honestly; the
                                    cause is shown through the fiction, never
                                    exposed as mechanic or hidden fact; hidden
                                    facts stay hidden and the PC may misread them
                                    ("he kicks you down", never "you failed")
  name everyone, make them human    each character from their record and voice,
                                    never the default agreeable voice
  ask provocative questions and     ask about the PC (what they feel, notice,
    build on the answers              intend) and move play on from the player's
                                    own reading; the player's guess drives the
                                    PC's action, never becomes world fact (M3)
  be a fan of the PCs               give them a hard time that means something;
                                    never take away what makes the PC great
                                    without a cause in the world; what the PC
                                    earns, they get, admirers included
  respond with trouble and          always give the PC what they worked for;
    intermittent rewards              complication comes on top of real results
                                    ("fuck around with, not fuck over"), from the
                                    dice bands and the actors, never from GM mood
  think off-screen too              step 1, the world moves everywhere
  sometimes disclaim decisions      plans, the usual answer and the dice decide,
                                    never the GM's wish
```

Layout, proposed:

```text
neo/
  NEO_DESIGN_v0.md     this record
  NEO_READING_v0.md    story and scene craft reading
  rules/  NEO_RULES, neo_math (py)
  world/  NEO_WORLD_TEMPLATE (background + save format)
  gm/     NEO_GM
```

## 4. The flow

```text
AGREED
1 WORLD      everything that exists now; time runs; every actor's due move
             happens wherever they are                      never NULL
2 SCENE/QUEST where the PC is and the situation they're in     NULL → time skipped
                                                                in one line, back to 1
3 NEED       what's at stake: a demand, a danger, an objective, an offer
                                                             NULL → free roam
4 PC DECISION the player chooses                              NULL → the world carries
                                                                on; silence is not a no
5 RESPONSE   others react from their own wants and knowledge; uncertain things
             are rolled                                     NULL → nothing happens
                                                                (valid)
6 OUTCOME    what changed: written down first, then shown     NULL → nothing changed
→ back to 1, always (never straight to 4): the world gets a turn between every
  decision, including the time the action took
```

```text
AGREED  any step may be NULL; when it happens, it follows this order
AGREED  NEED comes only from an actor's want, a real danger, a quest, or the PC's
        own goal; the GM never invents a need
AGREED  the world can open a scene itself (ambush, messenger, raid): step 1
        produces step 2
AGREED  who acts first is decided by awareness:
          PC could reasonably notice it coming → PC's turn first: the danger is
            shown, the PC decides
          PC had no way to know → the world acts first
          honestly unclear → roll: the PC's alertness vs the other side's stealth
AGREED  OUTCOME is written as changes before any prose (an AI decides in the
        order it writes); this is what makes "narration can't change the state"
        hold
```

### Step 6 — OUTCOME, decisions

```text
AGREED  the full GM-Δ block (every change, hidden ones included, plain text) goes
        at the top of the round, before the prose; same block and save-building
        as v6.3, moved so the changes are written first
AGREED  the block is set apart visually and kept compact (its own code block,
        collapsed where the chat page can collapse it) so it doesn't bury the
        story; it is never moved back below the prose
AGREED  prose: v6.3 narration craft (detail by importance, evidence before
        explanation, no explaining hidden motive, routine compressed), plus:
          POV check: before any line, could the PC see, hear, or know this? no →
            not written, even in passing
          the telling detail: a detail earns its place only if it tells the
            player something about a person or the situation (their state, what
            they intend, a danger), shown through what someone does; never
            decoration
            e.g. not "Bakshi is nervous" but "Bakshi has wiped the same teacup
            three times since you came in"
AGREED  saving as v6.3: readable part + capsule, built by merge from the previous
        save and the GM-Δ blocks since, checked by validate; auto saves on fixed
        10-round marks; a manual save never shifts them; a due save is made, never
        offered; the 50-round self-check rides on the save (§7c)
```

### Step 1 — WORLD, decisions

```text
AGREED  who acts: only actors with a due inside the time that passed; every
        important actor must always have a due (a time or a trigger); the tool
        flags any important actor without one, so the gap is caught by the tool,
        not the AI's attention
AGREED  important = read from the current world state (the save + changes since),
        never from the background: the background is only Round 0 and goes stale
        as the run moves (at Round 0 the two are the same)
        important when the record shows: a relationship with the PC (credit,
        grievance, bond), a role in a quest, pressure, or case, or a deal with
        the PC; dead, departed, or no longer involved → no longer important; met
        once with no record → incidental, no due
AGREED  time: the GM estimates how long the action takes; the tool runs the whole
        span at once
        then check the result: something reached the PC partway (an ambush on
        the road, a messenger at the door) → everything after that moment is
        thrown away; the skip stops there and the scene opens at that moment
        (who acts first by awareness, §4); the thrown-away part never happened
        and is run fresh when time moves on
AGREED  the tool runs events in time order and stops by itself at the first
        candidate that could reach the PC (in the PC's zone, or aimed at them),
        returning only up to that point; the AI judges whether it reaches them:
        yes → the scene opens there; no → the tool continues; the AI never sees
        anything past the stop (replaces the earlier "throw away" weak spot)
AGREED  random encounters as in v6.3: one roll per zone per daypart the PC spends
        there, from the zone's own encounter list, danger set by its stability
AGREED  pressures keep tracks (moving a zone's stability) and clocks (segments),
        under the same rule as actors: everything that moves has a due; the tool
        flags anything that doesn't; one rule, not two
```

### Step 2 — SCENE / QUEST, decisions

```text
AGREED  a quest is an objective the PC has taken on (offered by an actor, required
        by a deal, or set by the PC); small record: code, objective, source,
        level (for XP), status, optional parts; no shape roll, no CHAIN machinery
AGREED  quest codes
  NEW       an independent quest takes the next unused letter: A, B, C … Z, AA, AB
  PARTS     stages of the same objective: A-1, A-2, A-3; no parts → just A
  FOLLOW-ON a case that grew out of another takes a new letter after its origin:
            A-B (B grew out of A); A-B-D (D grew out of A-B)
  UNIQUE    the last letter is unique in the campaign, never reused; the front part
            only shows where it came from
  WHEN      a code is given when the quest becomes the PC's, never at design time
            (no gaps that hint at hidden quests)
  FIXED     codes never change; carried across chapters
  XP        each code pays once; a whole quest pays only what its parts didn't
  STATUS    a lowercase letter at the end shows how it stands:
            (none) active · s succeeded · p partly succeeded · f failed ·
            a abandoned
            e.g. A-1s, A-2p, A-Cf, Ba
  e.g. Sheet Anchor: A find the Syamantaka (A-1 the plate, A-2 the throne, A-3 the
       cave) · B who stole from Meera's lab · A-C the palace night
AGREED  a quest becomes the PC's on any clear commitment: an explicit yes, pay
        agreed in talk, or starting the work without holding back; asking,
        comparing, haggling are not acceptance; the PC's own stated goals are not
        quests
AGREED  enter late: a scene starts when something can change (the world reaches the
        PC, or the PC arrives where they mean to act); the way there gets at most
        one line unless something happened on it; the opening shows place, who is
        there, what is pressing, then hands over to the player
AGREED  leave early, as far as the player's words cover: once what could change has
        changed, the scene closes in a line; the player's order covers what comes
        next → carry on; it doesn't → close with the PC free to act, ending on the
        situation as it stands, never on an invented NPC question
WEAK    a case that grows from two quests shows only the main one in its code; the
        other goes in its source line
WEAK    deep chains make long codes; two or three levels expected in practice
```

### Step 3 — NEED, decisions

```text
AGREED  sources: an actor's want, a real danger, a quest, the PC's own goal; never
        invented (§4)
AGREED  how it reaches the player: through the scene, plus plain stakes where the
        danger is real and the PC could judge it, clear enough to choose by; never
        a hidden danger; no odds stop
```

### Step 4 — PC DECISION, decisions

```text
AGREED  the player's words bind as said; the GM fills in only the ordinary
        competent steps the PC's job and habits imply; standing orders and
        fighting style hold until changed; the method is the player's: different
        routes with different risks → ask; an order with two readings and
        different outcomes at real stakes → ask one line
        (v6.3 §7, AI_RULES and §12 gathered in one place)
AGREED  a message starting with "ps" is out of character, to the GM; anything else
        is in-game action or speech
AGREED  the player speaks only for the PC: telling another character what to do is
        a request, answered from that character's own wants, ties and judgment
        (agree, refuse, warn, do it their way); binding only where the PC has real
        authority over them
```

### Step 5 — RESPONSE, decisions

```text
AGREED  order for an NPC's answer:
        1 the NPC's own plan touches the question → the plan decides, no roll:
          fits the plan → yes; works against it → no, or only on the plan's
          terms; a plan with a condition → the condition decides
        2 the usual answer is clear (common sense, the record) → that answer,
          no roll
        3 honestly open → v6.3 ask roll: 2d10 + likelihood from at most two
          recorded facts per side → YES AND / YES / NO BUT / NO AND
AGREED  characters joining the PC: v6.3 JOIN AIM as it is (own / adopt / none;
        own keeps its plan with a due; re-weighed only on a real change)
AGREED  NPC vs NPC: the PC is there, or it involves the PC's people or business →
        played out in a scene with both sides present, never settled through the
        PC; otherwise off-screen by their plans; character sets what they try and
        how, dice set whether it works (one roll, the other side as challenge)
AGREED  the AI honestly doesn't know whether the PC would be there or involved →
        roll for it rather than guess
AGREED  action roll: same maths as v6.3 (2d10 + ability + tool ≥ difficulty); the
        AI fills a short form (who acts, skill, opposition strength as a level or
        word, tool fit, conditions by name, cost on failure); the tool combines,
        keeps Challenge and Difficulty apart, applies caps, prints the roll line;
        the AI never adds or caps a number itself
WEAK    needs a model that can run code; without the tool there is no roll
AGREED  the tool takes its form as a JSON file or stdin, never as command-line
        text (shell arguments ate `$` amounts in the Sheet Anchor run)
AGREED  cost on failure from what is actually present, fixed ladder:
          nothing that can hurt the PC → setback (time, position, a lost chance)
          something that can hurt and can reach them in this action → loss
          something whose direct result is death, crippling or capture (a long
            fall, a gun at the head, a closing trap) → severe
        the AI names the danger on the form; the ladder sets the tier; a danger's
        normal effect decides (a knife fight → loss)
        reach on success as v6.3: what this action can achieve from here
        (partial / full / decisive)
AGREED  combat: v6.3's model (one roll per exchange for the player's side, the
        opponents' attacks are the cost, attack budget, morale settled not
        rolled), run in a batch by the tool:
          the AI sets it up once: sides, plan, fighting style, stop conditions
          the tool rolls exchange after exchange and applies damage
          the tool pauses at turning points: someone falls, a leader falls, the
            PC reaches a threshold from their style, the objective is met, the PC
            goes down
          at each pause the AI settles morale and checks for anything the plan
            doesn't cover: nothing → continue; something → the player decides
WEAK    the tool can't see outside the fight (noise heard, fire spreading); at
        every pause the AI also checks the world around the fight
AGREED  vitals: HP, damage by weapon, armour soak, down at 0, survival roll, and
        recovery as v6.3; a lasting condition is a named entry with one plain
        effect ("broken leg: harder to run or climb"); it enters rolls only through
        the form's conditions slot, applied once by the tool; v6.3's seven "homes"
        are dropped (the form's one slot per thing already prevents double
        counting)
AGREED  skill growth: v6.3's rules (evidence from a successful roll against a real
        challenge, tiers raised at a growth boundary, class raise needs a real
        source), with:
          the tool decides whether a roll qualifies, straight from the form, and
            credits evidence itself; the AI never has to remember
          threshold loosened: challenge ≥ personal skill level − 2 (was − 1); the
            Difficulty ≥ 15 route stays
CALIBRATE  the new threshold is a guess from the Ashfall stall (evidence 0 by R90);
           test runs decide whether it holds
AGREED  kept as v6.3: XP and levels (the tool owns formula and table; combat,
        event and quest XP each paid once; each quest code pays once); equipment
        tiers (one more slot on the form)
```

## 5. No help from nowhere

```text
AGREED  a person, thing, or event made just to help the PC is never developed
        help exists only if:
          1 the background designed it, or
          2 it would exist anyway: common sense says it usually exists here (a
            taxi in Bombay, a chai stall) → exists, no roll, or
          3 the player asks for something possible but not usual → flat 15+ on
            2d10, no odds set by the AI (the AI sets odds generously)
        impossible in this setting (a helicopter in 1868 London) → no
        (merges the earlier §5 route 2 and §7a; conflict settled)
AGREED  the 15+ is adjusted by reach: the PC's own network, a related NPC's
        network the PC can actually call on, an organisation the PC belongs to
        with reach in this place
AGREED  each source counts once and lowers the target by 1, at most 3 → best 12+
          (≈ 45%); a place hostile to the PC's people raises it by 1 (16+ ≈ 15%);
          the AI names the sources on the form, the tool applies them
          2d10 odds: 15+ 21% · 14+ 28% · 13+ 36% · 12+ 45% · 16+ 15%
AGREED  the GM never offers help unasked
TEST    would this exist if the PC didn't need it?
AGREED  item points stay allowed: the PC's own resource spent on their own
        preparation, not help from the GM; v6.3 rules kept (pool by social rank,
        a fifth refilled per good rest, nothing above T2, reason committed before
        narration)
```

## 6. Common sense

```text
AGREED  common sense can't be listed; a list never ends
AGREED  the AI asks one question: what would usually happen here, for these
        people, in this place and time?
        sources: 1 the real world · 2 the setting (era, norms, economy, the
        background's own logic, e.g. movie logic) · 3 the person (role,
        knowledge, what they find normal)
        clear usual answer → that is the answer, no roll; dice only where it
        could honestly go either way
        guards: never overrides the fixed core or a dice result; "usual" never
        slides into genre cliché unless the background asks for it
```

## 7. Story craft

```text
AGREED  character-driven, not plot-driven: development comes from what each
        person wants and does now, never from what the story needs
AGREED  the background fixes the core; the engine develops from the PC's moves and
        what they trigger; no rule stops a logical PC action
AGREED  the round stays the unit of play (saves, numbering, cadence keep it)
AGREED  character acting: the GM plays each character from their record and
        source: voice, manner, competence; never softened into the default
        agreeable voice
        WORLD template gets an optional voice: field per character (how they talk,
        a couple of habits), apart from character: (personality)
AGREED  scene craft shapes what the GM shows inside rounds: enter late, leave early
        (agreed in step 2); see NEO_READING_v0.md
```

## 7a. Developing the unwritten

```text
AGREED  not set by the background → follow canon (source game, history, the real
        world)
        not set by canon either → the AI develops it by checking the background's
        own setting (anchors, norms, tone, era)
        developed once, then fixed (established) like anything else
AGREED  anything developed that meets a need of the PC's → only on a dice roll of
        15 or more; otherwise it doesn't exist
AGREED  the roll is always 2d10 (15+ ≈ 21%), adjusted by reach (§5)
```

## 7b. How information travels

```text
AGREED  not a rule: follows the background and common sense
AGREED  people judge a source and choose to believe it or not
AGREED  information that physically can't travel doesn't travel
        e.g. the PC kills a man in the dark, nobody knows him, nobody saw it →
        a dead end: no one learns of it, unless someone who could uncovers it
        from the PC's own traces (a detective working the scene)
```

## 7c. Long campaigns

```text
AGREED  the save is built for the long run and is the GM's memory
AGREED  every 50 rounds the AI stops for a self-check; fail → ask the player's
        permission to reread all files
AGREED  the self-check runs with the save on R50, R100 … (rides on validate, no
        extra step):
          1 the AI answers fixed questions from memory, no verdict: where the key
            NPCs are, open quests and their status, the PC's money, current HP
          2 the tool compares those answers with the save and runs its own
            checks (actors without dues, quest statuses, money adding up, HP
            matching logged damage); the tool gives the verdict; a mismatch = fail
          3 shown to the player: the AI's answers, what the tool checked, the
            result, so a fake or empty check is visible
          (as built: see §9 LIMIT for what the tool can and can't check)
          4 fail → the AI asks the player's permission to reread all files
        the AI never judges itself
```

## 8. Weak spots — status after steps 1–5 (Nov 10)

```text
SMALLER  RULES / AI GM line blurs: the form-and-tool decisions put the maths
         clearly in RULES; judgment calls (naming the danger, opposition strength)
         still sit on the line
SMALLER  three layers don't shrink the set by themselves: real cuts now decided
         (shape roll and CHAIN, seven condition homes, odds stop, maths in rule
         text, separate pressure timing); true size unknown until written
SMALLER  running the clock every loop: one span, one tool call per loop; extra
         work only when something reaches the PC partway
RESOLVED changes written before prose: agreed (Nov 11)
SMALLER  "usual" can drift: common sense question agreed with its guards; drift
         still possible in play
RESOLVED self-check grades itself: now tool-run against the save (Nov 11)
RESOLVED the AI seeing thrown-away results: the tool stops at the first candidate
         (Nov 11)
RESOLVED §5 / §7a conflict: usual → yes · possible → 15+ · impossible → no (Nov 11)
STILL    the combat tool can't see outside the fight (step 5)
LOSS     dropping the odds stop: a player can walk into a severe, low-odds action
         with only plain stakes as warning; first thing to bring back if tests
         show players blindsided
STILL    quest codes: two-origin cases, long chains (step 2)
NEW      tool dependency grew: rolls, combat, growth and dues all need the tool;
         a model without code tools can't run Neo; the tool itself needs a large
         rewrite (form input, batch combat, growth crediting, flags), which is
         real build and test work
RESOLVED scene craft inside rounds: enter late and leave early agreed in step 2
```

## 9. Open

```text
DONE  all six flow steps decided (Nov 11)
DONE  play files drafted (Nov 11): gm/NEO_GM_v0 (27.7 KB), rules/NEO_RULES_v0
      (58.4 KB, incl. §15 the world), world/NEO_WORLD_v0 (49.8 KB); total 136 KB
      vs v6.3's 158 KB (engine 91 + AI_RULES 15 + background 37 + save 15)
CHANGE  v6.3's R20/R40 save audit folded into the R50 self-check ("open items
      unchanged 20+ rounds"); to confirm
DONE  Sheet Anchor converted (world/BACKGROUND_SHEET_ANCHOR_NEO_v0.md): depth, voice,
      want/fear/line/pull/belief/secret on all 17 NPCs; invented secrets listed to
      the person for review; auction dues now say "Day 2 night"
DONE  tool built and tested (rules/neo_math_v0.py, 166 KB, run not read): JSON
      forms action, help, ask, combat, span, selfcheck, award + the record
      commands (merge, validate, flatten) and single calculations
      tested on Sheet Anchor: two-save chain, self-check pass and fail, growth
      credit, cost ladder, one-item-once, help odds (62/300 at 15+), time with
      stop and resume, batch combat with stop condition
CHANGE  quest status: the record holds the word (active, succeeded, partly,
      failed, abandoned); the letter is how the code is shown (Bs)
LIMIT  self-check: money is compared to the save, not re-added; HP is checked
      against its maximum, not against logged damage (neither can be derived
      from GM-Δ, which records values, not transactions)
LIMIT  span: a due naming only a day is placed by its wording (night, morning…),
      else 08:00, and marked time_assumed; backgrounds should word dues with a
      daypart
LIMIT  combat: fighters without a world record (unnamed mercs) have no HP written
      back; the GM carries their HP in the next combat form
AUDIT  Nov 11, whole set: rules unreached from the loop, nine rules in 2–4 places,
      no single precedence order, 65% of RULES carried without the keep/merge/cut
      mapping this record had called for; fixed the same day: see NEO_MAP_v0.md
      (every RULES section has a caller; one home per rule; one precedence list
      in the GM header; the law moved to GM §1; GM §9 is now the word list)
OPEN  NEO_MAP §5: rules that are wired but may not be needed in every world
      (nerve, MP, canon mode, NPC growth, threads, food/water, usage dice)
LAYOUT  Nov 11: flat runtime path. neo/ holds only the play set (NEO_GM, NEO_RULES,
      NEO_WORLD, neo_math, README); worlds/ the backgrounds; design/ these notes
      (never loaded in play); tests/ the tool's checks (49 pass). Paths named
      earlier in this record (gm/, rules/, world/) are the old layout.
GAP   Nov 11: no procedure for making a world (the audit checked only the play
      loop); fixed: GM §10.0 making a world (ask → record requested → Part 0 →
      fill by depth → tool check → show the person what was invented → file);
      WORLD D2 now names the depth fields; tool `check` form for a background
      before play (51 tests pass); Sheet Anchor passes with 8 dues that name a
      day but no time of day (the tool assumes 08:00)
NEXT  the person's test run of the NEO set (README.md lists the files)
DONE  NEO_GM v0 drafted (neo/gm/); its DECIDE 1–3 settled Nov 11: moves as cost
      forms before the roll · hand-back by choice type · the GM tells what the
      PC would know of the off-screen world, never hidden facts
DONE  NPC record agreed (Nov 11): want, fear, pull, belief, secret, line for the
      actors the story turns on; NPC depth levels 0–3 (passer-by, regular,
      supporting, story-turning), rising as the save shows they matter, never
      down; WORLD template gets the fields, GM §4 the play rules
NEXT  a cheap test before mapping the rest of v6.3: play
      Sheet Anchor v6.3 in the clean project with one added instruction (NPC
      answers: plan first, usual second, roll third); a full Neo test needs the
      written rules and the rewritten tool
TEST  the person runs the tests later
REDO  Nov 12: play set rewritten so every rule says what to do (no "never" lists,
      no v6 scars); GM gains "where to hold hardest" with Sheet Anchor examples;
      chapters removed; out of character only when marked (ps, out of game, to the
      GM or AI); WORLD split into NEO_SAVE (play) and
      templates/BACKGROUND_TEMPLATE_NEO_v0.md (making worlds, attached on demand);
      powers, canon mode and no-levels moved to modules/NEO_MODULES_v0.md; law tags
      I1–I12 dropped; full/short narration profile dropped; tool's flatten command
      is now unused (chapters)
GUARDS Nov 12: a "never" stays where it blocks the AI's pull toward pleasing,
      drama or convenience (§1 AGREED), placed beside the rule it guards: no
      invented hook or loss, no hidden fact told, no help unasked or made to fit,
      no NPC answer softened or turned on the PC, no encounter or pressure aimed
      at the PC or moved by pacing, no case rebuilt from a theory, no stop for
      drama; nevers that only scolded or restated a positive rule stay out
TOOL  Nov 12: removed flatten (chapters), dues (span replaced it), the lite and
      odds output modes, the profile enum, and command-line commands no form uses
TEST  Nov 12: 20-round Sheet Anchor test (West.L, treasure hunter). Opening,
      runner, customs held. Fixed from it, within existing design: quest codes
      are designed with the quest as in the Step 2 example and given to the
      player on take-on (the check asks for them); a due with several moves
      starts each move with the code of the quest or part it serves and puts
      its status letter after once resolved (A-1s), so the tool reads which moves
      are open · span gives the §9.1 zone point with each actor's due · a position
      names a recorded place by whole name, else the GM develops and records it
      (no guessing from one word) · quest and contract point at each other by
      terms and code (RULES §10) · merge applies a whole-record change field by
      field, splitting a whole parent first · paid or closed dues aren't overdue ·
      incidental dues accepted
```

---

## Appendix — GM draft decision history (moved out of the play file Nov 11)



### Settled Nov 11

```text
1  moves = the forms a cost can take, picked before the roll, only what the
   danger present would normally do (§5.5 FORMS)
2  hand-back by choice type: obvious → end on the situation · known options →
   name them · fully open → may ask outright (§6 HAND-BACK)
3  the GM tells the player what the PC would know of the off-screen world
   (public, their channels, their life), scene or not; never hidden facts; a
   world that moves unseen and is never told feels dead (§5.1 WORD)
4  agreed: PROPOSAL 4 below, with NPC depth levels (Nov 11):
   0 passer-by     name, job, one manner line; not recorded unless play makes
                   them matter
   1 regular       want, fear, voice
   2 supporting    + line, an ordinary secret, ties (relationships, bond)
   3 story-turning all six (want, fear, pull, belief, secret, line) + plan, due,
                   knowledge
   UP     an NPC rises when the save shows they matter more (a tie with the PC,
          a role in a quest or case, a deal); new fields developed once
          (background → canon → setting), then fixed; never moves down; a dead or
          departed NPC keeps the record
   START  the background sets each NPC's level; an NPC made in play starts at 0,
          or 1 if they'll clearly be seen again
```

### PROPOSAL 4 — NPCs whose reasons pull against each other

From three sources, read for their examples:

- **Detective fiction** (Killer Nashville, suspect design): every suspect has a motive and an opportunity, and "several of the innocent suspects should have their own secrets", which is why they evade and lie: an affair, distrust of authority from a rough upbringing, shielding someone, believing the act was justified. Misdirection comes "largely from suspects acting in their own interest". "There are no throwaway characters."
- **Character writing** (Jami Gold, goals vs needs vs false beliefs): a character has an outer goal and an inner need set so they "can't easily reach both"; a false belief, born of an old hurt, makes them hesitate or sabotage themselves; a fear keeps them from the thing that would help.
- **Game design** (Crusader Kings 3): characters can act against their own nature, but it builds stress until a small setback breaks them; the system "punishes out-of-character choices without blocking them".

Proposed NPC record (WORLD), only the fields a character needs:

```text
WANT    one plain main want: what the PC can push on (AW)
FEAR    what they dread
PULL    a second want that fights the first; both can't be had (Ravi: undo what he
        did · never let Meera find out)
BELIEF  what they believe that isn't true (M2)
SECRET  what they hide, and their own ordinary reason (privacy, shame, love,
        money, fear); usually not the case at hand (M5)
LINE    what they won't do; crossing it is possible, at a cost
```

Proposed play rules (GM §5.5):

```text
TORN    a question touches both WANT and PULL → their plan decides if it covers
        it; else the one the record shows is more pressing now; honestly torn →
        ask roll, each side's pull as its facts
LIES    an NPC lies, evades, misleads or over-helps for their own reason, never to
        make or keep a mystery; the reason is in the record before the lie
CROSSES pushed past their LINE → they may do it, and it costs them: a nerve
        tension mark, a changed attitude, a slip the PC can see (the teacup)
SHOWS   pull and secret show as behaviour, never as narration of the inner fight
```

Weak spot: more fields per NPC means heavier backgrounds; only actors the story turns on would get PULL, BELIEF, SECRET and LINE; extras keep WANT alone.

### [DECIDE 1] The GM's moves: what a failure looks like (settled: A)

AW gives the MC fourteen moves: separate them · capture someone · put someone in a spot · trade harm for harm · announce off-screen badness · announce future badness · inflict harm · take away their stuff · make them buy · activate their stuff's downside · tell them the possible consequences and ask · offer an opportunity, with or without a cost · turn their move back on them · make a threat move. After every move, ask "what do you do?". The author's summary: every move puts the characters in a position to make a choice and act.

In AW the MC picks a move *after* a miss, as hard as they like. Neo fixes the cost *before* the dice (danger ladder). So the moves can't be a free choice after the roll.

- **A.** Use the moves as the **forms a cost can take**, picked on the form *before* the roll, and only ones the danger present can actually do: "a gun at his head" can be *capture* or *inflict harm*, never *take away their stuff* from nowhere. The ladder still sets how bad. Gives the GM a vocabulary beyond "you take damage", which AIs lean on.
- **B.** No move list; the named danger alone shapes the failure.

Claude's lean: **A**. Weak spot: a list tempts the AI to pick the most dramatic form; the rule must be "the form the danger would normally take".

### [DECIDE 2] "What do you do?"

AW ends every move with the literal question "what do you do?". You've objected to scenes ending on pointless questions, but that was an NPC's question; this is the GM's.

- **A.** Never write it; end on the situation, which already asks it.
- **B.** Write it only when the world just made a move that the order doesn't cover (an ambush, a demand), so the hand-back is unmistakable.
- **C.** End every turn with it, as AW does.

Claude's lean: **A**. Weak spot: a player may not notice the turn is theirs; if that happens in tests, move to B.

### [DECIDE 3] Off-screen badness

AW's MC tells the *players* what's happening off-screen ("meanwhile, Dremmer's gang is moving on your hold") so they feel the world move and can feel dread before their characters know. Your engine says events reach the PC only through a channel, and no GM-only knowledge.

- **A.** Through a channel only: a rumour, a messenger, smoke on the horizon, a pressure's visible sign.
- **B.** Allow the AW way for pressures' visible signs only: a short line the player sees that the PC could also learn of soon ("Word in the bazaar: crates of 'handicrafts' are moving north").
- **C.** Allow true cutaways.

Claude's lean: **A**. B is A in different words if the sign is already reachable; C breaks your knowledge rule.

### [DECIDE 4] How complex an NPC's wants are

AW: give NPCs straightforward, sensible self-interest, because "complicated desires make it difficult for the PCs to know where to push", and for the MC to know whether pushing works. Your mystery logic (M2, M5) wants NPCs with secrets, false beliefs, overlapping roles.

- **A.** Both, split: every NPC has one plain main want on top of their drives (what you'd push on), and the complexity lives in what they believe, know, hide, and misread, not in their wants.
- **B.** Keep wants as complex as the background writes them.

Claude's lean: **A**. It makes step 5's "the plan decides" much more reliable, and loses none of M2/M5, which are about knowledge and belief.

---


---

*End of Neo design record v0*
