import random

kleuren = ("GROEN", "BLAUW", "ROOD")

nummer = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? :"))

mo = []
def zakje():
    for x in range(nummer):
        kleur = random.choice(kleuren)
        mo.append(kleur)
        mo.append("oranje")

for x in range(kleuren):
    print(x)
zakje()
print(f"aantal zakjes {nummer}\nen de kleuren: {mo}")