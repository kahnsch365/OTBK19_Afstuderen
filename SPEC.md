# SPEC – Afstudeeronderwerp en onderzoeksvoorstel (OTBK19)

> Uitkomst van het interview op 22-11-2026. Deze spec beschrijft **het gekozen onderwerp** en **wat `/build` moet
> opleveren**: een ingevuld concept-onderzoeksvoorstel dat zo snel mogelijk kan worden ingediend.
> Bronnen: `schooldocumenten/README.md`, de handleiding (§3.2, §3.3, §4.1, §5) en `context/persoonlijk-profiel.md`.

## 1. Gekozen richting

**Werktitel:** *Van ieder z'n eigen aanpak naar een standaard projectproces: ontwerp van een schaalbare,
AI-ondersteunde implementatiemethode voor het SAP Business One-team van JIS Nederland.*

| Aspect | Keuze |
|---|---|
| Opdrachtgever | JIS Nederland, SAP Business One-team (6 consultants, 16 medewerkers totaal). Grootte en IT/ERP-omgeving zijn toegestaan, mits er echt naar **processen** wordt gekeken. |
| Scope van het proces | **Alle (klant)projecten van het SAP B1-team**, in één proces: volledige SAP B1-implementaties, add-on-implementaties en kleinere uitbreidingen. De dagelijkse supportstroom valt buiten het proces en dient alleen als bron (rework na go-live). |
| Kern van het resultaat | **Een gestandaardiseerde, schaalbare projectaanpak**: één kernproces met vaste fasen, deliverables, templates/checklists en overdrachtsmomenten, plus een **lichte variant** voor add-ons en kleine projecten. Welke deliverables per projecttype verplicht zijn, is een ontwerpkeuze (projectclassificatie). |
| AI | **Onderdeel van het ontwerp, niet het hoofdonderwerp.** Eerst standaardiseren, dan ondersteunen. AI wordt ingezet waar de methode vastlegging en overdracht vraagt, bv. een concept-functioneel ontwerp of -verslag uit workshopnotities, een doorzoekbare kennisbank over dossiers en inrichtingskeuzes, en het genereren van testscripts of overdrachtsdocumenten. Klantdata en de AVG zijn een harde randvoorwaarde. |
| Onderdelen binnen de kern | **Kennisborging**: vaste klantdocumentatie en overdracht als deliverables in de methode. **Stuurinformatie**: een beperkte set KPI's (uren t.o.v. budget, doorlooptijd t.o.v. planning, rework na go-live), als onderdeel van de methode en niet als los dashboardproject. |
| Procesmodel | **DMADV**. Er is nog geen standaardproces, dus het gaat om een ontwerp en niet om het verbeteren van een bestaand proces (DMAIC). |
| Invoering | Veel ruimte: een **pilot** in een of meer lopende trajecten (Verify-fase). Dat dekt de eis "implementatie of aanzet daartoe". |
| Reserveonderwerp | Geen. De focus ligt op JIS. |

### Waarom dit onderwerp aan de eisen voldoet (§3.2 / §4.1)
- **Proces:** het projectproces van offerte/overdracht tot go-live en de overdracht naar nazorg wordt opnieuw ontworpen, voor projecten van verschillende omvang. Dat is Procesmanagement (verplicht) en Technologie & Innovatiemanagement (ERP, plus AI als innovatie binnen het proces).
- **Niet uitgewerkt:** iedere consultant werkt nu op zijn eigen manier en het team is gegroeid van 1 naar 6. Kennis zit "in het hoofd".
- **Geen standaardoplossing:** de methode moet passen bij een klein team, bij B1-projecten van uiteenlopende omvang (van volledige implementatie tot add-on) en bij de rol van sales in de begroting. Daarvoor is analyse van data en interviews nodig, plus literatuur (projectmatig werken, standaardisatie, kennismanagement, ERP-implementatiemethoden zoals SAP Activate, AI in kenniswerk).
- **Meerdere partijen met verschillende belangen:**
  - consultants;
  - directie/eigenaar;
  - sales: maakt de urenbegroting in beperkt overleg met de consultant en heeft een eigen belang;
  - support/nazorg;
  - indirect de klanten.
- **Groot belang voor de opdrachtgever:** de symptomen zijn urenoverschrijdingen, uitgestelde go-lives en rework na go-live.
- **Individueel en haalbaar:** de scope is afgebakend tot één kernproduct. Ondanks minder dan 8 uur per week is het haalbaar, mede omdat Koen deels in werktijd mag werken.

## 2. Voorlopige probleemschets (input voor formulier onderdeel 3a)

Het SAP Business One-team van JIS is in korte tijd gegroeid van 1 naar 6 consultants. Projecten (volledige
implementaties, add-on-implementaties en kleinere uitbreidingen, met de fasen vooranalyse, inrichting, go-live en
nazorg) worden door iedere consultant op een eigen manier uitgevoerd. Er is geen vastgelegde
methode, geen vaste deliverables en geen eenduidige vastlegging van klantinrichting en afspraken. De leidinggevende
structuur boven het team is informeel. De urenbegroting komt van sales, in beperkt overleg met de consultant.
Waargenomen symptomen:
- overschrijding van uren of budget;
- uitgestelde go-lives;
- fouten en rework na go-live.

Omdat niet iedereen meer weet waar een collega mee bezig is, zijn overdracht en onderlinge vervanging lastig.

*Nog te onderbouwen met data in het vooronderzoek (zie §4): hoe groot zijn de overschrijdingen en hoe vaak komt rework voor?*

## 3. Concept doel- en vraagstelling (input voor formulier onderdeel 3c)

**Extern doel (bedrijf):** de voorspelbaarheid van SAP B1-projecten verbeteren: minder urenoverschrijding, minder
uitstel van go-live en minder rework na go-live, zodat het team kan groeien zonder kwaliteitsverlies.

**Intern doel (onderzoek), concept SMART:** binnen de afstudeerperiode (ca. 20 weken na de GO op het onderzoeksvoorstel)
een gestandaardiseerde, schaalbare projectmethode ontwerpen voor het SAP B1-team (kernproces plus lichte variant) en in
minimaal één lopend project als pilot toetsen. De methode bevat vaste fasen, deliverables (inclusief klantdocumentatie
en overdracht), 3–5 KPI's en ten minste één uitgewerkte AI-toepassing ter ondersteuning van vastlegging of overdracht.
*De concrete streefwaarden (bv. maximaal x% urenoverschrijding) volgen uit de nulmeting in de Measure-fase.*

**Concept hoofdvraag:** *Hoe kan het SAP Business One-team van JIS Nederland zijn projectproces voor implementaties en
add-ons standaardiseren, zodat de uren- en planningsoverschrijdingen en het rework na go-live afnemen?*

**Concept deelvragen per DMADV-fase:**

| Fase | Deelvraag | Methode / bron |
|---|---|---|
| Define | 1. Hoe verlopen projecten nu (volledige implementaties, add-ons, kleinere uitbreidingen), van offerte/overdracht door sales tot de overdracht naar nazorg, en welke stakeholders en belangen spelen een rol? | Interviews met consultants, directie, sales en support. Procesmapping per projecttype (swimlane/brown paper). Stakeholderanalyse. |
| Measure | 2. In welke mate treden urenoverschrijding, uitstel van go-live en rework na go-live op, en verschilt dat per projecttype? | Bestaande data: urenregistratie, projectplanning/budget, supporttickets na go-live. Afgeronde en lopende projecten van alle typen, wat meer cases oplevert. |
| Analyze | 3. Welke oorzaken in het proces verklaren deze afwijkingen? | Analyse van de data uit deelvraag 2, interviews en projectdossiers/mail (oorzaak-gevolg/visgraat). Klantperspectief indirect via tickets, dossiers en sales. |
| Design | 4. Aan welke eisen moet een standaardmethode voor projecten van verschillende omvang voldoen, en hoe ziet die eruit (kernproces, lichte variant, deliverables, templates, KPI's)? | Literatuur (ERP-implementatiemethoden zoals SAP Activate, standaardisatie, kennisborging). Eisen ophalen bij de stakeholders. Ontwerp. |
| Design | 5. Hoe kan AI de vastlegging, kennisborging en overdracht binnen de methode ondersteunen, gegeven de randvoorwaarden rond klantdata (AVG)? | Literatuur over AI in kenniswerk. Inventarisatie van beschikbare tools en het AI-/privacybeleid van JIS. Selectie van toepassingen met een afwegingsmatrix (nut, risico, kosten). |
| Verify | 6. In hoeverre zijn de methode en de AI-toepassing werkbaar en dragen ze bij aan de doelen, gelet op een pilot in een lopend project? | Pilot, evaluatie met de betrokken consultants, eerste KPI-meting, aanpassingen en implementatieplan. |

## 4. Kaders, risico's en afspraken

| Onderwerp | Afspraak / maatregel |
|---|---|
| Klanten | **Niet interviewen of enquêteren.** Het klantperspectief komt indirect uit supporttickets, projectdossiers/mail en sales/accountmanagers. Benoem dit als beperking in betrouwbaarheid en validiteit. |
| Rolconflict | Koen onderzoekt zijn eigen team ("lastig maar te doen"). Daarom: afspraken over anonimiteit in interviews, focus op het proces en niet op personen, en reflectie op de eigen rol (input voor het reflectieverslag). |
| AI en klantdata | Klantgegevens niet zonder toestemming in externe AI-tools. Toets elke AI-toepassing aan het (eventuele) AI-/privacybeleid van JIS en aan de AVG. Voor de pilot gebruik je bij voorkeur geanonimiseerde of interne informatie. Dit staat los van Koens eigen AI-gebruik bij het schrijven (zie AI-gebruik). |
| Weinig cases | Minder dan 5 volledige implementaties per jaar. Omdat add-on-implementaties en kleinere uitbreidingen binnen de scope vallen, stijgt het aantal cases. Vul aan met de supportstroom als bron. De analyse is vooral kwalitatief, met beschrijvende statistiek waar de data het toelaat. |
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
- De dagelijkse support als proces (alleen als databron voor rework).
- Het bouwen of uitrollen van een eigen AI-tool. Het onderzoek selecteert en ontwerpt AI-toepassingen binnen de methode. In de pilot is een eenvoudige toets met bestaande tools mogelijk.
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
4. De hoofdvraag, het doel en de 6 deelvragen in `.md` en `.docx` zijn letterlijk gelijk (controle met een script), en elke deelvraag is aan een DMADV-fase gekoppeld.
5. Een woordtelling van 3a–3d in het `.docx` toont dat het voorstel compact blijft (richtlijn: maximaal ca. 2 A4 voor onderdeel 3).
6. `git status` is schoon en alles is gepusht naar `main`.
