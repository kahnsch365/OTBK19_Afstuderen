# SPEC – Afstudeeronderwerp en onderzoeksvoorstel (OTBK19)

> Uitkomst van het interview op 22-11-2026. Deze spec beschrijft **het gekozen onderwerp** en **wat `/build` moet
> opleveren**: een ingevuld concept-onderzoeksvoorstel dat zo snel mogelijk kan worden ingediend.
> Bronnen: `schooldocumenten/README.md`, de handleiding (§3.2, §3.3, §4.1, §5) en `context/persoonlijk-profiel.md`.

## 1. Gekozen richting

**Werktitel:** *Van ieder z'n eigen aanpak naar een standaard implementatieproces: ontwerp van een uniforme
implementatiemethode voor het SAP Business One-team van JIS Nederland.*

| Aspect | Keuze |
|---|---|
| Opdrachtgever | JIS Nederland, SAP Business One-team (6 consultants, 16 medewerkers totaal). Grootte en IT/ERP-omgeving zijn toegestaan, mits er echt naar **processen** wordt gekeken. |
| Kern van het resultaat | **Een gestandaardiseerde implementatieaanpak**: fasen, deliverables, templates/checklists en overdrachtsmomenten |
| Onderdelen binnen de kern | **Kennisborging**: vaste klantdocumentatie en overdracht als deliverables in de methode. **Stuurinformatie**: een beperkte set KPI's (uren t.o.v. budget, doorlooptijd t.o.v. planning, rework na go-live), als onderdeel van de methode en niet als los dashboardproject. |
| Procesmodel | **DMADV**. Er is nog geen standaardproces, dus het gaat om een ontwerp en niet om het verbeteren van een bestaand proces (DMAIC). |
| Invoering | Veel ruimte: een **pilot** in een of meer lopende trajecten (Verify-fase). Dat dekt de eis "implementatie of aanzet daartoe". |
| Reserveonderwerp | Geen. De focus ligt op JIS. |

### Waarom dit onderwerp aan de eisen voldoet (§3.2 / §4.1)
- **Proces:** het implementatieproces van offerte/overdracht tot go-live en de overdracht naar nazorg wordt opnieuw ontworpen. Dat is Procesmanagement (verplicht) en Technologie & Innovatiemanagement (ERP).
- **Niet uitgewerkt:** iedere consultant werkt nu op zijn eigen manier en het team is gegroeid van 1 naar 6. Kennis zit "in het hoofd".
- **Geen standaardoplossing:** de methode moet passen bij een klein team, B1-projecten en de rol van sales in de begroting. Daarvoor is analyse van data en interviews nodig, plus literatuur (projectmatig werken, standaardisatie, kennismanagement, ERP-implementatiemethoden zoals SAP Activate).
- **Meerdere partijen met verschillende belangen:**
  - consultants;
  - directie/eigenaar;
  - sales: maakt de urenbegroting in beperkt overleg met de consultant en heeft een eigen belang;
  - support/nazorg;
  - indirect de klanten.
- **Groot belang voor de opdrachtgever:** de symptomen zijn urenoverschrijdingen, uitgestelde go-lives en rework na go-live.
- **Individueel en haalbaar:** de scope is afgebakend tot één kernproduct. Ondanks minder dan 8 uur per week is het haalbaar, mede omdat Koen deels in werktijd mag werken.

## 2. Voorlopige probleemschets (input voor formulier onderdeel 3a)

Het SAP Business One-team van JIS is in korte tijd gegroeid van 1 naar 6 consultants. Implementaties (vooranalyse,
inrichting, go-live, nazorg) worden door iedere consultant op een eigen manier uitgevoerd. Er is geen vastgelegde
methode, geen vaste deliverables en geen eenduidige vastlegging van klantinrichting en afspraken. De leidinggevende
structuur boven het team is informeel. De urenbegroting komt van sales, in beperkt overleg met de consultant.
Waargenomen symptomen:
- overschrijding van uren of budget;
- uitgestelde go-lives;
- fouten en rework na go-live.

Omdat niet iedereen meer weet waar een collega mee bezig is, zijn overdracht en onderlinge vervanging lastig.

*Nog te onderbouwen met data in het vooronderzoek (zie §4): hoe groot zijn de overschrijdingen en hoe vaak komt rework voor?*

## 3. Concept doel- en vraagstelling (input voor formulier onderdeel 3c)

**Extern doel (bedrijf):** de voorspelbaarheid van SAP B1-implementaties verbeteren: minder urenoverschrijding, minder
uitstel van go-live en minder rework na go-live, zodat het team kan groeien zonder kwaliteitsverlies.

**Intern doel (onderzoek), concept SMART:** binnen de afstudeerperiode (ca. 20 weken na de GO op het onderzoeksvoorstel)
een gestandaardiseerde implementatiemethode ontwerpen voor het SAP B1-team en in minimaal één lopend traject als pilot
toetsen. De methode bevat vaste fasen, deliverables (inclusief klantdocumentatie en overdracht) en 3–5 KPI's.
*De concrete streefwaarden (bv. maximaal x% urenoverschrijding) volgen uit de nulmeting in de Measure-fase.*

**Concept hoofdvraag:** *Hoe kan het SAP Business One-team van JIS Nederland zijn implementatieproces standaardiseren,
zodat de uren- en planningsoverschrijdingen en het rework na go-live afnemen?*

**Concept deelvragen per DMADV-fase:**

| Fase | Deelvraag | Methode / bron |
|---|---|---|
| Define | 1. Hoe verloopt het implementatieproces nu, van offerte/overdracht door sales tot de overdracht naar nazorg, en welke stakeholders en belangen spelen een rol? | Interviews met consultants, directie, sales en support. Procesmapping (swimlane/brown paper). Stakeholderanalyse. |
| Measure | 2. In welke mate treden urenoverschrijding, uitstel van go-live en rework na go-live op bij afgeronde en lopende trajecten? | Bestaande data: urenregistratie, projectplanning/budget, supporttickets na go-live. Afgeronde trajecten plus kleinere projecten voor meer cases. |
| Analyze | 3. Welke oorzaken in het proces verklaren deze afwijkingen? | Analyse van de data uit deelvraag 2, interviews en projectdossiers/mail (oorzaak-gevolg/visgraat). Klantperspectief indirect via tickets, dossiers en sales. |
| Design | 4. Aan welke eisen moet een standaardmethode voor een klein B1-team voldoen, en hoe ziet die eruit (fasen, deliverables, templates, KPI's)? | Literatuur (ERP-implementatiemethoden zoals SAP Activate, standaardisatie, kennisborging). Eisen ophalen bij de stakeholders. Ontwerp. |
| Verify | 5. In hoeverre is de methode werkbaar en draagt ze bij aan de doelen, gelet op een pilot in een lopend traject? | Pilot, evaluatie met de betrokken consultants, eerste KPI-meting, aanpassingen en implementatieplan. |

## 4. Kaders, risico's en afspraken

| Onderwerp | Afspraak / maatregel |
|---|---|
| Klanten | **Niet interviewen of enquêteren.** Het klantperspectief komt indirect uit supporttickets, projectdossiers/mail en sales/accountmanagers. Benoem dit als beperking in betrouwbaarheid en validiteit. |
| Rolconflict | Koen onderzoekt zijn eigen team ("lastig maar te doen"). Daarom: afspraken over anonimiteit in interviews, focus op het proces en niet op personen, en reflectie op de eigen rol (input voor het reflectieverslag). |
| Weinig cases | Minder dan 5 implementaties per jaar. Vul aan met afgeronde trajecten, kleinere projecten en de supportstroom. De analyse is vooral kwalitatief, met beschrijvende statistiek waar de data het toelaat. |
| Bedrijfsbegeleider | Directeur/eigenaar en/of een senior consultant. **Nog niet besproken.** Eis: hbo-denkniveau, (potentieel) leidinggevende, 2 uur per week. |
| Sales | Sales heeft een eigen belang in de begroting. Neem sales mee als stakeholder. De offerte-/overdrachtsstap valt binnen het proces, het verkoopproces zelf niet. |
| Planning | Het voorstel moet **zo snel mogelijk** worden ingediend; de uitvoering mag weken tot maanden later starten. **Geen interviews of metingen vóór de GO op het onderzoeksplan.** |
| Vertrouwelijkheid | De repo is privé. Gebruik in repo-documenten geen klantnamen (Klant A, B, …). Vraag JIS of het onderzoek vertrouwelijk moet zijn (§4.3/§8.4). |
| AI-gebruik | Toegestaan, mits verantwoord volgens §8.3 (in de tekst en in de bronnenlijst). Houd een logboek bij. |

## 5. Wat `/build` moet opleveren

### Bestanden
| Bestand | Inhoud |
|---|---|
| `afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.md` | Het ingevulde **Formulier Onderzoeksvoorstel TBK**, met dezelfde volgorde en kopjes als `schooldocumenten/Formulier Voorstel Afstudeeronderzoek TBK - 2021-2022.md`: 1 Gegevens student · 2 Gegevens bedrijf en bedrijfsbegeleider · 3a Probleemstelling · 3b Opdrachtomschrijving · 3c Doelstelling, onderzoeksvraag en deelvragen · 3d Onderzoeksontwerp. Velden die alleen Koen kan invullen (studentnummer, telefoon, adressen, naam begeleider) worden `[INVULLEN: …]`. Inhoud gebaseerd op §1–§4 van deze spec, in lopende tekst op hbo-niveau, met APA-verwijzingen waar literatuur wordt genoemd. |
| `afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.docx` | Dezelfde inhoud in het **originele Word-formulier**: de kopie van de `.docx` uit `schooldocumenten/` wordt ingevuld, dus niet zelf opgemaakt. Dit is het in te dienen bestand. |
| `afstuderen/01-onderzoeksvoorstel/checklist-eisen.md` | Tabel: elke eis uit handleiding §3.2, §4.1 en §5.1 (a–e) → waar in het voorstel die wordt aangetoond → status (✅ / ⚠️ open). |
| `afstuderen/01-onderzoeksvoorstel/gesprek-opdrachtgever.md` | Een korte agenda en vragenlijst voor het eerste gesprek met de directeur/senior consultant: probleem toetsen, rol als bedrijfsbegeleider, ruimte voor de pilot, vertrouwelijkheid, toegang tot data. |
| `afstuderen/README.md` | Index van de afstudeermap plus de status-checklist (welke stap, welke deadline). |
| `README.md` (root) | De structuurtabel aanvullen met `afstuderen/`. |

### Buiten scope
- Het onderzoeksplan (dat komt na de GO op het voorstel), de literatuurstudie in de volle breedte, dataverzameling, interviews en de pilot zelf.
- Het Jeeves-team en het verkoopproces van sales (alleen de overdracht van sales naar consultant valt binnen de scope).
- Klantinterviews of -enquêtes.
- Een los dashboard- of BI-project. KPI's zitten alleen in de methode.
- Het indienen in Brightspace: dat doet Koen zelf.

## 6. Open acties voor Koen (vóór indienen)
1. Het idee bespreken met de directeur en/of een senior consultant (gebruik `gesprek-opdrachtgever.md`) en een bedrijfsbegeleider vastleggen.
2. In Brightspace de exacte deadline controleren (week 4 van het kwartiel vóór de start) en kijken of er een nieuwere versie van het formulier is dan die van 2021-2022.
3. De `[INVULLEN: …]`-velden aanvullen.
4. Het voorstel met ten minste twee vertegenwoordigers van JIS doorspreken, zoals het formulier adviseert.

## 7. End-to-end verificatie
`/build` is pas klaar als al deze punten aantoonbaar kloppen (laat de output zien):
1. `pandoc afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.docx -t plain` draait zonder fouten. De output bevat alle kopjes van het originele formulier (1, 2, 3a–3d), en bij 3a–3d staat geen lege of placeholdertekst behalve de expliciete `[INVULLEN: …]`-velden voor persoonsgegevens.
2. Een diff van de kopjesstructuur van het originele formulier en het ingevulde `.docx` toont geen verwijderde of hernoemde secties.
3. In `checklist-eisen.md` staat elke eis uit §3.2, §4.1 en §5.1 (a–e) met een verwijzing naar een concrete sectie. Alle inhoudelijke eisen zijn ✅; alleen acties van Koen (begeleider, deadline) mogen ⚠️ zijn.
4. De hoofdvraag, het doel en de 5 deelvragen in `.md` en `.docx` zijn letterlijk gelijk (controle met een script), en elke deelvraag is aan een DMADV-fase gekoppeld.
5. Een woordtelling van 3a–3d in het `.docx` toont dat het voorstel compact blijft (richtlijn: maximaal ca. 2 A4 voor onderdeel 3).
6. `git status` is schoon en alles is gepusht naar `main`.
