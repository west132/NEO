# NEO v0

A rule set and one tool that turn a chat AI into a Game Master who keeps track of things.

## The play set

Attach these five to a chat with a model that can run code, then send: `Load the NEO files, start <background>.`

| File | What it is |
|---|---|
| `NEO_GM_v0.md` | How the GM runs the game: the law, its job, the six-step loop, narration, stops, saving, starting and loading. Read every turn. |
| `NEO_RULES_v0.md` | How the game resolves. Opened when a step of the loop calls it. |
| `NEO_WORLD_v0.md` | The shape of a world: background and save. |
| `neo_math_v0.py` | The tool. Part of the rules, never optional. Run it, never read it: one JSON form in, one JSON result out. |
| `worlds/BACKGROUND_<name>_NEO_v0.md` | One world. Attach exactly one. |

To continue a campaign: the same five files and your newest save. Send: `Continue from this save.`

To make a new world: attach the four play files (no background) and send: `Make a new world: <what you want>.` The GM follows its making-a-world steps, checks the result with the tool, and shows you what it invented before you play.

Out of character: start a message with `ps`, or say it is out of game, to the GM or to the AI.

## Not part of play

| Folder | What it is |
|---|---|
| `design/` | Design record, reading note, rule map. History and reasons, for people. Never attach these to a game: they are not an authority in play. |
| `tests/` | Checks for the tool. From this folder: `python -m unittest discover -s tests -t tests` |

All play files share one version. Don't mix versions.
