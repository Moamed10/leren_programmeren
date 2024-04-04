from fruitmand import fruitmand
from fruitmand import fruitmand
# Vertalingen van kleuren
kleur_vertaling = {
    'red': 'rood',
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'brown' : 'bruin'

}
lijst = [ ]
for fruit in fruitmand:
     lijst.append(fruit['name'])
     langste =  (max(lijst, key=len))
     fruit['color'].replaced[kleur_vertaling]

gewicht = langste['weight']
print(gewicht)
# langste =  (max(lijst, key=len))

print(f"de lansgte fruitnaam is {langste} en heeft het kleur")