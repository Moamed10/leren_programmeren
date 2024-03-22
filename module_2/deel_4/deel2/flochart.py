import random
import math
ronde = 0
punten = 0 

while ronde < 20:
    kansen = 0
    getal = random.randint(1,1000)
    while kansen < 10:

        print(getal)
        keuze = int(input("raad het getal tussen 1 en 1000 : "))
        print(getal)
        verschil = getal - keuze
        if getal == keuze:
            ronde +=1
            punten +=1
            print("je hebt het goed ")
            goedgeraden = input("wil je nieuw ronde beginne ? ja/nee ")
            if goedgeraden.lower() == "nee":
                print(f"je score wordt {punten} punten ,, good bye")
                break
        elif getal != keuze:
            kansen +=1
            if getal > keuze:
                print("fout hoger ")
            else:
                (" fout kleiner")
            if abs(verschil) < 20 : 
                print("je bent heel warm ")
            elif abs(verschil) < 50:
                print("je bent  warm ") 
        if kansen == 10:
            print(f"je hebt 10 x geraden het getal was {getal}")
            ronde +=1
            if ronde <= 20:
             again =  input("wil ej nog een ronde spelen ? ja/nee")
             if again == "nee":
                 print(punten )
                 break

                



    