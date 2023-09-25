# Maak de Python applicatie "Pizza Calculator" in pizzaCalculator.py

 

# De functionaliteiten die in de applicatie moeten zitten zijn:

# de klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.
# zoek op internet naar passende prijzen voor deze pizza afmetingen en noteer deze prijzen in je applicatie
# Toon op het scherm met goede omschrijving het aantal bestelde pizza's voor elke afmeting en berekenen per afmeting de prijs uit
# Toon op het scherm de totaalprijs van alle pizza's.
# Bovenaan in de Python file noteer je als commenteer het volgende: voornaam, achternaam en opdracht: Pizza calculator
# De volgende zaken dienen ook op orde te zijn:

# leesbare layout van de code
# naamgeving is duidelijk en 'self explaining'
# er is passend commentaar toegevoegd in de code
# laat de uitkomst er uit zien als een bonnetje

# Voornaam: [mohamed]
# Achternaam: [almahmoud]
# Opdracht: Pizza Calculator

SMALL_PRIJS = 8.99
MEDIUM_PRIJS = 12.99
LARGE_PRIJS = 16.99

aantal_small = int(input("Hoeveel small pizza's wil je bestellen? "))
aantal_medium = int(input("Hoeveel medium pizza's wil je bestellen? "))
aantal_large = int(input("Hoeveel large pizza's wil je bestellen? "))

prijs_small = aantal_small * SMALL_PRIJS
prijs_medium = aantal_medium * MEDIUM_PRIJS
prijs_large = aantal_large * LARGE_PRIJS

totaal_prijs = prijs_small + prijs_medium + prijs_large

print("Bestellingsoverzicht:")
print(f"{aantal_small} small pizza('s): €{prijs_small:.2f}")
print(f"{aantal_medium} medium pizza('s): €{prijs_medium:.2f}")
print(f"{aantal_large} large pizza('s): €{prijs_large:.2f}")
print(f"Totaalprijs: €{totaal_prijs:.2f}")
