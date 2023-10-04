
OPTIES = print("Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit")
vragen_1 = [
    'Ik voel stress of blokkades bij het maken van programmeeropdrachten.',
    'Ik stel programmeeropdrachten en -uitdagingen uit.',
    'Ik denk dat ik geen talent heb voor de opleiding.',
    'Ik vermijd assessments (CJV) en feedback van kritische docenten.',
    'Ik vergelijk mezelf met anderen die beter lijken te zijn.',
    'Ik voel geen interesse in nieuwe programmeertechnieken.',
    'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'
]
totaal_vragen = 0

aantwoorden = []
for steling in vragen_1:
    totaal_vragen += 1
    print (steling)
    print(OPTIES)
    aantwoord = int(input("Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"))
    aantwoorden.append(aantwoord)

totaal_aantworden = sum(aantwoorden) 
gemmideld_score = totaal_aantworden / totaal_vragen

 






if gemmideld_score <= 2:
    print("Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.")


if gemmideld_score == 3:
    print("Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaartin het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!")

if gemmideld_score == 4:
    print("Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart inhet leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!")



print(f"you aantwoorde {aantwoorden}")