# Werkwijze (voor mij, niet voor Claude)

## Welke aanpak?
| Situatie | Doe |
|---|---|
| Kleine wijziging, in één zin te beschrijven | Gewoon vragen |
| Groter, meerdere bestanden of onduidelijk | `/build <taak>` |
| Nieuwe feature zonder duidelijk plan | `/interview <idee>` → nieuwe sessie → `/build implement SPEC.md` |
| Echte livegang | `/release` (alleen ik start deze) |
| Iets wordt vaste afspraak | `/standard <afspraak>` |

## Verbruik laag houden
- `/clear` tussen taken die niks met elkaar te maken hebben.
- Twee keer gecorrigeerd en nog fout? `/clear` en opnieuw met een betere prompt.
- Wees specifiek: noem bestanden, het gewenste gedrag en hoe je het test.
- Zijvraag die niet in de context hoeft: `/btw <vraag>`.
- Onderzoek laten doen door een subagent ("gebruik de researcher om …").

## Handig
- `Esc` stopt Claude; `Esc Esc` of `/rewind` zet terug naar een eerder punt.
- `Shift+Tab` wisselt naar plan mode (Opus denkt mee via `opusplan`).
- `/rename <naam>` geeft een sessie een naam; `claude --continue` pakt de laatste op.
- `/context` laat zien wat er geladen is; `/code-review` reviewt de huidige diff.

## Onderhoud
- Af en toe `/doctor`: stelt voor wat uit CLAUDE.md kan.
- Na een nieuwe modelrelease: regels nalopen die misschien niet meer nodig zijn.
- Doet Claude iets steeds fout ondanks een regel? CLAUDE.md is waarschijnlijk te lang.
