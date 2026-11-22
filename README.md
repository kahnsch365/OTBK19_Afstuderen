# Repo template

Basis voor nieuwe projecten met vaste afspraken voor GitHub en Claude Code.
Gericht op solo-gebruik en zo laag mogelijk verbruik.

## Afspraken
- **`main`** = werk- en testbranch. Claude commit per werkende stap en pusht na elke taak.
- **`live`** = alleen voor een echte livegang, via `/release`. Claude Code vraagt
  altijd bevestiging bij acties op `live`.
- Geen GitHub Actions, CI of betaalde diensten.

## Wat zit erin
| Bestand | Doel |
|---|---|
| `CLAUDE.md` | Korte regels die altijd gelden |
| `WORKFLOW.md` | Spiekbriefje en gewoontes voor mij |
| `.claude/settings.json` | Model `opusplan`, compact bij 250k, Accept edits, rechten, hook |
| `.claude/skills/` | `/build`, `/interview`, `/release`, `/standard` |
| `.claude/agents/` | `researcher` (goedkoop, alleen lezen), `reviewer` (frisse blik) |
| `.claude/hooks/session-start.sh` | Installeert dependencies in cloud-sessies |

## Nieuw project starten
1. GitHub → **Use this template** → privé repo.
2. Vul in `CLAUDE.md` het blok `# Project` in (test/lint/run-commando's).
3. Optioneel, afhankelijk van taal/stack:
   - code-intelligence plugin, bijv. `/plugin install typescript-lsp@claude-plugins-official`
   - formatter-hook na edits (vraag Claude: "maak een hook die na elke edit <formatter> draait")
   - extra install-stappen in `.claude/hooks/session-start.sh`
4. Groot project geworden? Zie de
   [large codebases-gids](https://code.claude.com/docs/en/large-codebases)
   (CLAUDE.md per map, deny-regels voor gegenereerde code).

## Eenmalig voor deze template-repo
GitHub → Settings → vink **Template repository** aan.
