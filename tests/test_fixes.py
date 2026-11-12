"""Fixes from the Nov 12 test run: move codes, the zone point, place matching,
whole-record changes."""
import os, tempfile, unittest
from _run import run, BG

TMP = tempfile.mkdtemp(prefix="neo_fix_")


def deltas(text):
    path = os.path.join(TMP, f"d{abs(hash(text))}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def span_ids(form):
    o = run({"cmd": "span", "background": BG, **form})
    return o, [e for e in o["events"] if e["kind"] == "due"]


class Fixes(unittest.TestCase):
    def test_actor_dues_carry_the_zone_point(self):
        _, dues = span_ids({"from": {"day": 9, "clock": 1200}, "minutes": 1440,
                            "pc_zone": "scp_4711"})
        doe = [e for e in dues if e["id"] == "npcs.stag_coordinator.state.due"][0]
        self.assertEqual(doe["in_disorder"], "thrives")
        self.assertEqual(doe["zone_point"], {"open": 0, "hidden": 1})   # pine barrens 0 / −2

    def test_one_shared_word_names_no_place(self):
        d = deltas("GM-Δ 1\n  ~ npcs.dr_brickston.state.position :: a diner in Ohio\n"
                   "  ~ npcs.dr_brickston.state.due :: Day 3 morning drives home\n")
        o, dues = span_ids({"from": {"day": 3, "clock": 300}, "minutes": 300,
                            "pc_zone": "scp_4711", "deltas": d})
        m = [e for e in dues if e["id"].startswith("npcs.dr_brickston")][0]
        self.assertNotEqual(m.get("zone"), "megs_diner")
        self.assertTrue(any("names no recorded location" in f for f in o["flags"]))

    def test_whole_record_change_is_applied_by_field(self):
        d = deltas("GM-Δ 1\n  + rights_obligations.door :: {type: contract, parties: [rosa_delgado, player], "
                   "state: {status: open}}\n"
                   "GM-Δ 2\n  ~ rights_obligations.door.state :: {status: paid in full R2}\n"
                   "  ~ locked_case_truths.loewes_case.state :: {copycat: caught}\n")
        o = run({"cmd": "merge", "background": BG, "deltas": d})
        self.assertNotIn("whole_record_update", o.get("warnings", {}))
        cap = o["capsule_yaml"]
        self.assertIn("rights_obligations.door.state.status :: R2: paid in full R2", cap)
        self.assertIn("locked_case_truths.loewes_case.state.copycat :: R2: caught", cap)

    def test_check_flags_several_moves_in_one_due(self):
        path = os.path.join(TMP, "bg.md")
        with open(BG, encoding="utf-8") as f:
            text = f.read().replace(
                "due: L Day 3 a late-night call West can overhear; L Day 12 skips cards night; "
                "L Day 29 copies the list if not helped",
                "due: Day 3 a late-night call West can overhear; Day 12 skips cards night")
        open(path, "w", encoding="utf-8").write(text)
        o = run({"cmd": "check", "background": path})
        self.assertTrue(any("no codes" in r for r in o["findings"].get("dues", [])))


    def test_a_resolved_move_stops_firing(self):
        d = deltas("GM-Δ 1\n  ~ npcs.leo_brandt.state.due :: Ls Day 3 a late-night call; "
                   "L Day 12 skips cards night; L Day 14 evening asks West for help\n")
        form = {"cmd": "span", "background": BG, "from": {"day": 2, "clock": 1200},
                "minutes": 13 * 1440, "pc_zone": "scp_4711", "deltas": d}
        steps = []
        for _ in range(120):
            o = run(form)
            steps += [e["step"] for e in o["events"]
                      if e["kind"] == "due" and e["id"] == "npcs.leo_brandt.state.due"]
            if not o["stopped"]:
                break
            form = {**form, **o["resume"]}
        self.assertEqual(steps, ["L", "L"])            # Day 12 and Day 14; the Day 3 move is done

    def test_a_move_code_must_name_a_quest_step(self):
        path = os.path.join(TMP, "bg2.md")
        with open(BG, encoding="utf-8") as f:
            text = f.read().replace("due: L Day 3 a late-night call", "due: Q-9 Day 3 a late-night call")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        o = run({"cmd": "check", "background": path})
        self.assertTrue(any("Q-9" in r for r in o["findings"].get("references", [])))


if __name__ == "__main__":
    unittest.main()
