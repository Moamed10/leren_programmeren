import random

kleuren = ("ORANJE", "BLAUW", "ROOD")

aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? : "))
mo = []

def zakje():
    for _ in range(aantal):
        kleur = random.choice(kleuren)
        mo.append(kleur)

zakje()
print(f"De hoeveelheid M&M's in de zak: {aantal}\nEn de kleuren: {mo}")
