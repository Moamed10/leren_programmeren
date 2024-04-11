from fruitmand import fruitmand
 
kleur_vertaling = {
    'yellow': 'gele',
    'green': 'groene',
    'orange': 'oranje',
    'red': 'rode',
    'brown': 'bruine'
}
 
 

def get_lenthname(x: dict) :
    return len(x['name'])

langste_naam_fruit = max(fruitmand, key= get_lenthname)

 
# vertaalde_kleur = kleur_vertaling.get(langste_naam_fruit['color'])


vertaalde_kleur = kleur_vertaling[langste_naam_fruit['color']]

print(f"Het fruit met de langste naam is de {vertaalde_kleur} {langste_naam_fruit['name']} met een gewicht van {langste_naam_fruit['weight']} gram.")
 