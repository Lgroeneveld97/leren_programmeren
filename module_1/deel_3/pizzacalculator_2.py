# Lucas Groeneveld, opdracht: Pizzacalculator

# prijs per pizza
small_pizza_prijs = 8
medium_pizza_prijs = 15
large_pizza_prijs = 21

# gebruiker vult in hoeveel pizza's hij/zij wilt
try:
    aantal_small_pizzas = int(input("Hoeveel small pizza's wilt u?"))
    print(aantal_small_pizzas)
except:
    aantal_small_pizzas = 0
    print("Dat is geen heel nummer!")

try:    
    aantal_medium_pizzas = int(input("Hoeveel medium pizza's wilt u?"))
    print(aantal_medium_pizzas)
except:
    aantal_medium_pizzas = 0
    print("Dat is geen heel nummer!")

try:
    aantal_large_pizzas = int(input("Hoeveel large pizza's wilt u?"))
    print(aantal_large_pizzas)
except:
    aantal_large_pizzas = 0
    print("Dat is geen heel nummer!")

# Totaal prijs per pizza
small_pizza_totaal = aantal_small_pizzas * small_pizza_prijs
medium_pizza_totaal = aantal_medium_pizzas * medium_pizza_prijs
large_pizza_totaal = aantal_large_pizzas * large_pizza_prijs

# Totaal prijs
totaal = small_pizza_totaal + medium_pizza_totaal + large_pizza_totaal

# Kassa bon
print("******* KASSA BON *******")
if aantal_small_pizzas > 0:
    print(f"Pizza's small:   {aantal_small_pizzas} x €{small_pizza_prijs:.2f} = €{small_pizza_totaal:.2f}")
if aantal_medium_pizzas > 0:
    print(f"Pizza's medium:  {aantal_medium_pizzas} x €{medium_pizza_prijs:.2f} = €{medium_pizza_totaal:.2f}")
if aantal_large_pizzas > 0:
    print(f"Pizza's large:   {aantal_large_pizzas} x €{large_pizza_prijs:.2f} = €{large_pizza_totaal:.2f}")
print("*************************")
print(f"Totaal:   €{totaal:.2f}")
