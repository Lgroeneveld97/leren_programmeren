cijfer = float(input("Voer een cijfer in tussen 1 en 10: "))

if cijfer < 1 or cijfer > 10:
    print("Dit kan ik niet omzetten!")
elif cijfer >= 10:
    print(f"Gefeliciteerd, uitmuntend je resultaat is een {cijfer}")
elif cijfer >= 9:
    print(f"Gefeliciteerd, zeer goed je resultaat is een {cijfer}")
elif cijfer >= 8:
    print(f"Gefeliciteerd, goed je resultaat is een {cijfer}")
elif cijfer >= 7:
    print(f"Gefeliciteerd, ruim voldoende je resultaat is een {cijfer}")
elif cijfer >= 6:
    print(f"Gefeliciteerd, voldoende je resultaat is een {cijfer}")
elif cijfer >= 5:
    print(f"Jammer, bijna voldoende je resultaat is een {cijfer}")
elif cijfer >= 4:
    print(f"Jammer, onvoldoende je resultaat is een {cijfer}")
elif cijfer >= 3:
    print(f"Jammer, gering je resultaat is een {cijfer}")
elif cijfer >= 2:
    print(f"Jammer, slecht je resultaat is een {cijfer}")
else:
    print(f"Jammer, zeer slecht je resultaat is een {cijfer}")
