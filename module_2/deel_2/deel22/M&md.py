
import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

nummer = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? :"))

mo = {}

def zakje():
    for x in range(nummer):
        if x == 0:
            # Voeg altijd "rood" toe bij de eerste iteratie
            kleur = "rood"
        else:
            kleur = random.choice(kleuren)

        if kleur in mo:
            mo[kleur] += 1
        else:
            mo[kleur] = 1

zakje()
print(mo)








