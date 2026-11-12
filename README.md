# NEO v0

A rule set and one tool that turn a chat AI into a Game Master who keeps track of things.

## The play set

Attach these to a chat with a model that can run code, then send: `Load the NEO files, start <background>.`

| File | What it is |
|---|---|
| `NEO_GM_v0.md` | How the GM runs the game: the job, the turn, narration, handing back, saving, starting and loading. Read every turn. |
| `NEO_RULES_v0.md` | How the game resolves. Opened when a step of the turn calls it. |
| `NEO_SAVE_v0.md` | How a background is read in play, and how changes and saves are written. |
| `neo_math_v0.py` | The tool. Part of the rules: run it with one JSON form in, one JSON result out. |
| `worlds/BACKGROUND_<name>_NEO_v0.md` | One world. Attach exactly one. |

Add `modules/NEO_MODULES_v0.md` when the background uses powers (MP), canon mode, or play without levels. The background's setting says so; Sheet Anchor uses none of them.

To continue a campaign: the same files and your newest save. Send: `Continue from this save.`

To make a new world: attach the play set (no background) plus `templates/BACKGROUND_TEMPLATE_NEO_v0.md`, and send: `Make a new world: <what you want>.` The GM follows the template's steps, checks the result with the tool, and shows you what it invented before you play.

Out of character: start a message with `ps`, or say it is out of game, to the GM or to the AI.

## Used when needed

| Folder | What it is |
|---|---|
| `modules/` | Rules for worlds with powers, canon mode, or no levels. |
| `templates/` | The background template and the steps for making a world. |

## Not part of play

| Folder | What it is |
|---|---|
| `design/` | Design record, reading note, rule map. History and reasons, for people; kept out of games. |
| `tests/` | Checks for the tool. From this folder: `python -m unittest discover -s tests -t tests` |

All play files share one version; keep them together.
