# Maak van de gasten variable in plaats van een boolean een integer. Aan de hand van wat je aan het testen bent pas je steeds de 
# code aan.

# Breid nu je programma uit (dus niet een nieuw bestand) dat het ook nog werkt met de volgende stellingen:

# Een feest met gasten kan pas beginnen als er minimaal 4 gasten zijn.
# Een feest kan niet starten als er meer dan 20 aanwezigen zijn.
# Let op: Zorg er voor dat de punten uit de vorige opdracht ook werken, als je 0 gasten hebt betekend dit dat er geen 
# gasten zijn. Je mag geen nieuwe 
# if’s aanmaken!


gastheer = input("Wie is de gastheer? (Laat leeg als er geen gastheer is): ")
gasten = int(input("hoeveel gaste? : "))

drank = True
chips = True

MIJN_NAAM = "mohamed"
SLP = "mo"


if gastheer == MIJN_NAAM:
    print("start party zelfde naam mijn naam")
elif gastheer == SLP:
    print("no party zelfde slp naam ")
elif(chips and drank and  (20>= gasten >= 4)) or (gastheer and drank ):
    print('Start the Party')
else:
    print('No Party')