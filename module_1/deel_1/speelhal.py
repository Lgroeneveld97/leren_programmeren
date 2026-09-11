# gegevens
aantal_personen = 5
prijs_toeganstickets = 7.45
tijd_vip_vr_gameseat = 45
kosten_vip_vr_gameseat = 0.37

# tickets prijs
prijs_tickets = aantal_personen * prijs_toeganstickets

# kosten game seat
kosten_game_seat = tijd_vip_vr_gameseat / 5 * kosten_vip_vr_gameseat

# kosten totaal p.p.
kosten_totaal_pp = prijs_tickets * kosten_game_seat / 2

print("Dit geweldige dagje uit met", aantal_personen, "personen in de speelhal met", tijd_vip_vr_gameseat, "VR kost je maar",
      kosten_totaal_pp, "p.p.")
