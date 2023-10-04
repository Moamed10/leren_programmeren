# Opdracht
# Maak van de gastheer variable in plaats van een boolean een input. Hierin vraag je de gebruiker de volgende vraag: 
# “Wie is de gastheer?”.

# Breid nu je programma uit (dus niet een nieuw bestand) dat het ook nog werkt met de volgende stellingen:

# Als de naam van de gastheer het zelfde is als jouw naam, dan is er hoe dan ook een feest.
# Als de naam van de gastheer het zelfde is als jouw SLB-er dan is er hoe dan ook geen feest.
# Let op: Zorg er voor dat de punten uit de vorige opdracht ook werken, als je geen naam invult bij de vraag 
# in je terminal dan betekend dit dat er geen gastheer is. Je mag geen nieuwe if’s aanmaken!






gastheer = input("Wie is de gastheer? (Laat leeg als er geen gastheer is): ")
gasten = True

drank = True
chips = True

MIJN_NAAM = "mohamed"
SLB = "mo"


if (gastheer == MIJN_NAAM  ) or (chips and drank and 20 >= gasten <= 4 and gastheer != SLB) or (gastheer and drank and gastheer != SLB ):
    print("start party")
else:
    print('No Party')




# elif gastheer == SLB:
#     print("no party")
# elif(chips and drank and gasten) or (gastheer and drank ):
#     print('Start the Party')
# else:
#     print('No Party')



