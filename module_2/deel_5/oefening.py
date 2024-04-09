from fruitmand import fruitmand

kleuren = set([fruit['color'] for fruit in fruitmand])
round = 0
not_round = 0 

vraag = input("Kies een kleur: ")

while vraag not in kleuren:
    vraag = input("Fout, kies een andere kleur: ")

for fruit in fruitmand:
    if fruit["color"] == vraag:
        round += 1
    elif fruit["color"] == vraag and fruit["round"] == False:
        not_round += 1

if round > not_round:
    print(f"Er zijn {round - not_round} meer ronde vruchten dan niet-ronde vruchten in de kleur {vraag}.")
elif not_round > round :
    print(f"Er zijn {not_round - round} meer niet-ronde vruchten dan ronde vruchten in de kleur {vraag}.")
else:
    print(f"Er zijn {round} ronde vruchten en {not_round} niet-ronde vruchten in de kleur {vraag}.")
