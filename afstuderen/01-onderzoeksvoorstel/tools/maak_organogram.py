"""Tekent het organogram van JIS Nederland (bijlage 1 bij het onderzoeksvoorstel).

Gebruik:  python3 afstuderen/01-onderzoeksvoorstel/tools/maak_organogram.py
Uitvoer:  afstuderen/01-onderzoeksvoorstel/bijlage-organogram.png

De bezetting staat in TEAMS en STAF hieronder; pas die aan als de organisatie verandert.
Coördinaten zijn in 'eenheden' (1600 breed = ca. 16 cm in het formulier) en worden
met SCHAAL vergroot voor een scherpe afdruk.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

MAP = Path(__file__).resolve().parent.parent
UIT = MAP / "bijlage-organogram.png"

SCHAAL = 2
B, H = 1600, 1000
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_VET = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_CURSIEF = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"

ZWART = "#1A1A1A"
LIJN = "#555555"
GRIJS_VAK = "#F2F2F2"
GRIJS_RAND = "#8C8C8C"
ACCENT = "#1F5C99"
ACCENT_LICHT = "#E6EEF7"
ACCENT_VAK = "#C9DAEE"

DIRECTEUR = "Directeur / eigenaar"
STAF = "Marketingmedewerker"
TEAMS = [  # (teamnaam, verkoper, aantal consultants, onderzoeksgebied?); verkoper=None: alleen consultants-vak
    ("Team Jeeves ERP", "Verkoper Jeeves", 5, False),
    ("Team SAP Business One", "Verkoper SAP Business One", 6, True),
    ("Team SuperOffice (CRM)", "SuperOffice-medewerker", 0, False),
]


def s(*waarden):
    return [round(w * SCHAAL) for w in waarden]


def font(grootte, soort=FONT):
    return ImageFont.truetype(soort, round(grootte * SCHAAL))


def tekst_midden(d, cx, y, tekst, f, kleur=ZWART):
    """Meerregelige tekst horizontaal gecentreerd rond cx, beginnend op y."""
    regelhoogte = f.size * 1.25 / SCHAAL
    for i, regel in enumerate(tekst.split("\n")):
        breedte = d.textlength(regel, font=f) / SCHAAL
        d.text(s(cx - breedte / 2, y + i * regelhoogte), regel, font=f, fill=kleur)


def vak(d, x1, y1, x2, y2, tekst, f, vulling=GRIJS_VAK, rand=GRIJS_RAND, dikte=2):
    d.rounded_rectangle(s(x1, y1, x2, y2), radius=round(8 * SCHAAL), fill=vulling, outline=rand,
                        width=round(dikte * SCHAAL))
    regels = tekst.count("\n") + 1
    hoogte = regels * f.size * 1.25 / SCHAAL
    tekst_midden(d, (x1 + x2) / 2, (y1 + y2) / 2 - hoogte / 2 + 2, tekst, f)


def lijn(d, *punten, kleur=LIJN, dikte=2.5):
    d.line(s(*punten), fill=kleur, width=round(dikte * SCHAAL))


def stippel_rechthoek(d, x1, y1, x2, y2, kleur, dikte=3, streep=16, gat=10):
    def stippellijn(xa, ya, xb, yb):
        lengte = abs(xb - xa) + abs(yb - ya)
        pos = 0.0
        while pos < lengte:
            eind = min(pos + streep, lengte)
            if xa == xb:
                lijn(d, xa, ya + pos, xb, ya + eind, kleur=kleur, dikte=dikte)
            else:
                lijn(d, xa + pos, ya, xa + eind, yb, kleur=kleur, dikte=dikte)
            pos += streep + gat

    stippellijn(x1, y1, x2, y1)
    stippellijn(x1, y2, x2, y2)
    stippellijn(x1, y1, x1, y2)
    stippellijn(x2, y1, x2, y2)


def poppetjes(d, cx, y, aantal, kleur):
    """Rij eenvoudige persoon-iconen (hoofd + schouders), één per consultant."""
    afstand = 62
    start = cx - (aantal - 1) * afstand / 2
    for i in range(aantal):
        x = start + i * afstand
        d.ellipse(s(x - 11, y - 30, x + 11, y - 8), fill=kleur)
        d.pieslice(s(x - 22, y - 4, x + 22, y + 38), 180, 360, fill=kleur)


def main() -> None:
    img = Image.new("RGB", s(B, H), "white")
    d = ImageDraw.Draw(img)
    f_titel = font(27, FONT_VET)
    f_vak = font(27)
    f_vak_vet = font(27, FONT_VET)
    f_klein = font(22)
    f_klein_cursief = font(22, FONT_CURSIEF)

    midden = B / 2
    # Directeur
    vak(d, midden - 230, 30, midden + 230, 110, DIRECTEUR, f_vak_vet, vulling="white", rand=ZWART, dikte=2.5)

    # Lijnen: directeur -> staf en -> teams
    tak_y, staf_y = 320, 200
    breedte, tussen = 490, 25
    links = (B - len(TEAMS) * breedte - (len(TEAMS) - 1) * tussen) / 2
    teams_x = [links + breedte / 2 + i * (breedte + tussen) for i in range(len(TEAMS))]
    lijn(d, midden, 110, midden, tak_y)
    lijn(d, teams_x[0], tak_y, teams_x[-1], tak_y)

    # Staf (direct onder de directeur)
    lijn(d, midden - 240, staf_y, midden, staf_y)
    vak(d, midden - 680, staf_y - 45, midden - 240, staf_y + 45, STAF, f_vak)

    # Teams
    for cx, (naam, verkoper, aantal, gebied) in zip(teams_x, TEAMS):
        x1, x2, y1 = cx - breedte / 2, cx + breedte / 2, 360
        y2 = 790 if aantal else 560
        lijn(d, cx, tak_y, cx, y1)
        if gebied:
            d.rectangle(s(x1, y1, x2, y2), fill=ACCENT_LICHT)
            stippel_rechthoek(d, x1, y1, x2, y2, ACCENT, dikte=3.5)
            label = "Onderzoeksgebied"
            f_label = font(20)
            lb = d.textlength(label, font=f_label) / SCHAAL + 20
            d.rounded_rectangle(s(x2 - lb - 10, y1 - 16, x2 - 10, y1 + 16), radius=round(6 * SCHAAL), fill=ACCENT)
            tekst_midden(d, x2 - 10 - lb / 2, y1 - 13, label, f_label, kleur="white")
            vulling, rand, poppetje = ACCENT_VAK, ACCENT, ACCENT
        else:
            d.rectangle(s(x1, y1, x2, y2), fill="#FAFAFA", outline=GRIJS_RAND, width=round(2 * SCHAAL))
            vulling, rand, poppetje = GRIJS_VAK, GRIJS_RAND, "#7A7A7A"
        tekst_midden(d, cx, y1 + 26, naam, f_titel)
        vak(d, cx - 215, 435, cx + 215, 515, verkoper, f_vak)
        if aantal:
            d.rounded_rectangle(s(cx - 215, 555, cx + 215, 760), radius=round(8 * SCHAAL), fill=vulling,
                                outline=rand, width=round(2 * SCHAAL))
            tekst_midden(d, cx, 580, f"{aantal} consultants", f_vak_vet)
            poppetjes(d, cx, 685, aantal, poppetje)

    # Legenda en toelichting
    y = 840
    stippel_rechthoek(d, 60, y, 110, y + 30, ACCENT, dikte=3, streep=10, gat=6)
    d.text(s(130, y + 2), "Onderzoeksgebied: het projectproces van het SAP Business One-team, van de overdracht",
           font=f_klein, fill=ZWART)
    d.text(s(130, y + 32), "door sales tot de overdracht naar nazorg.", font=f_klein, fill=ZWART)
    d.text(s(60, y + 80), "Totaal 16 medewerkers. De teams hebben geen formele teamleider; de lijn loopt via de directeur.",
           font=f_klein, fill=ZWART)
    d.text(s(60, y + 112), "Bron: eigen weergave (2026).", font=f_klein_cursief, fill=LIJN)

    img.save(UIT, dpi=(254, 254))
    print(f"Geschreven: {UIT.relative_to(MAP.parents[1])}")


if __name__ == "__main__":
    main()
