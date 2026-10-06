# variabelen
wachtwoord = ""
aantal_pogingen = 5

wachtwoord = input("Voer uw nieuwe wachtwoord in: ")

while aantal_pogingen > 0:
    wachtwoordcheck = input("Voer uw wachtwoord in: ")
    if not wachtwoord == wachtwoordcheck:
        aantal_pogingen -= 1
        print(f"Incorrect, u heeft nog {aantal_pogingen} pogingen over")
    else:
        aantal_pogingen = 0
        print("Correct!")
        exit()

