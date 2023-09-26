# In bezit van een geldig Vrachtwagen rijbewijs. Een echte circusdirecteur rijdt ook de grootste circuswagen zelf!
# In bezit van een hoge hoed.
# Is zwaarder dan 90 kg en lichter dan 120 kg
# Is langer dan 150 cm en korter dan 220 cm
# Heeft Certificaat “Overleven met gevaarlijk personeel”
# Heeft:
# minimaal 4 jaar praktijkervaring met dieren-dressuur OF
# minimaal 5 jaar ervaring met jongleren OF
# minimaal 3 jaar praktijkervaring met acrobatiek.
# Let op: Vraag de jaren ervaring afzonderlijk voor alle kuns

# minimaal 4 jaar praktijkervaring met dieren-dressuur OF
# minimaal 5 jaar ervaring met jongleren OF
# minimaal 3 jaar praktijkervaring met acrobatiek.

naam = input("wat is uw naam :")
rijbewijs = input("heeft uw rijbewijs ? j/n :")
gewicht = int(input("hoeveel weegt u (kg) ? :"))
lengte = int(input("hoelang bent u (cm) ? :"))

dieren_dressuur = int(input("hoelang u heeft praktijkervaring met dieren-dressuur ? :"))
jogleren_1 = int(input("hoelang heeft u ervaring met jongleren ? :"))
acrobatiek = int(input("hoelang heeft u ervaring met acrobatiek ? :"))

MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220

DIEREN_ERVARING_NODIG = 4
JOGLEREN_2ERVARING = 5
ACROBATIEK_2ERVARING = 5


if rijbewijs is "ja" and MIN_GEWICHT <= gewicht <= MAX_GEWICHT and MIN_LENGTE <= lengte <= MAX_LENGTE and (dieren_dressuur >= DIEREN_ERVARING_NODIG or jogleren_1 >= JOGLEREN_2ERVARING or  acrobatiek >= ACROBATIEK_2ERVARING):
    print("goed")
else:
    print("no")  
    
    