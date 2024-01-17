import random
kleuren = ["Harten", "Ruiten", "Klaveren", "Schoppen"]
waareds = list(map(str, range(2, 11))) + ["Boer", "Vrouw", "Heer", "Aas"]
deck = []
for kleur in kleuren:
    for waarde in waareds:
        kaart = f"{waarde} van {kleur}"
        deck.append(kaart)
deck.append("Joker")
deck.append("Joker")
random.shuffle(deck)
bovenste_7 = deck[:7]
overige_kaarten = deck[7:]
aantal = len(overige_kaarten)
print("Bovenste 7 kaarten:" )
for kaart in bovenste_7:
    print(kaart)
print(f"\nOverige kaarten in het deck: {aantal}")
for kaart in overige_kaarten:
    print(kaart, end=", ")
