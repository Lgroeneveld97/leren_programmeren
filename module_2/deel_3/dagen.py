dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print() # Witregel voor betere leesbaarheid
print("Alle dagen van de week zijn:")
print() # Witregel voor betere leesbaarheid
for dag in dagen:
    print(f"{dag}, ", end="")

print() # Witregel voor betere leesbaarheid
print(f"De weekenddagen zijn: {dagen[5]} & {dagen[6]}.")

print() # Witregel voor betere leesbaarheid
for dag in dagen[4]:
    print(f"De werkdagen zijn: {dagen[0]} ", end="")

print() # Witregel voor betere leesbaarheid
print(f"Alle dagen van de week in omgekeerde volgorde zijn: {dagen[6]} -> {dagen[5]} -> {dagen[4]} -> {dagen[3]} -> {dagen[2]} -> {dagen[1]} -> {dagen[0]}.")

print() # Witregel voor betere leesbaarheid
print("De werkdagen in omgekeerde volgorde zijn:")
for dag in dagen[4::-1]:
    print(f"- {dag}")

print() # Witregel voor betere leesbaarheid
print(f"De weekenddagen in omgekeerde volgorde zijn: {dagen[6]} -> {dagen[5]}.")
print() # Witregel voor betere leesbaarheid