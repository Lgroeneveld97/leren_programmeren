dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print()
print("Alle dagen van de week zijn:")
print()
for dag in dagen:
    print(f"{dag}, ")

print()
print(f"De weekenddagen zijn: {dagen[5]} & {dagen[6]}.")
print()

print("De werkdagen zijn:")
for dag in dagen[0:5]:
    print(f" - {dag}")

print()
print(f"Alle dagen van de week in omgekeerde volgorde zijn:")
for dag in dagen[::-1]:
    print(f" - {dag}")

print()
print("De werkdagen in omgekeerde volgorde zijn:")
for dag in dagen[4::-1]:
    print(f" - {dag}")

print()
print(f"De weekenddagen in omgekeerde volgorde zijn: {dagen[6]} -> {dagen[5]}.")
print()