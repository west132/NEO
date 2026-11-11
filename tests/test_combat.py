import unittest
from _run import run, BG, World

W = World()


class Combat(unittest.TestCase):
    def test_pauses_at_a_turning_point(self):
        o = run({"cmd": "combat", "background": BG,
                 "side": [{"actor": "asian_hawk", "skill": "brawling", "damage": "1d3"}],
                 "opponents": [{"name": "merc 1", "level": 3, "damage": "1d6"},
                               {"name": "merc 2", "level": 3, "damage": "1d6"}]})
        self.assertTrue(o["paused"])
        self.assertGreaterEqual(o["exchanges"], 1)
        self.assertIn("at_pause", o)

    def test_stop_condition_from_the_plan(self):
        seen = False
        for _ in range(12):
            o = run({"cmd": "combat", **W.w20,
                     "side": [{"actor": "pc", "skill": "brawling", "damage": "1d3"}],
                     "opponents": [{"actor": "ruud_kasteel", "skill": "brawling", "damage": "1d8"}],
                     "stop": {"hp_at_or_below": "half"}})
            if "stop condition" in o["paused"]:
                seen = True
                self.assertLessEqual(o["side"][0]["hp"], 7)   # half of 14
                break
        self.assertTrue(seen, "the plan's stop condition never fired in 12 fights")

    def test_hp_never_below_zero_and_is_written_back(self):
        o = run({"cmd": "combat", **W.w20,
                 "side": [{"actor": "pc", "skill": "brawling", "damage": "1d3"}],
                 "opponents": [{"actor": "ruud_kasteel", "skill": "brawling", "damage": "1d8"}]})
        for f in o["side"] + o["opponents"]:
            self.assertGreaterEqual(f["hp"], 0)
        for line in o["gm_delta"]:
            self.assertRegex(line, r"^~ (player\.condition|npcs\.\w+\.state)\.hp :: \d+$")

    def test_outnumbered_is_one_condition(self):
        o = run({"cmd": "combat", "background": BG,
                 "side": [{"actor": "asian_hawk", "skill": "brawling", "damage": "1d3"}],
                 "opponents": [{"name": "a", "level": 3}, {"name": "b", "level": 3},
                               {"name": "c", "level": 3}], "max_exchanges": 1})
        first = [l for l in o["copy"] if "Difficulty" in l][0]
        self.assertIn("Difficulty: 11", first)                # 10 + 1, never more

    def test_continue_with_hp_as_it_stands(self):
        o = run({"cmd": "combat", "background": BG,
                 "side": [{"actor": "asian_hawk", "skill": "brawling", "damage": "1d3", "hp": 5}],
                 "opponents": [{"name": "merc", "level": 3, "hp": 2}], "max_exchanges": 1})
        self.assertLessEqual(o["side"][0]["hp"], 5)
        self.assertLessEqual(o["opponents"][0]["hp"], 2)


if __name__ == "__main__":
    unittest.main()
