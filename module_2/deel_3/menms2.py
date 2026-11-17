import random

kleuren = ("Rood", "Blauw", "Groen", "Geel", "Bruin")

print() # Witregel voor betere leesbaarheid
aantal_menms = int(input("Hoeveel M%M's moeten er aan de zak worden toegevoegd? "))

zak_menms = {
    "Rood": 0,
    "Blauw": 0,
    "Groen": 0,
    "Geel": 0,
    "Bruin": 0
}

aantal = 0

for i in range(aantal_menms):
    kleur = random.choice(kleuren)
    aantal = zak_menms.get(kleur) # 
    aantal += 1
    zak_menms.update({kleur : aantal})

print() # Witregel voor betere leesbaarheid
print(zak_menms)
print() # Witregel voor betere leesbaarheid