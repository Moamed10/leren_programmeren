# Definieert een functie genaamd genereer_lijstjes met een parameter aantal_lijstjes
def genereer_lijstjes(aantal_lijstjes):
    # Maakt een lege lijst genaamd lijstjes
    lijstjes = []

    # Start een for-loop die loopt van 1 tot aantal_lijstjes + 1
    for i in range(1, aantal_lijstjes + 1):
        # Vraagt de gebruiker om de lengte van het huidige lijstje in te voeren
        lengte_lijst = int(input(f"Hoeveel in lijst {i}? "))
        
        # Genereert een lijst met behulp van range en voegt deze toe aan de lijstjes
        lijst = list(range(i, i * lengte_lijst + 1, i))
        lijstjes.append(lijst)

    # Geeft de lijst van lijstjes terug
    return lijstjes

# Definieert de main-functie, het hoofdgedeelte van het programma
def main():
    # Vraagt de gebruiker om het aantal lijstjes in te voeren
    aantal_lijstjes = int(input("Hoeveel lijstjes? "))
    
    # Roept de genereer_lijstjes-functie aan met het ingevoerde aantal lijstjes
    resultaat = genereer_lijstjes(aantal_lijstjes)
    
    # Drukt het resulterende lijstje van lijstjes af
    print(resultaat)

# Controleert of het script rechtstreeks wordt uitgevoerd (niet geïmporteerd als module)
if __name__ == "__main__":
    # Roept de main-functie aan om het programma uit te voeren
    main()
