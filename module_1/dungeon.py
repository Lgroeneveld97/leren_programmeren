import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_key = False
player_room = 1

# === [kamer 1] === #

print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)
player_room = 2

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
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print("Daarboven zie je een som staan {} {} {} = ?".format(getal1, operator, getal2))
antwoord = int(input('Wat toest je in?'))

if antwoord == som:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
    player_key = True
else:
    print('Er gebeurt niets....')

print('Je zie twee deuren achter het standbeeld.')
print('Welke deur kies je?', 
      "A) Kamer 6", 
      "B) Kamer 3", )
keuze = input('? ')

if keuze == 'b':
    player_room = 3
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
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            player_health = (player_attack_amount * zombie_hit_damage)
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
else:    

    # === [kamer 3] === #

    item = random.choice(["schild", "zwaard"])
    if item == "schild":
        player_defense += 1
    else:
        player_attack += 2

    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)
    player_room = 4

    # === [kamer 4] === #

    vijand_attack = 2
    vijand_defense = 0
    vijand_health = 3

    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
    print('Je loopt tegen een vijand aan.')

    vijand_hit_damage = (vijand_attack - player_defense)

    if vijand_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de vijand, hij kan je geen schade doen.')
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
