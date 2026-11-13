import unittest
from _run import run, BG, World

W = World()


def act(**kw):
    f = {"cmd": "action", **W.w20, "actor": "pc", "action": "test", "skill": "brawling",
         "opposition": {"level": 4}}
    f.update(kw)
    return run(f)


def until(success, tries=60, **kw):
    for _ in range(tries):
        o = act(**kw)
        if o["success"] == success:
            return o
    raise AssertionError("never rolled the wanted result")


class Growth(unittest.TestCase):
    # PC: level 3, brawling T2 → personal skill level 5; threshold is challenge ≥ 3
    def test_a_real_challenge_credits_evidence(self):
        o = until(True, opposition={"level": 4})
        self.assertEqual(o["growth"]["gain"], 1)
        self.assertIn("~ player.skills.brawling.evidence :: 1", o["gm_delta"])

    def test_threshold_is_skill_level_minus_two(self):
        self.assertEqual(until(True, opposition={"level": 3})["growth"]["gain"], 1)
        self.assertEqual(until(True, opposition={"level": 2})["growth"]["gain"], 0)

    def test_failure_credits_nothing(self):
        o = until(False, opposition={"level": 9})
        self.assertNotIn("growth", o)

    def test_one_credit_per_skill_per_period(self):
        o = until(True, skill="acrobatics", opposition={"level": 5})   # already credited
        self.assertEqual(o["growth"]["gain"], 0)

    def test_boundary_raises_tier_at_threshold(self):
        o = run({"cmd": "boundary", "cls": "NORMAL", "tier": "T1", "evidence": 12})
        self.assertEqual(o["new"]["tier"], "T2")
        self.assertEqual(o["new"]["evidence"], 2)

    def test_ceiling_holds_without_a_source(self):
        o = run({"cmd": "boundary", "cls": "NORMAL", "tier": "T2", "evidence": 25})
        self.assertEqual(o["new"]["tier"], "T2")
        self.assertEqual(o["new"]["class"], "NORMAL")

    def test_class_raise_needs_a_source(self):
        o = run({"cmd": "boundary", "cls": "NORMAL", "tier": "T2", "evidence": 25,
                 "class_source": "trained under a master"})
        self.assertEqual(o["new"]["class"], "ELITE")


class XpAndPoints(unittest.TestCase):
    def test_award_writes_the_paid_marker(self):
        o = run({"cmd": "award", **W.w20, "actor": "pc", "challenge": 4, "scope": "meaningful",
                 "source": "quest B"})
        self.assertGreater(o["award"], 0)
        self.assertTrue(any("material_history" in l for l in o["gm_delta"]))

    def test_item_points(self):
        self.assertEqual(run({"cmd": "points", "rank": "commoner", "current": 37, "spend": 3,
                              "label": "lockpicks"})["current"], 34)
        o = run({"cmd": "points", "rank": "commoner", "current": 10, "refill": True})
        self.assertEqual((o["refill"], o["current"]), (8, 18))          # a fifth of 40
        o = run({"cmd": "points", "rank": "commoner", "current": 2, "spend": 3, "label": "x"})
        self.assertEqual((o["spent"], o["current"]), (0, 2))            # the spend fails


if __name__ == "__main__":
    unittest.main()
