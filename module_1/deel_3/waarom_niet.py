# e kandidaat moet ook nog voldoen aan de volgende criteria:

# In bezit van een Diploma MBO-4 ondernemen OF
# Is al meer dan 3 jaar ondernemer EN met minimaal 5 werknemers in loondienst.

# Is man EN heeft snor breder dan 10 cm OF
# is vrouw EN draagt rood krulhaar langer dan 20 cm OF

# is anders EN heeft brede glimlach breder dan 10 cm





naam = input("wat is uw naam :")
rijbewijs = input("heeft uw rijbewijs ? j/n :")
gewicht = int(input("hoeveel weegt u (kg) ? :"))
lengte = int(input("hoelang bent u (cm) ? :"))
ondernemer_jaren = int(input("Hoeveel jaar bent u al ondernemer? (0 als u geen ondernemer bent): "))
aantal_werknemers = int(input("Hoeveel werknemers heeft u in loondienst? (0 als u er geen heeft): "))
geslacht = input("Wat is uw geslacht? (man/vrouw/anders): ")

dieren_dressuur = int(input("hoelang u heeft praktijkervaring met dieren-dressuur ? :"))
jogleren_1 = int(input("hoelang heeft u ervaring met jongleren ? :"))
acrobatiek = int(input("hoelang heeft u ervaring met acrobatiek ? :"))

snorlengte = 0
haarlengte = 0
glimlach_breedte = 0

MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220

DIEREN_ERVARING_NODIG = 4
JOGLEREN_2ERVARING = 5
ACROBATIEK_2ERVARING = 5
MIN_ONDERNEMER_JAREN = 3
MIN_WERKNEMERS = 5

MIN_SNOR_BREEDTE = 10
MIN_HAAR_LENGTE = 20
MIN_GLIMLACH_BREEDTE = 10

if geslacht == "man":
    snorlengte = int(input("Hoe breed is uw snor (in cm)? : "))
elif geslacht == "vrouw":
    haarlengte = int(input("Hoe lang is uw rood krulhaar (in cm)? : "))
else:
    glimlach_breedte = int(input("Hoe breed is uw glimlach (in cm)? : "))



if rijbewijs is "ja" and MIN_GEWICHT <= gewicht <= MAX_GEWICHT and MIN_LENGTE <= lengte <= MAX_LENGTE and (dieren_dressuur >= DIEREN_ERVARING_NODIG 
or jogleren_1 >= JOGLEREN_2ERVARING
 or  acrobatiek >= ACROBATIEK_2ERVARING) and (ondernemer_jaren >= MIN_ONDERNEMER_JAREN 
or aantal_werknemers >= aantal_werknemers) and (snorlengte >= MIN_SNOR_BREEDTE or haarlengte >= MIN_HAAR_LENGTE 
or glimlach_breedte >= MIN_GLIMLACH_BREEDTE) :
    print("goed")
else:
    print("no")  
    