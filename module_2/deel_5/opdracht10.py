from fruitmand import fruitmand
# gewichts = []
# for fruit in fruitmand:
#     gewichts.append(fruit['weight'])
# gewichts.sort(reverse=True)
# print(gewichts)



def get_weight(data: dict) -> float:
    return data.get('weight', 0)

fruitmand.sort(key=get_weight, reverse=True)
print(fruitmand)