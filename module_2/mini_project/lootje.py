import random

namen_lijst = []

ok = True
while ok:
    naam = input("Voer een naam in: ")
    if naam in namen_lijst:
        print("Deze naam is al ingevoerd. Voer een unieke naam in.")
    else:
        namen_lijst.append(naam)
        if len(namen_lijst) >= 3:
            extra_naam_optie = input("Wil je nog een naam invoeren? (ja/nee): ") 
            if extra_naam_optie.lower() == "nee":
                ok = False





copy_lijst = namen_lijst.copy()
random.shuffle(copy_lijst)

again = True

while again:
    namen_dict = {}
    for x in range(len(namen_lijst)):
        if namen_lijst[x] == copy_lijst[x]:
            random.shuffle(copy_lijst)
            break
        else:
            namen_dict[ namen_lijst[x]] = copy_lijst[x]

    if 
    len(namen_dict) == len(namen_lijst):
        again = False

for key, value in namen_dict.items():
    print(key, ":", value)







# while again:
#     namen_dict = {}



# while again:
#     namen_dict = {}
#     for x in range(len(namen_lijst)):
#         if namen_lijst[x] == copy_lijst[x]:
#             random.shuffle(copy_lijst)
#             break
#         else:
#            namen_lijst[x][naam] = copy_lijst[x]
#            again=False

# for key, value in namen_dict.items():
#     print(key, ":", value)





# for x in range(len(namen_lijst)):
#     print(f"{namen_lijst[x]} : {copy_lijst[x]}")
    





    # for naam, lootje in [namen_lijst, copy_lijst]:










# welke_naam = input("welke naam wil je zien ? ")
# print(f"{welke_naam} heeft het lootje {namen_dict[welke_naam]}")
# for key, value in namen_dict.items():
#     print(key, ":", value)

# while again:
#     namen_dict = {}
#     for naam, lootje in zip(namen_lijst, copy_lijst):
#         if naam == lootje:
#             random.shuffle(copy_lijst)
#             break
#         else:
#             namen_dict[naam] = lootje


#     if len(namen_dict) == len(namen_lijst):
#         again = False

