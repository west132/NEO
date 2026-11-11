"""Shared helpers for the neo_math tests. Run all tests from the neo/ folder:
    python -m unittest discover tests
Dice are genuinely random, so tests assert rules and bounds, never exact rolls."""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TOOL = os.path.join(ROOT, "neo_math_v0.py")
BG = os.path.join(ROOT, "worlds", "BACKGROUND_SHEET_ANCHOR_NEO_v0.md")


def run(form):
    """Send one JSON form on stdin; return the JSON result."""
    r = subprocess.run([sys.executable, TOOL], input=json.dumps(form),
                       capture_output=True, text=True)
    return json.loads(r.stdout)


READABLE = """# SAVE — Sheet Anchor R{round}

## Part A — readable

```yaml
background_ref: {{id: sheet_anchor_india_1991}}
language: en
profile: full
round:
  last_completed_round: {round}
  saved_completed_round: {round}
world_state:
  location: chor_bazaar
  time: {{season: monsoon, day_index: 2, date: Day 2 (July 1991), clock_minutes: 1320, daypart: evening, precision: exact}}
  environment: {{weather: first monsoon rain}}
player:
  identity: {{name: Lok, age: 27, origin: Hong Kong, history: [film stunt performer in Bombay]}}
  archetype: film stunt performer
  job: film stunt performer
  belongs: [independent]
  gender: man
  character: player-defined in play
  status: bruised
  skills:
    acrobatics: {{class: NORMAL, tier: T2, evidence: 1, class_source: the role's work, abilities: []}}
    brawling: {{class: NORMAL, tier: T2, evidence: 0, class_source: the role's work, abilities: []}}
  traits: [knows how to fall]
  expertise: {{established: [stunt rigging], limitations: [no formal schooling]}}
  growth_period: {{opened: 0, credited: [acrobatics]}}
  progression:
    system: numeric_level_xp
    state: {{level: 3, xp: 40}}
  condition:
    hp: {hp}
    conditions: []
    nerve: {{baseline: 1, current: 1, tension: 0}}
    fatigue: tired
    last_rest: full night, Day 1
  equipment:
    - {{item_id: stunt_harness, name: stunt harness, type: tool, capability_domain: acrobatics, condition: serviceable, special_properties: [], tier: T1, abilities: []}}
  money: {{cash: "₹1,350"}}
  resources: {{}}
  item_points: {{current: 37, max: 40, rank: commoner}}
  routines: {{}}
  fighting_style: []
  knowledge: {{facts: {{rumour: a plate, an auction}}, channels: [the street, the papers, their own people]}}
enabled_modules: {{numeric_level_xp: true, flexible_item_entitlement: true}}
narrative_theme: {{initial: {{tone: pulp}}, current: {{tone: pulp}}}}
index:
  npcs: {{pinky_malhotra: "Pinky — your boss; you saved her riggers"}}
  quests: {{B: "who stole from Meera's lab — active"}}
```

## Part B — capsule

```yaml
{capsule}```
"""

DELTAS_1 = """GM-Δ 1 ⟵ 0
  ~ npcs.meera_raghavan.state.position :: the train to Bombay
GM-Δ 2 ⟵ 1
  + quests.side_lab_theft.code :: B (R2, the PC agreed to help Meera)
  ~ quests.side_lab_theft.status :: active
  + npcs.pinky_malhotra.relationships.pc.credit.set_saved :: pulled two riggers out of the collapsing set (R2)
GM-Δ 3 none
"""

DELTAS_2 = """GM-Δ 11 ⟵ 10
  ~ quests.side_lab_theft.status :: succeeded (R11, Ravi confessed)
  ~ npcs.ravi_kumar.state.plan :: tell Meera himself
  ~ npcs.ravi_kumar.state.due :: Day 3 morning tells Meera
  ~ player.condition.hp :: 12
GM-Δ 12 none
"""


class World:
    """A temp folder holding a two-save chain: R10, then R20 built on it."""
    def __init__(self):
        self.dir = tempfile.mkdtemp(prefix="neo_test_")
        p = lambda n: os.path.join(self.dir, n)
        self.p = p
        def put(n, text):
            with open(p(n), "w", encoding="utf-8") as fh:
                fh.write(text)
        def get(n):
            with open(p(n), encoding="utf-8") as fh:
                return fh.read()
        put("d1.txt", DELTAS_1)
        self.merge1 = run({"cmd": "merge", "background": BG, "deltas": p("d1.txt"),
                           "out": p("cap1.txt"), "save_round": 10})
        self.save10 = p("save_R10.md")
        put("save_R10.md", READABLE.format(round=10, hp=9, capsule=get("cap1.txt")))
        put("d2.txt", DELTAS_2)
        self.merge2 = run({"cmd": "merge", "base": self.save10, "background": BG,
                           "deltas": p("d2.txt"), "out": p("cap2.txt"), "save_round": 20})
        self.save20 = p("save_R20.md")
        put("save_R20.md", READABLE.format(round=20, hp=12, capsule=get("cap2.txt")))
        self.w10 = {"background": BG, "save": self.save10}
        self.w20 = {"background": BG, "save": self.save20}
