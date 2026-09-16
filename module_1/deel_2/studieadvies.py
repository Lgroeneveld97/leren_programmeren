from studieadviestext import (
    AANTAL_WEKEN_VRAAG,
    COMPETENTIE_ADVIES_GERUSTSTELLEND,
    COMPETENTIE_ADVIES_TITEL,
    COMPETENTIE_ADVIES_TWIJFELACHTIG,
    COMPETENTIE_ADVIES_ZORGELIJK,
    COMPETENTIE_STELLING_1,
    COMPETENTIE_STELLING_2,
    COMPETENTIE_STELLING_3,
    COMPETENTIE_STELLING_4,
    COMPETENTIE_STELLING_5,
    COMPETENTIE_STELLING_6,
    COMPETENTIE_STELLING_7,
    OPTIES,
    STUDIEDOKTER_TITEL
)

print(STUDIEDOKTER_TITEL)

vraag1 = int(input(COMPETENTIE_STELLING_1))
while vraag1 < 1 or vraag1 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag1 = int(input(COMPETENTIE_STELLING_1))


vraag2 = int(input(COMPETENTIE_STELLING_2))
while vraag2 < 1 or vraag2 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag2 = int(input(COMPETENTIE_STELLING_2))


vraag3 = int(input(COMPETENTIE_STELLING_3))
while vraag3 < 1 or vraag3 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag3 = int(input(COMPETENTIE_STELLING_3))


vraag4 = int(input(COMPETENTIE_STELLING_4))
while vraag4 < 1 or vraag4 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag4 = int(input(COMPETENTIE_STELLING_4))


vraag5 = int(input(COMPETENTIE_STELLING_5))
while vraag5 < 1 or vraag5 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag5 = int(input(COMPETENTIE_STELLING_5))


vraag6 = int(input(COMPETENTIE_STELLING_6))
while vraag6 < 1 or vraag6 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag6 = int(input(COMPETENTIE_STELLING_6))


vraag7 = int(input(COMPETENTIE_STELLING_7))
while vraag7 < 1 or vraag7 > 4:
    print("Voer een cijfer van 1 tot en met 4 in")
    vraag7 = int(input(COMPETENTIE_STELLING_7))


gemiddelde = (
    vraag1 + vraag2 + vraag3 + vraag4 + vraag5 + vraag6 + vraag7
) / 7

print(COMPETENTIE_ADVIES_TITEL)
if gemiddelde <= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
