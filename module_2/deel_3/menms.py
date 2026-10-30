import random

kleuren = ("orange", "blauw", "groen", "bruin")

print("") # Witregel voor betere leesbaarheid
aantal_menms = int(input("Hoeveel M%M's moeten er aan de zak worden toegevoegd? "))

zak_menms = []

for i in range(aantal_menms):
    zak_menms.append(random.choice(kleuren))
    
print("") # Witregel voor betere leesbaarheid
print(zak_menms)
print("") # Witregel voor betere leesbaarheid