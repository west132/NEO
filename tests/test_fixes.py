"""Fixes from the Nov 12 Sheet Anchor test run: due steps, the zone point, place
matching, incidental dues, work linked to its quest, whole-record changes."""
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
        _, dues = span_ids({"from": {"day": 2, "clock": 1200}, "minutes": 120,
                            "pc_zone": "patna_university"})
        bak = [e for e in dues if e["id"] == "npcs.bakshi.state.due"][0]
        self.assertEqual(bak["in_disorder"], "thrives")
        self.assertEqual(bak["zone_point"], {"open": 0, "hidden": 1})   # Bombay −1 / −2

    def test_one_shared_word_names_no_place(self):
        d = deltas("GM-Δ 1\n  ~ npcs.meera_raghavan.state.position :: the university guesthouse, Fort\n"
                   "  ~ npcs.meera_raghavan.state.due :: Day 3 morning examines the half\n")
        o, dues = span_ids({"from": {"day": 3, "clock": 300}, "minutes": 300,
                            "pc_zone": "bombay", "deltas": d})
        m = [e for e in dues if e["id"].startswith("npcs.meera_raghavan")][0]
        self.assertNotEqual(m.get("zone"), "patna_university")
        self.assertTrue(any("names no recorded location" in f for f in o["flags"]))

    def test_whole_record_change_is_applied_by_field(self):
        d = deltas("GM-Δ 1\n  + rights_obligations.door :: {type: contract, parties: [bakshi, player], "
                   "state: {status: open}}\n"
                   "GM-Δ 2\n  ~ rights_obligations.door.state :: {status: paid in full R2}\n"
                   "  ~ locked_case_truths.plate.state :: {plate: snapped in two}\n")
        o = run({"cmd": "merge", "background": BG, "deltas": d})
        self.assertNotIn("whole_record_update", o.get("warnings", {}))
        cap = o["capsule_yaml"]
        self.assertIn("rights_obligations.door.state.status :: R2: paid in full R2", cap)
        self.assertIn("locked_case_truths.plate.state.plate :: R2: snapped in two", cap)

    def test_check_flags_several_moves_in_one_due(self):
        path = os.path.join(TMP, "bg.md")
        text = open(BG, encoding="utf-8").read().replace(
            "due: B-1 Day 1 morning goes with Meera if she lets him",
            "due: Day 1 morning goes with Meera; Day 3 morning tells her")
        open(path, "w", encoding="utf-8").write(text)
        o = run({"cmd": "check", "background": path})
        self.assertTrue(any("no codes" in r for r in o["findings"].get("dues", [])))


    def test_a_resolved_move_stops_firing(self):
        d = deltas("GM-Δ 1\n  ~ npcs.nathan_drake.state.due :: A-3s Day 2 night the auction; "
                   "A-10 Day 5 afternoon Sully offers it to Sterne; A-11 Day 6 night the well\n")
        form = {"cmd": "span", "background": BG, "from": {"day": 2, "clock": 1200},
                "minutes": 5 * 1440, "pc_zone": "patna_university", "deltas": d}
        steps = []
        for _ in range(60):
            o = run(form)
            steps += [e["step"] for e in o["events"]
                      if e["kind"] == "due" and e["id"] == "npcs.nathan_drake.state.due"]
            if not o["stopped"]:
                break
            form = {**form, **o["resume"]}
        self.assertEqual(steps, ["A-10", "A-11"])      # Day 5 and Day 6; the auction move is done

    def test_a_move_code_must_name_a_quest_step(self):
        path = os.path.join(TMP, "bg2.md")
        with open(BG, encoding="utf-8") as f:
            text = f.read().replace("due: B-1 Day 1 morning goes with Meera", "due: Q-9 Day 1 morning goes with Meera")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        o = run({"cmd": "check", "background": path})
        self.assertTrue(any("Q-9" in r for r in o["findings"].get("references", [])))


if __name__ == "__main__":
    unittest.main()
