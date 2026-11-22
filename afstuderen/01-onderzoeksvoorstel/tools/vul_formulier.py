#!/usr/bin/env python3
"""Vult het originele Saxion-formulier in met de tekst uit onderzoeksvoorstel.md.

Gebruik (vanuit de repo-root of vanuit deze map):
    python3 afstuderen/01-onderzoeksvoorstel/tools/vul_formulier.py

- Bron:   schooldocumenten/Formulier Voorstel Afstudeeronderzoek TBK - 2021-2022.docx (wordt niet gewijzigd)
- Tekst:  afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.md
- Uitvoer: afstuderen/01-onderzoeksvoorstel/onderzoeksvoorstel.docx

Kopjes en instructieteksten van het formulier blijven staan; de antwoorden komen direct
na de instructie van elk onderdeel. Pas de tekst dus aan in de .md en draai dit script opnieuw.
Vereist: python-docx (pip install python-docx).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm

MAP = Path(__file__).resolve().parent.parent
ROOT = MAP.parents[1]
BRON = ROOT / "schooldocumenten" / "Formulier Voorstel Afstudeeronderzoek TBK - 2021-2022.docx"
MD = MAP / "onderzoeksvoorstel.md"
UIT = MAP / "onderzoeksvoorstel.docx"

FONT = "Verdana"
SZ_TEKST = 18  # halve punten: 9 pt, zoals de invulvelden van het formulier
SZ_TABEL = 16  # 8 pt in de tabel van het onderzoeksontwerp

# Tabel 0: label in de .md -> (rij, kolom) van de invulcel in het formulier
CELLEN = {
    "Naam student & studentnummer": (1, 1),
    "Telefoonnummer": (2, 1),
    "Naam bedrijf": (6, 1),
    "Naam opdrachtgever": (7, 1),
    "Bedrijfssoort/sector": (8, 1),
    "Aantal medewerkers": (8, 8),
    "(Bezoek)adres": (9, 1),
    "Postcode": (10, 1),
    "Plaats": (10, 4),
    "Land": (11, 1),
    "Alg. telefoonnummer": (12, 1),
    "Homepage": (13, 1),
    "Alg. e-mail": (13, 6),
    "Postbusnr": (14, 1),
    "Postcode postbus": (14, 4),
    "Naam bedrijfsbegeleider": (18, 1),
    "Voorletters": (18, 7),
    "Roepnaam": (19, 1),
    "Afdeling": (20, 1),
    "Functie en opleidingsniveau": (21, 1),
    "Telefoonnr. begeleider": (22, 1),
    "Mobiel begeleider": (22, 5),
    "E-mailadres begeleider": (23, 1),
}
# Tabel 0, rij 4 (studievoortgang): label -> (paragraafindex, vast voorvoegsel)
STUDIEVOORTGANG = {
    "Afstudeerperiode": (2, ""),
    "Propedeuse behaald": (7, "Propedeuse behaald: "),
    "Max. 20 studiepunten openstaan": (8, "Max. 20 studiepunten openstaan: "),
    "Openstaande vakken": (9, "Openstaande vakken: "),
}


# ---------------------------------------------------------------- markdown lezen
def lees_md(tekst: str) -> tuple[dict[str, str], dict[str, str], str]:
    """Geeft (velden uit de tabellen van 1 en 2, secties op kopje, datum)."""
    velden: dict[str, str] = {}
    secties: dict[str, list[str]] = {}
    huidig = None
    for regel in tekst.splitlines():
        kop = re.match(r"^(#{2,3}) (.+)$", regel)
        if kop:
            huidig = kop.group(2).strip()
            secties[huidig] = []
            continue
        if huidig is not None:
            secties[huidig].append(regel)
        if huidig and huidig[0] in "12" and regel.startswith("|"):
            cellen = [c.strip() for c in regel.strip("|").split("|")]
            if len(cellen) == 2 and cellen[0] not in ("Veld",) and not set(cellen[0]) <= set("-: "):
                velden[cellen[0]] = cellen[1]
    datum = re.search(r"^\*\*Datum:\*\* (.+)$", tekst, re.M)
    return velden, {k: "\n".join(v).strip() for k, v in secties.items()}, datum.group(1).strip() if datum else ""


def blokken(tekst: str) -> list[tuple[str, object]]:
    """Splitst een sectie in blokken: para, kop4, bullet, tabel."""
    uit: list[tuple[str, object]] = []
    regels = tekst.splitlines()
    i = 0
    while i < len(regels):
        r = regels[i]
        if not r.strip():
            i += 1
        elif r.startswith("|"):
            rijen = []
            while i < len(regels) and regels[i].startswith("|"):
                cellen = [c.strip() for c in regels[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cellen):
                    rijen.append(cellen)
                i += 1
            uit.append(("tabel", rijen))
        elif r.startswith("#### "):
            uit.append(("kop4", r[5:].strip()))
            i += 1
        elif r.startswith("- "):
            delen = [r[2:].strip()]
            i += 1
            while i < len(regels) and regels[i].startswith("  ") and regels[i].strip():
                delen.append(regels[i].strip())
                i += 1
            uit.append(("bullet", " ".join(delen)))
        else:
            delen = []
            while i < len(regels) and regels[i].strip() and not regels[i].startswith(("|", "- ", "#### ")):
                delen.append(regels[i].strip())
                i += 1
            uit.append(("para", " ".join(delen)))
    return uit


def inline(tekst: str) -> list[tuple[str, bool, bool]]:
    """**vet** en *cursief* -> lijst van (tekst, vet, cursief)."""
    stukken = []
    for deel in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", tekst):
        if not deel:
            continue
        if deel.startswith("**"):
            stukken.append((deel[2:-2], True, False))
        elif deel.startswith("*") and deel.endswith("*") and len(deel) > 1:
            stukken.append((deel[1:-1], False, True))
        else:
            stukken.append((deel.replace("`", ""), False, False))
    return stukken


def platte_tekst(tekst: str) -> str:
    return "".join(t for t, _, _ in inline(tekst))


# ---------------------------------------------------------------- docx-hulpjes
def rpr(vet=False, cursief=False, sz=SZ_TEKST):
    r = OxmlElement("w:rPr")
    f = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        f.set(qn(a), FONT)
    r.append(f)
    if vet:
        r.append(OxmlElement("w:b"))
    if cursief:
        r.append(OxmlElement("w:i"))
    for tag in ("w:sz", "w:szCs"):
        e = OxmlElement(tag)
        e.set(qn("w:val"), str(sz))
        r.append(e)
    return r


def maak_run(tekst, vet=False, cursief=False, sz=SZ_TEKST):
    r = OxmlElement("w:r")
    r.append(rpr(vet, cursief, sz))
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = tekst
    r.append(t)
    return r


def maak_p(md_tekst="", sz=SZ_TEKST, na=80, inspring=None, voor="", alles_vet=False):
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0")
    sp.set(qn("w:after"), str(na))
    sp.set(qn("w:line"), "264")
    sp.set(qn("w:lineRule"), "auto")
    ppr.append(sp)
    if inspring:
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), str(inspring))
        ind.set(qn("w:hanging"), str(inspring))
        ppr.append(ind)
    ppr.append(rpr(sz=sz))
    p.append(ppr)
    if voor:
        p.append(maak_run(voor, sz=sz))
    for tekst, vet, cursief in inline(md_tekst):
        p.append(maak_run(tekst, vet or alles_vet, cursief, sz))
    return p


def zet_tekst(paragraaf, tekst, vet=False):
    """Vervangt alle runs van een bestaande paragraaf door één run (opmaak paragraaf blijft)."""
    for r in list(paragraaf._p):
        if r.tag != qn("w:pPr"):
            paragraaf._p.remove(r)
    paragraaf._p.append(maak_run(tekst, vet=vet))


def vink_aan(paragraaf):
    cb = paragraaf._p.find(".//" + qn("w:checkBox"))
    if cb is None:
        raise SystemExit(f"Geen selectievakje in: {paragraaf.text!r}")
    cb.find(qn("w:default")).set(qn("w:val"), "1")
    if cb.find(qn("w:checked")) is None:
        cb.append(OxmlElement("w:checked"))


def tabel_element(cel, rijen):
    """Maakt een tabel (rand, kopregel grijs) en geeft het w:tbl-element terug."""
    tabel = cel.add_table(rows=len(rijen), cols=len(rijen[0]))
    # python-docx voegt na de tabel een lege paragraaf toe; die halen we weg
    nakomer = tabel._tbl.getnext()
    if nakomer is not None and nakomer.tag == qn("w:p"):
        nakomer.getparent().remove(nakomer)
    tblpr = tabel._tbl.tblPr
    randen = OxmlElement("w:tblBorders")
    for kant in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{kant}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "808080")
        randen.append(e)
    tblpr.append(randen)
    breedtes = [Cm(2.0), Cm(5.4), Cm(5.4), Cm(4.0)][: len(rijen[0])]
    for ri, rij in enumerate(rijen):
        for ci, waarde in enumerate(rij):
            c = tabel.cell(ri, ci)
            c.width = breedtes[ci]
            tc = c._tc
            for p in list(tc.findall(qn("w:p"))):
                tc.remove(p)
            tc.append(maak_p(waarde, sz=SZ_TABEL, na=0, alles_vet=(ri == 0)))
            if ri == 0:
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), "D9D9D9")
                tc.get_or_add_tcPr().append(shd)
    return tabel._tbl


def schrijf_blokken(cel, anker, tekst):
    """Zet de blokken van een sectie direct na het anker-element in de cel."""
    huidig = anker
    for soort, inhoud in blokken(tekst):
        if soort == "tabel":
            nieuw = tabel_element(cel, inhoud)
            nieuw.getparent().remove(nieuw)
            huidig.addnext(nieuw)
            huidig = nieuw
            nieuw = maak_p("", na=0)  # witregel na tabel
        elif soort == "kop4":
            nieuw = maak_p(inhoud, alles_vet=True, na=40)
        elif soort == "bullet":
            nieuw = maak_p(inhoud, inspring=284, voor="•\t", na=40)
        else:
            nieuw = maak_p(inhoud)
        huidig.addnext(nieuw)
        huidig = nieuw
    leeg = maak_p("", na=0)
    huidig.addnext(leeg)
    return leeg


def is_leeg(p_el):
    return p_el.tag == qn("w:p") and not "".join(t.text or "" for t in p_el.iter(qn("w:t"))).strip()


def verwijder_lege_na(anker, tot=None):
    """Verwijdert lege paragrafen direct na het anker tot het volgende niet-lege element."""
    e = anker.getnext()
    while e is not None and e is not tot and is_leeg(e):
        volgende = e.getnext()
        e.getparent().remove(e)
        e = volgende


def sectie(secties, begin):
    for kop, tekst in secties.items():
        if kop.startswith(begin):
            return tekst
    raise SystemExit(f"Sectie '{begin}' niet gevonden in {MD.name}")


# ---------------------------------------------------------------- invullen
def main() -> None:
    velden, secties, datum = lees_md(MD.read_text(encoding="utf-8"))
    nodig = [*CELLEN, *STUDIEVOORTGANG, "Opleiding", "Persoonlijke relatie",
             "Tijd voor begeleiding (min. 2 uur per week)"]
    ontbrekend = [label for label in nodig if label not in velden]
    if ontbrekend:
        raise SystemExit(f"Velden ontbreken in {MD.name}: {', '.join(ontbrekend)}")
    doc = Document(str(BRON))
    t0, t1 = doc.tables

    # Datum
    for p in doc.paragraphs:
        if p.text.strip() == "Datum:" and datum:
            p._p.append(maak_run(" " + datum))
            break

    # Tabel 0: gewone invulcellen
    for label, (r, c) in CELLEN.items():
        cel = t0.cell(r, c)
        zet_tekst(cel.paragraphs[0], velden[label])
        if label != "Functie en opleidingsniveau":  # die cel bevat ook de afspraak over begeleidingstijd
            for p in cel.paragraphs[1:]:  # overbodige lege regels in de cel
                if not p.text.strip():
                    p._p.getparent().remove(p._p)

    # Studievoortgang
    cel = t0.cell(4, 1)
    for label, (idx, voorvoegsel) in STUDIEVOORTGANG.items():
        zet_tekst(cel.paragraphs[idx], voorvoegsel + velden[label])

    # Opleiding: selectievakje
    for p in t0.cell(3, 1).paragraphs:
        if p.text.strip() == velden["Opleiding"]:
            vink_aan(p)
            break
    else:
        raise SystemExit("Opleiding niet gevonden bij de selectievakjes")

    # Persoonlijke relatie
    relatie = velden["Persoonlijke relatie"]
    for p in t0.cell(15, 1).paragraphs:
        if relatie.startswith("Ja") and "Ja, nl:" in p.text:
            vink_aan(p)
            for t in p._p.iter(qn("w:t")):
                if "Ja, nl:" in (t.text or ""):
                    t.text = " " + relatie
            break
        if relatie.startswith("Nee") and p.text.strip() == "Nee":
            vink_aan(p)
            break

    # Tijd voor begeleiding: "ja / nee" vervangen door de waarde
    p = t0.cell(21, 1).paragraphs[2]
    runs = p._p.findall(qn("w:r"))
    for r in runs[1:]:
        p._p.remove(r)
    runs[0].find(qn("w:t")).text = runs[0].find(qn("w:t")).text.rstrip() + "  "
    p._p.append(maak_run(velden["Tijd voor begeleiding (min. 2 uur per week)"]))

    # Organisatie: tekst onder de instructie
    cel = t0.cell(16, 1)
    schrijf_blokken(cel, cel.paragraphs[-1]._p, sectie(secties, "Organisatie"))

    # Onderdeel 3a-3c (tabel 1, rij 1) en 3d (tabel 1, rij 2)
    instructies = {
        "3a": "Deze informatie zal worden gebruikt om te toetsen of voldaan wordt aan de eis",
        "3b": "Deze informatie wordt gebruikt om te beoordelen of voldaan wordt aan de eisen multidisciplinair",
        "3c": "Deze informatie zal worden gebruikt om te toetsen of het onderzoek voldoende complex",
        "3d": "Deze informatie zal worden gebruikt om te toetsen of het onderzoek uitvoerbaar",
    }
    for code, begin in instructies.items():
        cel = t1.cell(2, 0) if code == "3d" else t1.cell(1, 0)
        anker = next((p._p for p in cel.paragraphs if p.text.strip().startswith(begin)), None)
        if anker is None:
            raise SystemExit(f"Instructie van {code} niet gevonden")
        verwijder_lege_na(anker)
        schrijf_blokken(cel, anker, sectie(secties, code + "."))

    doc.save(str(UIT))
    print(f"Geschreven: {UIT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
