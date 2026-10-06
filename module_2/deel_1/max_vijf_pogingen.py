# variabelen
wachtwoord = ""
aantal_pogingen = 5
pogingen = 0

wachtwoord = input("Voer uw nieuwe wachtwoord in: ")

while aantal_pogingen > 0:
    wachtwoordcheck = input("Voer uw wachtwoord in: ")
    if not wachtwoord == wachtwoordcheck:
        aantal_pogingen -= 1
        pogingen += 1
        if aantal_pogingen > 0:
            print(f"Incorrect, u heeft nog {aantal_pogingen} pogingen over")
        else:
            print("Te veel foute pogingen, je mag niet meer inloggen.")
            exit()
    else:
        aantal_pogingen = 0
        pogingen += 1
        print(f"Correct! Juiste wachtwoord in {pogingen} pogingen")
        exit()

