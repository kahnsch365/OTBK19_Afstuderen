---
name: interview
description: Interview the user about a new feature or project and write SPEC.md. Use before building something larger that has no spec yet.
---
I want to build: $ARGUMENTS

Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs.
Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to
SPEC.md that:
- names the files and interfaces involved
- states what is out of scope
- ends with an end-to-end verification step that proves it works

Commit and push SPEC.md, then tell me to start a fresh session and run
`/build implement SPEC.md`.
