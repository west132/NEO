import collections, unittest
from _run import run, BG


def walk(form, limit=80):
    """Run a span to its end, always judging "it doesn't reach the PC"."""
    dues, calls, flags, out = [], 0, [], None
    while calls < limit:
        out = run(form); calls += 1
        for e in out["events"]:
            if e["kind"] == "due":
                dues.append((e["at"], e["id"], bool(e.get("could_reach_pc"))))
        flags = out["flags"]
        if not out["stopped"]:
            break
        form = {**form, **out["resume"]}
    return dues, calls, flags, out


class Time(unittest.TestCase):
    def test_every_due_fires_once(self):
        dues, _, _, out = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 1200},
                                "minutes": 2 * 1440, "pc_zone": "chor_bazaar"})
        self.assertFalse(out["stopped"])
        count = collections.Counter((at, rid) for at, rid, _ in dues)
        self.assertFalse([k for k, v in count.items() if v > 1], "a due fired twice")
        who = {rid.split(".")[1] for _, rid, _ in dues}
        for npc in ("julian_sterne", "lara_croft", "nathan_drake", "asian_hawk", "bakshi"):
            self.assertIn(npc, who)                           # all at the Day 2 auction

    def test_stops_only_at_what_could_reach_the_pc(self):
        far, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 1200},
                             "minutes": 2 * 1440, "pc_zone": "patna_university"})
        bak = [d for d in far if "bakshi" in d[1]]
        self.assertTrue(bak and not bak[0][2])                # Bombay is not where the PC is
        near, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 1200},
                              "minutes": 2 * 1440, "pc_zone": "chor_bazaar"})
        bak = [d for d in near if "bakshi" in d[1]]
        self.assertTrue(bak and bak[0][2])

    def test_a_stop_hides_what_comes_after(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 1200},
                 "minutes": 5 * 1440, "pc_zone": "chor_bazaar"})
        if o["stopped"]:
            last = o["events"][-1]["at"]
            self.assertTrue(all(e["at"] <= last for e in o["events"]))
            self.assertIn("resume", o)
            self.assertGreater(o["remaining_minutes"], 0)

    def test_night_due_is_placed_at_night(self):
        dues, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 1200},
                              "minutes": 2 * 1440, "pc_zone": "patna_university"})
        at = [d[0] for d in dues if "bakshi" in d[1]][0]
        self.assertEqual(at, "day 2 21:00")

    def test_triggers_are_listed_not_fired(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 0, "clock": 480},
                 "minutes": 30, "pc_zone": "bombay"})
        ids = [t["id"] for t in o["triggers_to_check"]]
        self.assertIn("npcs.kamini.state.due", ids)
        self.assertIn("quests.side_palace_night.trigger", ids)

    def test_background_has_no_flags(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 0, "clock": 480},
                 "minutes": 30, "pc_zone": "bombay"})
        self.assertEqual(o["flags"], [])

    def test_unknown_zone(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 0, "clock": 480},
                 "minutes": 30, "pc_zone": "atlantis"})
        self.assertIn("error", o)


if __name__ == "__main__":
    unittest.main()
