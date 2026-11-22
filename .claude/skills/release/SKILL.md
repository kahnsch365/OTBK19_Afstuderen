---
name: release
description: Promote main to the live branch for a real go-live. Only when the user runs /release.
disable-model-invocation: true
---
Promote `main` to `live`. Notes: $ARGUMENTS

1. `git fetch origin` and make sure local `main` is clean and equals `origin/main`.
2. Run the checks from CLAUDE.md. Stop if anything fails.
3. Show what will go live: `git log --oneline origin/live..origin/main`
   (if `live` doesn't exist yet, say it will be created from `main`).
4. Ask for explicit confirmation.
5. Fast-forward only: `git push origin main:live`. If that is rejected
   (live has commits main doesn't), stop and explain. Never force-push.
6. Report the commit now on `live`.
