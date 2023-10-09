SMALL_PRIJS = 8.99
MEDIUM_PRIJS = 12.99
LARGE_PRIJS = 16.99
while True:
    try:
        aantal_small = int(input(f"Hoeveel small pizza's van {SMALL_PRIJS} wil je bestellen? "))
        aantal_medium = int(input(f"Hoeveel medium pizza's van {MEDIUM_PRIJS} wil je bestellen? "))
        aantal_large = int(input(f"Hoeveel large pizza's wil van {LARGE_PRIJS} je bestellen? "))

        prijs_small = aantal_small * SMALL_PRIJS
        prijs_medium = aantal_medium * MEDIUM_PRIJS
        prijs_large = aantal_large * LARGE_PRIJS

        totaal_prijs = prijs_small + prijs_medium + prijs_large

        print("Bestellingsoverzicht:")
        print(f"{aantal_small} small pizza('s): €{prijs_small:.2f}")
        print(f"{aantal_medium} medium pizza('s): €{prijs_medium:.2f}")
        print(f"{aantal_large} large pizza('s): €{prijs_large:.2f}") 
        print(f"Totaalprijs: €{totaal_prijs:.2f}")
        break
    except ValueError:
        print("fout propeer opnieuw")
        
    

