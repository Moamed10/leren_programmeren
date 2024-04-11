from fruitmand2 import fruitmand
kleuren = []
# print(fruitmand)
for fruit in fruitmand:
 kleur = fruit['color']
 if fruit["name"] == "druif":
    fruitmand.remove(fruit)
 elif kleur not in kleuren:
      kleuren.append(kleur)



#     kleur = fruit['color']
#  elif kleur not in kleuren: 
#     kleuren.append(kleur)

# for fruit in fruitmand:
#     if fruit["name"] != "druif":
#         kleur = fruit['color']
#         if kleur not in kleuren:
#             kleuren.append(kleur)
print(kleuren)
# print(fruitmand)
