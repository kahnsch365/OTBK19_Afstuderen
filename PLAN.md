# Plan: implement SPEC.md (concept-onderzoeksvoorstel)

## Context
Het onderwerp staat vast in `SPEC.md` (JIS Nederland, SAP B1-team, DMADV, schaalbare AI-ondersteunde projectmethode).
Koen wil het onderzoeksvoorstel **zo snel mogelijk** indienen. "Implementeren" betekent hier: het originele
Word-formulier invullen, plus de begeleidende werkdocumenten die SPEC §5 noemt. SPEC.md is leidend.

## Bevindingen uit het verkennen
- Formulier `schooldocumenten/Formulier Voorstel Afstudeeronderzoek TBK - 2021-2022.docx`:
  - **Tabel 0** (24 rijen): de gegevens van student en bedrijf, label in c0 en waarde in c1 (sommige cellen zijn samengevoegd). Rij 3 ("Opleiding") en rij 15 ("Persoonlijke relatie") gebruiken oude Word-checkboxen (`w:checkBox/w:default w:val="0"`).
  - **Tabel 1, rij 1, één cel:**
    - p3 is de kop 3a, met een italic instructie in p4; daarna lege paragrafen p5–10;
    - p11 is de kop 3b, instructie p12, lege paragrafen p13–24;
    - p25 is de kop 3c, instructie p26, lege paragrafen p27–40.
  - **Tabel 1, rij 2:** p1 is de kop 3d, instructie p2, lege paragrafen p3–15.
- Beschikbaar: python-docx 1.2.0, pandoc en LibreOffice (voor een render-check naar PDF).

## Aanpak
1. **PLAN.md** opslaan (kopie van dit plan), committen.
2. **`afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.md`**: de bron-tekst, met dezelfde kopjes als het formulier.
   - **1 Student:** Koen, SPS TBK Enschede. Studentnummer, telefoon en periode als `[INVULLEN]`. Propedeuse: ja. Toelating: voldoet.
   - **2 Bedrijf:** JIS Nederland, sector ERP-dienstverlening (Jeeves en SAP Business One), 16 medewerkers. Adres, website en begeleider als `[INVULLEN]`. Persoonlijke relatie: ja, consultant SAP B1 sinds oktober 2024. Onderzoeksgebied en technische omgeving zoals in SPEC §1.
   - **3a:** 6W-tekst uit SPEC §2, plus een quickscan-plaatshouder voor cijfers.
   - **3b:** opdracht, scope en eindproduct, met multidisciplinair, innovatief, tactisch/operationeel en technische omgeving elk onderbouwd.
   - **3c:** extern doel, intern SMART-doel, hoofdvraag en deelvragen 1–5 (met 4b), letterlijk uit SPEC §3.
   - **3d:** type onderzoek (ontwerpgericht, DMADV), tabel per deelvraag (dataverzameling, analyse, resultaat), kernbronnen in APA, betrouwbaarheid en validiteit (triangulatie, member check, logboek, anonimiteit, rolconflict) en haalbaarheid in 18 weken met een globale fasering.
   - Compact: onderdeel 3 is ca. 2 A4 (≈ 1000–1300 woorden).
3. **Script `afstuderen/01-onderzoeksvoorstel/tools/vul_formulier.py`** (python-docx):
   - Kopieert het origineel en vult de waardecellen van tabel 0 (Verdana, zoals het origineel).
   - Zet de checkboxen voor "SPS TBK Enschede" en "Ja" aan, en vult de tekst achter "Ja, nl:" in.
   - Zet de datum.
   - Plaatst per onderdeel 3a–3d de tekst in de lege paragrafen ná de instructie. Kopjes en instructies blijven ongewijzigd; extra paragrafen worden ingevoegd waar nodig, lege overbodige paragrafen verwijderd.
   - Bij 3d komt de DMADV-tabel als geneste tabel in de cel.
   - Leest de inhoud uit `onderzoeksvoorstel.md` (secties via kopjes), zodat `.md` en `.docx` letterlijk gelijk blijven.
   - Het script wordt meegecommit, zodat Koen na het invullen van de `[INVULLEN]`-velden in de `.md` opnieuw kan genereren.
4. **`onderzoeksvoorstel.docx`** genereren. Render-check met LibreOffice naar PDF en daarvan een PNG van de pagina's om de opmaak visueel te controleren (alleen in de scratchpad).
5. **`checklist-eisen.md`**: §3.2 (alle bullets), §4.1 (1–2), §5.1 a–e en de toetsvragen uit het formulier → sectie in het voorstel → ✅/⚠️.
6. **`quickscan-data.md`**: een sjabloon zoals in SPEC §5, met instructie en een kolom voor datakwaliteit.
7. **`gesprek-opdrachtgever.md`**: agenda en vragen voor de directeur en de begeleider (SPEC §5).
8. **`afstuderen/README.md`**: index en status. In de root-`README.md`: `afstuderen/` toevoegen aan de structuurtabel en de status "Onderwerp kiezen" afvinken.
9. Na elke stap committen. Review door de `reviewer`-subagent tegen PLAN.md en SPEC.md, echte bevindingen fixen. PLAN.md verwijderen en pushen.

## Buiten scope (uit SPEC)
Het onderzoeksplan, formele dataverzameling en interviews, de invoering of pilot, het Jeeves-team en het
verkoopproces, klantinterviews, een losse dashboard- of AI-tool, en het indienen in Brightspace.

## Verificatie (SPEC §7)
1. `pandoc onderzoeksvoorstel.docx -t plain` draait zonder fouten en bevat alle formulierkopjes. Bij 3a–3d alleen `[INVULLEN]` als placeholder.
2. Een script vergelijkt de kopjes en instructies van het origineel met het ingevulde `.docx`: alles is nog aanwezig en ongewijzigd.
3. In `checklist-eisen.md` zijn alle inhoudelijke regels ✅; alleen Koens acties zijn ⚠️.
4. Een script vergelijkt de hoofdvraag, het interne doel en de deelvragen 1–5 en 4b tussen `.md` en `.docx` (letterlijk), en controleert dat de kernwoorden van het doel in de hoofdvraag staan.
5. Met grep: "technische omgeving", "multidisciplinair", "innovatief" en "tactisch/operationeel" staan in 3a/3b.
6. Woordtelling van 3a–3d.
7. `git status` is schoon en alles is gepusht naar `main`.
