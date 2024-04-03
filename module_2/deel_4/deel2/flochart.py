import random

ronde = 0
punten = 0

while ronde < 20:
    kansen = 0
    getal = random.randint(1, 1000)
    print("Ronde:", ronde + 1)
    
    while kansen < 10:
        # print(getal)
        keuze = int(input("Raad het getal tussen 1 en 1000: "))
        # print(getal)
        verschil = getal - keuze
        
        if getal == keuze:
            ronde += 1
            punten += 1
            print("Je hebt het goed geraden!")
            goedgeraden = input("Wil je een nieuwe ronde beginnen? ja/nee: ")
            if goedgeraden.lower() == "nee":
                print(f"Je score wordt {punten} punten. Tot ziens!")
                ronde = 20  
                break
            # else:
            #     break
        elif getal != keuze:
            kansen += 1
            if getal > keuze:
                print("Fout, het getal is hoger.")
            else:
                print("Fout, het getal is kleiner.")
                
            if abs(verschil) < 20: 
                print("Je bent heel warm.")
            elif abs(verschil) < 50:
                print("Je bent warm.")
                
        if kansen == 10:
            print(f"Je hebt 10 keer geraden. Het getal was: {getal}")
            ronde += 1
            if ronde < 20:
                again = input("Wil je nog een ronde spelen? ja/nee: ")
                if again.lower() == "nee":
                    print(f"Je score is {punten} punten. Tot ziens!")
                    ronde = 20  
                    break

print(f"Je eindscore is: {punten} punten.")
