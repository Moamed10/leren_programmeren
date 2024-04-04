from fruitmand import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit["name"] != "druif":
        kleur = fruit['color']
        if kleur not in kleuren:
            kleuren.append(kleur)
print(kleuren)
