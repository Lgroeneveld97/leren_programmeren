naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
lievelingskleur = input("Wat is je favoriete kleur? ")
lievelingsgetal = int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-lievelingsgetal)
pronounce = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{pronounce.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", lievelingskleur)
print(f"Het verschil tussen {pronounce} leeftijd en {lievelingsgetal} is:", verschil)
