import random
kleuren = ["Harten", "Ruiten", "Klaveren", "Schoppen"]
waareds = [ 2,3,4,5,6,7,8,9,10,"Boer", "Vrouw", "Heer", "Aas"]
deck = []
for kleur in kleuren:
    for waarde in waareds:
        kaart = f"{waarde} van {kleur}"
        deck.append(kaart)
deck.append("Joker")
deck.append("Joker")
random.shuffle(deck)
print("Bovenste 7 kaarten:" )
for x in range(7):
    print(deck.pop(0))   
print(f"\nOverige kaarten in het deck: {len(deck)}")
print(deck)
# for kaart in overige_kaarten:
#     print(kaart, end=", ")


# bovenste_7 = deck[:7]
# overige_kaarten = deck[7:]
# aantal = len(overige_kaarten)
# print("Bovenste 7 kaarten:" )
# for kaart in bovenste_7:
#     print(kaart)
# print(f"\nOverige kaarten in het deck: {len(dec)}")
# for kaart in overige_kaarten:
#     print(kaart, end=", ")



# waareds = list(map(str, range(2, 11))) + ["Boer", "Vrouw", "Heer", "Aas"]
