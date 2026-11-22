# SPEC – Afstudeeronderwerp en onderzoeksvoorstel (OTBK19)

> Uitkomst van het interview op 22-11-2026, aangescherpt na toetsing aan de handleiding, het formulier, de rubrics
> (Onderzoeksplan, Portfolio, Voorwaarden) en de OND-documenten. Deze spec beschrijft **het gekozen onderwerp** en
> **wat `/build` moet opleveren**: een ingevuld concept-onderzoeksvoorstel dat zo snel mogelijk kan worden ingediend.
> Bronnen: `schooldocumenten/README.md`, de handleiding (§1, §3.2, §3.3, §4.1, §5, §6, §8), het formulier,
> de rubrics, OND 1/2/4/5 en `context/persoonlijk-profiel.md`.

## 1. Gekozen richting

**Werktitel:** *Van ieder z'n eigen aanpak naar een standaard projectproces: ontwerp van een schaalbare,
AI-ondersteunde implementatiemethode voor het SAP Business One-team van JIS Nederland.*

| Aspect | Keuze |
|---|---|
| Opdrachtgever | JIS Nederland, SAP Business One-team (6 consultants, 16 medewerkers totaal; het formulier eist minimaal 15). **Probleemeigenaar:** de directeur/eigenaar. Grootte en IT/ERP-omgeving zijn toegestaan, mits er echt naar **processen** wordt gekeken. |
| Scope van het proces | **Alle (klant)projecten van het SAP B1-team**, in één proces: volledige SAP B1-implementaties, add-on-implementaties en kleinere uitbreidingen. Het proces loopt van de overdracht door sales tot de overdracht naar nazorg. De dagelijkse supportstroom valt buiten het proces en dient alleen als bron (rework na go-live). |
| Kern van het resultaat | **Een gestandaardiseerde, schaalbare projectaanpak**: één kernproces met vaste fasen, deliverables, templates/checklists en overdrachtsmomenten, plus een **lichte variant** voor add-ons en kleine projecten. Welke deliverables per projecttype verplicht zijn, is een ontwerpkeuze (projectclassificatie). |
| Onderdelen binnen de kern | **Kennisborging**: vaste klantdocumentatie en overdracht als deliverables. **Stuurinformatie**: 3–5 KPI's (uren t.o.v. budget, doorlooptijd t.o.v. planning, rework na go-live). **AI**: ondersteunt vastlegging en overdracht (zie hieronder). **Draagvlak**: de consultants ontwerpen mee, zodat de methode ook echt gebruikt wordt. |
| AI | **Onderdeel van het ontwerp, niet het hoofdonderwerp.** Eerst standaardiseren, dan ondersteunen. Voorbeelden: een concept-functioneel ontwerp of -verslag uit workshopnotities, een doorzoekbare kennisbank over dossiers en inrichtingskeuzes, en het genereren van testscripts of overdrachtsdocumenten. Klantdata en de AVG zijn een harde randvoorwaarde. |
| Procesmodel | **DMADV**, zuiver toegepast: er is nog geen standaardproces, dus het gaat om een (her)ontwerp en niet om het verbeteren van een bestaand proces (DMAIC). Measure = eisen (CTQ's) en nulmeting; Analyze = oorzaken en ontwerpalternatieven; Verify = validatie van het ontwerp. |
| Eindproduct afstuderen | Het **onderzoek, het ontwerp, het advies en een aanzet tot implementatie** (handleiding §1: "implementeer je (of je maakt een aanzet tot implementatie van)…"). Concreet: een gevalideerd ontwerp, een kosten-batenanalyse en een **implementatieplan**. **De invoering zelf valt buiten de afstudeerperiode.** |
| Reserveonderwerp | Geen. De focus ligt op JIS. |

### Toets aan het formulier (onderdeel 2, 3a en 3b): dit moet in het voorstel expliciet worden aangetoond
| Eis uit formulier | Invulling |
|---|---|
| **Technische omgeving** ("toon dat goed aan!") | JIS implementeert ERP-systemen: technische informatiesystemen waarin de primaire processen van klanten worden ingericht (inkoop, voorraad, productie, verkoop, financiën). De klanten zijn veelal productie- en handelsbedrijven. Het onderzochte proces is het **implementatieproces zelf**: een technisch-bedrijfskundig projectproces waarin systeemconfiguratie, datamigratie, testen en procesinrichting bij de klant samenkomen. Leg dit vast met een organogram als bijlage. |
| **Kern procesoptimalisatie of -(her)ontwerp** | Het projectproces wordt (her)ontworpen (DMADV). |
| **Multidisciplinair** | Procesmanagement (procesontwerp, KPI's), projectmanagement (fasering, begroting), kennismanagement (borging en overdracht), technologie en innovatie (ERP en AI) en mensen in organisaties (draagvlak en verandering). |
| **Innovatief** | Er is nog geen methode, dus de methode is nieuw voor JIS. Daarnaast wordt AI ingezet in het kenniswerk van consultants, met de AVG als randvoorwaarde, en is de methode schaalbaar naar projecttype. |
| **Niveau** | **Tactisch/operationeel**: de inrichting van het primaire projectproces en de besturing daarvan. Met een strategische raakvlak: het team moet kunnen groeien zonder kwaliteitsverlies. |
| **Persoonlijke relatie met het bedrijf** | Ja: Koen is SAP B1-consultant bij JIS (sinds oktober 2024). Benoem dat en benoem de maatregelen voor objectiviteit (zie §4). |
| **Zelfstandig uitvoerbaar in een half jaar** | Ja: de implementatie valt buiten de periode, het onderzoek gebruikt bestaande data en interne bronnen, en er is één kernproduct. |

### Waarom dit onderwerp aan de eisen voldoet (§3.2 / §4.1)
- **Beroepsthema's:** de focus ligt op Procesmanagement en Technologie & Innovatiemanagement (§3.2 punt 1). Mensen in organisaties komt terug via draagvlak en verandering.
- **Niet uitgewerkt:** iedere consultant werkt nu op zijn eigen manier, het team is gegroeid van 1 naar 6 en kennis zit "in het hoofd".
- **Geen standaardoplossing:** de methode moet passen bij een klein team, bij B1-projecten van uiteenlopende omvang en bij de rol van sales in de begroting. Daarvoor is een systematische analyse van data en interviews nodig, plus vakliteratuur (zie §3.1).
- **Meerdere partijen met verschillende belangen:**
  - directie/eigenaar (probleemeigenaar);
  - consultants;
  - sales: maakt de urenbegroting in beperkt overleg met de consultant en heeft een eigen belang;
  - support/nazorg;
  - indirect de klanten.
- **Dilemma's:** Koen onderzoekt zijn eigen team; standaardisatie staat tegenover de professionele autonomie van consultants; inzet van AI staat tegenover de vertrouwelijkheid van klantdata.
- **Groot belang voor de opdrachtgever:** urenoverschrijdingen (niet-factureerbare uren), uitgestelde go-lives en rework na go-live.
- **Individueel en haalbaar:** één afgebakend kernproduct, uitgevoerd door één student. De invoering valt erbuiten, dus het past in 18 weken (§5.1d), ondanks minder dan 8 uur per week eigen tijd plus deels werktijd.

## 2. Voorlopige probleemschets (input voor formulier onderdeel 3a, langs de 6W)

| W | Antwoord (concept) |
|---|---|
| Wat is het probleem? | Er is geen gestandaardiseerd projectproces. Consultants werken ieder op hun eigen manier, zonder vaste fasen, deliverables of vastlegging van klantinrichting en afspraken. |
| Wat is de aanleiding? | Snelle groei van het SAP B1-team (van 1 naar 6 consultants). Daarnaast zijn overschrijdingen, uitgestelde go-lives en rework na go-live gesignaleerd. |
| Wie heeft het probleem? | De directie (probleemeigenaar: rendement en groei), de consultants (rework, lastige overdracht), sales (begroting die niet klopt), support (rework na go-live) en indirect de klanten. |
| Wanneer is het ontstaan? | Met de groei van het team. Wat met één consultant "in het hoofd" kon, werkt met zes niet meer. |
| Waarom is het een probleem? | Niet-factureerbare uren, verlies van voorspelbaarheid en klanttevredenheid, kwetsbaarheid bij uitval of overdracht van een consultant, en een rem op verdere groei. |
| Waar doet het zich voor? | In het projectproces van het SAP B1-team: van de overdracht door sales via vooranalyse, inrichting, testen en go-live tot de overdracht naar nazorg. De leidinggevende structuur boven het team is informeel. |

**Vooronderzoek vóór het indienen (quickscan):** zet voor een paar afgeronde projecten de bestaande cijfers op een rij (begrote tegenover bestede uren, geplande tegenover werkelijke go-live, aantal tickets na go-live). Gebruik ze om het probleem in 3a te kwantificeren. De rubric eist een probleemanalyse "uit meerdere objectieve bronnen". Dit is vooronderzoek op bestaande data, geen formele meting. Leg dit wel voor aan de afstudeerbegeleider zodra die bekend is. Geen interviews of vragenlijsten vóór de GO op het onderzoeksplan.

## 3. Concept doel- en vraagstelling (input voor formulier onderdeel 3c)

**Extern doel (bedrijf):** de voorspelbaarheid en kwaliteit van SAP B1-projecten verbeteren, met minder
urenoverschrijding, minder uitstel van go-live en minder rework na go-live, zodat het team kan groeien zonder
kwaliteitsverlies.

**Intern doel (onderzoek), SMART en volgens het format van OND 2:**
*"Het uitvoeren van een ontwerpgericht onderzoek in opdracht van de directie van JIS Nederland, om binnen de
afstudeerperiode van 18 weken (uiterlijk [INVULLEN: einddatum]) een gestandaardiseerde, schaalbare projectmethode
voor het SAP Business One-team te ontwerpen en te valideren. De methode bestaat uit een kernproces met een lichte
variant voor add-ons, vaste deliverables voor vastlegging en overdracht, 3–5 stuur-KPI's met streefwaarden en ten
minste één uitgewerkte AI-toepassing. Het ontwerp wordt opgeleverd als adviesrapport met kosten-batenanalyse en
implementatieplan, zodat JIS de uren- en planningsoverschrijdingen en het rework na go-live structureel kan
terugdringen."*
*De streefwaarden van de KPI's (bv. maximaal x% urenoverschrijding) volgen uit de quickscan en de nulmeting.*

**Concept hoofdvraag** (sluit aan op de kernwoorden van het doel):
*"Hoe moet een gestandaardiseerde, schaalbare en door AI ondersteunde projectmethode voor implementaties en add-ons
van het SAP Business One-team van JIS Nederland eruitzien, zodat de uren- en planningsoverschrijdingen en het rework
na go-live afnemen, en hoe kan deze vóór [INVULLEN: einddatum] als gevalideerd ontwerp met implementatieplan worden
opgeleverd?"*
*Bij `/build`: deze vraag mag compacter, zolang de kernwoorden (gestandaardiseerd, schaalbaar, AI, implementaties en
add-ons, overschrijdingen, rework, periode) blijven staan.*

**Concept deelvragen: één per DMADV-fase, elke deelvraag bouwt voort op de vorige:**

| Fase | Deelvraag | Methode / bron | Resultaat |
|---|---|---|---|
| Define | 1. Hoe verloopt het projectproces nu per projecttype (volledige implementatie, add-on, kleine uitbreiding), van de overdracht door sales tot de overdracht naar nazorg, en welke stakeholders en belangen spelen daarbij een rol? | Semigestructureerde interviews met consultants, directie, sales en support. Procesmapping per projecttype (swimlane, brown paper). Stakeholderanalyse (macht-belangmatrix). | Procesmodel van de huidige situatie, stakeholderanalyse en afbakening |
| Measure | 2. Waaraan moet een standaardmethode volgens de stakeholders voldoen (CTQ's), en hoe presteert het huidige proces op uren t.o.v. budget, go-live t.o.v. planning en rework na go-live? | CTQ-boom op basis van de interviews. Bestaande data: urenregistratie, projectplanning/budget en supporttickets na go-live van afgeronde en lopende projecten. | Eisenlijst (CTQ's) en nulmeting van de KPI's |
| Analyze | 3. Welke procesoorzaken verklaren de afwijkingen, en welke ontwerpalternatieven (bv. SAP Activate-light, faseringsmodellen, checklistgedreven werken) passen bij de eisen? | Visgraatdiagram en Pareto op data, interviews en dossiers/mail (triangulatie). Klantperspectief indirect via tickets, dossiers en sales. Vergelijking van alternatieven met een afwegingsmatrix tegen de CTQ's. | Oorzakenanalyse en gekozen ontwerprichting |
| Design | 4. Hoe ziet de methode eruit: het kernproces, de lichte variant, de deliverables, de templates, de KPI's met streefwaarden en de rolverdeling tussen sales en consultant?<br>4b. Welke AI-toepassingen ondersteunen de vastlegging, kennisborging en overdracht binnen de methode, binnen de randvoorwaarden van de AVG en het beleid van JIS? | Ontwerp op basis van 1–3 en literatuur. Co-design-sessie(s) met consultants voor draagvlak. Voor 4b: literatuur over AI in kenniswerk, inventarisatie van tools en het beleid van JIS, en een afwegingsmatrix (nut, risico, kosten). | Procesontwerp (BPMN), templates en checklists, KPI-set en AI-toepassing(en) |
| Verify | 5. In hoeverre voldoet het ontwerp aan de eisen (CTQ's) en wordt het door de stakeholders gedragen, en wat zijn de kosten, de baten en de stappen voor invoering? | Validatiesessie met consultants en directie (member check). Droogtest op een afgerond project (walkthrough). Beoordeling van de AI-toepassing met een geanonimiseerd voorbeeld. Kosten-batenanalyse (overschreden en niet-factureerbare uren × tarief tegenover invoeringskosten). Verandermodel voor het implementatieplan. | Gevalideerd ontwerp, kosten-batenanalyse en implementatieplan (aanzet tot implementatie) |

### 3.1 Theorieën en modellen (input voor het technisch ontwerp; rubric 2.1 vraagt een mix van vakgebieden)
| Vakgebied | Kandidaten |
|---|---|
| Onderzoeksaanpak | Leen & Mertens (2017), *Praktijkgericht onderzoek in bedrijf*; DMADV (Design for Six Sigma) |
| Procesmanagement | Procesmapping/BPMN, standaardisatie van werkprocessen, CTQ-boom, visgraat, Pareto |
| Projectmanagement / ERP | SAP Activate-methodologie, (vereenvoudigd) PRINCE2 of een agile/hybride aanpak, kritieke succesfactoren bij ERP-implementaties |
| Kennismanagement | SECI-model (Nonaka & Takeuchi), expliciete tegenover impliciete kennis |
| Mensen en verandering | Een verandermodel (bv. Kotter of ADKAR, of de kleurendenken-benadering van De Caluwé & Vermaak), weerstand tegen verandering |
| Technologie en innovatie (AI) | Technology Acceptance Model / UTAUT, (generatieve) AI in kenniswerk, AVG |
| Bredere context (rubric 1.1, niveau D) | AI-ontwikkelingen, krapte aan ERP-consultants, groei van het MKB-ERP-segment |

## 4. Kaders, risico's en afspraken

| Onderwerp | Afspraak / maatregel |
|---|---|
| Klanten | **Niet interviewen of enquêteren.** Het klantperspectief komt indirect uit supporttickets, projectdossiers/mail en sales/accountmanagers. Benoem dit als beperking in betrouwbaarheid en validiteit. |
| Rolconflict en objectiviteit | Koen onderzoekt zijn eigen team ("lastig maar te doen"). Maatregelen: anonimiteit in interviews, focus op het proces en niet op personen, triangulatie, member checking en peer debriefing met de bedrijfsbegeleider. Reflectie op de eigen rol is input voor het reflectieverslag. |
| Draagvlak | Standaardisatie raakt de autonomie van consultants. Betrek ze daarom in de Design-fase (co-design) en de Verify-fase (validatie). Het implementatieplan gebruikt een verandermodel. |
| AI en klantdata | Klantgegevens gaan niet zonder toestemming in externe AI-tools. Toets elke AI-toepassing aan het (eventuele) AI-/privacybeleid van JIS en aan de AVG. Beoordeel de toepassing met geanonimiseerde of interne informatie. |
| Weinig cases | Minder dan 5 volledige implementaties per jaar. Omdat add-ons en kleinere uitbreidingen binnen de scope vallen, stijgt het aantal cases. Vul aan met de supportstroom als bron. De analyse is vooral kwalitatief, met beschrijvende statistiek waar de data het toelaat. |
| Datakwaliteit | Het is nog niet zeker dat uren per project (en per fase) tegenover een budget worden geregistreerd. Controleer dit in de quickscan; als het ontbreekt, reconstrueer het uit offertes en facturen en benoem de beperking. |
| Haalbaarheid | 18 weken; minder dan 8 uur per week eigen tijd plus deels werktijd. Beheersing: de invoering valt erbuiten, Verify is een validatie (geen pilot), AI is één deelvraag (4b) en het onderzoek gebruikt bestaande data. |
| Bedrijfsbegeleider | Directeur/eigenaar en/of een senior consultant. **Nog niet besproken.** Eisen (H11): hbo/wo-denkniveau, (potentieel) leidinggevende, kennis van de organisatie en minimaal 2 uur per week. Het formulier adviseert te spreken met de begeleider **én** de probleemeigenaar (de directeur). |
| Sales | Sales heeft een eigen belang in de begroting. Neem sales mee als stakeholder. De overdracht van sales naar consultant valt binnen het proces, het verkoopproces zelf niet. |
| Planning | Het voorstel moet **zo snel mogelijk** worden ingediend, uiterlijk in week 4 van het kwartiel vóór de start. De uitvoering mag weken tot maanden later starten. **Geen interviews of metingen vóór de GO op het onderzoeksplan.** |
| Vertrouwelijkheid | De repo is privé. Gebruik in repo-documenten geen klantnamen (Klant A, B, …). Vraag JIS of het onderzoek vertrouwelijk moet zijn (§4.3/§8.4). |
| AI-gebruik bij het schrijven | Toegestaan, mits verantwoord volgens §8.3 (in de tekst en in de bronnenlijst). Houd een logboek bij. |

## 5. Wat `/build` moet opleveren

### Bestanden
| Bestand | Inhoud |
|---|---|
| `afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.md` | Het ingevulde **Formulier Onderzoeksvoorstel TBK**, met dezelfde volgorde en kopjes als `schooldocumenten/Formulier Voorstel Afstudeeronderzoek TBK - 2021-2022.md`: 1 Gegevens student · 2 Gegevens bedrijf en bedrijfsbegeleider (inclusief persoonlijke relatie = ja, aantal medewerkers = 16, onderzoeksgebied en technische omgeving) · 3a Probleemstelling (langs de 6W, zie §2) · 3b Opdrachtomschrijving (multidisciplinair, innovatief, niveau en technische omgeving expliciet aangetoond, zie §1) · 3c Doelstelling, onderzoeksvraag en deelvragen (extern en intern doel gescheiden) · 3d Onderzoeksontwerp (DMADV-tabel, kernbronnen, aanpak voor betrouwbaarheid en validiteit, haalbaarheid in 18 weken). Velden die alleen Koen kan invullen (studentnummer, telefoon, adressen, naam begeleider, einddatum, cijfers uit de quickscan) worden `[INVULLEN: …]`. Lopende tekst op hbo-niveau, met APA-verwijzingen waar literatuur wordt genoemd. |
| `afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.docx` | Dezelfde inhoud in het **originele Word-formulier**: de kopie van de `.docx` uit `schooldocumenten/` wordt ingevuld, dus niet zelf opgemaakt. Dit is het in te dienen bestand. |
| `afstuderen/01-onderzoeksvoorstel/checklist-eisen.md` | Tabel: elke eis uit handleiding §3.2, §4.1 en §5.1 (a–e) **en** de toetsvragen uit het formulier (technische omgeving, procesoptimalisatie of -ontwerp, multidisciplinair, innovatief, niveau, complexiteit, uitvoerbaarheid, min. 15 medewerkers, 2 uur begeleiding) → waar in het voorstel die wordt aangetoond → status (✅ / ⚠️ open). |
| `afstuderen/01-onderzoeksvoorstel/quickscan-data.md` | Een sjabloon voor het vooronderzoek: een tabel per afgerond project (type, begrote en bestede uren, geplande en werkelijke go-live, tickets in de eerste 3 maanden na go-live), plus aantekeningen over de datakwaliteit. Wordt door Koen ingevuld en voedt 3a. |
| `afstuderen/01-onderzoeksvoorstel/gesprek-opdrachtgever.md` | Een korte agenda en vragenlijst voor het gesprek met de directeur (probleemeigenaar) en de beoogde begeleider: probleem toetsen, rol als bedrijfsbegeleider (eisen H11), toegang tot data, beleid rond AI en privacy, vertrouwelijkheid, verwachtingen (implementatie valt buiten het afstuderen). |
| `afstuderen/README.md` | Index van de afstudeermap plus de status-checklist (welke stap, welke deadline). |
| `README.md` (root) | De structuurtabel aanvullen met `afstuderen/`. |

### Buiten scope
- Het onderzoeksplan (dat komt na de GO op het voorstel), de literatuurstudie in de volle breedte, de formele dataverzameling en interviews.
- **De daadwerkelijke invoering of pilot van de methode.** Het afstuderen levert een gevalideerd ontwerp en een implementatieplan op.
- Het Jeeves-team en het verkoopproces van sales (alleen de overdracht van sales naar consultant valt binnen de scope).
- Klantinterviews of -enquêtes.
- Een los dashboard- of BI-project. KPI's zitten alleen in de methode.
- De dagelijkse support als proces (alleen als databron voor rework).
- Het bouwen of uitrollen van een eigen AI-tool. Het onderzoek selecteert en ontwerpt AI-toepassingen binnen de methode.
- Het indienen in Brightspace: dat doet Koen zelf.

## 6. Open acties voor Koen (vóór indienen)
1. Het idee bespreken met de directeur (probleemeigenaar) en de beoogde bedrijfsbegeleider, met `gesprek-opdrachtgever.md`. Het formulier adviseert minimaal twee vertegenwoordigers van JIS.
2. De quickscan invullen (`quickscan-data.md`) en de cijfers in 3a verwerken.
3. In Brightspace de exacte deadline controleren (week 4 van het kwartiel vóór de start) en kijken of er een nieuwere versie van het formulier is dan die van 2021-2022.
4. **Bewijs dat Koen aan de toelatingseisen voldoet** klaarzetten: dit moet samen met het voorstel worden ingeleverd (handleiding H2).
5. De `[INVULLEN: …]`-velden aanvullen.

## 7. End-to-end verificatie
`/build` is pas klaar als al deze punten aantoonbaar kloppen (laat de output zien):
1. `pandoc afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.docx -t plain` draait zonder fouten. De output bevat alle kopjes van het originele formulier (1, 2, 3a–3d), en bij 3a–3d staat geen lege of placeholdertekst behalve de expliciete `[INVULLEN: …]`-velden.
2. Een diff van de kopjesstructuur van het originele formulier en het ingevulde `.docx` toont geen verwijderde of hernoemde secties.
3. In `checklist-eisen.md` staat elke eis uit §3.2, §4.1, §5.1 (a–e) en elke toetsvraag uit het formulier met een verwijzing naar een concrete sectie. Alle inhoudelijke eisen zijn ✅; alleen acties van Koen (begeleider, deadline, quickscan, toelatingsbewijs) mogen ⚠️ zijn.
4. De hoofdvraag, het interne doel en de 5 deelvragen (met 4b) in `.md` en `.docx` zijn letterlijk gelijk (controle met een script). Elke deelvraag is aan een DMADV-fase gekoppeld, en de kernwoorden van het doel komen terug in de hoofdvraag.
5. In de tekst van 3a/3b komen de termen "technische omgeving", "multidisciplinair", "innovatief" en "tactisch/operationeel" aantoonbaar voor (controle met grep), elk met een onderbouwing.
6. Een woordtelling van 3a–3d in het `.docx` toont dat het voorstel compact blijft (richtlijn: maximaal ca. 2 A4 voor onderdeel 3).
7. `git status` is schoon en alles is gepusht naar `main`.
