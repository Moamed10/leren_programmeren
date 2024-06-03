def gulden(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    getal = [0, 1]
    for x in range(2, n):
        getal.append( getal[-1] + getal[-2])
    return getal

# def goud(a):
#     if len(a) < 2:
#         return None
#     return a[-1] / a[-2]
    

a = gulden(3)
print(a)

# golden_ratio = goud(a)
# print(golden_ratio)
