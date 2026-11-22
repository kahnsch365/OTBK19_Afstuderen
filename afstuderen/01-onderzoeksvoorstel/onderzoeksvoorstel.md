# Onderzoeksvoorstel afstuderen TBK – JIS Nederland

> **Concept.** Dit bestand is de bron van de tekst in `onderzoeksvoorstel.docx` (het ingevulde originele formulier).
> Pas de tekst hier aan en genereer de `.docx` opnieuw met `python3 tools/vul_formulier.py`. Vul alle
> `[INVULLEN: …]`-velden in vóór het indienen. Structuur en kopjes volgen het *Formulier Onderzoeksvoorstel
> Technische Bedrijfskunde deeltijd*.

**Datum:** [INVULLEN: datum van indienen]

## 1. Gegevens student

| Veld | Invulling |
|---|---|
| Naam student & studentnummer | Koen [INVULLEN: achternaam], [INVULLEN: studentnummer] |
| Telefoonnummer | [INVULLEN: telefoonnummer] |
| Opleiding | SPS TBK Enschede |
| Afstudeerperiode | van: [INVULLEN: startdatum] t/m: [INVULLEN: einddatum] |
| Propedeuse behaald | ja |
| Max. 20 studiepunten openstaan | [INVULLEN: ja / nee, controleren in het studievoortgangsoverzicht] |
| Openstaande vakken | [INVULLEN: openstaande vakken en verwachte resultaatdatum, of "geen"] |

## 2. Gegevens bedrijf en bedrijfsbegeleider

| Veld | Invulling |
|---|---|
| Naam bedrijf | JIS Nederland |
| Naam opdrachtgever | [INVULLEN: naam], directeur/eigenaar JIS Nederland |
| Bedrijfssoort/sector | ICT-dienstverlening: verkoop en implementatie van ERP-systemen (Jeeves ERP, SAP Business One) en CRM (SuperOffice) |
| Aantal medewerkers | 16 |
| (Bezoek)adres | [INVULLEN: adres] |
| Postcode | [INVULLEN: postcode] |
| Plaats | [INVULLEN: plaats] |
| Land | Nederland |
| Alg. telefoonnummer | [INVULLEN: telefoonnummer] |
| Homepage | [INVULLEN: website] |
| Alg. e-mail | [INVULLEN: algemeen e-mailadres] |
| Postbusnr | [INVULLEN: postbus, of "n.v.t."] |
| Postcode postbus | [INVULLEN: postcode, of "n.v.t."] |
| Persoonlijke relatie | Ja, nl: de student werkt sinds oktober 2024 als consultant SAP Business One in het onderzochte team (zie 3d voor de maatregelen voor objectiviteit). |
| Naam bedrijfsbegeleider | [INVULLEN: achternaam] (M / V: [INVULLEN]) |
| Voorletters | [INVULLEN: voorletters] |
| Roepnaam | [INVULLEN: roepnaam] |
| Afdeling | [INVULLEN: afdeling, bv. directie of SAP Business One-team] |
| Functie en opleidingsniveau | [INVULLEN: functie, bv. directeur/eigenaar of senior consultant; opleidingsniveau hbo/wo] |
| Tijd voor begeleiding (min. 2 uur per week) | [INVULLEN: ja / nee] |
| Telefoonnr. begeleider | [INVULLEN: telefoonnummer] |
| Mobiel begeleider | [INVULLEN: mobiel nummer] |
| E-mailadres begeleider | [INVULLEN: e-mailadres] |

### Organisatie

**Onderzoeksgebied.** JIS Nederland verkoopt en implementeert ERP-systemen en heeft twee ERP-teams: Jeeves ERP en
SAP Business One. Daarnaast verkoopt JIS sinds kort het CRM-systeem SuperOffice, als aparte productlijn. Het
onderzoek richt zich op het SAP Business One-team (6 consultants) en het projectproces dat dit team uitvoert: van de overdracht door sales, via vooranalyse, inrichting, datamigratie, testen en go-live, tot de
overdracht naar nazorg. Directie, sales en support zijn betrokken als stakeholders. Het Jeeves-team, SuperOffice
en het verkoopproces vallen buiten het onderzoek. Een organogram met het onderzoeksgebied is opgenomen in bijlage 1.

**Technische omgeving.** Een ERP-systeem is een technisch informatiesysteem waarin de primaire processen van een
bedrijf worden ingericht: inkoop, voorraad, productie, verkoop en financiën. De klanten van JIS zijn vooral productie-
en handelsbedrijven. Het onderzochte proces is het implementatieproces zelf: een technisch-bedrijfskundig projectproces
waarin systeemconfiguratie, datamigratie, koppelingen, testen en het inrichten van de logistieke en productieprocessen
van de klant samenkomen. De opdracht wordt daarmee uitgevoerd in de context van een technische omgeving.

## 3. De opdracht / het uit te voeren onderzoek

### 3a. Probleemstelling

Het SAP Business One-team van JIS Nederland voert alle klantprojecten voor dit ERP-pakket uit: volledige
implementaties, add-ons en kleinere uitbreidingen (zie onderdeel 2). De probleemstelling langs de 6W (Leen & Mertens,
2017):

**Wat is het probleem?** Het SAP Business One-team heeft geen gestandaardiseerd projectproces. Iedere consultant werkt
op een eigen manier, zonder vaste fasen, deliverables, overdrachtsmomenten of vaste vastlegging van inrichtingskeuzes en
klantafspraken. Projectkennis zit daardoor vooral in de hoofden van consultants.

**Wat is de aanleiding?** Het team is in korte tijd gegroeid van 1 naar 6 consultants. Tegelijk worden urenoverschrijdingen,
uitgestelde go-lives en rework na go-live gesignaleerd. De omvang daarvan is nog niet gemeten; dat gebeurt in de
Measure-fase van het onderzoek.

**Wie heeft het probleem?** De directie is probleemeigenaar: zij is verantwoordelijk voor rendement en groei. De
consultants hebben last van rework en lastige overdrachten, sales van begrotingen die niet kloppen en support van
meldingen na go-live. Klanten merken het indirect, via uitstel en fouten.

**Wanneer is het ontstaan?** Met de groei van het team. Wat met één consultant informeel werkte, werkt met zes
consultants en meer parallelle projecten niet meer.

**Waarom is het een probleem?** Overschrijdingen leveren niet-factureerbare uren op. Daarnaast nemen de voorspelbaarheid
en de klanttevredenheid af, is het team kwetsbaar bij uitval of overdracht van een consultant, en remt dit de verdere
groei van het team.

**Waar doet het probleem zich voor?** In het projectproces van het SAP Business One-team: van de overdracht door sales,
via vooranalyse, inrichting en testen, tot go-live en de overdracht naar nazorg.

Het is daarmee een procesvraagstuk in een technische omgeving, met het (her)ontwerpen van een projectproces als kern.

### 3b. Opdrachtomschrijving

**Werktitel.** *Van ieder z'n eigen aanpak naar een standaard projectproces: ontwerp van een schaalbare,
AI-ondersteunde implementatiemethode voor het SAP Business One-team van JIS Nederland.*

De opdracht is het ontwerpen van een gestandaardiseerde, schaalbare projectmethode voor het SAP Business One-team. De
methode bestaat uit:

- één kernproces met vaste fasen, deliverables, templates/checklists en overdrachtsmomenten;
- een lichte variant voor add-ons en kleine uitbreidingen, met een projectclassificatie die per projecttype bepaalt welke
  deliverables verplicht zijn;
- 3–5 stuur-KPI's (uren t.o.v. budget, go-live t.o.v. planning, rework na go-live);
- ten minste één AI-toepassing die vastlegging, kennisborging en overdracht ondersteunt.

Het resultaat is een gevalideerd ontwerp met kosten-batenanalyse en implementatieplan: een aanzet tot implementatie.
De invoering zelf valt buiten de afstudeerperiode. Ook buiten de scope vallen het Jeeves-team, het verkoopproces
(behalve de overdracht naar de consultant), support als proces (alleen databron) en het bouwen van een eigen AI-tool.

De opdracht is **multidisciplinair**. Ze combineert procesmanagement (procesontwerp, standaardisatie, KPI's),
projectmanagement (fasering, begroting, ERP-implementatiemethoden), kennismanagement (borging en overdracht van
klantkennis), technologie en innovatie (ERP en AI in het kenniswerk van consultants) en mensen in organisaties
(draagvlak, weerstand en verandering: standaardisatie raakt de professionele autonomie van consultants).

De opdracht is **innovatief**: JIS heeft nog geen projectmethode, de methode schaalt mee met het projecttype en zet
generatieve AI in bij het kenniswerk van consultants, met de AVG en de vertrouwelijkheid van klantdata als harde
randvoorwaarde.

De opdracht is **tactisch/operationeel** van aard. Ze gaat over de inrichting en besturing van het primaire
projectproces: hoe projecten worden uitgevoerd, overgedragen en gestuurd. Er is een strategisch raakvlak: de methode
moet het team in staat stellen te groeien zonder kwaliteitsverlies.

De **technische omgeving** is de implementatie van ERP-systemen, waarin de logistieke, productie- en financiële
processen van klanten worden ingericht (zie onderdeel 2, Organisatie).

### 3c. Doelstelling, onderzoeksvraag en deelvragen

**Doel van het bedrijf (extern doel).** De voorspelbaarheid en kwaliteit van SAP Business One-projecten verbeteren,
met minder urenoverschrijding, minder uitstel van go-live en minder rework na go-live, zodat het team kan groeien zonder
kwaliteitsverlies.

**Onderzoeksdoel (intern doel).** Het uitvoeren van een ontwerpgericht onderzoek in opdracht van de directie van JIS
Nederland, om binnen de afstudeerperiode van 18 weken (uiterlijk [INVULLEN: einddatum]) een gestandaardiseerde,
schaalbare en door AI ondersteunde projectmethode voor implementaties en add-ons van het SAP Business One-team te
ontwerpen en te valideren. De methode bestaat uit een
kernproces met een lichte variant voor add-ons, vaste deliverables voor vastlegging en overdracht, 3–5 stuur-KPI's met
streefwaarden en ten minste één uitgewerkte AI-toepassing. Het ontwerp wordt opgeleverd als adviesrapport met
kosten-batenanalyse en implementatieplan, zodat JIS de uren- en planningsoverschrijdingen en het rework na go-live
structureel kan terugdringen. De streefwaarden van de KPI's volgen uit de nulmeting in de Measure-fase.

**Hoofdvraag.** Hoe moet een gestandaardiseerde, schaalbare en door AI ondersteunde projectmethode voor implementaties
en add-ons van het SAP Business One-team van JIS Nederland eruitzien, zodat de uren- en planningsoverschrijdingen en
het rework na go-live afnemen, en hoe kan deze vóór [INVULLEN: einddatum] als gevalideerd ontwerp met implementatieplan
worden opgeleverd?

**Deelvragen.** Elke deelvraag hoort bij een fase van DMADV en bouwt voort op de vorige.

**1. (Define)** Hoe verloopt het projectproces nu per projecttype (volledige implementatie, add-on, kleine uitbreiding), van de overdracht door sales tot de overdracht naar nazorg, en welke stakeholders en belangen spelen daarbij een rol?

**2. (Measure)** Waaraan moet een standaardmethode volgens de stakeholders voldoen (CTQ's), en hoe presteert het huidige proces op uren t.o.v. budget, go-live t.o.v. planning en rework na go-live?

**3. (Analyze)** Welke procesoorzaken verklaren de afwijkingen, en welke ontwerpalternatieven (bv. SAP Activate-light, faseringsmodellen, checklistgedreven werken) passen bij de eisen?

**4. (Design)** Hoe ziet de methode eruit: het kernproces, de lichte variant, de deliverables, de templates, de KPI's met streefwaarden en de rolverdeling tussen sales en consultant?

**4b. (Design)** Welke AI-toepassingen ondersteunen de vastlegging, kennisborging en overdracht binnen de methode, binnen de randvoorwaarden van de AVG en het beleid van JIS?

**5. (Verify)** In hoeverre voldoet het ontwerp aan de eisen (CTQ's) en wordt het door de stakeholders gedragen, en wat zijn de kosten, de baten en de stappen voor invoering?

Het vraagstuk vraagt om bedrijfskundig onderzoek: het probleem is nog niet in kaart gebracht en er is geen
standaardoplossing (bestaande methoden zoals SAP Activate zijn bedoeld voor grotere projecten en teams). Een passende
methode vraagt een systematische analyse van data en interviews, een afweging van alternatieven en vakliteratuur uit
meerdere vakgebieden.

### 3d. Onderzoeksontwerp

**Type onderzoek en procesmodel.** Het onderzoek is een ontwerpgericht praktijkonderzoek (Leen & Mertens, 2017),
gestructureerd met DMADV uit Design for Six Sigma (Yang & El-Haik, 2009). DMADV past beter dan DMAIC, omdat er geen
bestaand standaardproces is om te verbeteren. Er moet een nieuw proces worden ontworpen. Measure legt de eisen (CTQ's)
en de nulmeting vast, Analyze de oorzaken en ontwerpalternatieven, en Verify valideert het ontwerp.

| Deelvraag (fase) | Dataverzameling | Analyse | Resultaat |
|---|---|---|---|
| 1 (Define) | Semigestructureerde interviews met consultants, directie, sales en support; projectdossiers | Procesmapping per projecttype (swimlane, brown paper); macht-belangmatrix | Huidig procesmodel, stakeholderanalyse en afbakening |
| 2 (Measure) | Interviews (eisen); bestaande data: urenregistratie, budgetten en planning, supporttickets na go-live | CTQ-boom; beschrijvende statistiek per projecttype | Eisenlijst (CTQ's) en nulmeting van de KPI's |
| 3 (Analyze) | Data en interviews uit 1–2; dossiers en mail; literatuur over ERP-implementatiemethoden | Visgraatdiagram, Pareto, triangulatie; afwegingsmatrix van alternatieven tegen de CTQ's | Oorzakenanalyse en gekozen ontwerprichting |
| 4 (Design) | Literatuur; co-design-sessie(s) met consultants | Procesontwerp in BPMN (Dumas et al., 2018); SECI-model voor kennisborging (Nonaka & Takeuchi, 1995) | Procesontwerp, templates/checklists, KPI-set met streefwaarden |
| 4b (Design) | Literatuur over AI in kenniswerk; inventarisatie van tools en het beleid van JIS | Afwegingsmatrix (nut, risico, kosten); TAM (Davis, 1989); toets aan de AVG | Uitgewerkte AI-toepassing(en) met randvoorwaarden |
| 5 (Verify) | Validatiesessie met consultants en directie; droogtest op een afgerond project; AI-test met een geanonimiseerd voorbeeld | Toets aan de CTQ's (member check); kosten-batenanalyse; verandermodel (Kotter, 1996) | Gevalideerd ontwerp, kosten-batenanalyse en implementatieplan |

**Betrouwbaarheid en validiteit.** Omdat de student het eigen team onderzoekt, worden interviews anoniem verwerkt en
ligt de focus op het proces, niet op personen. Bevindingen worden getrianguleerd (data, interviews en dossiers), via
member checks voorgelegd aan de geïnterviewden en besproken met de bedrijfsbegeleider (peer debriefing). Een
interviewprotocol en een onderzoekslogboek maken het onderzoek herhaalbaar. Beperkingen: klanten worden niet
geïnterviewd (hun perspectief komt uit supporttickets, dossiers en sales) en het aantal volledige implementaties is
klein. Add-ons en kleine uitbreidingen vergroten het aantal cases; de analyse is vooral kwalitatief. Klantgegevens gaan
niet zonder toestemming in externe AI-tools.

**Haalbaarheid in 18 weken.** Eén student voert het onderzoek uit, deels in werktijd, met bestaande data, interne
bronnen en één kernproduct. De invoering valt erbuiten, Verify is een validatie (geen pilot) en AI is één afgebakende
deelvraag (4b). Globale fasering: week 1–3 onderzoeksplan; week 3–5
Define; week 5–7 Measure; week 7–9 Analyze; week 9–12 Design; week 12–14 Verify, kosten-baten en implementatieplan;
week 15 overzicht beroepsproducten; week 15–18 adviesrapport, portfolio en reflectieverslag.

#### Bronnen

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). *Fundamentals of business process management* (2nd ed.). Springer.

Kotter, J. P. (1996). *Leading change*. Harvard Business School Press.

Leen, J., & Mertens, J. (2017). *Praktijkgericht onderzoek in bedrijf* (2e druk). Coutinho.

Nonaka, I., & Takeuchi, H. (1995). *The knowledge-creating company: How Japanese companies create the dynamics of innovation*. Oxford University Press.

Yang, K., & El-Haik, B. (2009). *Design for Six Sigma: A roadmap for product development* (2nd ed.). McGraw-Hill.

#### Verantwoording AI-gebruik

Bij het structureren en formuleren van dit voorstel is generatieve AI gebruikt (Claude; Anthropic, 2026). De student
heeft de inhoud gecontroleerd, aangevuld en is verantwoordelijk voor de tekst. Gebruik van AI wordt in een logboek
bijgehouden.

Anthropic. (2026). *Claude* [Groot taalmodel]. https://claude.ai

## Bijlage 1 – Organogram JIS Nederland

![Organogram JIS Nederland](bijlage-organogram.png)
