
import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

nummer = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? :"))

mm = {"zwart": 0}

def zakje():
    for x in range(nummer):
        kleur = random.choice(kleuren)

        if kleur in mm:
            mm[kleur] += 1
        else:
            mm[kleur] = 1
        mm["zwart"] = (mm["blauw"])
        
        
zakje()
print(mm)
