import random

kleuren = ["harten", "ruiten", "schoppen", "klaveren"]
nummers = ["aas", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "boer", "vrouw", "heer"]
deck = []
kaarten = []

for kleur in kleuren:
    for nummer in nummers:
        deck.append(f"{kleur} {nummer}")

deck.append("joker")
deck.append("joker")

random.shuffle(deck)

for i in range(7):
    kaart = deck.pop(0)
    kaarten.append(kaart)

aantal_kaarten = len(deck)

print(kaarten)

print() # Witregel voor betere leesbaarheid
print(f"Deck ({aantal_kaarten} kaarten): {deck}")
print() # Witregel voor betere leesbaarheid