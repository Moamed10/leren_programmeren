# Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’

# Dat kost een TOEGANS_TIECKET per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

# Maak een programma speelhal.py voor deze berekening.
TOTAAL_PERSONEN = int(input("hoeveel personen ? "))
TOEGANS_TIECKET  = 7.45
VIP_VR_5MIN = 0.37
aantal_min_per_persoon = int(input("hoeveel min wilt u in de vip blijve "))
TOEGANS_TIECKET_prijs = TOTAAL_PERSONEN * TOEGANS_TIECKET

aantal_min_vp_prijs = (VIP_VR_5MIN / 5 * aantal_min_per_persoon ) * TOTAAL_PERSONEN

totaal = aantal_min_vp_prijs + TOEGANS_TIECKET_prijs

roud_totaal = round(totaal,2)

print(f"het totaal bedrag voor {TOTAAL_PERSONEN} personen is  {roud_totaal} euro ")

print(f"Dit geweldige dagje-uit met {TOTAAL_PERSONEN} mensen in speelhal {aantal_min_per_persoon} minuten VR kost je maar { roud_totaal}")





# Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro’