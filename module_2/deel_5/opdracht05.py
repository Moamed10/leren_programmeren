from fruitmand import fruitmand


for fruit in reversed(fruitmand):
    print(fruit['name'])


for fruit in fruitmand[6:0:-1]:
    print(fruit['name'])
