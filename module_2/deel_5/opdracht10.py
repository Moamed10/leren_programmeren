from fruitmand import fruitmand
gewichts = []
for fruit in fruitmand:
    gewichts.append(fruit['weight'])
gewichts.sort(reverse=True)
print(gewichts)
