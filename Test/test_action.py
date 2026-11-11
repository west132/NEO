import unittest
from _run import run, BG, World

W = World()


class Action(unittest.TestCase):
    def base(self, **kw):
        f = {"cmd": "action", **W.w20, "actor": "pc", "action": "test", "skill": "brawling",
             "opposition": {"level": 4}}
        f.update(kw)
        return f

    def test_capability_read_from_the_world(self):
        o = run({"cmd": "action", "background": BG, "actor": "asian_hawk", "action": "vault",
                 "skill": "acrobatics", "opposition": {"level": 5}})
        self.assertEqual(o["bound"]["capability"], 11)        # level 8 + T3

    def test_roll_adds_up(self):
        o = run(self.base())
        d = o["copy"][0]
        self.assertIn("2d10:", d)
        self.assertEqual(o["success"], o["total"] >= o["difficulty"])

    def test_cost_ladder(self):
        none = run(self.base())
        self.assertIn("setback/", none["copy"][1])
        loss = run(self.base(danger={"what": "a knife", "reaches": "yes", "direct_result": "harm"},
                             cost_form="inflict harm"))
        self.assertIn("loss/", loss["copy"][1])
        severe = run(self.base(danger={"what": "a long fall", "reaches": "yes",
                                       "direct_result": "death"}, cost_form="inflict harm"))
        self.assertIn("severe/", severe["copy"][1])
        far = run(self.base(danger={"what": "a sniper", "reaches": "no", "direct_result": "death"}))
        self.assertIn("setback/", far["copy"][1])

    def test_cost_form_required_when_something_can_hurt(self):
        o = run(self.base(danger={"what": "a knife", "reaches": "yes", "direct_result": "harm"}))
        self.assertIn("cost_form", o["error"])

    def test_a_category_counts_once(self):
        o = run(self.base(conditions=[{"category": "time", "effect": "adverse", "fact": "rushed"},
                                      {"category": "time", "effect": "adverse", "fact": "late"}]))
        self.assertIn("twice", o["error"])

    def test_a_condition_needs_its_fact(self):
        o = run(self.base(conditions=[{"category": "time", "effect": "adverse"}]))
        self.assertIn("fact", o["error"])

    def test_one_item_counts_once(self):
        o = run({"cmd": "action", "background": BG, "actor": "lara_croft", "action": "shoot",
                 "skill": "firearms", "gear_tier": "twin pistols", "tool": {"fit": "good"},
                 "opposition": {"level": 6}})
        self.assertIn("once", o["error"])

    def test_opposition_is_exactly_one_kind(self):
        o = run(self.base(opposition={"level": 3, "grade": "easy"}))
        self.assertIn("opposition", o["error"])

    def test_unknown_actor(self):
        o = run(self.base(actor="nobody"))
        self.assertIn("no actor", o["error"])

    def test_no_odds_stop(self):
        o = run(self.base(odds=True))
        self.assertNotIn("odds_percent", o)


class HelpAndAsk(unittest.TestCase):
    def test_help_target(self):
        self.assertEqual(run({"cmd": "help", "ask": "x"})["target"], 15)
        self.assertEqual(run({"cmd": "help", "ask": "x", "sources": ["a", "b", "c"]})["target"], 12)
        self.assertEqual(run({"cmd": "help", "ask": "x", "hostile": True})["target"], 16)

    def test_help_at_most_three_sources(self):
        self.assertIn("error", run({"cmd": "help", "ask": "x", "sources": list("abcd")}))

    def test_help_odds_near_21_percent(self):
        hits = sum(run({"cmd": "help", "ask": "x"})["exists"] for _ in range(300))
        self.assertTrue(35 <= hits <= 95, hits)               # 21% of 300 = 63

    def test_ask_two_facts_a_side(self):
        o = run({"cmd": "ask", "who": "x", "question": "q",
                 "for": [{"fact": "a", "points": 2}, {"fact": "b", "points": 1},
                         {"fact": "c", "points": 1}]})
        self.assertIn("error", o)

    def test_ask_gives_a_band(self):
        o = run({"cmd": "ask", "who": "Joe", "question": "fly tonight?",
                 "for": [{"fact": "paid double", "points": 2}],
                 "against": [{"fact": "the storm", "points": 2}]})
        self.assertIn(o["answer"], ("YES, AND", "YES", "NO, BUT", "NO, AND"))


if __name__ == "__main__":
    unittest.main()
