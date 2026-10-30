import random

kleuren = ["harten", "ruiten", "schoppen", "klaveren"]
nummers = ["aas", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "boer", "vrouw", "heer"]
deck = []

for kleur in kleuren:
    for nummer in nummers:
        deck.append(f"{kleur} {nummer}")

deck.append("joker")
deck.append("joker")

random.shuffle(deck)

n = 47

kaarten = deck[n:]
deck = deck[:n]

aantal_kaarten = len(deck)

print(kaarten)

print("") # Witregel voor betere leesbaarheid
print(f"Deck ({aantal_kaarten} kaarten): {deck}")
print("") # Witregel voor betere leesbaarheid