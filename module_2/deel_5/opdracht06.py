from fruitmand import fruitmand
for fruit in fruitmand:
    if fruit["name"] == 'appel':
        print(f"het gewicht wordt {fruit['weight']}")


for fruit in fruitmand:
    print(f"het gewicht van {fruit['name']} wordt {fruit['weight']} ")