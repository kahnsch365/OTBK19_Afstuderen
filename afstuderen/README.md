# Afstuderen – eigen producten

Onderwerp: **een gestandaardiseerde, schaalbare, AI-ondersteunde projectmethode voor het SAP Business One-team van
JIS Nederland** (DMADV). Achtergrond, keuzes en afbakening: [`SPEC.md`](../SPEC.md).

## Inhoud
| Map / bestand | Inhoud |
|---|---|
| [`01-onderzoeksvoorstel/onderzoeksvoorstel.md`](01-onderzoeksvoorstel/onderzoeksvoorstel.md) | Brontekst van het voorstel (onderdelen 1, 2 en 3a–3d van het formulier). **Hier pas je de tekst aan.** |
| `01-onderzoeksvoorstel/onderzoeksvoorstel.docx` | Het ingevulde originele Saxion-formulier: **dit bestand dien je in**. Gegenereerd uit de `.md`. |
| [`01-onderzoeksvoorstel/tools/vul_formulier.py`](01-onderzoeksvoorstel/tools/vul_formulier.py) | Script dat de `.docx` opnieuw maakt uit de `.md` (vereist `python-docx`). |
| [`01-onderzoeksvoorstel/checklist-eisen.md`](01-onderzoeksvoorstel/checklist-eisen.md) | Toetsing van het voorstel aan handleiding §3.2, §4.1, §5.1 en de toetsvragen van het formulier. |
| [`01-onderzoeksvoorstel/quickscan-data.md`](01-onderzoeksvoorstel/quickscan-data.md) | Sjabloon voor het vooronderzoek op bestaande projectdata (cijfers voor 3a). |
| [`01-onderzoeksvoorstel/gesprek-opdrachtgever.md`](01-onderzoeksvoorstel/gesprek-opdrachtgever.md) | Agenda en vragen voor het gesprek met de directeur en de beoogde bedrijfsbegeleider. |

De `.docx` opnieuw maken na een wijziging in de `.md`:

```bash
python3 afstuderen/01-onderzoeksvoorstel/tools/vul_formulier.py
```

## Status en volgende stappen
| Stap | Wanneer | Status |
|---|---|---|
| Concept-onderzoeksvoorstel (`.md` + ingevuld formulier) | nu | ✅ klaar |
| Gesprek met directeur en beoogde bedrijfsbegeleider | zo snel mogelijk | ⬜ |
| Quickscan invullen en cijfers in 3a verwerken | na het gesprek (toegang tot data) | ⬜ |
| `[INVULLEN: …]`-velden aanvullen, organogram als bijlage, `.docx` opnieuw genereren | vóór indienen | ⬜ |
| Deadline controleren in Brightspace (formulier 2021-2022 is actueel) | vóór indienen | ⬜ |
| Bewijs toelatingseisen klaarzetten | vóór indienen | ⬜ |
| Voorstel + bewijs indienen in Brightspace | uiterlijk week 4 van het kwartiel vóór de start | ⬜ |
| GO op het voorstel → onderzoeksplan schrijven (`02-onderzoeksplan/`) | start afstudeerperiode | ⬜ |
