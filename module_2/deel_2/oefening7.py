import random

kleuren = ("ORANJE", "BLAUW", "ROOD")

nummer = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? :"))

mo = []
def zakje():
    for _ in range(nummer):
        kleur = random.choice(kleuren)
        mo.append(kleur)


# zakje()
print(f"aantal zakjes {nummer}\nen de kleuren: {mo}")