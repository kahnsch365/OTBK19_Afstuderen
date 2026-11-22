---
name: standard
description: Record a newly agreed default or convention in the Claude setup (CLAUDE.md, settings, skills). Use when the user says something is "the standard" or a recurring correction should stick.
---
New standard: $ARGUMENTS

Pick the lightest place that makes it stick:
- Must happen every time, no exceptions → `.claude/settings.json` (permission rule or hook)
- Applies to every task, one line → CLAUDE.md
- Procedure or only sometimes relevant → a skill in `.claude/skills/`
- Habit for the user, not Claude → WORKFLOW.md

Rules:
- CLAUDE.md stays under ~30 lines. If it grows, move detail into a skill.
- Replace or remove outdated rules instead of stacking new ones.
- Show the diff, then commit and push.
