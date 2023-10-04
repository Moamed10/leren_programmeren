# Maak op de plek van ??? in de if één if statement waarbij alle onderstaande stellingen kloppen.

# Alleen chips is geen feest.
# Een feest met chips, maar zonder drank kan niet beginnen.
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.
# Een feest moet minimaal gasten of een gastheer hebben.
# Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
# Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.
# Let op:  Zorg er voor dat je het goed test. Dit kun je doen door de variabelen op True en/of False te zetten,
# dit doe je door bijvoorbeeld als je punt 1 wilt testen door gastheer, gasten en drank de waarde False te geven 
# en chips de waarde True, dan het programma “No Party” aan moeten geven.





gastheer = False
gasten = True
drank = True
chips = False



if (chips and drank and gasten) or (gastheer and drank ):
    print('Start the Party')
else:
    print('No Party')
