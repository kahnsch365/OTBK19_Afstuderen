"""Tekent het organogram van JIS Nederland (bijlage 1 bij het onderzoeksvoorstel).

Gebruik:  python3 afstuderen/01-onderzoeksvoorstel/tools/maak_organogram.py
Uitvoer:  afstuderen/01-onderzoeksvoorstel/bijlage-organogram.png

De bezetting staat in STAF en TEAMS hieronder; pas die aan als de organisatie verandert.
Coördinaten zijn in 'eenheden' (1600 breed = ca. 16 cm in het formulier) en worden
met SCHAAL vergroot voor een scherpe afdruk. Vereist: Pillow.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

MAP = Path(__file__).resolve().parent.parent
UIT = MAP / "bijlage-organogram.png"

SCHAAL = 2
B, H = 1600, 610
FONTMAP = Path("/usr/share/fonts/truetype/liberation")
FONT = FONTMAP / "LiberationSans-Regular.ttf"
FONT_VET = FONTMAP / "LiberationSans-Bold.ttf"
FONT_CURSIEF = FONTMAP / "LiberationSans-Italic.ttf"

TEKST = "#1A1A1A"
LIJN = "#595959"
RAND = "#7F7F7F"
DONKER = "#1F3864"  # directeur
KOP = "#D6DCE4"  # teamkoppen
ACCENT = "#2E5597"  # onderzoeksgebied
ACCENT_LICHT = "#EEF2F8"

DIRECTEUR = "Directeur / eigenaar"
STAF = "Marketingmedewerker"
TEAMS = [  # (productlijn, functies, onderzoeksgebied?)
    ("Jeeves (ERP)", ["Verkoper", "Consultants (5)"], False),
    ("SAP Business One (ERP)", ["Verkoper", "Consultants (6)"], True),
    ("SuperOffice (CRM)", ["Medewerker (1)"], False),
]


def s(*waarden):
    return [round(w * SCHAAL) for w in waarden]


def font(grootte, soort=FONT):
    return ImageFont.truetype(str(soort), round(grootte * SCHAAL))


def tekst_in(d, x1, y1, x2, y2, tekst, f, kleur=TEKST):
    """Tekst gecentreerd in een rechthoek."""
    d.text(s((x1 + x2) / 2, (y1 + y2) / 2), tekst, font=f, fill=kleur, anchor="mm")


def vak(d, x1, y1, x2, y2, tekst, f, vulling="white", rand=RAND, kleur=TEKST, dikte=1.5):
    d.rectangle(s(x1, y1, x2, y2), fill=vulling, outline=rand, width=max(1, round(dikte * SCHAAL)))
    tekst_in(d, x1, y1, x2, y2, tekst, f, kleur)


def lijn(d, *punten, kleur=LIJN, dikte=1.5):
    d.line(s(*punten), fill=kleur, width=max(1, round(dikte * SCHAAL)))


def stippel_rechthoek(d, x1, y1, x2, y2, kleur, dikte=2, streep=12, gat=7):
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

    for zijde in ((x1, y1, x2, y1), (x1, y2, x2, y2), (x1, y1, x1, y2), (x2, y1, x2, y2)):
        stippellijn(*zijde)


def main() -> None:
    img = Image.new("RGB", s(B, H), "white")
    d = ImageDraw.Draw(img)
    f_vet = font(24, FONT_VET)
    f_tekst = font(23)
    f_klein_cursief = font(19, FONT_CURSIEF)

    midden = B / 2
    breedte, tussen = 400, 90
    links = (B - len(TEAMS) * breedte - (len(TEAMS) - 1) * tussen) / 2
    teams_x = [links + breedte / 2 + i * (breedte + tussen) for i in range(len(TEAMS))]
    kop_y1, kop_y2 = 300, 360
    vak_h, vak_gat = 56, 22

    # Onderzoeksgebied (achtergrond, eerst tekenen)
    for cx, (_, functies, gebied) in zip(teams_x, TEAMS):
        if gebied:
            x1, x2 = cx - breedte / 2 - 22, cx + breedte / 2 + 22
            y1 = kop_y1 - 22
            y2 = kop_y2 + vak_gat + len(functies) * (vak_h + vak_gat) + 44
            d.rectangle(s(x1, y1, x2, y2), fill=ACCENT_LICHT)
            stippel_rechthoek(d, x1, y1, x2, y2, ACCENT)
            label = "Onderzoeksgebied"
            lb = d.textlength(label, font=f_klein_cursief) / SCHAAL
            d.text(s(x2 - lb - 12, y2 - 32), label, font=f_klein_cursief, fill=ACCENT)

    # Directeur en staf
    vak(d, midden - 190, 30, midden + 190, 95, DIRECTEUR, f_vet, vulling=DONKER, rand=DONKER, kleur="white")
    staf_y = 165
    lijn(d, midden, 95, midden, 250)
    lijn(d, midden - 200, staf_y, midden, staf_y)
    vak(d, midden - 530, staf_y - 30, midden - 200, staf_y + 30, STAF, f_tekst)

    # Teams
    lijn(d, teams_x[0], 250, teams_x[-1], 250)
    for cx, (naam, functies, _) in zip(teams_x, TEAMS):
        x1, x2 = cx - breedte / 2, cx + breedte / 2
        lijn(d, cx, 250, cx, kop_y1)
        vak(d, x1, kop_y1, x2, kop_y2, naam, f_vet, vulling=KOP, rand=RAND)
        ruggengraat = x1 + 30
        y = kop_y2 + vak_gat
        laatste_midden = y + (len(functies) - 1) * (vak_h + vak_gat) + vak_h / 2
        lijn(d, ruggengraat, kop_y2, ruggengraat, laatste_midden)
        for functie in functies:
            lijn(d, ruggengraat, y + vak_h / 2, x1 + 60, y + vak_h / 2)
            vak(d, x1 + 60, y, x2, y + vak_h, functie, f_tekst)
            y += vak_h + vak_gat

    img.save(UIT, dpi=(254, 254))
    print(f"Geschreven: {UIT.relative_to(MAP.parents[1])}")


if __name__ == "__main__":
    main()
