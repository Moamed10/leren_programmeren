from fruitmand import fruitmand
import random


aantal_keer = int(input('hoveel keer '))

# for aantal in range(aantal_keer):
#     x = random.randint(0,6)
#     print(fruitmand[x]['name'])
    


lengte = len(fruitmand )


for aantal in range(aantal_keer):
    x = random.randint(0,lengte -1)
    print(fruitmand[x]['name'])


