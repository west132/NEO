#!/usr/bin/env python3
"""neo_math — the NEO RULES tool: dice, arithmetic, record handling.
Owns no state and decides nothing. Input is one JSON form, from a file or stdin:
    python neo_math_v0.py form.json        python neo_math_v0.py < form.json
Every form has "cmd". `{"cmd": "forms"}` lists them. Lines under "copy" go into the
turn verbatim; lines under "gm_delta" go into the round's GM-Δ block."""
from __future__ import annotations
import argparse, json, math, re, secrets

TOOL_VERSION = "neo-0"
_rng = secrets.SystemRandom()

XP_REQ = {
    1:126,2:164,3:220,4:297,5:400,6:534,7:705,8:918,9:1181,
    10:1500,11:1883,12:2339,13:2875,14:3500,15:4225,16:5059,17:6012,
    18:7096,19:8321,20:9700,21:11245,22:12969,23:14885,24:17008,
    25:19350,26:21928,27:24755,28:27849,29:31225,30:34900,31:38891,
    32:43216,33:47892,34:52939,
}
LEVEL_CAP = 35
TIER_BONUS = {"T1":1,"T2":2,"T3":3,"T4":4}
CEILING = {"NORMAL":"T2","ELITE":"T3","LEGENDARY":"T4"}
NEXT_CLASS = {"NORMAL":"ELITE","ELITE":"LEGENDARY"}
CLASS_THRESHOLD = {"NORMAL":20,"ELITE":40}
TIER_ORDER = ["T1","T2","T3","T4"]
GROWTH_THRESHOLD = {"T1":10,"T2":20,"T3":40}
SCOPE = {"routine":0.0,"minor":0.5,"meaningful":1.0,"major":1.25,"exceptional":1.5}
CONDITION_CATEGORIES = ("environment","time","sensory","position","simultaneous")
# item points
RANK_MAX = {"outcast": 20, "commoner": 40, "working_adult": 60, "well_off": 90, "elite": 120}


class InputError(ValueError):
    pass


def fail(msg: str):
    print(json.dumps({"tool": TOOL_VERSION, "error": msg}, ensure_ascii=False))
    raise SystemExit(2)


def round_half_up(x: float) -> int:
    if x < 0:
        raise InputError("negative values are not valid for XP rounding")
    return int(math.floor(x + 0.5))


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def roll_spec(spec: str):
    m = re.fullmatch(r"(\d+)d(\d+)", spec.strip().lower())
    if not m:
        raise InputError("dice must use NdM format, e.g. 2d10")
    n, sides = map(int, m.groups())
    if not (1 <= n <= 20):
        raise InputError("number of dice must be 1..20")
    if not (2 <= sides <= 1000):
        raise InputError("die sides must be 2..1000")
    dice = [_rng.randint(1, sides) for _ in range(n)]
    return {"spec": spec, "dice": dice, "sum": sum(dice),
            "rng_source": "python.secrets.SystemRandom"}


def capmod(actor_capability: int, challenge: int) -> int:
    """Banded capability gap. Only used when a numeric Challenge applies."""
    if actor_capability < 1 or challenge < 1:
        raise InputError("capability and challenge must be >= 1")
    d = actor_capability - challenge
    if d <= -5: return -4
    if d <= -2: return -2
    if d <= 1:  return 0
    if d <= 4:  return 2
    return 4


def do_check(a):
    """Difficulty = base + execution penalties (positive = harder), 1..20."""
    for name in CONDITION_CATEGORIES:
        v = getattr(a, name)
        if v not in (-1, 0, 1, 2):
            raise InputError(f"{name} must be -1 (favourable), 0, +1 (adverse), or +2 (severely adverse)")
    if a.fit not in (-2, -1, 0, 1, 2):
        raise InputError("fit must be -2..+2")
    if a.condition not in (0, -1, -2):
        raise InputError("condition must be 0, -1, or -2")
    numeric = a.cmp is not None or a.challenge is not None
    if numeric:
        if a.cmp is None or a.challenge is None:
            raise InputError("a numeric check needs both --cmp and --challenge")
        if a.capmod is not None:
            raise InputError("pass either --cmp/--challenge or --capmod, not both")
        if a.base is not None and a.base != 10:
            raise InputError("with a numeric Challenge the base is always 10 — "
                             "task power belongs to the Challenge, not the base")
        a.base = 10
        cm = capmod(a.cmp, a.challenge)
        mode = "numeric_challenge"
    else:
        if a.capmod is None:
            raise InputError("pass --cmp/--challenge, or --capmod for an absolute capability grade")
        if a.capmod not in (-4, -2, 0, 2, 4):
            raise InputError("capmod must be one of -4,-2,0,+2,+4")
        if a.base is None:
            raise InputError("without a numeric Challenge, --base is required: "
                             "the task's own difficulty on the 1-20 scale")
        cm = a.capmod
        mode = "absolute_capability"
    if not 1 <= a.base <= 20:
        raise InputError("base difficulty must be 1..20")

    tool = clamp(a.fit + a.condition, -2, 2)
    penalties = {n: getattr(a, n) for n in CONDITION_CATEGORIES if getattr(a, n) != 0}
    penalty_total = clamp(sum(penalties.values()), -3, 3)   # the rules bounded
    difficulty = clamp(a.base + penalty_total, 1, 20)

    r = roll_spec("2d10")
    total = r["sum"] + cm + tool
    return {"tool": TOOL_VERSION, "mode": mode, "dice": r["dice"],
            "capability_modifier": cm, "tool_modifier": tool,
            "base_difficulty": a.base, "execution_penalties": penalties,
            "penalty_total": penalty_total,
            "difficulty": difficulty, "total": total,
            "success": total >= difficulty, "rng_source": r["rng_source"]}


def _level_carry(level: int, xp: int):
    ups = []
    while level < LEVEL_CAP and xp >= XP_REQ[level]:
        xp -= XP_REQ[level]
        level += 1
        ups.append(level)
    if level == LEVEL_CAP:
        xp = 0
    return level, xp, ups


def validate_progress(level: int, xp: int):
    if not 1 <= level <= LEVEL_CAP:
        raise InputError(f"level must be 1..{LEVEL_CAP}")
    if xp < 0:
        raise InputError("xp must be >= 0")
    if level == LEVEL_CAP and xp != 0:
        raise InputError(f"at level {LEVEL_CAP} canonical xp is 0")


def do_xp(a):
    """derive: award from R, P, scope. apply: a decided amount, e.g. one summed award
    for several enemies in one encounter, each vs the level at its start."""
    validate_progress(a.level, a.xp)
    level, xp = a.level, a.xp

    if a.amount is not None:
        if a.r is not None or a.scope is not None:
            raise InputError("use either --amount or --r/--p/--scope, not both")
        if a.amount < 0:
            raise InputError("amount must be >= 0")
        award = a.amount
        detail = {"mode": "apply"}
    else:
        if a.r is None or a.p is None or a.scope is None:
            raise InputError("deriving an award needs --r, --p and --scope")
        if a.r < 1:
            raise InputError("challenge R must be >= 1")
        if a.p != a.level:
            raise InputError("P must equal the participant's current overall level")
        gap = a.r - a.p
        learn = 0.0 if gap <= -5 else 0.5 if gap <= -3 else 0.75 if gap <= -1 else 1.0
        relevant = round_half_up((20 + 6 * a.r) * learn)
        award = round_half_up(relevant * SCOPE[a.scope])
        detail = {"mode": "derive", "challenge_r": a.r, "participant_p": a.p,
                  "scope": a.scope, "learning_multiplier": learn,
                  "relevant_base_xp": relevant}

    if level >= LEVEL_CAP:
        return {"tool": TOOL_VERSION, **detail, "award": award,
                "new": {"level": LEVEL_CAP, "xp": 0}, "level_ups": [],
                "note": "at level cap"}

    level, xp, ups = _level_carry(level, xp + award)
    return {"tool": TOOL_VERSION, **detail, "award": award,
            "new": {"level": level, "xp": xp}, "level_ups": ups,
            "next_requirement": XP_REQ.get(level)}


def do_accrue(a):
    """Evidence earned by one qualifying roll. No tier or class change happens here
    — that is resolved at a growth boundary."""
    cls, tier = a.cls.upper(), a.tier.upper()
    if cls not in CEILING or tier not in TIER_ORDER:
        raise InputError("invalid class or tier")
    if TIER_ORDER.index(tier) > TIER_ORDER.index(CEILING[cls]):
        raise InputError("tier is above the class ceiling")
    if not 1 <= a.difficulty <= 20:
        raise InputError("difficulty must be 1..20")
    if a.personal_skill_level is not None and a.personal_skill_level < 1:
        raise InputError("personal skill level must be >= 1")
    if a.challenge is not None and a.challenge < 1:
        raise InputError("challenge must be >= 1")

    numeric_gain = 0
    if (a.challenge is not None and a.personal_skill_level is not None
            and a.challenge >= a.personal_skill_level - 2):
        gap = a.challenge - a.personal_skill_level
        numeric_gain = 1 if gap <= 1 else 2 if gap <= 4 else 3
    condition_gain = 2 if a.difficulty >= 19 else 1 if a.difficulty >= 15 else 0
    gain = max(numeric_gain, condition_gain) if a.success else 0
    at_ceiling = tier == CEILING[cls]
    return {"tool": TOOL_VERSION, "evidence_gain": gain,
            "numeric_gain": numeric_gain, "condition_gain": condition_gain,
            "at_ceiling": at_ceiling, "add_to": "evidence",
            "note": "resolve tiers and class at a growth boundary, not now"}


def do_boundary(a):
    """Resolve accumulated evidence at a growth boundary: tier raises, and a class
    raise when the threshold is met and a class source was materially involved."""
    cls, tier = a.cls.upper(), a.tier.upper()
    if cls not in CEILING or tier not in TIER_ORDER:
        raise InputError("invalid class or tier")
    if TIER_ORDER.index(tier) > TIER_ORDER.index(CEILING[cls]):
        raise InputError("tier is above the class ceiling")
    if a.evidence < 0:
        raise InputError("evidence must be >= 0")

    ev, raised = a.evidence, []
    while tier != CEILING[cls] and ev >= GROWTH_THRESHOLD[tier]:
        ev -= GROWTH_THRESHOLD[tier]
        tier = TIER_ORDER[TIER_ORDER.index(tier) + 1]
        raised.append(tier)

    out = {"tool": TOOL_VERSION, "raised": raised,
           "new": {"class": cls, "tier": tier, "evidence": ev}}
    threshold = CLASS_THRESHOLD.get(cls)
    if tier == CEILING[cls]:
        if threshold is None:
            out["note"] = "LEGENDARY T4 is the top of the scale"
        elif ev >= threshold and a.class_source:
            out["new"]["class"] = NEXT_CLASS[cls]
            out["new"]["evidence"] = 0
            out["class_raised"] = NEXT_CLASS[cls]
            out["note"] = "class raised; the next tier is open and must be earned normally"
        elif ev >= threshold:
            out["class_threshold"] = threshold
            out["note"] = "class threshold met, waiting on a class source"
        else:
            out["class_threshold"] = threshold
            out["note"] = "accumulating toward the class threshold"
    return out


ASK_ANSWERS = ((16, "YES, AND"), (12, "YES"), (7, "NO, BUT"), (-99, "NO, AND"))


def do_ask(a):
    """Open question: 2d10 + likelihood. The GM decides the question, whether the
    record settles it, and each likelihood point; this only rolls and answers."""
    if not -3 <= a.likelihood <= 3:
        raise InputError("likelihood is clamped to -3..+3")
    for col, txt in (("for", a.for_), ("against", a.against)):
        if txt and txt.strip().lower() != "none" and len([x for x in txt.split(";") if x.strip()]) > 2:
            raise InputError(f"at most two facts per column; '{col}' has more — separate facts with ';'")
    r = roll_spec("2d10")
    total = r["sum"] + a.likelihood
    answer = next(name for floor, name in ASK_ANSWERS if total >= floor)
    return {"tool": TOOL_VERSION, "dice": r["dice"], "likelihood": a.likelihood,
            "total": total, "answer": answer}


def do_points(a):
    """Item points: spend or refill one pool. The GM decides the cost
    and whether a spend is valid; this does the arithmetic."""
    if a.rank is not None:
        if a.rank not in RANK_MAX:
            raise InputError(f"rank must be one of {', '.join(RANK_MAX)}")
        mx = RANK_MAX[a.rank]
        if a.max is not None and a.max != mx:
            raise InputError(f"rank {a.rank} sets max {mx}; pass one of --rank or --max")
    elif a.max is not None:
        mx = a.max
    else:
        raise InputError("pass --rank or --max")
    if mx < 0:
        raise InputError("max must be >= 0")
    cur = mx if a.current is None else a.current
    if not 0 <= cur <= mx:
        raise InputError("current must be 0..max")
    if (a.spend is None) == (not a.refill):
        raise InputError("pass exactly one of --spend N or --refill")
    if a.refill:
        gain = min(mx // 5, mx - cur)
        new, line = cur + gain, f"Item points {cur} +{gain} (good rest, max {mx}) → {cur + gain}"
        out = {"tool": TOOL_VERSION, "refill": gain, "current": new, "max": mx}
    else:
        if a.spend < 0:
            raise InputError("spend must be >= 0")
        if a.spend > cur:
            line = f"Item points {cur} − {a.spend} — not enough; spend fails, costs 0"
            out = {"tool": TOOL_VERSION, "spent": 0, "current": cur, "max": mx,
                   "note": "not enough points: the spend fails and commits nothing"}
            return line if a.brief else out
        new = cur - a.spend
        label = f" ({a.label})" if a.label else ""
        line = f"Item points {cur} − {a.spend}{label} → {new}"
        out = {"tool": TOOL_VERSION, "spent": a.spend, "current": new, "max": mx}
    return line if a.brief else out


def _capsule_yaml(recs, retired, save_round, supersedes, delta_of=None):
    """Capsule as YAML header + one line per record: `id :: content`, plain text."""
    rows = []
    for rid, text in recs:
        text = text.replace("\r", " ").replace("\n", " ")
        rows.append(f"    {rid} :: {text}")
    header = ["capsule:"]
    if save_round is not None:
        header.append(f"  save_round: {save_round}")
    if delta_of:
        header.append(f"  delta_of: {delta_of}   # records equal to this BACKGROUND are not repeated")
    if supersedes is not None:
        header.append(f"  supersedes_deltas_through: {supersedes}")
    header.append("  records:")
    text = "\n".join(header) + "\n" + "\n".join(rows) + "\n"
    if retired:
        text += "  retired:\n" + "".join(
            f"    {rid} :: {why.replace(chr(10), ' ')}\n" for rid, why in retired)
    return text


def _read_entry(entry):
    """One record's or GM-Δ entry's text; an empty one is degraded."""
    if entry is None or not str(entry).strip():
        return {"ok": False, "error": "empty record — mark this id degraded"}
    return {"ok": True, "text": entry}


_OP = r"^\s*([+~\-−])\s+(\S+)\s+::\s+"
_DELTA_PLAIN = re.compile(_OP + r"(.+?)\s*$")
_ROUND = re.compile(r"^\s*GM-Δ\s+(\d+)")
_SECTION = re.compile(r"^\s*(records|retired):\s*$")
_CAPLINE = re.compile(r"^\s+([A-Za-z_][\w\-]*(?:\.[\w\-]+)*)\s+::\s?(.*?)\s*$")


def _scan(path: str, want_retired: bool = False):
    """Capsule records and GM-Δ entries in a save or transcript (deltas only inside a
    GM-Δ block); retired ids returned separately."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    found, retired, rnd, in_block, section = [], [], None, False, None
    for line in lines:
        if line.strip() and not line[0].isspace():
            section = None
        m = _SECTION.match(line)
        if m:
            section = m.group(1)
            continue
        if section == "retired":
            m = _CAPLINE.match(line)
            if m:
                retired.append({"id": m.group(1), "reason": m.group(2) or None})
            continue
        if section == "records":
            m = _CAPLINE.match(line)
            if m:
                found.append({"source": "capsule", "id": m.group(1), "entry": m.group(2)})
                continue
        m = _ROUND.match(line)
        if m:
            rnd, in_block = int(m.group(1)), True
            continue
        if in_block:
            m = _DELTA_PLAIN.match(line)
            if m:
                op, rid, text = m.groups()
                found.append({"source": f"delta {rnd}", "op": op.replace("−", "-"),
                              "id": rid, "entry": text})
                continue
            if line.strip() and not line.strip().startswith("```"):
                in_block = False
    return (found, retired) if want_retired else found


QUEST_STATUS = {"available", "blocked", "active", "succeeded", "partly", "failed", "abandoned"}
ENUMS = {
    "quests": {"status": QUEST_STATUS},
    "development_threads": {"status": {"active", "available", "dormant", "blocked",
                                       "completed", "abandoned"}},
    "*": {"precision": {"exact", "daypart", "degraded"},
          "tracking": {"exact", "usage_die"},
          "usage_die": {"d12", "d10", "d8", "d6", "d4", "empty"}},
}
ITEM_CONDITION = {"serviceable", "worn", "damaged", "critical"}
REQUIRED = {"npcs": ("name", "job", "belongs", "gender", "character"),
            "factions": ("name", "role")}
_BKEY = re.compile(r"^(\s*)(-\s+)?([A-Za-z_][\w\-]*)\s*:(\s|$)")


def _flow_dups(line: str):
    """Duplicate keys inside {...} flow mappings on one line."""
    dups, stack, tok, q, expect = [], [], "", None, False
    i = 0
    while i < len(line):
        ch = line[i]
        if q:
            if ch == q: q = None
            i += 1; continue
        if ch in "\"'":
            q = ch
        elif ch == "{":
            stack.append(set()); tok, expect = "", True
        elif ch == "[":
            stack.append(None); tok, expect = "", False
        elif ch in "}]":
            if stack: stack.pop()
            tok, expect = "", False
        elif ch == ",":
            tok, expect = "", bool(stack) and stack[-1] is not None
        elif ch == ":" and stack and stack[-1] is not None and expect \
                and (i + 1 == len(line) or line[i + 1] in " }"):
            k = tok.strip()
            if re.fullmatch(r"[A-Za-z_][\w\- ]*", k):
                if k in stack[-1]: dups.append(k)
                stack[-1].add(k)
            tok, expect = "", False
        else:
            tok += ch
        i += 1
    return dups


def _split_top(s: str):
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch in "{[": depth += 1
        elif ch in "}]": depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur); cur = ""
        else:
            cur += ch
    if cur.strip(): parts.append(cur)
    return [p.strip() for p in parts]


def _lint(lines):
    """lines: [(lineno, text)] of the readable part."""
    problems = {"duplicate_keys": [], "bad_values": [], "missing_identity": [],
                "conditions_without_effect": []}
    fenced = any(t.strip().startswith("```") for _, t in lines)
    inside, stack, top = not fenced, [], None
    top_seen, fence_top = set(), set()
    entries = {}            # (section, id) -> [text]
    cur_entry = None
    for idx, (n, t) in enumerate(lines):
        if t.strip().startswith("```"):
            inside, stack, top, cur_entry = (not inside), [], None, None
            fence_top = set()
            continue
        if not inside or not t.strip() or t.lstrip().startswith("#"):
            continue
        m = _BKEY.match(t)
        if m:
            ind, dash, key = len(m.group(1)), m.group(2), m.group(3)
            if dash:
                kind = ind + len(dash)
                while stack and stack[-1][0] > ind: stack.pop()
                stack.append([kind, {key}])
            else:
                while stack and stack[-1][0] > ind: stack.pop()
                if stack and stack[-1][0] == ind:
                    if key in stack[-1][1]:
                        problems["duplicate_keys"].append({"line": n, "key": key})
                    stack[-1][1].add(key)
                else:
                    stack.append([ind, {key}])
            if ind == 0 and not dash:
                if key in top_seen and key not in fence_top:
                    problems["duplicate_keys"].append({"line": n, "key": key,
                                                       "note": "section repeated"})
                top_seen.add(key); fence_top.add(key)
                top, cur_entry = key, None
            elif top in REQUIRED and ind == 2 and not dash:
                cur_entry = (top, key); entries[cur_entry] = [t]
        for k in _flow_dups(t):
            problems["duplicate_keys"].append({"line": n, "key": k})
        if cur_entry and (not m or len(m.group(1)) > 2):
            entries[cur_entry].append(t)
        for scope in (top, "*"):
            for field, allowed in ENUMS.get(scope, {}).items():
                for v in re.findall(r"(?:^|[\s{,])" + field + r":\s*([^,}\n#]+)", t):
                    v = v.strip().strip("\"'")
                    if v and v not in allowed and not v.startswith("{"):
                        problems["bad_values"].append({"line": n, "field": field, "value": v})
        if "item_id:" in t:
            for v in re.findall(r"(?:^|[\s{,])condition:\s*([^,}\n#]+)", t):
                v = v.strip()
                if v not in ITEM_CONDITION:
                    problems["bad_values"].append({"line": n, "field": "condition", "value": v})
        mi = re.match(r"^(\s*)conditions:\s*(.*)$", t)
        inline = [mm.end() - 1 for mm in re.finditer(r"conditions:\s*\[", t)]
        for start in inline:
            depth, end = 0, None
            for k in range(start, len(t)):
                if t[k] in "[{": depth += 1
                elif t[k] in "]}":
                    depth -= 1
                    if depth == 0: end = k; break
            for it in _split_top(t[start + 1:end] if end else t[start + 1:]):
                if "effect:" not in it:
                    problems["conditions_without_effect"].append({"line": n, "condition": it[:80]})
        if mi and not inline:
            ind, rest = len(mi.group(1)), mi.group(2).strip()
            items = []
            if not rest:
                j = idx + 1
                while j < len(lines):
                    tt = lines[j][1]
                    if not tt.strip(): j += 1; continue
                    lead = len(tt) - len(tt.lstrip())
                    if lead < ind or (lead == ind and not tt.lstrip().startswith("- ")): break
                    if tt.lstrip().startswith("- "): items.append(tt.strip()[2:])
                    elif items: items[-1] += " " + tt.strip()
                    j += 1
            for it in items:
                if "effect:" not in it:
                    problems["conditions_without_effect"].append({"line": n, "condition": it[:80]})
    for (sec, aid), texts in entries.items():
        body = " ".join(texts)
        miss = [f for f in REQUIRED[sec]
                if not re.search(r"(?:^|[\s{,])" + f + r":", body.split(":", 1)[1])]
        if miss:
            problems["missing_identity"].append({"id": f"{sec}.{aid}", "missing": miss})
    return problems


_HDR = re.compile(r"^\s*GM-Δ\s+(\d+)\b(.*)$")
# the rules owners held in the capsule; records under these carry fields
CAPSULE_OWNERS = {"world_state", "locations", "rights_obligations", "active_commitments",
                  "quests", "development_threads", "npcs", "factions",
                  "active_world_pressures", "locked_case_truths", "ending_conditions",
                  "continuity_status"}
FIELD_RECORD_OWNERS = {"npcs", "factions", "quests", "locations", "active_world_pressures",
                       "locked_case_truths", "rights_obligations", "development_threads"}
# held by the readable save, not the capsule
READABLE_PREFIXES = ("player", "world_state.time", "world_state.location",
                     "world_state.environment", "enabled_modules", "narrative_theme")
_CAP_INT = {k: re.compile(r"^\s*" + k + r":\s*(\d+)\s*$", re.M)
            for k in ("save_round", "supersedes_deltas_through")}


def _chain(path):
    """GM-Δ blocks in file order: [{round, entries, line}]; `none` blocks have no entries. A block ends at the first
    non-blank line that is neither an entry nor a code fence."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    blocks, cur = [], None
    for n, line in enumerate(lines, 1):
        m = _HDR.match(line)
        if m:
            cur = {"round": int(m.group(1)), "entries": [], "line": n}
            blocks.append(cur)
            continue
        if cur is None:
            continue
        s = line.strip()
        if not s or s.startswith("```"):
            continue
        m = _DELTA_PLAIN.match(line)
        if m:
            op, rid, text = m.groups()
            cur["entries"].append((op, rid, text, n)); continue
        if re.match(r"^\s*[+~\-−]\s+\S", line):
            # looks like an entry but its id is malformed (e.g. two ids): keep the block
            # going and report it, so later entries are not silently dropped
            cur["entries"].append(("?", s[:60], s, n)); continue
        cur = None
    return blocks


def _seg_key(i):
    return [(0, int(x)) if x.isdigit() else (1, x) for x in i.split(".")]


_BG_OWNERS = ("npcs", "factions", "locations", "rights_obligations", "active_commitments",
              "quests", "development_threads", "active_world_pressures",
              "locked_case_truths", "ending_conditions", "world_state")


def _bg_tree(path):
    """BACKGROUND's Round-0 records: every ```yaml block of the file merged into one tree;
    a block that starts indented continues the block before it (template layout)."""
    try:
        import yaml
    except ImportError:
        raise InputError("--background needs PyYAML (pip install pyyaml)")
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    blocks = []
    for b in re.findall(r"```ya?ml\n(.*?)```", text, re.S) or [text]:
        if blocks and b[:1] in (" ", "\t"):
            blocks[-1] += b
        else:
            blocks.append(b)
    tree = {}
    for b in blocks:
        try:
            part = yaml.safe_load(b)
        except Exception as e:
            raise InputError(f"background YAML will not parse: {e}")
        if not isinstance(part, dict):
            continue
        for k, v in part.items():
            if isinstance(tree.get(k), dict) and isinstance(v, dict):
                tree[k].update(v)
            else:
                tree[k] = v
    if "background_id" not in tree:
        raise InputError(f"{path} is not a BACKGROUND (no background_id)")
    return tree


_MISS = object()


def _bg_get(tree, rid):
    node = tree
    for part in rid.split("."):
        if isinstance(node, dict) and part in node:
            node = node[part]
        elif isinstance(node, list) and re.fullmatch(r"r0_(\d+)", part) \
                and 0 < int(part[3:]) <= len(node):
            node = node[int(part[3:]) - 1]   # list item filed as r0_NN
        else:
            return _MISS
    return node


def _norm(v):
    return re.sub(r"\s+", " ", str(v)).strip()


def _same_as_bg(tree, rid, text):
    """True if an unstamped capsule record only repeats BACKGROUND's Round-0 value."""
    if re.match(r"^R\d+:", text or ""):
        return False
    if rid.startswith(READABLE_PREFIXES) or not rid.startswith(_BG_OWNERS):
        return False
    bg = _bg_get(tree, rid)
    if bg is _MISS:
        return False
    try:
        import yaml
        val = yaml.safe_load(text) if text.strip() else None
    except Exception:
        val = _MISS
    if val is not _MISS and val == bg:
        return True
    if isinstance(bg, (dict, list)):
        try:
            return json.loads(text) == bg
        except Exception:
            return False
    return _norm(bg) == _norm(text) or (bg is None and text.strip() in ("", "null", "~"))


def do_merge(a):
    """Next capsule = base save's capsule + GM-Δ chain; behaviour: merge --help."""
    bg = _bg_tree(a.background) if a.background else None
    if a.base:
        caps, base_retired = _capsule_records(a.base)
        if not caps and bg is None:
            raise InputError(f"no capsule records in {a.base} — "
                             "use merge --background with no --base for a first capsule")
        base_text = open(a.base, encoding="utf-8").read()
        cap_at = re.search(r"^\s*capsule:\s*$", base_text, re.M)
        cap_text = base_text[cap_at.start():] if cap_at else base_text
        m = _CAP_INT["supersedes_deltas_through"].search(cap_text)
        folded = int(m.group(1)) if m else None
        if folded is None:
            m = _CAP_INT["save_round"].search(cap_text)
            folded = int(m.group(1)) if m else None
    elif bg is not None:
        caps, base_retired, folded = [], [], None
    else:
        raise InputError("merge needs --base, or --background for a campaign's first save")

    records, degraded = {}, []
    for r in caps:
        t = _text_of(r)
        if t is None:
            degraded.append({"id": r["id"], "error": "base record unreadable — restore it "
                             "from an earlier save, else mark it degraded"})
            records[r["id"]] = "degraded: unreadable in the previous save"
        else:
            records[r["id"]] = t

    # chain: order, replays, folded blocks
    kept, replays, skipped = [], [], []
    for b in _chain(a.deltas):
        if folded is not None and b["round"] <= folded:
            skipped.append(b["round"]); continue
        if kept and b["round"] <= kept[-1]["round"]:
            void = [k["round"] for k in kept if k["round"] >= b["round"]]
            kept = [k for k in kept if k["round"] < b["round"]]
            replays.append({"replayed_from": b["round"], "void_blocks": void})
        kept.append(b)
    if not kept:
        raise InputError("no GM-Δ blocks after the base save's round in " + a.deltas)
    first = (folded + 1) if folded is not None else kept[0]["round"]
    have = {b["round"] for b in kept}
    gaps = [n for n in range(first, kept[-1]["round"] + 1) if n not in have]

    added, changed, appended, retired = [], [], [], []
    if bg is not None:   # delta capsule: retirements of BACKGROUND paths must persist
        retired = [(r["id"], r["reason"] or "retired") for r in base_retired]
    readable_skipped = 0
    notes = {"whole_record_update": [], "applied_by_field": [],
             "unknown_owner": [], "retire_nothing": [], "several_in_one": []}
    for b in kept:
        stamp = f"R{b['round']}"
        for op, rid, entry, lineno in b["entries"]:
            op = op.replace("−", "-")
            where = f"R{b['round']} line {lineno}"
            if op == "?":
                degraded.append({"at": where, "entry": rid,
                                 "error": "unreadable entry (one id per entry: "
                                          "<op> <owner>.<id>.<field> :: <content>) — "
                                          "rewrite it in the deltas file, else mark degraded"})
                continue
            d = _read_entry(entry)
            if not d["ok"]:
                degraded.append({"at": where, "id": rid, "error": d["error"]}); continue
            text = d["text"]
            if any(rid == p or rid.startswith(p + ".") for p in READABLE_PREFIXES):
                readable_skipped += 1; continue
            owner = rid.split(".")[0]
            if re.search(r"\s[a-z_]+\.[\w.]+\s*::", text):
                notes["several_in_one"].append(f"{where} {rid}")
            if owner not in CAPSULE_OWNERS and owner not in notes["unknown_owner"]:
                notes["unknown_owner"].append(owner)
            deeper = [k for k in records if k.startswith(rid + ".")]
            bgv = _bg_get(bg, rid) if bg is not None else _MISS
            if op in ("~", "+", "-"):
                # a change inside a record that was written whole: split the whole
                # record into its fields first, down to this path, then apply
                parts_ = rid.split(".")
                for depth in range(2, len(parts_)):
                    anc = ".".join(parts_[:depth])
                    if anc not in records:
                        continue
                    whole_v = _record_value(records[anc])
                    if not isinstance(whole_v, dict):
                        break
                    st_ = (_STAMP.match(records[anc]) or [None, None])[1]
                    for ok, ov in whole_v.items():
                        records.setdefault(f"{anc}.{ok}", f"R{st_}: {_flow(ov)}" if st_ else _flow(ov))
                    del records[anc]
                deeper = [k for k in records if k.startswith(rid + ".")]
            fields = None
            if op in ("~", "+"):
                try:
                    import yaml
                    v = yaml.safe_load(text) if text.strip().startswith("{") else None
                    fields = v if isinstance(v, dict) and v else None
                except Exception:
                    fields = None
            existing = rid in records or bool(deeper) or isinstance(bgv, dict)
            if fields is not None and existing:
                # a whole record changed at once: apply each field as its own record
                for fk, fv in fields.items():
                    fid = f"{rid}.{fk}"
                    for k in [k for k in records if k.startswith(fid + ".")]:
                        del records[k]
                    records[fid] = f"{stamp}: {_flow(fv)}"
                    changed.append(fid)
                if rid in records and not deeper and not isinstance(bgv, dict):
                    old = _record_value(records[rid])
                    if isinstance(old, dict):   # spread the old whole record into fields too
                        for ok, ov in old.items():
                            records.setdefault(f"{rid}.{ok}", f"{stamp}: {_flow(ov)}")
                    del records[rid]
                notes["applied_by_field"].append(f"{where} {rid}")
                continue
            if bgv is not _MISS and rid not in records and op == "~" and isinstance(bgv, dict):
                # whole BACKGROUND record, not a mapping: keep its fields, add a dated note
                nk = rid + ".notes"
                records[nk] = f"{records[nk]} | {stamp}: {text}" if nk in records else f"{stamp}: {text}"
                appended.append(rid); notes["whole_record_update"].append(f"{where} {rid}")
                continue
            parts = rid.split(".")
            ancestor = next((".".join(parts[:i]) for i in range(len(parts) - 1, 0, -1)
                             if ".".join(parts[:i]) in records), None)
            if op == "+" and rid in records:
                op = "~"
            if op == "+":
                records[rid] = f"{stamp}: {text}"; added.append(rid)
            elif op == "~":
                whole = owner in FIELD_RECORD_OWNERS and rid.count(".") == 1
                if rid in records and (whole or deeper):
                    # never replace a record that holds more than this one field
                    records[rid] = f"{records[rid]} | {stamp}: {text}"; appended.append(rid)
                    notes["whole_record_update"].append(f"{where} {rid}")
                elif rid in records:
                    records[rid] = f"{stamp}: {text}"; changed.append(rid)
                else:
                    records[rid] = f"{stamp}: {text}"; added.append(rid)
            else:
                gone = [k for k in list(records) if k == rid or k.startswith(rid + ".")]
                if gone or bgv is not _MISS:
                    for k in gone:
                        del records[k]
                    retired = [r for r in retired if not r[0].startswith(rid + ".")]
                    retired.append((rid, text))
                elif ancestor:
                    records[rid] = f"{stamp}: no longer holds — {text}"; added.append(rid)
                else:
                    notes["retire_nothing"].append(f"{where} {rid}")

    out = {"tool": TOOL_VERSION, "base": a.base, "deltas": a.deltas,
           "folded_before": folded, "applied_rounds": [kept[0]["round"], kept[-1]["round"]],
           "added": len(set(added)), "changed": len(set(changed)),
           "appended_notes": len(appended), "retired": [r[0] for r in retired]}
    hints = {
        "whole_record_update": "a whole record changed by plain text: kept, with a dated note; "
                               "name the field, or give the new fields as a {mapping}",
        "applied_by_field": "a whole record changed at once: applied field by field",
        "unknown_owner": "not a record owner: file these under their real owner",
        "retire_nothing": "nothing to retire",
        "several_in_one": "one entry holds several records' facts (all filed under the first "
                          "id); write one entry per record",
    }
    w = {k: {"count": len(v), "note": hints[k], "examples": v[:3]} for k, v in notes.items() if v}
    if w:
        out["warnings"] = w
    if readable_skipped:
        out["skipped_readable"] = (f"{readable_skipped} entries name player, time, location, "
                                   "environment, modules or theme — the readable save holds "
                                   "those; not put in the capsule")
    if skipped:
        out["skipped_already_folded"] = sorted(set(skipped))
    if replays:
        out["replays"] = replays
    if gaps:
        out["gaps"] = gaps
        out["gap_note"] = ("these rounds have no GM-Δ block; mark what they committed "
                           "degraded in continuity_status")
    if degraded:
        out["degraded"] = degraded
        out["degraded_note"] = ("these entries were not applied: mark each id degraded in "
                                "continuity_status")
    dropped_bg = 0
    if bg is not None:
        for k in [k for k, t in records.items() if _same_as_bg(bg, k, t)]:
            del records[k]; dropped_bg += 1
        out["delta_of"] = bg.get("background_id")
        out["dropped_same_as_background"] = dropped_bg
    recs = sorted(records.items(), key=lambda kv: _seg_key(kv[0]))
    save_round = a.save_round if a.save_round is not None else kept[-1]["round"]
    yaml_text = _capsule_yaml(recs, retired, save_round, kept[-1]["round"],
                              bg.get("background_id") if bg is not None else None)
    out["valid"] = True
    out["records"] = len(recs)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(yaml_text)
        out["written_to"] = a.out
    else:
        out["capsule_yaml"] = yaml_text
    return out


def _capsule_split(path):
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    readable = []
    for n, t in enumerate(lines, 1):
        if re.match(r"^\s*capsule:\s*$", t):
            break
        readable.append((n, t))
    return readable


def _capsule_records(path):
    found, retired = _scan(path, want_retired=True)
    caps = [r for r in found if r["source"] == "capsule"]
    return caps, retired


def _text_of(r):
    d = _read_entry(r["entry"])
    return d.get("text") if d["ok"] else None


# ordered values: a lower rank is a loss (item condition, usage die, skill tier)
_RANK = {"serviceable": 0, "worn": -1, "damaged": -2, "critical": -3,
         "d12": 5, "d10": 4, "d8": 3, "d6": 2, "d4": 1, "empty": 0,
         "T1": 1, "T2": 2, "T3": 3, "T4": 4}
_SKIP = {"hp", "mp", "fatigue", "last_rest", "growth_period", "evidence", "nerve",
         "tension", "status", "item_points"}   # move in normal play


def _lost(a, b, path, out):
    """the rules: what the player block lost (gone, lower number, lower rank)."""
    if isinstance(a, dict):
        b = b if isinstance(b, dict) else {}
        for k, v in a.items():
            if k in _SKIP or v in (None, "", [], {}):
                continue
            if b.get(k) in (None, "", [], {}):
                out.append(f"{path}.{k} :: gone")
            else:
                _lost(v, b[k], f"{path}.{k}", out)
    elif isinstance(a, list):
        key = lambda x: str(x.get("item_id") or x.get("name") or x.get("condition")) \
            if isinstance(x, dict) else str(x)
        bk = {key(x): x for x in (b if isinstance(b, list) else [])}
        for x in a:
            if key(x) not in bk:
                out.append(f"{path}.{key(x)[:40]} :: gone")
            else:
                _lost(x, bk[key(x)], f"{path}.{key(x)[:40]}", out)
    elif a != b:
        x, y = (_RANK[a], _RANK[b]) if a in _RANK and b in _RANK else (a, b)
        try:
            if float(str(y).replace(",", "")) < float(str(x).replace(",", "")):
                out.append(f"{path} :: {a} → {b}")
        except ValueError:
            if path.endswith("money"):
                out.append(f"{path} :: {a} → {b} (check)")


def _readable_losses(prev_path, new_path):
    p = _readable_tree(prev_path).get("player")
    if not isinstance(p, dict):
        return ["not checked: no player block in the previous save"]
    out = []
    _lost(p, _readable_tree(new_path).get("player"), "player", out)
    return out


def do_validate(a):
    found, retired = _scan(a.file, want_retired=True)
    ftext = open(a.file, encoding="utf-8").read()
    dm = re.search(r"^\s*delta_of:\s*([\w\-]+)", ftext, re.M)
    if not found and not dm:
        raise InputError("no capsule records or GM-Δ entries found in the file")
    degraded = []
    for r in found:
        res = _read_entry(r["entry"])
        if not res["ok"]:
            degraded.append(r["id"])
    caps = [r for r in found if r["source"] == "capsule"]
    ids = [r["id"] for r in caps]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    ret_ids = [r["id"] for r in retired]
    no_reason = [r["id"] for r in retired if not r["reason"]]
    out = {"tool": TOOL_VERSION,
           "read": {"records": len(found), "degraded": degraded},
           "capsule": {"records": len(caps), "duplicate_ids": dup_ids,
                       "retired": ret_ids, "retired_without_reason": no_reason}}
    bad = bool(degraded or dup_ids or no_reason)

    if a.against:
        prev, _ = _capsule_records(a.against)
        if not prev:
            raise InputError(f"no capsule records in {a.against}")
        new_by = {r["id"]: r for r in caps}
        prev_by = {r["id"]: r for r in prev}
        bg = _bg_tree(a.background) if a.background else None
        def _gone(i):
            return any(i == r or i.startswith(r + ".") for r in ret_ids)
        dropped = sorted(i for i in set(prev_by) - set(new_by) if not _gone(i)
                         and (bg is None or not _same_as_bg(bg, i, _text_of(prev_by[i]) or "")))
        revived = sorted(set(ret_ids) & set(new_by))
        changed = sorted(i for i in set(prev_by) & set(new_by)
                         if _text_of(prev_by[i]) != _text_of(new_by[i]))
        shrunk = sorted(i for i in changed
                        if len(_text_of(new_by[i]) or "") < len(_text_of(prev_by[i]) or ""))
        out["survival"] = {"against": a.against, "dropped": dropped,
                           "retired_but_present": revived, "changed": changed,
                           "shrunk": shrunk,
                           "note": "every changed id needs a ~ entry; check shrunk "
                                   "ids for detail lost without one"}
        bad = bad or bool(dropped or revived)
        out["readable_losses"] = {
            "losses": _readable_losses(a.against, a.file),
            "note": "advisory: each needs its in-play cause (spent, sold, "
                    "given, healed, broken); none → GM error, restore it before delivering"}
    else:
        out["survival"] = "not checked (no --against)"

    if dm and not a.background:
        out["delta_note"] = ("delta capsule without --background: the records it leaves to the "
                             "BACKGROUND cannot be checked; pass --background")
        bad = True
    lint = _lint(_capsule_split(a.file))
    out["lint"] = {k: v for k, v in lint.items() if v}
    bad = bad or any(lint.values())
    out["valid"] = not bad
    vbg = _bg_tree(a.background) if a.background else None
    if dm and vbg is not None and vbg.get("background_id") != dm.group(1):
        out["background_mismatch"] = (f"capsule delta_of {dm.group(1)} ≠ BACKGROUND "
                                      f"{vbg.get('background_id')}: wrong BACKGROUND, cannot load")
        out["valid"] = False
    srm = _CAP_INT["save_round"].search(ftext)
    out["dues"] = _dues(a.file, caps, retired, vbg, int(srm.group(1)) if srm else None)
    return out


_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})(?:[ T](\d{1,2}):(\d{2}))?")
_CLOSED = re.compile(r"\b(closed|done|completed?|succeeded|partly|paid in full|ended|cancell?ed|void|"
                     r"expired|failed|abandoned|retired|held|nothing owed)\b", re.I)
_EVENT = re.compile(r"\b(if|when|whenever|on|once|until|unless|immediately)\b", re.I)
_WORK = re.compile(r"\b(contract|hire|job|commission|brokered|retainer|paid service|"
                   r"fee|service)\b", re.I)


_DAYN = re.compile(r"\bDay\s+([−-]?\d+)\b(?:[^\d\n;]{0,12}?(\d{1,2}):(\d{2}))?", re.I)


def _anchor(bg, path=None):
    """(ISO start date, its day_index): BACKGROUND's start, else the readable save's
    date. Lets ISO dates and relative `Day N` dues be compared on one scale."""
    import datetime as _dt
    t = (((bg or {}).get("world_state") or {}).get("time") or {})
    pairs = [(str(t.get("date") or ""), t.get("day_index"))]
    if path:
        date = dix = None
        for _, line in _capsule_split(path):
            m = re.search(r"(?:^|[\s{,])date:\s*['\"]?([^'\",}#\n]+)", line)
            if m and date is None: date = m.group(1)
            m = re.search(r"\bday_index:\s*(\d+)", line)
            if m and dix is None: dix = int(m.group(1))
        pairs.append((date or "", dix))
    for d, dix in pairs:
        m = _DATE.search(d)
        if m and dix is not None:
            y, mo, dd = (int(x) for x in m.group(1).split("-"))
            return _dt.date(y, mo, dd), int(dix)
    return None


def _points(text, anchor=None):
    """Every dated point in a text as (key, minutes); date-only = end of day.
    `Day N` keys by day_index; ISO dates key by day_index when an anchor is known, else by
    calendar date. Compare only keys of the same kind."""
    import datetime as _dt
    pts = []
    for d, h, mi in _DATE.findall(text or ""):
        y, m, dd = (int(x) for x in d.split("-"))
        key = (("d", anchor[1] + (_dt.date(y, m, dd) - anchor[0]).days) if anchor
               else ("i", y, m, dd))
        pts.append((key, int(h) * 60 + int(mi) if h else 1439))
    for n, h, mi in _DAYN.findall(text or ""):
        pts.append((("d", int(n.replace("−", "-"))), int(h) * 60 + int(mi) if h else 1439))
    return pts


def _now(path):
    """Current game time from the readable part: (label, (key, minutes)) or None.
    Keyed by day_index whenever the save records one."""
    date = mins = dix = None
    for _, t in _capsule_split(path):
        m = re.search(r"(?:^|[\s{,])date:\s*['\"]?([^'\",}#\n]+)", t)
        if m and date is None: date = m.group(1).strip()
        m = re.search(r"\bclock_minutes:\s*(\d+)", t)
        if m and mins is None: mins = int(m.group(1))
        m = re.search(r"\bday_index:\s*(\d+)", t)
        if m and dix is None: dix = int(m.group(1))
    mins = mins if mins is not None else 0
    if dix is not None:
        return f"{date or 'day ' + str(dix)}", (("d", dix), mins)
    if date and _DATE.search(date):
        return date, (_points(date)[0][0], mins)
    return None


def _flow(v):
    if isinstance(v, (dict, list)):
        import yaml
        return yaml.safe_dump(v, default_flow_style=True, width=10 ** 9,
                              allow_unicode=True).strip()
    return "" if v is None else str(v)


_AUDIT_OWNERS = ("quests", "rights_obligations")


def _world(caps, retired, bg):
    """Current records for the dues check: BACKGROUND under the capsule, minus retired.
    A capsule record replaces BACKGROUND at its path and everything below it."""
    cur = {}
    if bg is not None:
        for owner in ("npcs", "factions"):
            for k, v in (bg.get(owner) or {}).items():
                cur[f"{owner}.{k}"] = _flow(v)
                st = (v or {}).get("state") if isinstance(v, dict) else None
                if isinstance(st, dict):
                    for f in ("due", "plan", "status"):
                        if f in st:
                            cur[f"{owner}.{k}.state.{f}"] = _flow(st[f])
        for k, v in (bg.get("active_world_pressures") or {}).items():
            cur[f"active_world_pressures.{k}"] = _flow(v)
            ck = (v or {}).get("clock") if isinstance(v, dict) else None
            if isinstance(ck, dict):
                cur[f"active_world_pressures.{k}.clock"] = _flow(ck)
                if "due" in ck:
                    cur[f"active_world_pressures.{k}.clock.due"] = _flow(ck["due"])
            tr = (v or {}).get("track") if isinstance(v, dict) else None
            if isinstance(tr, dict):
                for z, t in tr.items():
                    cur[f"active_world_pressures.{k}.track.{z}"] = _flow(t)
                    if isinstance(t, dict) and "due" in t:
                        cur[f"active_world_pressures.{k}.track.{z}.due"] = _flow(t["due"])
        for k, v in (((bg.get("world_state") or {}).get("pending")) or {}).items():
            cur[f"world_state.pending.{k}"] = _flow(v)
            if isinstance(v, dict) and "due" in v:
                cur[f"world_state.pending.{k}.due"] = _flow(v["due"])
        for owner in _AUDIT_OWNERS + ("locked_case_truths",):
            for k, v in (bg.get(owner) or {}).items():
                cur[f"{owner}.{k}"] = _flow(v)
                st = (v or {}).get("state") if isinstance(v, dict) else None
                if isinstance(st, dict) and "status" in st:
                    cur[f"{owner}.{k}.state.status"] = _flow(st["status"])
                if isinstance(v, dict) and "status" in v:
                    cur[f"{owner}.{k}.status"] = _flow(v["status"])
    bg_keys = set(cur)
    for r in sorted(caps, key=lambda r: r["id"].count(".")):
        p = r["id"]
        for k in [k for k in cur if k in bg_keys and k.startswith(p + ".")]:
            del cur[k]; bg_keys.discard(k)
        cur[p] = _text_of(r) or ""
        bg_keys.discard(p)
    gone = [r["id"] for r in retired]
    return {i: t for i, t in cur.items()
            if not any(i == g or i.startswith(g + ".") for g in gone)}


def _last_round(caps, base):
    """Latest round any capsule record at or under `base` was written; 0 = Round 0."""
    n = 0
    for r in caps:
        if r["id"] == base or r["id"].startswith(base + "."):
            m = re.match(r"^R(\d+):", _text_of(r) or "")
            if m:
                n = max(n, int(m.group(1)))
    return n


def _dues(path, caps, retired=(), bg=None, save_round=None):
    """Advisory lists for the rules; never changes validity."""
    anc = _anchor(bg, path)
    cur = _world(caps, retired, bg)
    for i, t in list(cur.items()):   # a due written inside a whole actor record
        if re.fullmatch(r"(npcs|factions)\.[\w\-]+", i) and f"{i}.state.due" not in cur:
            m = re.search(r"\bdue:\s*([^,}]+)", t)
            if m:
                cur[f"{i}.state.due"] = m.group(1).strip()
    now = _now(path)
    nowk = now[1] if now else None
    same = lambda pts: [p for p in pts if nowk and p[0][0] == nowk[0][0]]
    overdue, unregistered, unclosed, no_quest, pressure_no_due, no_plan = [], [], [], [], [], []
    unread, incidental, aim_open = [], [], []
    for rid, txt in cur.items():
        body = re.sub(r"^R\d+:\s*", "", txt)
        if rid.endswith(".due"):
            base_ = re.sub(r"\.(state\.)?due$", "", rid)
            st_ = cur.get(f"{base_}.state.status") or cur.get(f"{base_}.status") or ""
            if not st_:
                m_ = re.search(r"\bstatus:\s*([^,}]+)", cur.get(base_, ""))
                st_ = m_.group(1) if m_ else ""
            if _CLOSED.search(re.sub(r"^R\d+:\s*", "", st_)):
                continue   # closed or paid: its due is spent
            pts = _points(body, anc)
            if not pts:
                if not _EVENT.search(body) and not re.search(r"\b(none|routine|incidental)\b",
                                                              body, re.I):
                    unregistered.append(f"{rid} :: {body[:90]}")
            elif nowk and not same(pts):
                unread.append(f"{rid} :: {body[:90]}")
            elif nowk and min(same(pts)) < nowk:
                overdue.append(f"{rid} :: {body[:90]}")
    pressures = {i.split(".")[1] for i in cur if i.startswith("active_world_pressures.")}
    for k in sorted(pressures):
        p = f"active_world_pressures.{k}"
        has_clock = f"{p}.clock" in cur or any(i.startswith(p + ".clock.") for i in cur) \
            or "clock:" in cur.get(p, "")
        if has_clock and f"{p}.clock.due" not in cur and "due:" not in cur.get(f"{p}.clock", "") \
                and "due:" not in cur.get(p, ""):
            pressure_no_due.append(f"{p}.clock")
        zones = {i.split(".")[3] for i in cur
                 if i.startswith(p + ".track.") and len(i.split(".")) >= 4}
        for z in sorted(zones):
            t = f"{p}.track.{z}"
            if f"{t}.due" not in cur and "due:" not in cur.get(t, ""):
                pressure_no_due.append(t)
    refs = " ".join(t for i, t in cur.items()
                    if i.startswith(("quests.", "active_world_pressures.", "locked_case_truths.",
                                     "rights_obligations.")))
    for owner in ("npcs", "factions"):
        actors = {i.split(".")[1] for i in cur if i.startswith(owner + ".")}
        for k in sorted(actors):
            base = f"{owner}.{k}"
            due = cur.get(f"{base}.state.due")
            if due is None:
                if owner == "npcs" or f"{base}.state.plan" in cur or re.search(r"\bplan\b",
                                                                                cur.get(base, "")):
                    no_plan.append(base)
            if owner == "npcs":   # the rules: row own needs its own due and a split
                aim = " ".join(t for i, t in cur.items() if i.startswith(f"{base}.state.aim"))
                for whole in (cur.get(base, ""), cur.get(f"{base}.state", "")):
                    m = re.search(r"\baim['\"]?:\s*\{[^}]*\}", whole)
                    if m:
                        aim += " " + m.group(0)
                if re.search(r"\brow['\"]?:\s*['\"]?own\b", aim) or f"{base}.state.aim.row" in cur \
                        and re.search(r"\bown\b", cur[f"{base}.state.aim.row"]):
                    split = re.search(r"\bsplit['\"]?:\s*['\"]?([^,}'\"]+)", aim)
                    split = split.group(1).strip() if split else cur.get(f"{base}.state.aim.split", "")
                    split = re.sub(r"^R\d+:\s*", "", split).strip()
                    if due is None or re.search(r"\b(none|incidental)\b", due) or not split \
                            or re.fullmatch(r"(none|null|~)?", split, re.I):
                        aim_open.append(f"{base} :: aim row own, missing "
                                        + ("due" if due is None or re.search(r"\b(none|incidental)\b", due)
                                           else "split"))
            if due is not None and re.search(r"\bincidental\b", due):
                nm = re.search(r"\bname:\s*([^,}]+)", cur.get(base, ""))
                names = [k] + ([nm.group(1).strip()] if nm else [])
                if any(re.search(r"\b" + re.escape(n) + r"\b", refs) for n in names if n):
                    incidental.append(base)
    quest_text = " ".join(t for i, t in cur.items() if i.startswith("quests."))
    bases = sorted({".".join(i.split(".")[:2]) for i in cur if i.startswith("rights_obligations.")})
    for b in bases:
        whole = cur.get(b, "")
        status = cur.get(f"{b}.state.status")
        if status is None:
            m = re.search(r"status:\s*([^,}]+)", whole)
            status = m.group(1) if m else ""
        if _CLOSED.search(status):
            continue
        name = b.split(".", 1)[1]
        txt = whole + " " + " ".join(t for i, t in cur.items() if i.startswith(b + "."))
        pts = same(_points(txt, anc))
        dated = re.search(r"type:\s*[^,}]*(appointment|promise|hire|contract|commission|"
                          r"brokered|service|meeting|delivery)", whole, re.I)
        if dated and nowk and pts and max(pts) < nowk:
            unclosed.append(f"{b} :: all dates past, status '{status.strip()[:40]}'")
        codes = set(re.findall(r"\bcode['\"]?:\s*['\"]?([A-Z]{1,2}(?:-[A-Z]{1,2})*(?:-\d+)?)", quest_text))
        qids = {i.split(".")[1] for i in cur if i.startswith("quests.")}
        linked = (name in quest_text or any(re.search(r"\b" + re.escape(q) + r"\b", txt) for q in qids)
                  or any(re.search(r"\bquest['\"]?:\s*['\"]?" + re.escape(c) + r"\b", txt) for c in codes))
        if _WORK.search(whole[:160]) and not linked:
            no_quest.append(b)
    out = {"now": (f"{now[0]} {now[1][1] // 60:02d}:{now[1][1] % 60:02d}" if now else
                   "unread: the save records no day_index or ISO date"),
           "overdue": overdue, "unregistered_trigger": unregistered,
           "unread_date": unread, "pressure_without_due": pressure_no_due,
           "actors_without_plan": no_plan, "incidental_but_referenced": incidental,
           "joined_aim_open": aim_open,
           "open_past_all_dates": unclosed, "work_without_quest": no_quest,
           "note": "advisory: fire, replan, or close each in the next "
                   "change; incidental_but_referenced: give a real plan or confirm; unread_date: "
                   "a date on another scale (ISO vs Day N with no anchor); work_without_quest lists work-type "
                   "deals no quest names — only work the player does needs one; joined_aim_open: "
                   "an ally keeping its own aim needs its own move with a due and a split "
                   "trigger"}
    if bg is None:
        out["coverage"] = "capsule only: pass --background to check unchanged BACKGROUND dues"
    if save_round and save_round % 50 == 0:
        stale = []
        def check(base, what):
            last = _last_round(caps, base)
            if save_round - last >= 20:
                stale.append(f"{base} :: {what}, unchanged since R{last}")
        for owner in _AUDIT_OWNERS:
            for k in sorted({i.split(".")[1] for i in cur if i.startswith(owner + ".")}):
                base = f"{owner}.{k}"
                st = cur.get(f"{base}.status") or cur.get(f"{base}.state.status") or ""
                if not st:
                    m = re.search(r"\bstatus:\s*([^,}]+)", cur.get(base, ""))
                    st = m.group(1) if m else ""
                if _CLOSED.search(st) or re.search(r"\b(completed|failed|abandoned)\b", st):
                    continue
                check(base, f"open {owner[:-1] if owner.endswith('s') else owner}")
        for k in sorted({i.split(".")[2] for i in cur if i.startswith("world_state.pending.")}):
            check(f"world_state.pending.{k}", "pending consequence")
        for k in sorted(pressures):
            check(f"active_world_pressures.{k}", "pressure not moved")
        for k in sorted({i.split(".")[1] for i in cur if re.match(
                r"locations\.[\w\-]+\.(surface|undercurrent)", i)}):
            for layer in ("surface", "undercurrent"):
                if any(i.startswith(f"locations.{k}.{layer}") for i in cur):
                    check(f"locations.{k}.{layer}", "zone off baseline, not moved")
        for owner in ("npcs", "factions"):
            for k in sorted({i.split(".")[1] for i in cur if i.startswith(owner + ".")}):
                due = cur.get(f"{owner}.{k}.state.due", "")
                fut = same(_points(due, anc))
                if fut and nowk and max(fut) >= nowk:
                    continue   # a dated future step is a live plan
                if due and not re.search(r"\b(incidental|dead)\b", due) and \
                        not re.search(r"\b(dead|killed|destroyed|died)\b",
                                      cur.get(f"{owner}.{k}.state.status", ""), re.I):
                    check(f"{owner}.{k}", "plan")
        out["audit"] = {"round": save_round, "stale": stale,
                        "note": "confirm, close, or replan each in the next change"}
    elif save_round:
        out["audit"] = f"next at R{(save_round // 50 + 1) * 50}"
    return out


def _live(save, deltas):
    """Capsule records now: the save's capsule (none before the first save) with every
    GM-Δ block after it applied (a replayed round voids the blocks it replaces)."""
    caps, retired, folded = [], [], None
    if save:
        caps, retired = _capsule_records(save)
        text = open(save, encoding="utf-8").read()
        at = re.search(r"^\s*capsule:\s*$", text, re.M)
        tail = text[at.start():] if at else text
        m = (_CAP_INT["supersedes_deltas_through"].search(tail)
             or _CAP_INT["save_round"].search(tail))
        folded = int(m.group(1)) if m else None
    recs = {r["id"]: _text_of(r) or "" for r in caps}
    gone = [(r["id"], r["reason"]) for r in retired]
    last = None
    if deltas:
        kept = []
        for b in _chain(deltas):
            if folded is not None and b["round"] <= folded:
                continue
            if kept and b["round"] <= kept[-1]["round"]:
                kept = [k for k in kept if k["round"] < b["round"]]
            kept.append(b)
        for b in kept:
            last = b["round"]
            for op, rid, entry, _ in b["entries"]:
                op = op.replace("−", "-")
                if op == "?" or rid.startswith(READABLE_PREFIXES):
                    continue
                d = _read_entry(entry)
                if not d["ok"]:
                    continue
                if op == "-":
                    for k in [k for k in recs if k == rid or k.startswith(rid + ".")]:
                        del recs[k]
                    gone.append((rid, d["text"]))
                else:
                    recs[rid] = f"R{b['round']}: {d['text']}"
    caps = [{"source": "capsule", "id": i, "entry": t or " "} for i, t in recs.items()]
    return caps, [{"id": i, "reason": w} for i, w in gone], last


def _num(text, key):
    m = re.search(r"\b" + key + r":\s*([−-]?\d+)", text or "")
    return int(m.group(1).replace("−", "-")) if m else None


def _zones(bg, caps):
    """locations → {name, zone, surface, undercurrent} as they stand now."""
    out = {}
    for k, v in ((bg or {}).get("locations") or {}).items():
        v = v if isinstance(v, dict) else {}
        su = v.get("surface") if isinstance(v.get("surface"), dict) else {}
        un = v.get("undercurrent") if isinstance(v.get("undercurrent"), dict) else {}
        out[k] = {"name": str(v.get("name") or k), "zone": v.get("zone"),
                  "surface": su.get("current"), "surface_baseline": su.get("baseline"),
                  "undercurrent": un.get("current"), "cover": v.get("cover"),
                  "hours": un.get("hours"), "sites": un.get("sites")}
    for r in sorted(caps, key=lambda r: r["id"].count(".")):
        parts = r["id"].split(".")
        if parts[0] != "locations" or len(parts) < 2:
            continue
        loc = out.setdefault(parts[1], {"name": parts[1], "zone": None, "surface": None,
                                        "surface_baseline": None, "undercurrent": None,
                                        "cover": None, "hours": None, "sites": None})
        t = _text_of(r) or ""
        rest = parts[2:]
        if not rest:
            m = re.search(r"\bname:\s*([^,}]+)", t)
            if m: loc["name"] = m.group(1).strip()
            m = re.search(r"\bzone:\s*([\w\-]+)", t)
            if m: loc["zone"] = m.group(1)
            for layer in ("surface", "undercurrent"):
                m = re.search(layer + r":\s*\{([^}]*)\}", t)
                if m and _num(m.group(1), "current") is not None:
                    loc[layer] = _num(m.group(1), "current")
                if layer == "surface" and m and _num(m.group(1), "baseline") is not None:
                    loc["surface_baseline"] = _num(m.group(1), "baseline")
        elif rest[0] in ("surface", "undercurrent"):
            v = _num(t, "current") if len(rest) == 1 else (
                _num("current: " + re.sub(r"^R\d+:\s*", "", t), "current")
                if rest[1:] == ["current"] else None)
            if v is not None:
                loc[rest[0]] = v
            if rest == ["surface", "baseline"] or (rest == ["surface"] and _num(t, "baseline") is not None):
                b = _num(t, "baseline") if len(rest) == 1 else \
                    _num("baseline: " + re.sub(r"^R\d+:\s*", "", t), "baseline")
                if b is not None:
                    loc["surface_baseline"] = b
        elif rest == ["cover"]:
            loc["cover"] = re.sub(r"^R\d+:\s*", "", t).strip() or None
        elif rest == ["zone"]:
            loc["zone"] = re.sub(r"^R\d+:\s*", "", t).strip()
    return out


_PLACE_WORDS = {"office", "house", "street", "rooms", "station", "north", "south", "east",
                "west", "building", "store", "market", "village", "district", "quarter",
                "night", "nights", "their", "there", "where", "under", "above", "behind"}


def _where(text, zones):
    """The location a position's text names: a recorded location's whole id or name
    (the longest wins); none → None. A position that names no recorded place is a
    place to develop and record (GM §7.5), never a guess from one shared word."""
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[_\-,.'’]", " ", str(s).lower())).strip()
    low = f" {norm(text or '')} "
    best, score = None, 0
    for k, z in zones.items():
        for whole in (norm(k), norm(re.sub(r"\s*\(.*?\)", "", str(z["name"]))),
                      norm(re.sub(r"^the\s+", "", str(z["name"]), flags=re.I))):
            if len(whole) > 3 and f" {whole} " in low and len(whole) > score:
                best, score = k, len(whole)
    return best


_STAMP = re.compile(r"^R(\d+):\s*")


def _set_path(tree, rid, value):
    """Put value at a dotted path, creating maps; a scalar in the way moves under _value."""
    parts = rid.split(".")
    node = tree
    for part in parts[:-1]:
        if isinstance(node, list) and re.fullmatch(r"r0_(\d+)", part) \
                and 0 < int(part[3:]) <= len(node):
            node = node[int(part[3:]) - 1]
            continue
        if not isinstance(node, dict):
            return False
        nxt = node.get(part)
        if not isinstance(nxt, (dict, list)):
            node[part] = {} if nxt is None else {"_value": nxt}
        node = node[part]
    if isinstance(node, list) and re.fullmatch(r"r0_(\d+)", parts[-1]) \
            and 0 < int(parts[-1][3:]) <= len(node):
        node[int(parts[-1][3:]) - 1] = value
        return True
    if isinstance(node, list):   # a list item added by id (e.g. credit.hind_leg)
        if value not in node:
            node.append(value)
        return True
    if not isinstance(node, dict):
        return False
    old = node.get(parts[-1])
    if isinstance(old, dict) and isinstance(value, dict):
        old.update(value)
    elif isinstance(old, dict) and not isinstance(value, dict):
        old["_value"] = value
    else:
        node[parts[-1]] = value
    return True


def _del_path(tree, rid):
    parts = rid.split(".")
    node = tree
    for part in parts[:-1]:
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    if isinstance(node, dict) and parts[-1] in node:
        del node[parts[-1]]
        return True
    return False


def _record_value(text):
    """A capsule record's content: a lone stamp is dropped and the rest parsed as YAML
    where it is a mapping or list; dated notes (`a | R12: b`) stay one string."""
    body = text or ""
    m = _STAMP.match(body)
    if m and " | R" not in body:
        body = body[m.end():]
        if body.lstrip().startswith(("{", "[")):
            try:
                import yaml
                v = yaml.safe_load(body)
                if isinstance(v, (dict, list)):
                    return v
            except Exception:
                pass
        return f"R{m.group(1)}: {body}"
    return body


def _readable_tree(path):
    """The readable save as a tree: every ```yaml block before the capsule, else the
    whole readable part; a part that will not parse is kept raw."""
    import yaml
    text = "\n".join(t for _, t in _capsule_split(path))
    blocks = re.findall(r"```ya?ml\n(.*?)```", text, re.S) or [text]
    tree, raw = {}, []
    for b in blocks:
        try:
            v = yaml.safe_load(b)
        except Exception:
            raw.append(b)
            continue
        if isinstance(v, dict):
            tree.update(v)
    if raw:
        tree["readable_unparsed"] = "\n".join(raw)
    return tree


SURFACE_NAMES = {3: "Sanctuary", 2: "Secure", 1: "Calm", 0: "Ordinary", -1: "Uneasy",
                 -2: "Unstable", -3: "Collapsed"}
NERVE_NAMES = {3: "unshakeable", 2: "hardened", 1: "steady", 0: "ordinary", -1: "shaken",
               -2: "fraying", -3: "broken"}
# surface: occurs on 1d10 >= x, hostile on 1d10 <= y, size-die modifier
SURFACE_ROLL = {2: (10, 0, 0), 1: (10, 1, 0), 0: (9, 2, 0), -1: (8, 4, 0), -2: (7, 6, 1),
                -3: (6, 10, 2)}
DEPTH_OCCURS = {-1: 9, -2: 8, -3: 7}


def _size_place(n):
    return "low" if n <= 5 else "middle" if n <= 8 else "top" if n == 9 else "top + rare"


def _roll_surface(v):
    """the rules: one daypart's roll for a zone at surface v."""
    if not -3 <= v <= 3:
        raise InputError("surface must be -3..+3")
    name = SURFACE_NAMES[v]
    if v == 3:
        return ({"layer": "surface", "surface": v, "state": name, "occurs": False,
                 "note": "Sanctuary: no roll"}, f"Surface +3 ({name}) — no roll")
    occ_at, hostile_at, size_mod = SURFACE_ROLL[v]
    o = roll_spec("1d10")["dice"][0]
    out = {"layer": "surface", "surface": v, "state": name, "occurs_die": o,
           "occurs": o >= occ_at}
    line = f"Surface {v:+d} ({name}) — 1d10 {o}" if v else f"Surface 0 ({name}) — 1d10 {o}"
    if o >= occ_at:
        k = roll_spec("1d10")["dice"][0]
        kind = "hostile" if k <= hostile_at else "ordinary"
        sz = roll_spec("1d10")["dice"][0]
        place = "low" if v == 2 else _size_place(min(10, sz + size_mod))
        out.update({"kind_die": k, "kind": kind, "size_die": sz,
                    "size_modifier": size_mod, "band_place": place})
        line += (f" → encounter · kind 1d10 {k} → {kind} · size 1d10 {sz}"
                 f"{f' {size_mod:+d}' if size_mod else ''} → {place} of band")
    else:
        line += " → nothing"
    return out, line


def _roll_depth(d):
    """the rules: one contact roll at depth d."""
    if d not in DEPTH_OCCURS:
        raise InputError("depth must be -1, -2 or -3 (none never rolls)")
    o = roll_spec("1d10")["dice"][0]
    out = {"layer": "undercurrent", "depth": d, "occurs_die": o,
           "occurs": o >= DEPTH_OCCURS[d]}
    line = f"Undercurrent {d} — 1d10 {o}"
    if o >= DEPTH_OCCURS[d]:
        r = roll_spec("1d10")["dice"][0]
        t = r + abs(d)
        res = "sign" if t <= 6 else "brush" if t <= 9 else "incident" if t <= 11 else "hostile"
        out.update({"result_die": r, "result_total": t, "result": res,
                    "horror_check": res != "sign"})
        line += f" → 1d10 {r} +{abs(d)} = {t} → {res}"
        if res != "sign":
            line += " (horror check)"
    else:
        line += " → nothing"
    return out, line


def do_encounter(a):
    """the rules: one zone's roll for one daypart. The GM picks the pool entry;
    this only rolls and reports."""
    if (a.surface is None) == (a.depth is None):
        raise InputError("pass exactly one of --surface (−3..+3) or --depth (−1..−3)")
    out, line = _roll_surface(a.surface) if a.surface is not None else _roll_depth(a.depth)
    if a.brief:
        return line
    return {"tool": TOOL_VERSION, **out}


DAYPARTS = ((0, "night"), (360, "morning"), (720, "afternoon"), (1080, "evening"))
MONTH_DAYS = 30


def _daypart_of(clock):
    return [n for start, n in DAYPARTS if clock >= start][-1]


STEP_MARKS = {1: 3, 2: 5, 3: 6}   # boundary by its outer value


def do_stability(a):
    """the rules: apply marks to one surface, undercurrent or nerve.
    The GM decides which marks an event earns (a pressure track's advance is one,
    the rules); this does the arithmetic. Marks past a boundary stay in tension.
    A zone layer steps at most once a week (--stepped, --day); nerve has no cap."""
    lo, hi = (-3, 0) if a.layer == "undercurrent" else (-3, 3)
    for name, v in (("current", a.current), ("baseline", a.baseline)):
        if not lo <= v <= hi:
            raise InputError(f"{name} must be {lo}..{hi} for {a.layer}")
    zone = a.layer != "nerve"
    if zone and a.stepped is not None and a.day is None:
        raise InputError("--stepped needs --day (today's day_index)")
    t0 = a.tension
    t = t0 + a.marks
    cur, note, moved = a.current, None, []
    week_held = zone and a.stepped is not None and a.day - a.stepped < 7
    while t != 0:
        d = 1 if t > 0 else -1
        target = cur + d
        if not lo <= target <= hi:
            note = "at the end of the scale; tension holds"
            t = d * min(abs(t), STEP_MARKS[3])
            break
        need = STEP_MARKS[max(abs(cur), abs(target))]
        if abs(t) < need:
            break
        if d > 0 and target > a.baseline and not a.lasting:
            note = ("an improving act stops at baseline; a lasting cause moves baseline "
                    "instead (pass --lasting)")
            t = need
            break
        if zone and (week_held or moved):
            note = (f"zone layer already stepped this week (day {a.stepped}); marks wait in "
                    "tension" if week_held else "one step per zone layer per week; the rest "
                    "wait in tension")
            break
        cur, t = target, t - d * need
        moved.append(d)
    step = sum(moved)
    names = SURFACE_NAMES if a.layer == "surface" else NERVE_NAMES if a.layer == "nerve" else None
    label = (lambda v: names[v]) if names else (lambda v: "none" if v == 0 else f"depth {v}")
    sg = lambda v: f"{v:+d}" if v else "0"
    out = {"tool": TOOL_VERSION, "layer": a.layer, "before": a.current,
           "after": cur, "state": label(cur), "tension": t, "stepped": bool(moved)}
    if zone and moved:
        out["record_stepped"] = a.day if a.day is not None else "today's day_index"
    if a.lasting and step > 0 and cur > a.baseline:
        out["baseline"] = cur
        out["baseline_note"] = "lasting cause: baseline moves with it"
    if note:
        out["note"] = note
    if a.layer == "nerve" and step:
        if step < 0 and cur in (-1, -2):
            out["condition_due"] = "add a lasting mind condition fitting what broke them"
        elif step < 0 and cur == -3:
            out["condition_due"] = "breakdown: a severe mind condition"
        elif step > 0 and a.current in (-1, -2, -3):
            out["condition_due"] = "the condition of the step left may go"
    if zone and moved:
        out["on_step"] = "check every pressure track on this zone and layer for an on_step at this value"
    if a.brief:
        mv = f"{sg(a.current)} → {sg(cur)} ({label(cur)})" if moved else f"{sg(cur)} ({label(cur)})"
        line = f"{a.layer.capitalize()} {mv} · tension {sg(t0)} {a.marks:+d} → {sg(t)}"
        if zone and moved:
            line += f" · record stepped: {out['record_stepped']}"
        if note:
            line += f" · {note}"
        if "condition_due" in out:
            line += f" · {out['condition_due']}"
        return line
    return out


SIZE_MULT = {"small": 0.5, "normal": 1, "large": 2, "huge": 4}


def do_vitals(a):
    """Maximums only. Whether an actor has MP at all is a Ledger decision."""
    if a.v < 1:
        raise InputError("V must be >= 1")
    if a.size not in SIZE_MULT:
        raise InputError("size must be small, normal, large or huge")
    hp = math.ceil((8 + 2 * a.v) * SIZE_MULT[a.size])
    out = {"tool": TOOL_VERSION, "v": a.v, "size": a.size, "max_hp": hp}
    if a.mp_tier is not None:
        t = a.mp_tier.upper()
        if t not in TIER_BONUS:
            raise InputError("mp tier must be T1..T4")
        out["max_mp"] = 2 * a.v + 4 * TIER_BONUS[t]
    return out


def do_harm(a):
    """Apply one or more hits. Each hit loses its damage minus soak (minimum 0)."""
    if a.max < 1 or not 0 <= a.hp <= a.max:
        raise InputError("need 0 <= hp <= max and max >= 1")
    if (a.dice is None) == (a.amount is None):
        raise InputError("pass exactly one of --dice or --amount")
    if a.soak < 0 or a.hits < 1:
        raise InputError("soak must be >= 0 and hits >= 1")
    if a.amount is not None and a.amount < 0:
        raise InputError("amount must be >= 0")
    hp, hits, lasting, state = a.hp, [], False, "standing" if a.hp > 0 else "down"
    for _ in range(a.hits):
        if a.dice is not None:
            r = roll_spec(a.dice); raw, dice = r["sum"], r["dice"]
        else:
            raw, dice = a.amount, None
        dmg = max(0, raw - a.soak)
        before = hp
        if dmg and state == "down":
            state = "dead"
        hp = max(0, hp - dmg)
        if dmg * 2 >= a.max or (before > 0 and hp == 0):
            lasting = lasting or dmg > 0
        if hp == 0 and state == "standing":
            state = "down"
        hits.append({"dice": dice, "raw": raw, "soak": a.soak, "damage": dmg})
        if state == "dead":
            break
    if a.brief:
        who = f"{a.who} " if a.who else ""
        parts = []
        for h in hits:
            roll = (f"{a.dice} ({'+'.join(map(str, h['dice']))})" if h["dice"] is not None
                    else f"{h['raw']}")
            parts.append(f"{roll} − soak {h['soak']} = {h['damage']}")
        tag = {"down": " — down", "dead": " — dead"}.get(state, "")
        line = f"Damage: {' · '.join(parts)} | {who}HP {a.hp} → {hp}{tag}"
        if lasting and state != "dead":
            line += "\nLasting condition: add one to condition.conditions as {condition, source: body, effect}"
        return line
    return {"tool": TOOL_VERSION, "hits": hits, "hp_before": a.hp,
            "hp": hp, "max_hp": a.max, "state": state, "lasting_condition": lasting}


def do_heal(a):
    if a.max < 1 or not 0 <= a.current <= a.max:
        raise InputError("need 0 <= current <= max and max >= 1")
    modes = [a.dice is not None, a.amount is not None, a.quarter, a.full]
    if sum(modes) != 1:
        raise InputError("pass exactly one of --dice, --amount, --quarter, --full")
    if a.full:
        gain, dice = a.max, None
    elif a.quarter:
        gain, dice = max(1, a.max // 4), None
    elif a.dice is not None:
        r = roll_spec(a.dice); gain, dice = r["sum"], r["dice"]
    else:
        if a.amount < 0:
            raise InputError("amount must be >= 0")
        gain, dice = a.amount, None
    new = min(a.max, a.current + gain)
    return {"tool": TOOL_VERSION, "dice": dice, "restored": new - a.current,
            "current": new, "max": a.max}


def do_cast(a):
    t = a.tier.upper()
    if t not in TIER_BONUS:
        raise InputError("tier must be T1..T4")
    if a.mp < 0:
        raise InputError("mp must be >= 0")
    cost = 3 * TIER_BONUS[t]
    if a.mp < cost:
        return {"tool": TOOL_VERSION, "cost": cost, "mp": a.mp, "cast": False,
                "note": "not enough MP — the power cannot be cast"}
    return {"tool": TOOL_VERSION, "cost": cost, "mp": a.mp - cost, "cast": True}


def do_time(a):
    if a.day < 0:
        raise InputError("day_index must be >= 0")
    if not 0 <= a.clock <= 1439:
        raise InputError("clock_minutes must be 0..1439")
    if a.add < 0:
        raise InputError("added time must be >= 0")
    total = a.clock + a.add
    return {"tool": TOOL_VERSION, "day_index": a.day + total // 1440,
            "clock_minutes": total % 1440,
            "hhmm": f"{(total % 1440)//60:02d}:{(total % 1440)%60:02d}",
            "days_rolled": total // 1440}


def _cli(argv):
    ap = argparse.ArgumentParser(prog="neo_math", description="neo_math internals")
    sp = ap.add_subparsers(dest="cmd", required=True)

    p = sp.add_parser("roll", help="roll NdM")
    p.add_argument("spec")

    p = sp.add_parser("xp", help="derive an award, or apply a known amount")
    p.add_argument("--level", type=int, required=True)
    p.add_argument("--xp", type=int, required=True)
    p.add_argument("--r", type=int, help="challenge reference")
    p.add_argument("--p", type=int, help="participant overall level")
    p.add_argument("--scope", choices=sorted(SCOPE))
    p.add_argument("--amount", type=int, help="apply an already-decided amount")

    p = sp.add_parser("boundary", help="resolve tiers and class at a growth boundary")
    p.add_argument("--cls", required=True)
    p.add_argument("--tier", required=True)
    p.add_argument("--evidence", type=int, required=True,
                   help="the skill's one evidence counter")
    p.add_argument("--class-source", action="store_true",
                   help="a valid class source was materially involved")

    p = sp.add_parser("merge", help="next capsule: previous save's capsule + GM-Δ chain",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Reads every GM-Δ block after the base save's round, in order.
  untouched records   copied verbatim
  +  new path         added (on an existing record: applied as ~, warned)
  ~  field record     replaced
  ~  whole record, or a path with deeper records
                      never replaced: a dated note is appended (warned)
  -  path             it and everything under it move to capsule.retired
  player, time, location, environment, modules, theme: skipped (readable save)
Every record written is stamped with its round (R112: ...). Where records
disagree, the later round wins; an unstamped record is older than any stamped.
A block whose round is <= an earlier block's is a replay: earlier blocks from
that round on are void. A round with no block is reported as a gap; an entry
that cannot be read is reported as degraded. Nothing is dropped silently.
--background: delta capsule. Records still equal to BACKGROUND's Round-0 value
are left out (the BACKGROUND travels with the save and supplies them); a
retired BACKGROUND path stays in capsule.retired so it never comes back.
A full capsule converts to a delta on its next merge.""")
    p.add_argument("--base", help="the previous save (its capsule is the base); omit only with "
                   "--background for a campaign's first save")
    p.add_argument("--background", help="the campaign's BACKGROUND file: the capsule keeps only "
                   "what differs from it (delta capsule, the rules)")
    p.add_argument("--deltas", required=True,
                   help="file holding this chat's GM-Δ blocks, in order")
    p.add_argument("--out", help="write the capsule YAML here")
    p.add_argument("--save-round", type=int, help="default: the last GM-Δ round")

    p = sp.add_parser("points", help="item points: spend, or refill on a good rest",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Max from --rank (outcast 20 · commoner 40 · working_adult 60 ·
well_off 90 · elite 120) or --max. --spend N takes N if current allows, else
the spend fails and costs 0. --refill adds max // 5, never above max. The GM
decides the cost and whether the spend is valid; this does the arithmetic.""")
    p.add_argument("--current", type=int, help="current points (default: full)")
    p.add_argument("--rank", help="social rank, sets max")
    p.add_argument("--max", type=int, help="max, when given directly")
    p.add_argument("--spend", type=int, help="cost to take")
    p.add_argument("--refill", action="store_true", help="a good rest: + a fifth of max")
    p.add_argument("--label", help="with --brief: what was bought")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")

    p = sp.add_parser("validate", help="read check + capsule survival + readable lint",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Every record reads; no duplicate ids; every retirement has a reason. --against:
each previous capsule id carried or retired, else invalid (silent loss); shrunk
records listed; readable_losses lists what the player block lost (advisory: each
needs its in-play cause). Readable lint: duplicate keys, enum values, actor
identity fields, lasting condition home + effect. valid: true = well-formed, no capsule id
dropped; not proof every change was recorded.""")
    p.add_argument("--file", required=True, help="the save to check")
    p.add_argument("--against", help="the previous save; every capsule id must be carried or retired")
    p.add_argument("--background", help="the BACKGROUND a delta capsule is relative to")

    p = sp.add_parser("time", help="clock and day rollover")
    p.add_argument("--day", type=int, required=True)
    p.add_argument("--clock", type=int, required=True)
    p.add_argument("--add", type=int, required=True)

    p = sp.add_parser("vitals", help="derived max HP and MP")
    p.add_argument("--v", type=int, required=True, help="overall level, or vitality value")
    p.add_argument("--size", default="normal", help="small | normal | large | huge")
    p.add_argument("--mp-tier", help="tier of the best MP-drawing skill, T1..T4")

    p = sp.add_parser("harm", help="apply damage hits to HP")
    p.add_argument("--hp", type=int, required=True)
    p.add_argument("--max", type=int, required=True)
    p.add_argument("--dice", help="damage dice per hit, e.g. 1d8")
    p.add_argument("--amount", type=int, help="fixed damage per hit")
    p.add_argument("--soak", type=int, default=0)
    p.add_argument("--hits", type=int, default=1)
    p.add_argument("--brief", action="store_true", help="print the rules damage line")
    p.add_argument("--who", help="with --brief: whose HP")

    p = sp.add_parser("heal", help="restore HP or MP up to the maximum")
    p.add_argument("--current", type=int, required=True)
    p.add_argument("--max", type=int, required=True)
    p.add_argument("--dice")
    p.add_argument("--amount", type=int)
    p.add_argument("--quarter", action="store_true")
    p.add_argument("--full", action="store_true")

    p = sp.add_parser("encounter", help="one zone's surface or undercurrent roll for a daypart",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
the rules --surface N (−3..+3): occurs, kind (hostile | ordinary), size die and
where in the challenge band it lands. --depth N (−1..−3): occurs, then sign · brush ·
incident · hostile; anything past sign brings a horror check. The GM picks the
pool entry.""")
    p.add_argument("--surface", type=int, help="zone surface, -3..+3")
    p.add_argument("--depth", type=int, help="zone undercurrent, -1..-3")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")

    p = sp.add_parser("stability", help="apply marks to a surface, undercurrent or nerve",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
the rules. Tension + marks; reaching the boundary's marks (0↔±1 3 ·
±1↔±2 5 · ±2↔±3 6) moves current one step and resets tension. Upward past
baseline needs --lasting (it then moves baseline too). Marks past a boundary stay
in tension. A zone layer steps once a week: pass --stepped (the day it last
stepped) and --day; record the day it reports. Nerve has no weekly cap.
A pressure track's advance is one mark, signed by its direction.""")
    p.add_argument("--layer", required=True, choices=("surface", "undercurrent", "nerve"))
    p.add_argument("--current", type=int, required=True)
    p.add_argument("--baseline", type=int, required=True)
    p.add_argument("--tension", type=int, default=0)
    p.add_argument("--marks", type=int, required=True, help="signed total of this event's marks")
    p.add_argument("--lasting", action="store_true", help="a lasting cause: may pass baseline")
    p.add_argument("--stepped", type=int, help="zone layer: day_index it last stepped")
    p.add_argument("--day", type=int, help="zone layer: today's day_index")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")

    p = sp.add_parser("cast", help="pay an MP-drawing power's cost")
    p.add_argument("--mp", type=int, required=True)
    p.add_argument("--tier", required=True)

    a = ap.parse_args(argv)
    if True:
        if a.cmd == "roll":
            out = {"tool": TOOL_VERSION, **roll_spec(a.spec)}
        elif a.cmd == "xp":
            out = do_xp(a)
        elif a.cmd == "boundary":
            out = do_boundary(a)
        elif a.cmd == "points":
            out = do_points(a)
        elif a.cmd == "merge":
            out = do_merge(a)
        elif a.cmd == "validate":
            out = do_validate(a)
        elif a.cmd == "time":
            out = do_time(a)
        elif a.cmd == "vitals":
            out = do_vitals(a)
        elif a.cmd == "harm":
            out = do_harm(a)
        elif a.cmd == "heal":
            out = do_heal(a)
        elif a.cmd == "encounter":
            out = do_encounter(a)
        elif a.cmd == "stability":
            out = do_stability(a)
        else:
            out = do_cast(a)
    return out



# ───────────────────────── the form layer ─────────────────────────
# One JSON form in, one JSON result out. Values the world already holds (level, tier,
# HP, gear tier) are read from the BACKGROUND, the newest save and the GM-Δ blocks
# since; the GM never types them.

import copy as _copy
import sys as _sys

FIT = {"unsuitable": -2, "poor": -1, "normal": 0, "good": 1, "exceptional": 2}
TOOL_CONDITION = {"serviceable": 0, "worn": -1, "damaged": -1, "critical": -2}
EFFECT = {"adverse": 1, "severe": 2, "favourable": -1, "favorable": -1}
GRADE = {"forgiving": 5, "easy": 8, "ordinary": 10, "awkward": 13, "demanding": 15,
         "severe": 17, "extreme": 20}
ABSOLUTE = {"deficient": -4, "basic": -2, "competent": 0, "advanced": 2, "exceptional": 4}
TIER_GRADE = {None: -2, "T1": 0, "T2": 2, "T3": 2, "T4": 4}
GEAR_BOOST = {"T1": 0, "T2": 1, "T3": 2, "T4": 4}
VITALITY = {"ordinary": 1, "seasoned": 3, "veteran": 5, "exceptional": 8, "heroic": 11,
            "legendary": 20}
SOAK = {None: 0, "none": 0, "light": 1, "heavy": 2}
COST_FORMS = ("separate them", "capture someone", "put someone in a spot",
              "trade harm for harm", "inflict harm", "take away their stuff",
              "make them buy", "activate their stuff's downside",
              "turn their move back on them", "a threat acts")
REACH = ("partial", "full", "decisive")
PC_IDS = ("pc", "player")
PART_WORDS = (("midnight", 0), ("dawn", 360), ("morning", 360), ("noon", 720),
              ("midday", 720), ("afternoon", 720), ("evening", 1080), ("dusk", 1080),
              ("night", 1260))


def _need(form, *keys):
    for k in keys:
        if form.get(k) in (None, ""):
            raise InputError(f"the form needs \"{k}\"")


def _parse_value(text):
    """A record's text as a value: a {map} or [list] is parsed, a bare number is a
    number, anything else stays the text it is."""
    t = str(text).strip()
    if re.fullmatch(r"[−-]?\d+", t):
        return int(t.replace("−", "-"))
    if t[:1] in ("{", "["):
        try:
            import yaml
            v = yaml.safe_load(t)
            return v if isinstance(v, (dict, list)) else t
        except Exception:
            return t
    return t


def _folded_round(save):
    if not save:
        return None
    text = open(save, encoding="utf-8").read()
    at = re.search(r"^\s*capsule:\s*$", text, re.M)
    tail = text[at.start():] if at else text
    m = (_CAP_INT["supersedes_deltas_through"].search(tail)
         or _CAP_INT["save_round"].search(tail))
    return int(m.group(1)) if m else None


def world_tree(background, save=None, deltas=None):
    """The world as it stands now: BACKGROUND under the capsule and the GM-Δ blocks
    since the save, retired paths removed, the readable part and player changes on top."""
    _need({"background": background}, "background")
    bg = _bg_tree(background)
    tree = json.loads(json.dumps(bg, default=str))
    caps, retired, last = _live(save, deltas)
    for r in sorted(caps, key=lambda r: (r["id"].count("."), _seg_key(r["id"]))):
        t = _text_of(r)
        if t is None:
            continue
        v = _record_value(t)
        if isinstance(v, str):
            body = v
            while _STAMP.match(body):
                body = _STAMP.sub("", body, count=1)
            v = _parse_value(body)
        _set_path(tree, r["id"], v)
    for r in retired:
        _del_path(tree, r["id"])
    if save:
        for k, v in _readable_tree(save).items():
            if k == "world_state" and isinstance(v, dict):
                tree.setdefault("world_state", {}).update(v)
            elif k not in ("round", "index"):
                tree[k] = v
    if deltas:   # player and time changes since the save live only in the GM-Δ blocks
        folded = _folded_round(save)
        kept = []
        for b in _chain(deltas):
            if folded is not None and b["round"] <= folded:
                continue
            if kept and b["round"] <= kept[-1]["round"]:
                kept = [k for k in kept if k["round"] < b["round"]]
            kept.append(b)
        for b in kept:
            for op, rid, entry, _ in b["entries"]:
                if not rid.startswith(READABLE_PREFIXES):
                    continue
                d = _read_entry(entry)
                if not d["ok"]:
                    continue
                if op.replace("−", "-") == "-":
                    _del_path(tree, rid)
                else:
                    _set_path(tree, rid, _parse_value(d["text"]))
    return tree, last


def _val(node):
    """A field that may have been wrapped as {_value: x} by a later sub-record."""
    return node.get("_value") if isinstance(node, dict) and "_value" in node else node


def _actor(tree, aid):
    if str(aid).lower() in PC_IDS:
        return "player", tree.get("player") or {}
    for owner in ("npcs", "factions"):
        rec = (tree.get(owner) or {}).get(aid)
        if isinstance(rec, dict):
            return f"{owner}.{aid}", rec
    raise InputError(f"no actor \"{aid}\" in the world (use \"pc\" for the player's character)")


def _level(tree, path, rec):
    if path == "player":
        prog = rec.get("progression") or {}
        st = prog.get("state") or {}
        if st.get("level") is not None:
            return int(st["level"]), int(st.get("xp") or 0), True
        v = _val(rec.get("vitality"))
        return VITALITY.get(str(v), 1), 0, False
    cap = rec.get("capability") or {}
    lv = _val(cap.get("overall_level"))
    if lv is None:
        raise InputError(f"{path} has no capability.overall_level — commit it before the roll")
    return int(lv), 0, True


def _skill(path, rec, skill):
    """(tier or None, class or None, evidence or None) for a skill on an actor."""
    if not skill:
        return None, None, None
    if path == "player":
        s = (rec.get("skills") or {}).get(skill)
        if isinstance(s, dict):
            return str(_val(s.get("tier"))).upper(), str(_val(s.get("class") or "NORMAL")).upper(), \
                int(_val(s.get("evidence")) or 0)
        return None, None, None
    s = ((rec.get("capability") or {}).get("skills") or {}).get(skill)
    if isinstance(s, dict):
        t = _val(s.get("tier"))
        return (str(t).upper() if t else None), str(_val(s.get("class") or "NORMAL")).upper(), \
            int(_val(s.get("evidence")) or 0)
    if isinstance(s, str) and s.upper() in TIER_BONUS:
        return s.upper(), None, None
    return None, None, None


def _capability(tree, aid, skill):
    path, rec = _actor(tree, aid)
    level, xp, numeric = _level(tree, path, rec)
    tier, cls, ev = _skill(path, rec, skill)
    return {"path": path, "rec": rec, "level": level, "xp": xp, "numeric": numeric,
            "tier": tier, "class": cls, "evidence": ev,
            "capability": level + (TIER_BONUS[tier] if tier else 0)}


def _gear_tier(rec, gear):
    if not gear:
        return None
    g = str(gear)
    if g.upper() in GEAR_BOOST:
        return g.upper()
    for it in rec.get("equipment") or []:
        if isinstance(it, dict) and g in (str(it.get("item_id")), str(it.get("name"))):
            t = str(_val(it.get("tier")) or "T1").upper()
            if t not in GEAR_BOOST:
                raise InputError(f"gear \"{g}\" has tier {t}; expected T1..T4")
            return t
        if isinstance(it, str) and g.lower() in it.lower():
            m = re.search(r"\bT[1-4]\b", it)
            return m.group(0) if m else "T1"
    raise InputError(f"no gear \"{g}\" on that actor — give its item_id, name, or a tier T1..T4")


def _hp(tree, aid):
    path, rec = _actor(tree, aid)
    level, _, _ = _level(tree, path, rec)
    size = str((rec.get("capability") or {}).get("size") or rec.get("size") or "normal")
    mx = math.ceil((8 + 2 * level) * SIZE_MULT.get(size, 1))
    if path == "player":
        cur = _val((rec.get("condition") or {}).get("hp"))
        field = "player.condition.hp"
    else:
        cur = _val((rec.get("state") or {}).get("hp"))
        field = f"{path}.state.hp"
    try:
        cur = mx if cur in (None, "") else int(cur)
    except (TypeError, ValueError):
        cur = mx
    return {"current": min(cur, mx), "max": mx, "field": field}


def _conditions(form, rec):
    """Named conditions → the five category values, one fact per category."""
    vals, basis = {c: 0 for c in CONDITION_CATEGORIES}, []
    for c in form.get("conditions") or []:
        cat, eff = str(c.get("category", "")).lower(), str(c.get("effect", "")).lower()
        if cat not in vals:
            raise InputError(f"condition category must be one of {', '.join(CONDITION_CATEGORIES)}")
        if eff not in EFFECT:
            raise InputError("condition effect must be adverse, severe or favourable")
        if not c.get("fact"):
            raise InputError(f"the {cat} condition needs its fact: the concrete state fact")
        if vals[cat]:
            raise InputError(f"{cat} is counted twice; one fact per category")
        vals[cat] = EFFECT[eff]
        basis.append(f"{cat} {EFFECT[eff]:+d}: {c['fact']}")
    have = []
    cond = (rec.get("condition") or {}).get("conditions") or (rec.get("state") or {}).get("conditions") or []
    for it in cond:
        have.append(str(it.get("condition") if isinstance(it, dict) else it).lower())
    for l in form.get("lasting") or []:
        name, cat = str(l.get("condition", "")).lower(), str(l.get("category", "")).lower()
        if cat not in vals:
            raise InputError("a lasting condition names the category it hampers: "
                             + ", ".join(CONDITION_CATEGORIES))
        if not any(name and (name in h or h in name) for h in have):
            raise InputError(f"\"{name}\" is not a lasting condition recorded on that actor")
        if vals[cat]:
            raise InputError(f"{cat} is already counted; a lasting condition counts once, "
                             "in a category nothing else uses")
        vals[cat] = 1
        basis.append(f"{cat} +1: {name} (lasting)")
    return vals, basis


def _cost_tier(danger):
    if not danger or not danger.get("what"):
        return "setback", "nothing present that can hurt"
    reaches = str(danger.get("reaches", "no")).lower() in ("yes", "true", "1")
    direct = str(danger.get("direct_result", "harm")).lower()
    if direct not in ("none", "harm", "death", "crippling", "capture"):
        raise InputError("danger.direct_result must be none, harm, death, crippling or capture")
    if not reaches or direct == "none":
        return "setback", f"{danger['what']} cannot reach them in this action"
    if direct in ("death", "crippling", "capture"):
        return "severe", f"{danger['what']}: its direct result is {direct}"
    return "loss", f"{danger['what']} can hurt and reaches them"


def _check_ns(**kw):
    base = dict(cmp=None, challenge=None, capmod=None, base=None, fit=0, condition=0,
                brief=False)
    base.update({c: 0 for c in CONDITION_CATEGORIES})
    base.update(kw)
    return argparse.Namespace(**base)


def _resolve(tree, form):
    """Everything about an action form except the dice: who, capability, difficulty."""
    _need(form, "actor", "action", "opposition")
    me = _capability(tree, form["actor"], form.get("skill"))
    opp = form["opposition"]
    if not isinstance(opp, dict) or len([k for k in ("actor", "level", "grade") if k in opp]) != 1:
        raise InputError("opposition is exactly one of {actor, domain} · {level} · {grade}")
    gear = _gear_tier(me["rec"], form.get("gear_tier"))
    boost = GEAR_BOOST[gear] if gear else 0
    vals, basis = _conditions(form, me["rec"])
    tool = form.get("tool") or {}
    fit = FIT.get(str(tool.get("fit", "normal")).lower())
    cond = TOOL_CONDITION.get(str(tool.get("condition", "serviceable")).lower())
    if fit is None or cond is None:
        raise InputError("tool.fit: unsuitable|poor|normal|good|exceptional · "
                         "tool.condition: serviceable|worn|damaged|critical")
    if boost and fit > 0:
        raise InputError("one item counts once: its tier (gear_tier) or its fit (tool.fit), "
                         "never both")
    kw = dict(fit=fit, condition=cond, **vals)
    challenge = None
    if "grade" in opp or not me["numeric"]:
        g = str(opp.get("grade", "ordinary")).lower()
        if "grade" in opp and g not in GRADE:
            raise InputError("opposition.grade: " + " | ".join(GRADE))
        if "grade" not in opp:   # no numeric progression: the opponent's power is the base
            lv = opp.get("level") if "level" in opp else \
                _capability(tree, opp["actor"], opp.get("domain") or form.get("skill"))["capability"]
            base = clamp(8 + int(lv), 1, 20)
        else:
            base = GRADE[g]
        ag = form.get("capability_grade")
        if ag is not None and str(ag).lower() not in ABSOLUTE:
            raise InputError("capability_grade: " + " | ".join(ABSOLUTE))
        cm = ABSOLUTE[str(ag).lower()] if ag is not None else TIER_GRADE.get(me["tier"], -2)
        if gear and ag is None:
            cm = min(4, cm + (2 if boost >= 2 else 0))
        kw.update(capmod=cm, base=base)
        opp_text = f"{g} task" if "grade" in opp else f"power {base}"
    else:
        if "level" in opp:
            challenge = int(opp["level"])
            opp_text = f"level {challenge}"
        else:
            o = _capability(tree, opp["actor"], opp.get("domain") or form.get("skill"))
            challenge = o["capability"]
            opp_text = f"{opp['actor']} ({challenge})"
        if challenge < 1:
            raise InputError("a challenge level must be >= 1")
        kw.update(cmp=me["capability"] + boost, challenge=challenge)
    return me, kw, challenge, basis, opp_text, gear


def _growth(me, form, challenge, difficulty, success, tree):
    """Evidence for a qualifying roll, credited once per skill per growth period."""
    skill = form.get("skill")
    if not skill or not me["tier"] or me["class"] is None or not success:
        return None
    psl = me["capability"] if me["numeric"] else None
    r = do_accrue(argparse.Namespace(cls=me["class"], tier=me["tier"], challenge=challenge,
                                     personal_skill_level=psl, difficulty=difficulty,
                                     success=True))
    if not r["evidence_gain"]:
        return {"gain": 0, "why": "not a real challenge for this skill"}
    base = "player" if me["path"] == "player" else me["path"]
    gp = (me["rec"].get("growth_period") or {})
    credited = [str(x) for x in (_val(gp.get("credited")) or [])]
    if skill in credited:
        return {"gain": 0, "why": "already credited this growth period"}
    new = (me["evidence"] or 0) + r["evidence_gain"]
    sk = f"{base}.skills.{skill}.evidence" if base == "player" else \
        f"{base}.capability.skills.{skill}.evidence"
    return {"gain": r["evidence_gain"], "evidence": new,
            "gm_delta": [f"~ {sk} :: {new}",
                         f"~ {base}.growth_period.credited :: [{', '.join(credited + [skill])}]"]}


def _apply_harm(tree, target, dice, soak, hits, who=None):
    hp = _hp(tree, target)
    r = do_harm(argparse.Namespace(hp=hp["current"], max=hp["max"], dice=dice, amount=None,
                                   soak=SOAK.get(soak if soak is None else str(soak).lower(), 0)
                                   if not isinstance(soak, int) else soak,
                                   hits=hits, brief=False, who=None))
    parts = []
    for h in r["hits"]:
        parts.append(f"{dice} ({'+'.join(map(str, h['dice']))}) − soak {h['soak']} = {h['damage']}")
    tag = {"down": " — down", "dead": " — dead"}.get(r["state"], "")
    label = target if who is None else who
    line = (f"Damage: {' · '.join(parts)} | {label + ' ' if label else ''}HP "
            f"{hp['current']} → {r['hp']}{tag}")
    out = {"line": line, "hp": r["hp"], "max": hp["max"], "state": r["state"],
           "gm_delta": [f"~ {hp['field']} :: {r['hp']}"] if r["hp"] != hp["current"] else []}
    if r["lasting_condition"] and r["state"] != "dead":
        out["lasting_due"] = (f"{label or 'the PC'}: add a lasting condition "
                              "{condition, source: body, effect}")
    return out


def do_action(form):
    tree, last = world_tree(form.get("background"), form.get("save"), form.get("deltas"))
    me, kw, challenge, basis, opp_text, gear = _resolve(tree, form)
    cost, why = _cost_tier(form.get("danger"))
    reach = str(form.get("reach", "full")).lower()
    if reach not in REACH:
        raise InputError("reach: partial | full | decisive")
    cf = form.get("cost_form")
    if cost != "setback":
        if not cf or str(cf).lower() not in COST_FORMS:
            raise InputError("cost_form must be the form the danger would normally take: "
                             + " · ".join(COST_FORMS))
    r = do_check(_check_ns(**kw))
    d1, d2 = r["dice"]
    who = "" if me["path"] == "player" else f"{form['actor']} — "
    outcome = "Success" if r["success"] else "Failure"
    stakes = f"{cost}/{reach}"
    src = f" [{(form.get('tool') or {}).get('name', 'tool')}]" if r["tool_modifier"] else ""
    b = f" [{'; '.join(basis)}]" if basis else ""
    lines = [f"{who}2d10: {d1}+{d2} | Capability: {r['capability_modifier']:+d} | "
             f"Tool: {r['tool_modifier']:+d}{src} | Total: {r['total']}",
             f"Difficulty: {r['difficulty']}{b} | Stakes: {stakes} | Outcome: {outcome}"]
    out = {"tool": TOOL_VERSION, "success": r["success"], "total": r["total"],
           "difficulty": r["difficulty"],
           "bound": {"actor": form["actor"], "skill": form.get("skill"),
                     "capability": me["capability"], "gear_tier": gear,
                     "opposition": opp_text, "conditions": basis},
           "result": (f"success — reach: {reach}" if r["success"] else
                      f"failure — cost: {cost}" + (f", as: {cf}" if cf and cost != "setback" else "")),
           "cost_basis": why, "copy": lines, "gm_delta": []}
    dmg = form.get("damage") or {}
    opp = form["opposition"]
    if r["success"] and reach in ("full", "decisive") and dmg.get("dealt") and "actor" in opp:
        h = _apply_harm(tree, opp["actor"], dmg["dealt"], dmg.get("target_soak"), 1)
        out["copy"].append(h["line"]); out["gm_delta"] += h["gm_delta"]
        if "lasting_due" in h: out["lasting_due"] = h["lasting_due"]
        out["target_state"] = h["state"]
    if not r["success"] and cost in ("loss", "severe") and dmg.get("taken") and \
            str(cf).lower() in ("inflict harm", "trade harm for harm"):
        hits = 1 if cost == "loss" else max(2, int(dmg.get("attackers", 1)))
        h = _apply_harm(tree, form["actor"], dmg["taken"], dmg.get("own_soak"), hits,
                        who="" if me["path"] == "player" else form["actor"])
        out["copy"].append(h["line"]); out["gm_delta"] += h["gm_delta"]
        if "lasting_due" in h: out["lasting_due"] = h["lasting_due"]
        out["actor_state"] = h["state"]
    g = _growth(me, form, challenge, r["difficulty"], r["success"], tree)
    if g:
        out["growth"] = {k: v for k, v in g.items() if k != "gm_delta"}
        out["gm_delta"] += g.get("gm_delta", [])
    return out


def do_help_roll(form):
    _need(form, "ask")
    src = [s for s in (form.get("sources") or []) if s]
    if len(src) > 3:
        raise InputError("at most three sources of reach, each once: the PC's own network · "
                         "a related NPC's network · an organisation with reach here")
    target = 15 - len(src) + (1 if form.get("hostile") else 0)
    r = roll_spec("2d10")
    d1, d2 = r["dice"]
    ok = r["sum"] >= target
    reach = f" [reach: {'; '.join(src)}]" if src else ""
    host = " [hostile place +1]" if form.get("hostile") else ""
    return {"tool": TOOL_VERSION, "exists": ok, "target": target,
            "copy": [f"{form['ask']} — 2d10: {d1}+{d2} = {r['sum']} vs {target}+{reach}{host} → "
                     f"{'it exists' if ok else 'no'}"],
            "note": "the answer is fixed; asking again needs a changed fact"}


def do_ask_form(form):
    _need(form, "who", "question")
    def col(name, sign):
        facts = form.get(name) or []
        if len(facts) > 2:
            raise InputError(f"at most two facts in \"{name}\"")
        pts, txt = 0, []
        for f in facts:
            p = abs(int(f.get("points", 1)))
            if p not in (1, 2) or not f.get("fact"):
                raise InputError("each fact is {fact, points: 1 or 2}")
            pts += sign * p; txt.append(f"{f['fact']} {sign * p:+d}")
        return pts, "; ".join(txt) or "none"
    f, ft = col("for", 1)
    a, at = col("against", -1)
    like = clamp(f + a, -3, 3)
    r = do_ask(argparse.Namespace(likelihood=like, for_=None, against=None, label=None,
                                  brief=False))
    d1, d2 = r["dice"]
    line = (f"{form['who']} — 2d10: {d1}+{d2} | Likelihood: {like:+d} "
            f"[for: {ft}; against: {at}] | Total: {r['total']} → {r['answer']}")
    return {"tool": TOOL_VERSION, "answer": r["answer"], "total": r["total"], "copy": [line]}


# ── combat: exchanges in a batch, pausing at turning points ──

def _fighter(tree, f, side):
    if "actor" in f:
        c = _capability(tree, f["actor"], f.get("skill"))
        hp = _hp(tree, f["actor"])
        name, cap = f["actor"], c["capability"]
        cur, mx, field = hp["current"], hp["max"], hp["field"]
    else:
        _need(f, "name", "level")
        name, cap = f["name"], int(f["level"])
        mx = math.ceil((8 + 2 * cap) * SIZE_MULT.get(str(f.get("size", "normal")), 1))
        cur, field = mx, None
    cur = int(f["hp"]) if f.get("hp") is not None else cur
    return {"name": name, "cap": cap + GEAR_BOOST.get(str(f.get("gear_tier", "")).upper(), 0),
            "hp": cur, "max": mx, "field": field, "side": side,
            "damage": f.get("damage", "1d6"), "soak": SOAK.get(str(f.get("armour", "none")).lower(), 0),
            "attacks": int(f.get("attacks", 1)), "leader": bool(f.get("leader")),
            "fit": FIT.get(str((f.get("tool") or {}).get("fit", "normal")).lower(), 0),
            "tcond": TOOL_CONDITION.get(str((f.get("tool") or {}).get("condition", "serviceable")).lower(), 0),
            "state": "standing" if cur > 0 else "down", "start_hp": cur}


def _hit(src, tgt):
    r = roll_spec(src["damage"])
    dmg = max(0, r["sum"] - tgt["soak"])
    before = tgt["hp"]
    if dmg and tgt["state"] == "down":
        tgt["state"] = "dead"
    tgt["hp"] = max(0, tgt["hp"] - dmg)
    bad = dmg * 2 >= tgt["max"]
    if tgt["hp"] == 0 and tgt["state"] == "standing":
        tgt["state"] = "down"
    line = (f"Damage: {src['damage']} ({'+'.join(map(str, r['dice']))}) − soak {tgt['soak']} = "
            f"{dmg} | {tgt['name']} HP {before} → {tgt['hp']}"
            f"{' — down' if tgt['state'] == 'down' else ' — dead' if tgt['state'] == 'dead' else ''}")
    return line, bad or (before > 0 and tgt["hp"] == 0 and dmg > 0)


def do_combat(form):
    """One roll per exchange for each fighter on the player's side; the opponents'
    attacks are the cost of a failed roll, drawn from each opponent's attack budget."""
    _need(form, "side", "opponents")
    tree, _ = world_tree(form.get("background"), form.get("save"), form.get("deltas"))
    ours = [_fighter(tree, f, "ours") for f in form["side"]]
    theirs = [_fighter(tree, f, "theirs") for f in form["opponents"]]
    vals, basis = _conditions(form, {})
    stop = form.get("stop") or {}
    def threshold(f):
        v = stop.get("hp_at_or_below")
        if v is None:
            return None
        if isinstance(v, str):
            frac = {"half": 0.5, "quarter": 0.25, "third": 1 / 3}.get(v.lower())
            if frac is None:
                raise InputError("stop.hp_at_or_below: a number, or half | third | quarter")
            return math.floor(f["max"] * frac)
        return int(v)
    max_ex = int(form.get("max_exchanges", 12))
    log, reason, ex = [], None, 0
    while reason is None and ex < max_ex:
        ex += 1
        standing = [t for t in theirs if t["state"] == "standing"]
        if not standing:
            reason = "no opponent left standing"; break
        budget = {t["name"]: t["attacks"] for t in standing}
        log.append(f"— exchange {ex} —")
        turn = []
        for i, f in enumerate([o for o in ours if o["state"] == "standing"]):
            standing = [t for t in theirs if t["state"] == "standing"]
            if not standing:
                break
            tgt = standing[i % len(standing)]
            extra = dict(vals)
            crowd = len(standing) > len([o for o in ours if o["state"] == "standing"])
            if crowd and not extra["simultaneous"]:
                extra["simultaneous"] = 1   # outnumbered: one condition, never also a cost
            r = do_check(_check_ns(cmp=f["cap"], challenge=max(1, tgt["cap"]), fit=f["fit"],
                                   condition=f["tcond"], **extra))
            d1, d2 = r["dice"]
            log.append(f"{f['name']} vs {tgt['name']} — 2d10: {d1}+{d2} | Capability: "
                       f"{r['capability_modifier']:+d} | Tool: {r['tool_modifier']:+d} | "
                       f"Total: {r['total']} | Difficulty: {r['difficulty']} | "
                       f"{'Success' if r['success'] else 'Failure'}")
            if r["success"]:
                line, bad = _hit(f, tgt)
                log.append(line)
                if tgt["state"] != "standing":
                    turn.append(f"{tgt['name']} falls")
                    if tgt["leader"]:
                        turn.append(f"their leader {tgt['name']} falls")
                elif bad:
                    turn.append(f"{tgt['name']} is badly hurt")
            else:
                src = tgt if budget.get(tgt["name"], 0) > 0 else next(
                    (t for t in standing if budget.get(t["name"], 0) > 0), None)
                if src is None:
                    log.append(f"{f['name']}: setback — no attack left to reach them")
                else:
                    budget[src["name"]] -= 1
                    line, bad = _hit(src, f)
                    log.append(line)
                    if f["state"] != "standing":
                        turn.append(f"{f['name']} goes down")
                    elif bad:
                        turn.append(f"{f['name']} is badly hurt")
            th = threshold(f)
            if th is not None and f["state"] == "standing" and f["hp"] <= th and i == 0:
                turn.append(f"{f['name']} at HP {f['hp']} — the plan's stop condition")
        if not [t for t in theirs if t["state"] == "standing"]:
            reason = "no opponent left standing"
        elif not [o for o in ours if o["state"] == "standing"]:
            reason = "nobody on the player's side is standing"
        elif turn:
            reason = "; ".join(dict.fromkeys(turn))
    if reason is None:
        reason = f"{max_ex} exchanges fought — check the world around the fight"
    delta = [f"~ {f['field']} :: {f['hp']}" for f in ours + theirs
             if f["field"] and f["hp"] != f["start_hp"]]
    state = lambda fs: [{"name": f["name"], "hp": f["hp"], "max": f["max"], "state": f["state"]}
                        for f in fs]
    over = not [t for t in theirs if t["state"] == "standing"] or \
        not [o for o in ours if o["state"] == "standing"]
    return {"tool": TOOL_VERSION, "paused": reason, "exchanges": ex, "fight_over": over,
            "copy": log, "side": state(ours), "opponents": state(theirs), "gm_delta": delta,
            "at_pause": ("settle morale for the side the fight turned against; check the world "
                         "around the fight (noise, fire, arrivals); nothing the plan doesn't "
                         "cover → send the form again with each fighter's hp as it stands"),
            "conditions": basis}


# ── time: run a span, stop at the first thing that could reach the PC ──

def _due_minutes(text, anchor):
    """Each dated point of a due as (absolute minute, segment text, assumed)."""
    out = []
    segs = [s.strip() for s in re.split(r";", text) if s.strip()] or [text]
    for seg in segs:
        for key, mins in _points(seg, anchor):
            if key[0] != "d":
                continue
            assumed = mins == 1439 and not re.search(r"23:59", seg)
            if assumed:
                low = seg.lower()
                mins = next((m for w, m in PART_WORDS if re.search(r"\b" + w + r"\b", low)), 480)
            out.append((key[1] * 1440 + mins, seg, assumed))
    return out


def _no_due(st):
    v = _val(st.get("due")) if isinstance(st, dict) else None
    body = _STAMP.sub("", str(v if v is not None else "")).strip()
    return not body or re.fullmatch(r"(none|incidental)\b.*", body, re.I) is not None


QUEST_CODE = re.compile(r"^([A-Z]{1,2}(?:-[A-Z]{1,2})*)(?:-(\d+))?([spfa])?$")
QUEST_STATE = {None: "active", "s": "succeeded", "p": "partly", "f": "failed", "a": "abandoned"}


def _clean(q, k):
    return _STAMP.sub("", str(_val(q.get(k)) or "")).strip().split(" ")[0]


def _base(m):
    return m.group(1) + (f"-{m.group(2)}" if m.group(2) else "")


def _code_of(q):
    """(code without its status letter, state word) from a quest record, or (None, raw)."""
    code, status = _clean(q, "code"), _clean(q, "status")
    word = re.sub(r"[^a-z]", "", status.lower())
    mc, ms = QUEST_CODE.match(code), QUEST_CODE.match(status)
    base = _base(mc) if mc else _base(ms) if ms else None
    if word in ("active", "succeeded", "partly", "failed", "abandoned", "available", "blocked"):
        return base, word
    for m in (ms, mc):
        if m:
            return base, QUEST_STATE[m.group(3)]
    return base, (word or "unknown")


def _quest_problems(tree):
    """Quest codes: well-formed, the last letter unique, code and status agreeing."""
    out, last = [], {}
    def look(path, q):
        if not isinstance(q, dict):
            return
        code, status = _clean(q, "code"), _clean(q, "status")
        if code:
            m = QUEST_CODE.match(code)
            if not m:
                out.append(f"{path} :: code \"{code}\" is not A, A-1, A-B or A-B-1 (+ s|p|f|a)")
            else:
                letter = m.group(1).split("-")[-1]
                if not m.group(2):
                    if letter in last and last[letter] != path:
                        out.append(f"{path} :: letter {letter} already names {last[letter]}")
                    last.setdefault(letter, path)
                ms = QUEST_CODE.match(status)
                if ms and _base(ms) != _base(m):
                    out.append(f"{path} :: status \"{status}\" does not carry its code \"{_base(m)}\"")
        elif status.lower() not in ("available", "blocked", "open", "", "none"):
            out.append(f"{path} :: taken on (status \"{status}\") but has no code")
        parts = q.get("parts")
        for pid, part in (parts.items() if isinstance(parts, dict) else []):
            look(f"{path}.parts.{pid}", part)
    for qid, q in (tree.get("quests") or {}).items():
        look(f"quests.{qid}", q)
    return out


DEPTH_NEEDS = {1: ("voice", "drives.want", "drives.fear"),
               2: ("voice", "drives.want", "drives.fear", "drives.line", "secret"),
               3: ("voice", "drives.want", "drives.fear", "drives.line", "secret",
                   "drives.pull", "knowledge.beliefs", "state.plan")}


def _depth_problems(tree):
    out = []
    for aid, rec in (tree.get("npcs") or {}).items():
        if not isinstance(rec, dict):
            continue
        try:
            d = int(_val(rec.get("depth")))
        except (TypeError, ValueError):
            continue
        miss = []
        for f in DEPTH_NEEDS.get(d, ()):
            node = rec
            for seg in f.split("."):
                node = node.get(seg) if isinstance(node, dict) else None
            if node in (None, "", {}, []):
                miss.append(f)
        if miss:
            out.append(f"npcs.{aid} :: depth {d} lacks {', '.join(miss)}")
    return out


def _important(tree):
    """Actors who must always have a due: read from the world as it stands."""
    refs = json.dumps({k: tree.get(k) for k in ("quests", "active_world_pressures",
                                                 "locked_case_truths", "rights_obligations")},
                      ensure_ascii=False, default=str).lower()
    pcname = str(((tree.get("player") or {}).get("identity") or {}).get("name") or "").lower()
    out = []
    for aid, rec in (tree.get("npcs") or {}).items():
        if not isinstance(rec, dict):
            continue
        st = rec.get("state") if isinstance(rec.get("state"), dict) else {}
        status = str(st.get("status") or "").lower()
        if re.search(r"\b(dead|killed|died|departed|gone for good)\b", status):
            continue
        rel = rec.get("relationships") or {}
        tie = any(str(k).lower() in PC_IDS + ((pcname,) if pcname else ()) for k in rel)
        named = re.search(r"\b" + re.escape(aid.lower()) + r"\b", refs) is not None
        try:
            deep = int(_val(rec.get("depth")) or 0) >= 2
        except (TypeError, ValueError):
            deep = False
        if tie or named or deep:
            out.append((aid, rec, st))
    return out


def _layers(loc, zones):
    """A location's surface and undercurrent (a building reads its zone's); no
    undercurrent recorded = none (0)."""
    z = zones.get(loc) or {}
    if z.get("zone") and z["zone"] in zones and z["zone"] != loc:
        z = zones[z["zone"]]
    if not z:
        return None, None
    return z.get("surface"), z.get("undercurrent") or 0


def _zone_point(side, surface, under):
    """RULES §9.1 ZONE: the likelihood point for an actor's uncertain act, by its
    in_disorder: open act → the surface, hidden act → the undercurrent."""
    def pt(v, open_):
        if v is None:
            return None
        k = 2 if v <= -3 else 1 if v <= -2 else 0
        if open_:
            k = -2 if v >= 3 else -1 if v >= 2 else k
        return {"thrives": k, "suffers": -k, "neither": 0}.get(side)
    return {"open": pt(surface, True), "hidden": pt(under, False)}


def do_span(form):
    _need(form, "background", "from", "minutes")
    tree, last = world_tree(form["background"], form.get("save"), form.get("deltas"))
    bg = _bg_tree(form["background"])
    anc = _anchor(bg, form.get("save"))
    day, clock = int(form["from"]["day"]), int(form["from"]["clock"])
    minutes = int(form["minutes"])
    if minutes < 0 or not 0 <= clock <= 1439:
        raise InputError("from.clock is 0..1439 and minutes >= 0")
    t0 = day * 1440 + clock
    t1 = t0 + minutes
    caps, retired, _ = _live(form.get("save"), form.get("deltas"))
    zones = _zones(bg, caps)
    pcz = form.get("pc_zone")
    if pcz and pcz not in zones:
        raise InputError(f"pc_zone \"{pcz}\" is not a recorded location")
    home = pcz
    if pcz and zones[pcz].get("zone") in zones:
        home = zones[pcz]["zone"]
    pcname = str(((tree.get("player") or {}).get("identity") or {}).get("name") or "").strip()
    aimed = re.compile(r"\b(the pc|pc|the player" + (("|" + re.escape(pcname)) if pcname and
                       "unassigned" not in pcname.lower() else "") + r")\b", re.I)

    events, triggers, flags = [], [], []
    seen = set(form.get("shown_at_start") or [])
    resumed = "shown_at_start" in form
    def add_dues(rid, text, zone_of=None, side=None):
        body = _STAMP.sub("", str(text or "")).strip()
        if not body or re.fullmatch(r"(none|incidental|routine)\b.*", body, re.I):
            return False
        pts = _due_minutes(body, anc)
        if not pts:
            if _EVENT.search(body):
                triggers.append({"id": rid, "trigger": body[:240]})
                return True
            flags.append(f"{rid} :: a due with no time and no trigger — \"{body[:60]}\"")
            return True
        for t, seg, assumed in pts:
            if t0 < t <= t1 or (t == t0 and resumed and f"{rid}|{seg[:240]}" not in seen):
                loc = zone_of
                here = bool(loc and home and (loc == home or zones.get(loc, {}).get("zone") == home
                                              or loc == pcz))
                ev = {"t": t, "kind": "due", "id": rid, "what": seg[:240],
                      "zone": loc, "candidate": here or bool(aimed.search(seg)),
                      "time_assumed": assumed}
                if side is not None:   # RULES §9.1 ZONE: the point for this actor's act
                    ev["in_disorder"] = side or "unset — set it once from role and drives"
                    if loc:
                        sv, uv = _layers(loc, zones)
                        ev["surface"], ev["undercurrent"] = sv, uv
                        if side in ("thrives", "suffers", "neither"):
                            ev["zone_point"] = _zone_point(side, sv, uv)
                events.append(ev)
        return True

    for owner in ("npcs", "factions"):
        for aid, rec in (tree.get(owner) or {}).items():
            if not isinstance(rec, dict):
                continue
            st = rec.get("state") if isinstance(rec.get("state"), dict) else {}
            pos = str(_val(st.get("position")) or "")
            loc = _where(pos, zones)
            if st.get("due") is not None and not _no_due(st):
                if pos and loc is None:
                    flags.append(f"{owner}.{aid}.state.position :: \"{pos[:60]}\" names no recorded "
                                 "location — develop the place once (GM §7.5) and record it")
                side = str(_val(rec.get("in_disorder")) or "").strip().lower()
                add_dues(f"{owner}.{aid}.state.due", _val(st.get("due")), loc, side)
    for pid, p in (tree.get("active_world_pressures") or {}).items():
        if not isinstance(p, dict):
            continue
        had = False
        ck = p.get("clock")
        if isinstance(ck, dict):
            had = add_dues(f"active_world_pressures.{pid}.clock.due", ck.get("due")) or had
        for z, tr in (p.get("track") or {}).items() if isinstance(p.get("track"), dict) else []:
            if isinstance(tr, dict):
                had = add_dues(f"active_world_pressures.{pid}.track.{z}.due", tr.get("due"), z) or had
        if not had and not re.search(r"\b(stopped|ended|resolved|retired)\b",
                                     json.dumps(p.get("state"), default=str), re.I):
            flags.append(f"active_world_pressures.{pid} :: a pressure with no due")
    for k, v in (((tree.get("world_state") or {}).get("pending")) or {}).items():
        if isinstance(v, dict) and v.get("due") is not None:
            add_dues(f"world_state.pending.{k}.due", v["due"])
    for rid, r in (tree.get("rights_obligations") or {}).items():
        if isinstance(r, dict) and str(r.get("type", "")).lower() == "owed":
            due = (r.get("state") or {}).get("due") if isinstance(r.get("state"), dict) else None
            if due is not None:
                add_dues(f"rights_obligations.{rid}.due", due)
    for qid, q in (tree.get("quests") or {}).items():
        if isinstance(q, dict) and str(_val(q.get("status"))).lower() == "blocked" and q.get("trigger"):
            triggers.append({"id": f"quests.{qid}.trigger", "trigger": str(q["trigger"])[:240]})
    for beat, bd in (tree.get("canon_course") or {}).items():
        if isinstance(bd, dict) and bd.get("opens"):
            triggers.append({"id": f"canon_course.{beat}.opens", "trigger": str(bd["opens"])[:240]})
    for aid, rec, st in _important(tree):
        if _no_due(st):
            flags.append(f"npcs.{aid} :: important and has no due — give a plan and a due")
    flags += _quest_problems(tree)

    for d in range(t0 // 1440 + 1, t1 // 1440 + 1):
        events.append({"t": d * 1440, "kind": "day", "what": f"day {d} begins: nerve day marks"})
        if d % MONTH_DAYS == 0:
            events.append({"t": d * 1440, "kind": "month",
                           "what": "30 days: monthly stability marks (drift toward baseline; "
                                   "no-cover bleed)"})
    if home:
        slots = []
        if form.get("arrived"):
            slots.append(t0)
        for d in range(t0 // 1440, t1 // 1440 + 1):
            for start, name in DAYPARTS:
                if t0 < d * 1440 + start <= t1:
                    slots.append(d * 1440 + start)
        for t in slots:
            events.append({"t": t, "kind": "encounter_slot", "zone": home})

    order = {"day": 0, "month": 1, "due": 2, "encounter_slot": 3}
    events.sort(key=lambda e: (e["t"], order[e["kind"]]))
    stamp = lambda t: f"day {t // 1440} {(t % 1440) // 60:02d}:{(t % 1440) % 60:02d}"
    shown, stop = [], None
    for e in events:
        row = {"at": stamp(e["t"]), "kind": e["kind"]}
        if e["kind"] == "encounter_slot":
            s_val = zones[home].get("surface")
            if not isinstance(s_val, int):
                row.update(kind="encounter", line=f"{zones[home]['name']}: no surface recorded — "
                           "derive and commit it, then roll")
                shown.append(row)
                continue
            o, ln = _roll_surface(s_val)
            row.update(kind="encounter", zone=home, occurs=o["occurs"],
                       line=f"{zones[home]['name']} — {ln}")
            if o["occurs"]:
                row.update(encounter_kind=o["kind"], band_place=o["band_place"],
                           pool=f"locations.{home}.encounters.{o['kind']}")
                shown.append(row); stop = e; break
            shown.append(row)
            continue
        row.update({k: e[k] for k in ("id", "what", "zone", "in_disorder", "surface",
                                      "undercurrent", "zone_point") if e.get(k) is not None})
        if e.get("time_assumed"):
            row["time_assumed"] = "the due names a day only; hour taken from its wording, else 08:00"
        shown.append(row)
        if e["kind"] == "due" and e["candidate"]:
            row["could_reach_pc"] = True
            stop = e; break
    seen_now = set()
    if stop:
        for r in shown:
            if r.get("kind") == "due" and r["at"] == stamp(stop["t"]):
                seen_now.add(f"{r['id']}|{r['what']}")
        if stop["t"] == t0:
            seen_now |= seen
    out = {"tool": TOOL_VERSION, "from": stamp(t0), "to": stamp(stop["t"] if stop else t1),
           "events": shown, "triggers_to_check": triggers, "flags": flags,
           "chain_through": last}
    if stop:
        left = t1 - stop["t"]
        out["stopped"] = True
        out["remaining_minutes"] = left
        out["judge"] = ("does this reach the PC? yes → time stops here and the scene opens "
                        "(who acts first: by awareness); no → send the form again from this "
                        "moment with the remaining minutes")
        out["resume"] = {"from": {"day": stop["t"] // 1440, "clock": stop["t"] % 1440},
                         "minutes": left, "shown_at_start": sorted(seen_now)}
    else:
        out["stopped"] = False
        out["now"] = {"day": t1 // 1440, "clock": t1 % 1440, "daypart": _daypart_of(t1 % 1440)}
    u = zones.get(home, {}).get("undercurrent") if home else None
    if u:
        out["undercurrent"] = (f"{zones[home]['name']} depth {u}, hours: "
                               f"{zones[home].get('hours') or '?'} — on contact, roll an "
                               f"encounter form with depth {u}")
    out["note"] = ("each due is a check, never a delivery: it acts if its cause still holds; "
                   "these lines stay out of the turn; only what the PC meets is narrated")
    return out


# ── the 50-round self-check ──

def do_selfcheck(form):
    _need(form, "background", "save", "answers")
    tree, _ = world_tree(form["background"], form["save"], form.get("deltas"))
    bg = _bg_tree(form["background"])
    caps, retired, _ = _live(form["save"], form.get("deltas"))
    zones = _zones(bg, caps)
    ans = form["answers"]
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()
    rows, mism = [], 0
    for aid, said in (ans.get("npc_positions") or {}).items():
        rec = (tree.get("npcs") or {}).get(aid)
        if not isinstance(rec, dict):
            rows.append({"check": f"where is {aid}", "answer": said, "record": "no such npc",
                         "match": False}); mism += 1; continue
        real = str(_val((rec.get("state") or {}).get("position")) or "unknown")
        a, b = _where(said, zones), _where(real, zones)
        ok = (a is not None and a == b) or norm(said) in norm(real) or norm(real) in norm(said)
        rows.append({"check": f"where is {aid}", "answer": said, "record": real, "match": ok})
        mism += not ok
    for q, said in (ans.get("quests") or {}).items():
        want = QUEST_CODE.match(str(q))
        qbase = _base(want) if want else None
        found = []
        def scan(qid, qd):
            if not isinstance(qd, dict):
                return
            base, state = _code_of(qd)
            if q == qid or (qbase and base == qbase):
                found.append(state)
            parts = qd.get("parts")
            for pid, part in (parts.items() if isinstance(parts, dict) else []):
                scan(pid, part)
        for qid, qd in (tree.get("quests") or {}).items():
            scan(qid, qd)
        real = found[0] if found else "no such quest"
        ok = norm(said).split()[:1] == norm(real).split()[:1]
        rows.append({"check": f"quest {q}", "answer": said, "record": real, "match": ok})
        mism += not ok
    pl = tree.get("player") or {}
    if "money" in ans:
        real = json.dumps(pl.get("money"), ensure_ascii=False, default=str)
        nums = lambda s: sorted(re.findall(r"\d[\d,]*", str(s).replace(",", "")))
        ok = nums(ans["money"]) == nums(real)
        rows.append({"check": "the PC's money", "answer": ans["money"], "record": real, "match": ok})
        mism += not ok
    if "hp" in ans:
        hp = _hp(tree, "pc")
        ok = int(ans["hp"]) == hp["current"]
        rows.append({"check": "the PC's HP", "answer": ans["hp"],
                     "record": f"{hp['current']} of {hp['max']}", "match": ok})
        mism += not ok
    if not rows:
        raise InputError("answers needs at least one of npc_positions, quests, money, hp")
    sr = form.get("round")
    own = _dues(form["save"], caps, retired, bg, int(sr) if sr else None)
    hp = _hp(tree, "pc")
    own_rows = {k: own[k] for k in ("overdue", "unregistered_trigger", "pressure_without_due",
                                    "actors_without_plan", "joined_aim_open",
                                    "open_past_all_dates") if own.get(k)}
    if isinstance(own.get("audit"), dict) and own["audit"].get("stale"):
        own_rows["unchanged_20_rounds"] = own["audit"]["stale"]
    imp = [f"npcs.{aid}" for aid, rec, st in _important(tree) if _no_due(st)]
    if imp:
        own_rows["important_without_due"] = imp
    for key, rows_ in (("quest_codes", _quest_problems(tree)),
                       ("depth_fields", _depth_problems(tree))):
        if rows_:
            own_rows[key] = rows_
    if not 0 <= hp["current"] <= hp["max"]:
        own_rows["hp_out_of_range"] = [f"{hp['current']} of {hp['max']}"]
    verdict = "pass" if mism == 0 else "fail"
    lines = [f"Self-check — {len(rows)} answers checked against the save: "
             f"{len(rows) - mism} match, {mism} differ → {verdict.upper()}"]
    lines += [f"  {'✓' if r['match'] else '✗'} {r['check']}: said \"{r['answer']}\" · "
              f"record \"{r['record']}\"" for r in rows]
    for k, v in own_rows.items():
        lines.append(f"  tool check — {k.replace('_', ' ')}: {len(v)}")
    out = {"tool": TOOL_VERSION, "verdict": verdict, "answers": rows, "tool_checks": own_rows,
           "copy": lines,
           "limits": "money is compared to the save, not re-added from a ledger; HP is checked "
                     "against its maximum, not against logged damage"}
    if verdict == "fail":
        out["next"] = "ask the player's permission to reread all files"
    return out


# ── a background on its own, before play ──

def do_check_background(form):
    """Everything the tool can check in a BACKGROUND before Round 0. It can't judge
    design: whether a secret is good, a pull is real, a route is fair."""
    _need(form, "background")
    bg = _bg_tree(form["background"])
    tree = json.loads(json.dumps(bg, default=str))
    anc = _anchor(bg, None)
    zones = _zones(bg, [])
    probs = {}
    add = lambda k, v: probs.setdefault(k, []).append(v)

    for k in ("background_id", "provenance", "setting", "setting_anchors", "content_bounds",
              "player", "world_state", "premise", "question"):
        if tree.get(k) in (None, "", {}, []):
            add("frame", f"{k} :: missing")
    if str(tree.get("provenance", "")).lower() in ("generated", "mixed") and not tree.get("requested"):
        add("frame", "requested :: a generated or mixed background lists what the person asked for")

    actors = set((tree.get("npcs") or {}).keys()) | set((tree.get("factions") or {}).keys())
    for aid, rec in (tree.get("npcs") or {}).items():
        if not isinstance(rec, dict):
            continue
        miss = [f for f in REQUIRED["npcs"] if rec.get(f) in (None, "")]
        if miss:
            add("npcs", f"npcs.{aid} :: lacks {', '.join(miss)}")
        if rec.get("depth") in (None, ""):
            add("npcs", f"npcs.{aid} :: no depth (0 passer-by · 1 regular · 2 supporting · 3 story-turning)")
        for tid in (rec.get("relationships") or {}):
            if str(tid).lower() not in PC_IDS and tid not in actors:
                add("references", f"npcs.{aid}.relationships.{tid} :: no such actor")
        st = rec.get("state") if isinstance(rec.get("state"), dict) else {}
        pos = _val(st.get("position"))
        if pos and not _where(str(pos), zones):
            add("references", f"npcs.{aid}.state.position :: \"{pos}\" names no recorded location")
        due = _STAMP.sub("", str(_val(st.get("due")) or "")).strip()
        did = f"npcs.{aid}.state.due"
        if due and not _no_due(st):
            if len(set(re.findall(r"\bday\s*\d+\b", due, re.I))) > 1:
                add("dues", f"{did} :: several moves in one due; an actor has one next move "
                            "and one due, the rest in its plan (RULES §15.1)")
            if not _due_minutes(due, anc) and not _EVENT.search(due):
                add("dues", f"{did} :: neither a time nor a trigger — \"{due[:60]}\"")
            elif re.search(r"\bday\s*\d+\b", due, re.I) and not re.search(
                    r"\d{1,2}:\d{2}|morning|noon|midday|afternoon|evening|dusk|dawn|night|midnight",
                    due, re.I):
                add("dues_without_time", f"{did} :: a day with no time of day; "
                                         "the tool will assume 08:00")
    for row in _depth_problems(tree):
        add("depth_fields", row)
    for aid, rec, st in _important(tree):
        if _no_due(st):
            add("important_without_due", f"npcs.{aid} :: important and has no plan with a due")

    cases = set((tree.get("locked_case_truths") or {}).keys())
    for qid, q in (tree.get("quests") or {}).items():
        if not isinstance(q, dict):
            continue
        status = str(_val(q.get("status")) or "").lower()
        if not q.get("code"):
            add("quests", f"quests.{qid} :: no code; a quest's code is designed with it (RULES §10)")
        if status not in ("available", "blocked"):
            add("quests", f"quests.{qid} :: status \"{status}\" at Round 0 (available | blocked)")
        if status == "blocked" and not q.get("trigger"):
            add("quests", f"quests.{qid} :: blocked with no trigger")
        for f in ("objective", "hook", "level"):
            if q.get(f) in (None, ""):
                add("quests", f"quests.{qid} :: lacks {f}")
        refs = [r for r in (q.get("support_refs") or []) if r in cases]
        for r in q.get("support_refs") or []:
            if r not in cases:
                add("references", f"quests.{qid}.support_refs :: no case \"{r}\"")
        if refs and len(q.get("routes") or []) < 3:
            add("quests", f"quests.{qid} :: tied to a case but lists {len(q.get('routes') or [])} "
                          "routes; a case tied to a quest needs ≥3 independent ones")

    for pid, pr in (tree.get("active_world_pressures") or {}).items():
        if not isinstance(pr, dict):
            continue
        ck, tr = pr.get("clock"), pr.get("track")
        dues = []
        if isinstance(ck, dict):
            dues.append(ck.get("due"))
        if isinstance(tr, dict):
            for z, t in tr.items():
                if z not in zones:
                    add("references", f"active_world_pressures.{pid}.track.{z} :: no such location")
                if isinstance(t, dict):
                    dues.append(t.get("due"))
        if isinstance(ck, dict) and isinstance(tr, dict):
            add("pressures", f"active_world_pressures.{pid} :: has both a clock and a track")
        if not [d for d in dues if d not in (None, "")]:
            add("pressures", f"active_world_pressures.{pid} :: no due")
        for a in pr.get("actors") or []:
            if a not in actors:
                add("references", f"active_world_pressures.{pid}.actors :: no actor \"{a}\"")

    for lid, loc in (tree.get("locations") or {}).items():
        if not isinstance(loc, dict):
            continue
        z = loc.get("zone")
        if z and z not in zones:
            add("references", f"locations.{lid}.zone :: no location \"{z}\"")
        if not z and not loc.get("closed") and not isinstance(loc.get("surface"), dict):
            add("locations", f"locations.{lid} :: neither a zone nor its own surface")

    for sid, sl in (tree.get("storylines") or {}).items():
        for ref in (sl or {}).get("refs") or []:
            owner, _, rid = str(ref).partition(".")
            if owner and rid and rid not in (tree.get(owner) or {}):
                add("references", f"storylines.{sid}.refs :: no {ref}")

    mods = tree.get("enabled_modules") or {}
    if mods.get("flexible_item_entitlement", True) is not False:
        rank = str(((tree.get("player") or {}).get("item_points") or {}).get("rank") or "")
        if rank and rank.lower() not in RANK_MAX and "[" not in rank:
            add("player", f"player.item_points.rank :: \"{rank}\" ({' | '.join(RANK_MAX)})")

    n = sum(len(v) for v in probs.values())
    hard = {k: v for k, v in probs.items() if k != "dues_without_time"}
    lines = [f"Background check — {tree.get('background_id') or form['background']}: "
             f"{n} finding{'s' if n != 1 else ''}"]
    for k, v in probs.items():
        lines.append(f"  {k.replace('_', ' ')}: {len(v)}")
    return {"tool": TOOL_VERSION, "ok": not hard, "findings": probs, "copy": lines,
            "cannot_check": "design: whether the hidden reality holds together, a secret has "
                            "a real reason, a pull truly fights the want, routes are really "
                            "independent; and what was invented, which the GM lists for the person"}


# ── awards and other forms that read the world ──

def do_award(form):
    _need(form, "actor", "challenge", "scope", "source")
    tree, _ = world_tree(form.get("background"), form.get("save"), form.get("deltas"))
    path, rec = _actor(tree, form["actor"])
    level, xp, numeric = _level(tree, path, rec)
    if not numeric or path != "player" and "progression" not in rec:
        if path != "player":
            raise InputError("XP is tracked for the player and tracked companions with a "
                             "progression record")
    r = do_xp(argparse.Namespace(level=level, xp=xp, r=int(form["challenge"]), p=level,
                                 scope=form["scope"], amount=None))
    base = "player" if path == "player" else path
    new = r["new"]
    line = (f"XP +{r['award']} ({form['source']}) → level {new['level']}, {new['xp']} XP"
            + (f" — level up to {r['level_ups'][-1]}" if r["level_ups"] else ""))
    return {"tool": TOOL_VERSION, "award": r["award"], "new": new, "copy": [line],
            "gm_delta": [f"~ {base}.progression.state :: {{level: {new['level']}, xp: {new['xp']}}}",
                         f"+ world_state.material_history.xp_{re.sub(r'[^A-Za-z0-9]+', '_', str(form['source'])).strip('_').lower()} "
                         f":: XP paid for {form['source']}: {r['award']}"],
            "once": "each source pays once: check material_history before paying again"}


PASSTHROUGH = {"roll": ["spec"], "xp": [], "boundary": [], "points": [], "merge": [],
               "validate": [], "vitals": [], "harm": [], "heal": [],
               "encounter": [], "stability": [], "cast": [], "time": []}

FIELDS = {"vitals": "v, size, mp_tier", "harm": "hp, max, dice | amount, soak, hits",
          "heal": "current, max, dice | amount | quarter | full", "cast": "mp, tier",
          "time": "day, clock, add", "roll": "spec", "boundary": "cls, tier, evidence, class_source",
          "points": "rank, current, spend | refill, label",
          "stability": "layer, current, baseline, tension, marks, lasting, stepped, day",
          "encounter": "surface | depth", "merge": "base, background, deltas, out, save_round",
          "validate": "file, against, background"}

FORMS = {
    "action": "an uncertain action: actor, action, skill, opposition, tool, gear_tier, "
              "conditions, lasting, danger, cost_form, reach, damage + world files",
    "help": "does help exist? ask, sources (≤3), hostile",
    "ask": "an NPC's open answer: who, question, for [{fact, points}], against [{fact, points}]",
    "combat": "a fight in a batch: side [..], opponents [..], conditions, stop {hp_at_or_below}",
    "span": "run time: from {day, clock}, minutes, pc_zone, arrived + world files; after a stop, "
            "send it again with the returned resume fields",
    "check": "a background before play: background → findings (frame, npcs, depth fields, dues, "
             "quests, pressures, locations, references); ok when nothing but untimed dues",
    "selfcheck": "R50 check: answers {npc_positions, quests, money, hp}, round + world files",
    "award": "XP: actor, challenge, scope, source + world files",
    "boundary": "growth boundary: cls, tier, evidence, class_source (yes when a valid source was involved)",
    "points": "item points: rank, current, spend | refill, label",
    "stability": "marks on a layer: layer, current, baseline, tension, marks, lasting, stepped, day",
    "encounter": "one roll: surface | depth",
    "vitals": "max HP and MP: v (level or vitality value), size, mp_tier",
    "harm": "damage to HP: hp, max, dice | amount, soak, hits",
    "heal": "restore: current, max, dice | amount | quarter | full",
    "cast": "pay a power's cost: mp, tier",
    "time": "clock arithmetic: day, clock, add (minutes)",
    "roll": "plain dice: spec (NdM)",
    "merge": "build a capsule: base, background, deltas, out, save_round",
    "validate": "check a save: file, against, background",
    "world files": "background (required), save (newest, once one exists), deltas (a file of "
                   "every GM-Δ block since that save)",
}


YES_NO = ("class_source", "refill", "arrived", "quarter", "full", "lasting",
          "brief", "success")


def _passthrough(cmd, form):
    argv = [cmd]
    for k, v in form.items():
        if k == "cmd" or v is None or v is False:
            continue
        if cmd == "roll" and k == "spec":
            argv.append(str(v)); continue
        flag = "--" + ("for" if k == "for_" else k.replace("_", "-"))
        if k in YES_NO:      # a yes/no field: any stated value but "no"/"false" is yes
            if str(v).strip().lower() not in ("no", "false", "0", "none", ""):
                argv.append(flag)
        elif v is True:
            argv.append(flag)
        else:
            argv += [flag, str(v)]
    import contextlib, io
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            return _cli(argv)
    except SystemExit:
        why = (err.getvalue().strip().splitlines() or [""])[-1]
        why = re.sub(r"^.*?error:\s*", "", why)
        why = re.sub(r"--([a-z][a-z-]*)", lambda m: m.group(1).replace("-", "_"), why)
        raise InputError(f"the \"{cmd}\" form: {why or 'a field is wrong or missing'}; "
                         f"fields: {FIELDS.get(cmd, 'see forms')}")


def run(form):
    if not isinstance(form, dict) or "cmd" not in form:
        raise InputError("a form is a JSON object with \"cmd\"")
    cmd = str(form["cmd"]).lower()
    if cmd == "forms":
        return {"tool": TOOL_VERSION, "forms": FORMS}
    table = {"action": do_action, "help": do_help_roll, "ask": do_ask_form,
             "combat": do_combat, "span": do_span, "selfcheck": do_selfcheck,
             "check": do_check_background,
             "award": do_award}
    if cmd in table:
        return table[cmd](form)
    if cmd in PASSTHROUGH:
        out = _passthrough(cmd, form)
        return out if isinstance(out, dict) else {"tool": TOOL_VERSION, "copy": str(out).split("\n")}
    raise InputError(f"unknown form \"{cmd}\"; send {{\"cmd\": \"forms\"}} for the list")


def main():
    args = _sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print(__doc__); return
    try:
        raw = open(args[0], encoding="utf-8").read() if args else _sys.stdin.read()
    except OSError as e:
        fail(f"cannot read the form: {e}")
    try:
        form = json.loads(raw)
    except ValueError as e:
        fail(f"the form is not valid JSON: {e}")
    unflag = lambda t: re.sub(r"--([a-z][a-z-]*)", lambda m: m.group(1).replace("-", "_"), t)
    def fields(v, key=None):
        """Messages name form fields, never command-line flags."""
        if key in ("copy", "gm_delta"):
            return v
        if isinstance(v, str):
            return unflag(v)
        if isinstance(v, list):
            return [fields(x) for x in v]
        if isinstance(v, dict):
            return {k: fields(x, k) for k, x in v.items()}
        return v
    try:
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            out = run(form)
    except InputError as e:
        fail(unflag(str(e)))
    print(json.dumps(fields(out), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
