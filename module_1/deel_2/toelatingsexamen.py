leeftijd = 13
heeft_magische_brief = True
magisch_huisdier = "uil" 
kent_spreuk = True
heeft_stok = True
op_zwarte_lijst = False
geslaagd_aanlegtest = True
heeft_strafblad = False

if leeftijd <= 11:
    print("Afgewezen: Je bent te jong.")
    exit
elif not heeft_magische_brief:
    print("Afgewezen: Geen magische uitnodiging ontvangen.")
    exit
elif not magisch_huisdier in ["uil", "pad", "kat"]:
    print("Afgewezen: Ongeldig magisch huisdier.")
    exit
elif not kent_spreuk:
    print("Afgewezen: Je kent nog geen spreuken.")
    exit
elif not heeft_stok:
    print("Afgewezen: Je hebt nog geen toverstok.")
    exit
elif op_zwarte_lijst:
    print("Afgewezen: Je staat op de zwarte lijst van het Ministerie.")
    exit
elif not geslaagd_aanlegtest:
    print("Afgewezen: Je bent niet geslaagd voor de Magische aanlegtest.")
    exit
elif heeft_strafblad:
    print("Afgewezen: Strafblad bij de goblinbank.")
    exit
else:
    print("Toegelaten!")
