goud = 0
levenspunten = 100

naam = input("Hoe heet je? ")
leeftijd = int(input("Hoe oud ben je? "))

print(f"Welkom, {naam}! Klaar voor avontuur?")

if leeftijd > 16:
    print("Je bent oud genoeg voor dit avontuur!")
else:
    print("Helaas! Je bent niet oud genoeg voor dit avontuur.")
    exit()

print("Je ziet twee gangen voor je.")
keuze = input("Welke gang kies je?, 1 = linker gang, 2 = rechter gang. ")

if keuze == "1":
    print("Je loopt de linker gang binnen en ziet een schatkist!")
    keuze = input("Wil je de kist openen?, ja/nee ")
    if "ja" in keuze:
        print("Je vindt 50 goud in de kist!")
        goud += 50
else:
    print("Je komt een monster tegen!")
    keuze = input("Vecht je tegen het monster?, ja/nee ")
    if "ja" in keuze:
        print("Je verslaat het monster en krijgt 30 goud!")
        goud += 30
    else:
        print("Het monster verslaat je en je verliest 80 levenspunten.")
        levenspunten -= 80

print("Je komt bij een gevaarlijke brug.")
if levenspunten > 20:
    print("Je steekt de brug veilig over.")
    status = True
else:
    print("Je hebt te weinig levenspunten en valt van de brug...")
    exit()

print("Avontuur voltooid! Hier zijn je stats:")
print(f"Naam: {naam}")
print(f"Aantal goudstukken: {goud}")
print(f"Levenspunten: {levenspunten}")
if status:
    print("Status: Gewonnen")
if goud> 40 and status:
    print("Titel: Meester-avonturier")