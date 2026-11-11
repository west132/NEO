import unittest
from _run import run, BG, World

W = World()


def put(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class Save(unittest.TestCase):
    def test_first_and_second_capsule_build(self):
        self.assertTrue(W.merge1["valid"])
        self.assertTrue(W.merge2["valid"])

    def test_validate_and_survival(self):
        o = run({"cmd": "validate", "file": W.save20, "against": W.save10, "background": BG})
        self.assertTrue(o["valid"])
        self.assertEqual(o["survival"]["dropped"], [])

    def test_player_changes_stay_out_of_the_capsule(self):
        with open(W.p("cap2.txt"), encoding="utf-8") as fh:
            cap = fh.read()
        self.assertNotIn("player.condition.hp", cap)

    def test_selfcheck_passes_on_right_answers(self):
        o = run({"cmd": "selfcheck", **W.w20, "round": 50, "answers": {
            "npc_positions": {"bakshi": "Bakshi's shop", "meera_raghavan": "the train to Bombay"},
            "quests": {"B": "succeeded", "side_palace_night": "blocked"},
            "money": "1350", "hp": 12}})
        self.assertEqual(o["verdict"], "pass", o["copy"])

    def test_selfcheck_fails_on_wrong_answers(self):
        o = run({"cmd": "selfcheck", **W.w20, "round": 50,
                 "answers": {"quests": {"B": "active"}, "hp": 9}})
        self.assertEqual(o["verdict"], "fail")
        self.assertIn("reread", o["next"])

    def test_selfcheck_reads_changes_since_the_save(self):
        d = W.p("d3.txt")
        put(d, "GM-Δ 21 ⟵ 20\n  ~ player.condition.hp :: 5\n")
        o = run({"cmd": "selfcheck", **W.w20, "deltas": d, "answers": {"hp": 5}})
        self.assertEqual(o["verdict"], "pass")

    def test_duplicate_quest_letter_is_flagged(self):
        d = W.p("d4.txt")
        put(d, "GM-Δ 21 ⟵ 20\n  + quests.tq_syamantaka.code :: B\n")
        o = run({"cmd": "selfcheck", **W.w20, "deltas": d, "answers": {"hp": 12}})
        self.assertTrue(any("letter B" in x for x in o["tool_checks"].get("quest_codes", [])))

    def test_important_actor_without_a_due_is_flagged(self):
        d = W.p("d5.txt")
        put(d, "GM-Δ 21 ⟵ 20\n  ~ npcs.bakshi.state.due :: none\n")
        o = run({"cmd": "selfcheck", **W.w20, "deltas": d, "answers": {"hp": 12}})
        self.assertIn("npcs.bakshi", o["tool_checks"].get("important_without_due", []))
        s = run({"cmd": "span", **W.w20, "deltas": d, "from": {"day": 2, "clock": 1320},
                 "minutes": 10, "pc_zone": "chor_bazaar"})
        self.assertTrue(any("npcs.bakshi" in f for f in s["flags"]))

    def test_flatten_runs(self):
        o = run({"cmd": "flatten", "background": BG, "save": W.save20, "out": W.p("flat.yaml"),
                 "summary": True})
        self.assertEqual(o["summary"]["quests"]["closed"], 1)  # B succeeded

    def test_background_meets_its_depth_fields(self):
        o = run({"cmd": "selfcheck", **W.w20, "answers": {"hp": 12}})
        self.assertNotIn("depth_fields", o["tool_checks"])


class Forms(unittest.TestCase):
    def test_input_is_json_only(self):
        self.assertIn("error", run({"no": "cmd"}))
        self.assertIn("error", run({"cmd": "nonsense"}))

    def test_errors_name_fields_not_flags(self):
        o = run({"cmd": "vitals", "level": 3})
        self.assertNotIn("--", o["error"])
        self.assertIn("v,", o["error"])

    def test_forms_list(self):
        forms = run({"cmd": "forms"})["forms"]
        for f in ("action", "help", "ask", "combat", "span", "selfcheck", "award", "merge"):
            self.assertIn(f, forms)


if __name__ == "__main__":
    unittest.main()
