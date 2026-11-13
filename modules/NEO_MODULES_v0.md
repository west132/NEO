# NEO MODULES — v0

Rules a world needs only when its background uses them. Attach this file alongside the play set when the background's setting has any of:

- `mp_powers.draws_mp` listing powers → **Powers**
- `mode: canon` → **Canon mode**
- `numeric_level_xp: false` → **Play without levels**

A background with none of these plays without this file.

---

## Powers (MP)

```text
MP        an actor with a power the setting draws from a pool; the tool derives
          max MP from level and the best MP-drawing skill's tier; the save holds
          current MP
DAMAGE    by the power's tier: T1 1d8 · T2 2d6 · T3 3d6 · T4 4d6, as damage or HP
          restored
CASTING   costs MP by the power's tier (the tool), paid on casting whether it works
          or not; a caster uses powers up to their own tier and when they have the
          MP; the background's mp_powers names the MP powers, and other powers
          follow their setting rule
RECOVERY  the background's mp_powers.recovery: fast = full after about 10 minutes
          out of danger · slow = a quarter per hour of rest, full after a night ·
          rest_only = full after a night
SEEN      the player sees the PC's own MP exactly; others' as they look
```

## Canon mode

For a background set in an existing story (a game, a novel, history) that keeps its course unless play changes it.

```text
COURSE    canon is the default course: canon actors follow its plans (the
          background's canon_course, else the source) while their causes hold
SETTLED   their plans are settled from the record; attempts still resolve
          normally (RULES §3, §8)
ANSWERS   +2 likelihood in an ask roll where canon records this outcome and play
          hasn't changed its causes (RULES §9.1)
GAPS      filled from canon first
FIT       new content fits around canon's people, places and events
BEATS     a beat's actors pursue it with their own means; it can pass without the
          PC, and the PC goes only where the player sends them
```

## Play without levels

When the background sets `numeric_level_xp: false`.

```text
CAPABILITY  the actor's grade in the domain: deficient · basic · competent ·
            advanced · exceptional (the form's capability_grade slot)
OPPOSITION  the engaged opponent's power is the base Difficulty; its attacks stay
            the danger
VITALITY    HP comes from vitality instead of level: ordinary · seasoned · veteran ·
            exceptional · heroic · legendary
XP          none; skills still grow by RULES §7
```

---

*End of NEO MODULES v0*
