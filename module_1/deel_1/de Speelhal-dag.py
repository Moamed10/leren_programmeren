# Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’

# Dat kost een TOEGANTICKET/ per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

# Maak een programma speelhal.py voor deze berekening.
totaal_personen = 4
TOEGANTICKET  = 7.45
vip_vr_45 = 0.37

TOEGANTICKET_prijs = totaal_personen * TOEGANTICKET

vp_prijs = (vip_vr_45 * 9) * 4

totaal = vp_prijs + TOEGANTICKET_prijs

roud_totaal = round(totaal)

print(f"het totaal bedrag voor {totaal_personen} personen is  {roud_totaal} euro ")

print(f"Dit geweldige dagje-uit met {totaal_personen} mensen in speelhal 45 minuten VR kost je maar {roud_totaal}")





# Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro’