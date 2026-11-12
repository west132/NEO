import os, tempfile, unittest
from _run import run, BG

BREAKS = [
    ("  ruud_kasteel:\n    depth: 2\n", "  ruud_kasteel:\n", "npcs.ruud_kasteel :: no depth"),
    ("    voice: fast and exact, like a lecture", "    vocie: fast and exact, like a lecture",
     "npcs.meera_raghavan :: depth 3 lacks voice"),
    ("      due: Day 2 night the auction — Sterne, Lara, Hawk bid",
     "      due_old: Day 2 night the auction — Sterne, Lara, Hawk bid",
     "npcs.bakshi :: important and has no plan"),
    ("    status: blocked\n    trigger: someone reads", "    status: blocked\n    trigger_x: someone reads",
     "quests.side_palace_night :: blocked with no trigger"),
    ("  side_lab_theft:\n    code: B\n", "  side_lab_theft:\n",
     "quests.side_lab_theft :: no code"),
    ("      due: Day 6\n      on_fill: the hill road", "      due_x: Day 6\n      on_fill: the hill road",
     "active_world_pressures.monsoon :: no due"),
    ("    actors: [julian_sterne, ruud_kasteel, anselm_hartog]",
     "    actors: [julian_sterne, ruud_kasteel, anselm_hartog, mr_lau]", "no actor \"mr_lau\""),
    ("    name: Chor Bazaar\n    zone: bombay", "    name: Chor Bazaar\n    zone: bombey",
     "locations.chor_bazaar.zone :: no location \"bombey\""),
    ("state: {position: Juhu aerodrome,", "state: {position: the moon,",
     "npcs.joe_dsouza.state.position :: \"the moon\""),
]


class Check(unittest.TestCase):
    def test_a_finished_background_passes(self):
        o = run({"cmd": "check", "background": BG})
        self.assertTrue(o["ok"], o["findings"])

    def test_each_fault_is_caught(self):
        with open(BG, encoding="utf-8") as fh:
            src = fh.read()
        d = tempfile.mkdtemp(prefix="neo_check_")
        for old, new, expect in BREAKS:
            with self.subTest(expect=expect):
                self.assertIn(old, src)
                path = os.path.join(d, "broken.md")
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(src.replace(old, new, 1))
                o = run({"cmd": "check", "background": path})
                self.assertFalse(o["ok"])
                found = [x for v in o["findings"].values() for x in v]
                self.assertTrue(any(expect in x for x in found), (expect, found))


if __name__ == "__main__":
    unittest.main()
