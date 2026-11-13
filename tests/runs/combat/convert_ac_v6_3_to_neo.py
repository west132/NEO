"""Convert the AC Syndicate v6.3 background to NEO v0. Writes the NEO background and
a list of what was added beyond the author's file (for review)."""
import re, sys, yaml, copy

src, out_path, inv_path = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(src, encoding="utf-8").read()
y0 = text.index("```yaml\n")
y1 = text.index("```", y0 + 8)
d = yaml.safe_load(text[y0 + 8:y1])
invented = []

def inv(what):
    invented.append(what)

# ---- frame ----
n = {}
for k in ("background_id", "provenance", "requested", "design_logic"):
    n[k] = d[k]
ch = d.pop("chapter")
n["setting"] = d["setting"]
cc = copy.deepcopy(d["canon_course"])
cc["timed_plans"] = cc.pop("timed_templar_plans")
n["canon_course"] = cc
n["setting_anchors"] = d["setting_anchors"]
for k in ("content_bounds", "enabled_modules", "narrative_theme", "premise", "question", "storylines"):
    n[k] = d[k]

# ---- quests ----
CODES = {"throat_of_london": "A", "tq_whitechapel": "A-1", "tq_syrup": "A-2", "tq_tower": "A-3",
         "tq_omnibus": "A-4", "tq_bank": "A-5", "tq_parliament": "A-6", "tq_vault_plans": "A-7",
         "tq_alhambra": "A-8", "tq_ball": "A-9", "side_mill_children": "B"}
SOURCES = {"throat_of_london": "canon_course", "side_mill_children": "clara_odea"}
qs = {}
for qid, q in d["quests"].items():
    nq = {"code": CODES[qid], "objective": q["objective"],
          "source": SOURCES.get(qid, "canon_course"), "spine": q["spine"], "hook": q["hook"],
          "level": q.get("quest_level", 7), "status": "available" if q["status"] == "active" else q["status"]}
    if qid == "throat_of_london":
        nq["parts_are"] = "quests A-1 … A-9, one per canon beat"
    for k in ("trigger", "routes", "support_refs"):
        if q.get(k) is not None:
            nq[k] = q[k]
    qs[qid] = nq
inv("quest codes A (throat_of_london), A-1 … A-9 (the beat quests, in beat order), B (side_mill_children); "
    "throat_of_london level 7 (the ball's level; v6.3 had none for the chain root)")
n["quests"] = qs
n["development_threads"] = d["development_threads"]
n["active_world_pressures"] = d["active_world_pressures"]
n["locked_case_truths"] = d["locked_case_truths"]

# ---- people: depth and depth fields (NEO_SAVE §1) ----
ADD = {
 "jacob_frye": dict(depth=3,
   voice="quick, cocky, cheerful; a joke before the punch; calls Evie \"dearest sister\" when she is right",
   want="London free of Starrick, his own way", fear="being his father's lesser",
   line="never leaves one of his own people behind",
   pull="to be taken seriously by Evie and the Brotherhood",
   secret={"what": "he came to London as much to get out from under the Council and his father's name as for the Creed",
           "why": "pride; he would never say it to Evie"},
   beliefs={"templars": "cut off the head and the body falls — the Templars are just men with titles"},
   due="A-1 Day 3 evening takes over the Clinkers in a Whitechapel pub and renames them the Rooks"),
 "evie_frye": dict(depth=3,
   voice="precise, dry, unhurried; a raised eyebrow in words; quotes their father when it helps",
   want="the Piece of Eden safe from the Templars", fear="Jacob getting them both killed",
   line="never risks bystanders for a target",
   pull="Henry, and what she feels for him, against the work",
   secret={"what": "her father's notes say more about the Shroud than she has told Jacob",
           "why": "he would charge at it before she knows where it is"},
   beliefs={"gangs": "London can be won without the gang war; the streets are Jacob's distraction"},
   due="A-3 Day 2 morning starts Henry's records and her father's notes on the Piece of Eden"),
 "henry_green": dict(depth=3,
   voice="soft, careful, formal; apologises before he disagrees; exact about history",
   want="the Templars out of London and the Shroud safe", fear="failing his father's name",
   line="never kills someone who isn't a combatant",
   pull="to stay safe behind his shop counter, and to stand in the field beside Evie",
   secret={"what": "he is Jayadeep Mir, son of the Assassin Arbaaz Mir, and tells almost no one",
           "why": "the weight of his father's name, and safety"},
   beliefs={"himself": "he is a helper to better Assassins, not a leader"},
   due="A-1 Day 1 morning meets the twins at his shop"),
 "frederick_abberline": dict(depth=2,
   voice="flat, patient, dry; notebook out; says \"we'll see\" and means no",
   want="Kaylock in a cell", fear="being bought or buried", line="never takes a bribe",
   secret={"what": "he keeps a private list of the bought constables at his lodgings",
           "why": "proof for the day someone above him will listen"},
   due="A-1 Day 4 morning posts bounties on Blighter men at the station board"),
 "clara_odea": dict(depth=2,
   voice="sharp and fast, East End Irish, swears like a docker, bargains like a fishwife",
   want="the mill children free", fear="the workhouse", line="never leaves a kid behind",
   secret={"what": "she worked a Starrick mill herself and ran from the workhouse",
           "why": "fear of being sent back"},
   due="B Day 5 afternoon sends a runner to whoever is fighting the Blighters"),
 "ned_wynert": dict(depth=2,
   voice="easy patter, a grin in every sentence; haggles for fun",
   want="free trade and a fair cut", fear="Starrick's monopoly", line="never breaks his word on a delivery",
   secret={"what": "he still carries the odd cargo for Starrick's people when the money is right",
           "why": "a trader with one customer is a dead trader"},
   due="A-1 when Whitechapel changes hands, offers cargo work to whoever holds it"),
 "agnes_macbean": dict(depth=2,
   voice="blunt Scots; short sentences; warms up slowly",
   want="her train back", fear="losing her livelihood", line="never lets anyone harm the engine",
   secret={"what": "she still has a spare set of the engine's keys hidden in the yard",
           "why": "she never accepted it was Kaylock's"},
   due="A-1 when Kaylock's train changes hands, claims it"),
 "crawford_starrick": dict(depth=3,
   voice="polished, possessive (\"my London\", \"my city\"); lists things in threes when anxious",
   want="total control of London", fear="disorder and losing face",
   line="never does his own dirty work where it can be seen — until the ball",
   pull="the need to be admired, against the need for order",
   secret={"what": "he means to kill the Queen and London's elite at the ball, and take the Shroud",
           "why": "a city that is his, permanently"},
   beliefs={"twins": "the new gang is a nuisance for his lieutenants, not a threat to him"}),
 "lucy_thorne": dict(depth=3,
   voice="cool, clipped, scholarly; corrects people's Latin",
   want="the Shroud, and her place in the Order", fear="Starrick taking the credit",
   line="never hands a Piece of Eden to anyone outside the Order",
   pull="knowledge for its own sake, against serving Starrick's ends",
   secret={"what": "she means to use the Shroud's full power, beyond anything Starrick plans",
           "why": "she thinks the Order wastes what it finds"},
   beliefs={"evie": "Evie Frye is a clever amateur, no match for a scholar"},
   due="A-3 when beat_2 opens, searches the Kenway mansion; A-3 when beat_3 opens, goes to St Paul's; then the Tower"),
 "rexford_kaylock": dict(depth=3,
   voice="loud, crude, boastful; railway slang; laughs at his own threats",
   want="Whitechapel, and Starrick's favour", fear="Roth's contempt",
   line="never backs down in front of his men",
   pull="to please Starrick, and to impress Roth",
   secret={"what": "he skims the Whitechapel protection money before it goes up the line",
           "why": "his own train, his own cut"},
   beliefs={"rooks": "the new gang is a pub brawl that will be over in a week"},
   due="A-1 Day 7 night his men start breaking Rook pubs"),
 "john_elliotson": dict(depth=2,
   voice="grand, lecturing, a doctor's certainty; never says \"poison\"",
   want="his syrup in every home in London", fear="being called a quack", line="never doubts his cure in front of others",
   secret={"what": "he records the deaths among his patients and buyers as fever",
           "why": "pride, and Starrick's money"},
   due="A-2 Day 20 night a new shipment from the docks; then every 14 days"),
 "malcolm_millner": dict(depth=2,
   voice="brusque, counting-house dry; speaks in prices",
   want="his lines moving and paid", fear="losing his lines to a rival", line="never touches the cargo himself",
   secret={"what": "he suspects Pearl Attaway wants his lines and is watching her",
           "why": "he knows how Templars rise"},
   due="A-4 Day 14 night a contraband train runs; then every 14 days"),
 "pearl_attaway": dict(depth=2,
   voice="gracious, warm, flattering; every kindness has a price",
   want="her own empire", fear="being seen as Starrick's lesser", line="never seen with Starrick in public",
   secret={"what": "she is Starrick's cousin, and his ally", "why": "her rival's pose is her best tool"},
   due="A-4 when beat_3 opens, invites the Rooks' leader to her office"),
 "philip_twopenny": dict(depth=2,
   voice="nervous, fussy, theatrical; dabs his brow",
   want="money, more of it", fear="being caught", line="never risks his own skin",
   secret={"what": "he is \"Plutus\", robbing his own bank", "why": "greed, and Starrick's plan"},
   due="A-5 Day 110 night the great Plutus robbery"),
 "earl_of_cardigan": dict(depth=2,
   voice="a parade-ground bark; tells the Light Brigade story to anyone",
   want="Disraeli gone", fear="being laughed at", line="a gentleman never runs",
   secret={"what": "he is \"Mr. B\", planning Disraeli's death", "why": "power, and Starrick's bills"},
   due="A-6 Day 130 afternoon the attempt on Disraeli"),
 "maxwell_roth": dict(depth=2,
   voice="theatrical, purring, witty; calls people \"darling\" and means \"prey\"",
   want="a show worth watching", fear="boredom", line="never lets a party be dull",
   secret={"what": "he means to turn on Starrick", "why": "Starrick bores him"},
   due="A-8 Day 150 night the factory; A-8 when beat_6 opens, courts the Rooks' leader"),
}
LIEUT = ["cletus_strain", "octavia_plumb", "bloody_nora", "edith_swinebourne", "victor_lynch", "lilla_graves"]
for lid in LIEUT:
    ADD[lid] = dict(depth=1, voice="a Blighter boss's swagger; the GM develops the rest from the game",
                    want="to hold the borough for Starrick", fear="Roth's contempt and Starrick's displeasure",
                    due="A when the Rooks contest the borough (rooks_rising), raids the Rooks and calls the gang war when the grip breaks")
ONE = {
 "charles_darwin": ("old, gentle, curious; stubborn about truth", "the syrup exposed", "Templar men at his door",
                    "A-2 when the syrup case reaches him, helps expose and destroy the distillery"),
 "charles_dickens": ("lively, sentimental, sharp-eyed; collects strange tales", "a good ghost story", "a dull evening", None),
 "karl_marx": ("intense, kind to workers; long sentences", "workers organised", "the bosses' men", None),
 "alexander_graham_bell": ("young, eager, words tumbling over each other", "to build and test", "a gadget failing in front of people",
                           "A-1 when the twins bring him the broken launcher, mends it"),
 "florence_nightingale": ("brisk, formidable, no patience for nonsense", "the syrup's deaths stopped", "her nurses overrun", None),
 "benjamin_disraeli": ("witty, theatrical, a phrase for everything", "to govern", "a knife in the Lords", None),
 "queen_victoria": ("grave, dutiful, private; in mourning", "to reign", "scandal", None),
}
for oid, (voice, want, fear, due) in ONE.items():
    ADD[oid] = dict(depth=1, voice=voice, want=want, fear=fear, due=due)

POSFIX = {"karl_marx": "Whitechapel", "alexander_graham_bell": "Whitechapel", "charles_dickens": "The Strand"}
npcs = {}
for aid, r in d["npcs"].items():
    a = ADD[aid]
    r = copy.deepcopy(r)
    nr = {"depth": a["depth"]}
    for k in ("name", "job", "belongs", "gender", "character"):
        nr[k] = r.pop(k)
    nr["voice"] = a["voice"]
    nr["in_disorder"] = r.pop("in_disorder")
    st = r.pop("state")
    if aid in POSFIX:
        st["position"] = POSFIX[aid]
    if a.get("due"):
        st["due"] = a["due"]
    nr["state"] = st
    old = r.pop("drives", {}) or {}
    dr = {"want": a["want"], "fear": a["fear"]}
    if a.get("line"): dr["line"] = a["line"]
    if a.get("pull"): dr["pull"] = a["pull"]
    for k in ("wants", "fears", "values", "loyalties"):
        if old.get(k): dr[k] = old[k]
    nr["drives"] = dr
    if a.get("secret"): nr["secret"] = a["secret"]
    if r.get("relationships"): nr["relationships"] = r.pop("relationships")
    kn = r.pop("knowledge", {}) or {}
    if a.get("beliefs"): kn["beliefs"] = a["beliefs"]
    if kn: nr["knowledge"] = kn
    for k, v in r.items():
        nr[k] = v
    npcs[aid] = nr
inv("depth for every NPC (3: Jacob, Evie, Henry, Starrick, Lucy Thorne, Kaylock · 2: Abberline, Clara, Ned, "
    "Agnes, Elliotson, Millner, Pearl, Twopenny, Cardigan, Roth · 1: the six borough leaders and the "
    "historical figures)")
inv("a voice line for every NPC")
inv("want and fear for each (from your wants/fears where you had them; one plain line each)")
for aid in ADD:
    a = ADD[aid]
    bits = []
    if a.get("line"): bits.append(f"line: {a['line']}")
    if a.get("pull"): bits.append(f"pull: {a['pull']}")
    if a.get("secret"): bits.append(f"secret: {a['secret']['what']} ({a['secret']['why']})")
    if a.get("beliefs"): bits.append("belief: " + "; ".join(a["beliefs"].values()))
    if bits:
        inv(f"{npcs[aid]['name']} — " + " · ".join(bits))
inv("dues re-written with quest codes and a time of day (Henry Day 1 morning, Evie Day 2 morning, Jacob Day 3 "
    "evening, Abberline Day 4 morning, Clara Day 5 afternoon, Kaylock Day 7 night, Millner Day 14 night, "
    "Elliotson Day 20 night, Twopenny Day 110 night, Cardigan Day 130 afternoon, Roth Day 150 night); trigger "
    "dues for the six borough leaders, Darwin and Bell, which had none")
inv("positions: Marx and Bell placed in Whitechapel, Dickens on the Strand (their old positions named no recorded place); throat_of_london status available (NEO Round 0 allows only available | blocked)")
n["npcs"] = npcs
n["factions"] = d["factions"]
n["locations"] = d["locations"]

# ---- player ----
pl = copy.deepcopy(d["player"])
pl["condition"] = {"hp": "[derived maximum]", **pl["condition"]}
pl["item_points"] = {"rank": pl["item_points"]["rank"], "basis": pl["item_points"]["basis"]}
n["player"] = pl
n["rights_obligations"] = d["rights_obligations"]
n["active_commitments"] = d["active_commitments"]

# ---- endings (chapters are gone in NEO) ----
n["ending_conditions"] = {"core_conditions": [
    "the Shroud vault resolved at the Queen's ball (canon_course beat_7_ball; quest A-9)",
    "Day 180 reached"], "hidden_conditions": [], "closed": []}
inv("ending_conditions from your chapter end (beat_7 or Day 180); NEO has no chapters")

ws = copy.deepcopy(d["world_state"])
ws = {k: ws[k] for k in ("location", "time", "environment", "material_history")} | {"pending": {}} | \
     {k: ws[k] for k in ("unowned_facts", "glossary")}
n["world_state"] = ws

yml = yaml.safe_dump(n, allow_unicode=True, sort_keys=False, width=110, default_flow_style=False)

# ---- prose ----
head = text[:y0]
tail = text[y1 + 3:]
R = [
 ("# BACKGROUND — Assassin's Creed Syndicate: London 1868 v6.3",
  "# BACKGROUND — Assassin's Creed Syndicate: London 1868 (NEO v0)"),
 ("For `NEW ENGINE v6.3`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead.",
  "A NEO v0 background (converted from v6.3). **Round-0 truth**; once play begins this file is history and the save changes instead. `mode: canon`: attach `modules/NEO_MODULES_v0.md` with the play set."),
 ("(engine I3, §13.1 CANON MODE, §16.6)", "(GM §7.5, modules: Canon mode, GM §7.4 WRONG FACT)"),
 ("(engine I6)", "(GM §1)"), ("(engine I3)", "(GM §1)"),
 ("(engine §13.4)", "(RULES §15.4)"), ("(helper stability --lasting)", "(the tool's stability form, lasting: yes)"),
 ("mark on that borough's grip track (engine §13.4: a hidden cause\n  removed +1, a decisive act +2)",
  "mark on that borough's grip track (RULES §15.4: a hidden cause\n  removed +1, a decisive act +2)"),
 ("routine continuation (engine §2)", "routine continuation (GM §3 ROUTINE, §7.2)"),
]
for a, b in R:
    assert a in head + tail, a
    head, tail = head.replace(a, b), tail.replace(a, b)
tail = tail.replace("Day 0 evening is routine continuation (engine §2)", "Day 0 evening is routine continuation (GM §7.2)")
tail = tail.replace("(economy_model)", "(economy_model, RULES §12 PRICES)")
tail = tail.replace("prompt continue or extend", "give the ending review (GM §7.6)")
left = re.findall(r"engine [§I]\S*|helper \w+", head + tail)
open(out_path, "w", encoding="utf-8").write(head + "```yaml\n" + yml + "```" + tail)
open(inv_path, "w", encoding="utf-8").write("\n".join(f"- {x}" for x in invented) + "\n")
print("left engine refs:", left)
