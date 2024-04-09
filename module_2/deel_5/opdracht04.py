from fruitmand import fruitmand
import random

aantal_keer = int(input('hoveel keer ? '))
lengte = len(fruitmand )
for _ in range(aantal_keer):
   fruit =(random.choice(fruitmand))
   print(fruit['name'])





    # x = random.randint(0,lengte )
    # print(fruitmand[x]['name'])


