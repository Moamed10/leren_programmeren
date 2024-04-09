from fruitmand import fruitmand

def fruitmand_gewicht():
    gewicht = 0
    for fruit in fruitmand:
     gewicht += fruit['weight']
    return gewicht

print(fruitmand_gewicht())



fruitmand.append({'name': 'watermeloen', 'weight': 5000})

print(fruitmand_gewicht())

