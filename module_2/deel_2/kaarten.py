import random

# Genereer een deck met 4 kleuren en 13 kaarten per kleur (2-10, boer, vrouw, heer, aas)
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten_per_kleur = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
deck = [(kleur, kaart) for kleur in kleuren for kaart in kaarten_per_kleur]

# Voeg 2 jokers toe aan het deck
deck.extend([('joker', '1'), ('joker', '2')])

# Schud het deck
random.shuffle(deck)

# Toon de bovenste 7 kaarten
bovenste_zeven = deck[:7]
print("Bovenste 7 kaarten:")
for kaart in bovenste_zeven:
    print(f"{kaart[1]} van {kaart[0]}")

# Toon de overige kaarten in het deck
overige_kaarten = deck[7:]
print("\nOverige kaarten in het deck:")
for kaart in overige_kaarten:
    print(f"{kaart[1]} van {kaart[0]}")
