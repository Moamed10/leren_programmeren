from fruitmand import fruitmand
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
for fruit in fruitmand:
    kleuren = set([fruit['color'] for fruit in fruitmand])
    
print(kleuren)


# for kleur in kleuren:
#     print(kleur)
