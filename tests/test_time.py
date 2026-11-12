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
        dues, _, _, out = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                                "minutes": 2 * 1440, "pc_zone": "scp_4711"})
        self.assertFalse(out["stopped"])
        count = collections.Counter((at, rid) for at, rid, _ in dues)
        self.assertFalse([k for k, v in count.items() if v > 1], "a due fired twice")
        who = {rid.split(".")[1] for _, rid, _ in dues}
        for npc in ("rosa_delgado", "commander_lindqvist", "gus_pembroke"):
            self.assertIn(npc, who)                           # Day 1 and Day 2 at Site-19

    def test_stops_only_at_what_could_reach_the_pc(self):
        far, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                             "minutes": 120, "pc_zone": "scp_4711"})
        rosa = [d for d in far if "rosa_delgado" in d[1]]
        self.assertTrue(rosa and not rosa[0][2])              # Malaysia is not where the PC is
        near, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                              "minutes": 120, "pc_zone": "site19"})
        rosa = [d for d in near if "rosa_delgado" in d[1]]
        self.assertTrue(rosa and rosa[0][2])

    def test_a_stop_hides_what_comes_after(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                 "minutes": 5 * 1440, "pc_zone": "site19"})
        if o["stopped"]:
            last = o["events"][-1]["at"]
            self.assertTrue(all(e["at"] <= last for e in o["events"]))
            self.assertIn("resume", o)
            self.assertGreater(o["remaining_minutes"], 0)

    def test_a_timed_due_is_placed_at_its_time(self):
        dues, _, _, _ = walk({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                              "minutes": 360, "pc_zone": "scp_4711"})
        at = [d[0] for d in dues if "commander_lindqvist" in d[1]][0]
        self.assertEqual(at, "day 1 10:00")

    def test_triggers_are_listed_not_fired(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                 "minutes": 30, "pc_zone": "site19"})
        ids = [t["id"] for t in o["triggers_to_check"]]
        self.assertIn("quests.darrows_list.trigger", ids)
        self.assertIn("active_world_pressures.pigeon_breakout.clock.due", ids)

    def test_background_has_no_flags(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                 "minutes": 30, "pc_zone": "site19"})
        self.assertEqual(o["flags"], [])

    def test_unknown_zone(self):
        o = run({"cmd": "span", "background": BG, "from": {"day": 1, "clock": 450},
                 "minutes": 30, "pc_zone": "atlantis"})
        self.assertIn("error", o)


if __name__ == "__main__":
    unittest.main()
