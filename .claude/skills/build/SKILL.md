---
name: build
description: Explore → Plan → Implement → Commit workflow for non-trivial changes (multiple files, unclear approach, unfamiliar code). Skip for changes you can describe in one sentence.
---
Task: $ARGUMENTS

1. **Explore** — in plan mode (enter it if not active; `opusplan` only uses Opus
   there). Read only what the task needs; use the `researcher` subagent for broad
   questions. If SPEC.md exists, it is the source of truth.
2. **Plan** — files to change, approach, edge cases, how to verify, what is out
   of scope. Wait for approval.
3. **Implement** — first save the approved plan to PLAN.md (it survives
   compaction). Work in small steps; after each working step run the checks from
   CLAUDE.md, then commit.
4. **Review** — have the `reviewer` subagent check the diff against PLAN.md
   (and SPEC.md). Fix real findings only.
5. **Finish** — delete PLAN.md, commit, `git push origin main`. Report what
   changed and show the check output.
