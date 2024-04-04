from fruitmand import fruitmand



def fruitmand_gewicht():
    gewicht = 0
    for fruit in fruitmand:
     gewicht += fruit['weight']
    print(gewicht)


fruitmand_gewicht()

fruitmand.append({'name': 'watermeloen', 'weight': 5000})

fruitmand_gewicht()

