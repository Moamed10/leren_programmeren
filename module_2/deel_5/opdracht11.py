from fruitmand import fruitmand
for fruit in fruitmand:
    kleuren = set([fruit['color'] for fruit in fruitmand])

round = 0
not_round = 0 

vraag = input("kiez een kleur ")
while vraag not in kleuren:
    vraag = input("fout kies andere kleur een kleur ")
    if vraag in kleuren:
        for fruit in fruitmand:
            if fruit["color"] == vraag and fruit["round"] == True:
                round +=1
            elif fruit["color"] == vraag and fruit["round"] == False:
                not_round +=1
                if round > not_round:
                    print(f"er zijn {round - not_round } meer ronde vruchten dan niet ronde vruchten in de kleur {vraag}")
                elif not_round > round :
                    print(f"er zijn {not_round - round } meer rondnit ronde e vruchten dan niet ronde vruchten in de kleur {vraag}")
                else:
                    print(f"er zijn {round} vruchten en {not_round} vruchten in kleur {vraag}")

print(round,not_round)

    







# for fruit in fruitmand:
#     if fruit["color"] == "red" and fruit["round"] == True:
#          round +=1
#     elif fruit["color"] == "red" and fruit["round"] == False:
#         not_round +=1