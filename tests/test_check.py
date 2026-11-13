import os, tempfile, unittest
from _run import run, BG

BREAKS = [
    ("  priya_raman:\n    depth: 1\n", "  priya_raman:\n", "npcs.priya_raman :: no depth"),
    ("    voice: warm and dry;", "    vocie: warm and dry;", "npcs.rosa_delgado :: depth 3 lacks voice"),
    ("      due: A-1 Day 1 08:30 meets West", "      due_old: A-1 Day 1 08:30 meets West",
     "npcs.rosa_delgado :: important and has no plan"),
    ("    status: blocked\n    trigger: Leo's behaviour", "    status: blocked\n    trigger_x: Leo's behaviour",
     "quests.darrows_list :: blocked with no trigger"),
    ("      due: Day 75\n      on_fill: Rosa learns", "      due_x: Day 75\n      on_fill: Rosa learns",
     "active_world_pressures.rosa_transfer :: no due"),
    ("    actors: [felix_darrow, leo_brandt]", "    actors: [felix_darrow, leo_brandt, mr_x]",
     "no actor \"mr_x\""),
    ("      position: Site-19 labs", "      position: the moon",
     "npcs.tomas_reyes_hart.state.position :: \"the moon\""),
    ("  night_shift:\n    code: C\n", "  night_shift:\n", "quests.night_shift :: no code"),
]


class Check(unittest.TestCase):
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
