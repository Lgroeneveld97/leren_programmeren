import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_key = False
player_room = 1
player_rupee = 0

if player_room == 1:
    # === [kamer 1] === #

    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    print('')
    time.sleep(1)
    player_room = 7

if player_room == 7:
    # === [kamer 7] === #

    kans = random.randint(1,10)

    print('Je loopt de kamer binnen.')
    print('Er hangt een betoverende mist in deze kamer')
    print("...")
    time.sleep(2)

    if kans == 1:
        print('Er verschijnt ineens een rupee op de grond liggen en je pakt deze op.')
        player_rupee += 1
    else:
        print("Er gebeurt niets...")

    print("Je ziet twee deuren voor je.")
    print('Welke kamer ga je naar binnen?', 
            "A Kamer 8", 
            "B Kamer 2", )
    keuze = input('? ')
    if keuze == 'b':
        player_room = 2
    else:
        player_room = 8
    
    print('')
    time.sleep(1)

if player_room == 2:
    # === [kamer 2] === #

    getal1 = random.randint(10,25)
    getal2 = random.randint(-5,75)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        som = getal1 + getal2 
    elif operator == "-":
        som = getal1 - getal2
    else:
        som = getal1 * getal2      

    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print("Daarboven zie je een som staan {} {} {} = ?".format(getal1, operator, getal2))
    antwoord = int(input('Wat toest je in?'))

    if antwoord == som:
        print('Het stadbeeld laat de rupee vallen en je pakt hem op')
        player_rupee +=1
    else:
        print('Er gebeurt niets...')

    print('Je zie twee deuren achter het standbeeld.')
    print('Welke deur kies je?', 
        "A Kamer 6", 
        "B Kamer 8", )
    keuze = input('? ')

    if keuze == 'b':
        player_room = 8
    else:
        player_room = 6
    
    print('')
    time.sleep(1)

if player_room == 6:
    # === [kamer 6] === #

    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2

    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
        
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            player_health = (player_attack_amount * zombie_hit_damage)
            print(f'Je health is nu {player_health}.')
            player_room = 8
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()

    print('Je zie weer twee deuren.')
    print('Welke deur kies je?', 
        "A Kamer 8", 
        "B Kamer 3", )
    keuze = input('? ')

    if keuze == 'b':
        player_room = 3
    else:
        player_room = 8    

    print('')
    time.sleep(1)        

if player_room == 8:
    # === [kamer 8] === #

    getal1 = random.randint(1,6)
    getal2 = random.randint(1,6)
    som = getal1 + getal2
    print("Je stapt de volgende kamer binnen.")
    print("In de kamer staat een gokmachine.")
    print('Wil je deze gebruiken?', 
            "A Ja", 
            "B Nee", )
    keuze = input('? ')
    if keuze == 'a':
        print("Nieuwsgierig zet je de gokmachine aan.")
        print("...")
        time.sleep(2)
        if som > 7:
            player_rupee *= 2
            print("Je hebt nu twee 2x zo veel rupees!")
        elif som < 7:
            player_health -= 1 
            print("Helaas, je hebt 1 hp verloren...")
        else:
             player_rupee += 1
             player_health += 4    
             print("Gefeliciteerd! Je hebt 1 rupee en 4 hp gekregen!")        
    else:
        print("Je negeert de gokmachine loopt naar de volgende deur.")

    print('Je zie weer twee deuren.')
    print('Welke deur kies je?', 
        "A Kamer 9", 
        "B Kamer 3", )
    keuze = input('? ')

    if keuze == 'b':
        player_room = 3
    else:
        player_room = 9  
    
    print('')
    time.sleep(1)

if player_room == 9:
    # === [kamer 9] === #

    uitkomst = random.choice(["health", "defense"])
    print("Je loopt de kamer binnen.")
    print("Er hangt hier een betoverende mist.")
    print("...")
    time.sleep(2)

    if uitkomst == "health":
       print('Je health is omhoog gegaan bij 1 punt!')
       player_health += 1
    else:
       print('Je defense is omhoog gegaan bij 2 punten!')
       player_defense += 2   
   
    print('')
    time.sleep(1)
    player_room = 3

if player_room == 3:
    # === [kamer 3] === #

    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print('In deze kamer staat een goblin.')
    print('Hij offert je een zwaard, een schild of een sleutel in ruil voor rupees.')
    print("")
    print('Wil je zaken met hem doen?', 
        "A Ja", 
        "B Nee", )
    keuze = input('? ')

    if keuze == 'a':
        if player_rupee <= 0:
            print("Maar je hebt geen rupees!")
            print("Je hebt geen andere keuze en loopt naar de volgende deur.")
        elif player_rupee == 1:
            print("Kies je voor het zwaard of het schild?", 
            "A Zwaard", 
            "B Schild",)
            keuze = input('? ')
            if keuze == "a":
                print("Je geeft de rupee an de goblin en hij geeft je het zwaard.")
                item = "zwaard"
                print(f'Dapper met je nieuwe {item} loop je verder.')
                player_rupee -= 1
                player_attack += 2
            else:
                print("Je geeft de rupee an de goblin en hij geeft je het schild.")
                item = "schild"
                print(f'Dapper met je nieuwe {item} loop je verder.')
                player_rupee -= 1
                player_defense += 1
        else:
            print("Kies je voor het zwaard, het schild, of de sleutel?", 
            "A Zwaard", 
            "B Schild",
            "C Sleutel")
            keuze = input('? ')
            if keuze == "a":
                print("Je geeft de rupee an de goblin en hij geeft je het zwaard.")
                item = "zwaard"
                print(f'Dapper met je nieuwe {item} loop je verder.')
                player_rupee -= 1
                player_attack += 2
            elif keuze == "b":
                print("Je geeft de rupee an de goblin en hij geeft je het schild.")
                item = "schild"
                print(f'Dapper met je nieuwe {item} loop je verder.')
                player_rupee -= 1
                player_defense += 1
            else:
                print("Je geeft de rupees aan de goblin en hij geeft je de sleutel.")
                player_key = True
                item = "sleutel"
                print(f"Met je nieuwe {item} op zak loop je verder.")
    else:
        print("Je slaat het aanbod over en loopt naar de volgende deur")

    print('')
    time.sleep(1)
    player_room = 4

if player_room == 4:
    # === [kamer 4] === #

    vijand_attack = 2
    vijand_defense = 0
    vijand_health = 3

    print("Je stapt de kamer binnen.")
    print('Je loopt tegen een vijand aan.')

    vijand_hit_damage = (vijand_attack - player_defense)

    if vijand_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de vijand, hij kan je geen schade doen.')
    else:
        vijand_attack_amount = math.ceil(player_health / vijand_hit_damage)
        
        player_hit_damage = (player_attack - vijand_defense)
        player_attack_amount = math.ceil(vijand_health / player_hit_damage)

        if player_attack_amount < vijand_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de vijand.')
            player_health = (player_attack_amount * vijand_hit_damage)
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de vijand te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)
    player_room = 5

if player_room == 5:
    # === [kamer 5] === #

    print('Voorzichtig open je de deur, je wilt niet nog een vijand tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if player_key:
        print("Je opent de schatkist.")
        exit()
    else:
        print("Maar je hebt geen sleutel!")
        exit()
