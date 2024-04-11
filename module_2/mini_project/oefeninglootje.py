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
            extra_naam_optie = input("Wil je nog een naam invoeren? (ja/nee): ").lower() 
            if extra_naam_optie == "nee":
                ok = False

copy_lijst = namen_lijst.copy()
random.shuffle(copy_lijst)
again = True

while again:
    namen_dict = {}
    for naam, lootje in zip(namen_lijst, copy_lijst):
        if naam == lootje:
            random.shuffle(copy_lijst)
        else:
            namen_dict[naam] = lootje

    if len(namen_dict) == len(namen_lijst):
        again = False

for key, value in namen_dict.items():
    print(key, ":", value)






