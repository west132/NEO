"""Shared helpers for the neo_math tests. Run all tests from the neo/ folder:
    python -m unittest discover tests
Dice are genuinely random, so tests assert rules and bounds, never exact rolls."""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TOOL = os.path.join(ROOT, "neo_math_v0.py")
BG = os.path.join(ROOT, "worlds", "BACKGROUND_SCP_OMEGA99_NEO_v0.md")



def run(form):
    """Send one JSON form on stdin; return the JSON result."""
    r = subprocess.run([sys.executable, TOOL], input=json.dumps(form),
                       capture_output=True, text=True)
    return json.loads(r.stdout)


READABLE = """# SAVE — Class of '99 R{round} (test fixture; the player block is a test agent)

## Part A — readable

```yaml
background_ref: {{id: scp_class_of_99_v5_2}}
language: en
round:
  last_completed_round: {round}
  saved_completed_round: {round}
world_state:
  location: site19
  time: {{season: early spring, day_index: 2, date: '2026-03-03', clock_minutes: 1320, daypart: evening, precision: exact}}
  environment: {{weather: cold, clear}}
player:
  identity: {{name: Test Agent, age: 27, origin: United States, history: [test fixture agent]}}
  archetype: field agent (test)
  job: Foundation field agent (test)
  belongs: [foundation, mtf_omega_99]
  gender: man
  character: player-defined in play
  status: bruised
  skills:
    acrobatics: {{class: NORMAL, tier: T2, evidence: 1, class_source: test, abilities: []}}
    brawling: {{class: NORMAL, tier: T2, evidence: 0, class_source: test, abilities: []}}
  traits: [test fixture]
  expertise: {{established: [test], limitations: [test]}}
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
    - {{item_id: stunt_harness, name: stunt harness, type: tool, capability_domain: acrobatics, condition: serviceable, special_properties: [], tier: T2, abilities: []}}
  money: {{cash_and_accessible_funds: "1,350", currency: USD}}
  resources: {{}}
  item_points: {{current: 37, max: 40, rank: commoner}}
  routines: {{}}
  fighting_style: []
  knowledge: {{facts: {{test: fixture}}, channels: [handler briefings]}}
enabled_modules: {{numeric_level_xp: true, flexible_item_entitlement: true}}
narrative_theme: {{initial: {{tone: light}}, current: {{tone: light}}}}
index:
  npcs: {{dmitri_volkov: "Dima — sparring partner"}}
  quests: {{B: "the Loewes file — active"}}
```

## Part B — capsule

```yaml
{capsule}```
"""

DELTAS_1 = """GM-Δ 1 ⟵ 0
  ~ npcs.rosa_delgado.state.position :: Site-88
GM-Δ 2 ⟵ 1
  ~ quests.loewes_file.status :: active
  + npcs.dmitri_volkov.relationships.pc.credit.sparring :: held his own at sparring (R2)
GM-Δ 3 none
"""

DELTAS_2 = """GM-Δ 11 ⟵ 10
  ~ quests.loewes_file.status :: succeeded (R11, the copycat caught)
  ~ npcs.leo_brandt.state.plan :: tell West
  ~ npcs.leo_brandt.state.due :: L Day 3 evening tells West
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
