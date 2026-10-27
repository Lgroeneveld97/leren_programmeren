eerste_lijst = []
lijst_nummer = 0
lijstjes = int(input("Hoeveel lijstjes wilt u? "))

for i in range(lijstjes):
    lijst_nummer += 1
    tweede_lijst = []
    lijst_lengte = int(input(f"Hoelang moet lijst {lijst_nummer} zijn? "))
    for x in range(lijst_lengte):
        tweede_lijst.append(x*lijst_nummer+lijst_nummer)
    eerste_lijst.append(tweede_lijst)

print(eerste_lijst)
