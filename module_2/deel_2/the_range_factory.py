lijstjes = int(input("Hoeveel lijstjes wilt u? "))
lijstjes += 1 # Zodat de juiste aantal lijstjes worden gevraagd.

for i in range(1,lijstjes):
    lijst_lengte = int(input(f"Hoelang moet lijst {i} zijn? "))

for i in range(lijst_lengte):
    print(f"[{i}]")