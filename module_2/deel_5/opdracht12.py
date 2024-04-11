from fruitmand import fruitmand

# Vertalingen van kleuren
kleur_vertaling = {
    'red': 'rood',
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'brown': 'bruin'
}

# Lijst om fruitnamen op te slaan
fruit_namen = []

# Loop door de fruitmand om de fruitnamen op te slaan en de langste fruitnaam te vinden
for fruit in fruitmand:
    fruit_namen.append(fruit['name'])

def get_weight(data: dict) -> float:
    return data.get('weight', 0)


# Vind de langste fruitnaam
langste = max(fruit_namen, key=len)

# Vind het fruitobject met de langste naam
langste_fruit = next((fruit for fruit in fruitmand if fruit['name'] == langste), None)

# Vertaal de kleur van het langste fruit
if langste_fruit and 'color' in langste_fruit:
    kleur = langste_fruit['color']
    vertaalde_kleur = kleur_vertaling.get(kleur, kleur)
else:
    vertaalde_kleur = "onbekend"

print(f"De langste fruitnaam is '{langste}' en het heeft de kleur '{vertaalde_kleur}'.")
