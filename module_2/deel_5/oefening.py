from fruitmand import fruitmand

# Vertalingen van kleuren
kleur_vertaling = {
    'red': 'rood',
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'brown': 'bruin'
}

# Zoek het fruit met de langste naam
langste_fruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

# Vertaal de kleur van het fruit
kleur = kleur_vertaling.get(langste_fruit['color'], langste_fruit['color'])

# Print de gegevens van het fruit met de langste naam
print(f"De langste fruitnaam is '{langste_fruit['name']}' met de kleur '{kleur}' en het gewicht {langste_fruit['weight']} gram.")
