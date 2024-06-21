def leeftijd_naam():
    dictonary = {}
    dictonary["name"] = input("Wat is je naam: ")
    dictonary["age"] = int(input("Hoe oud bent u: "))
    return dictonary





def data_verzamelen():
    gegevens = []
    while True:
        dicto = leeftijd_naam()
        if dicto["name"] == "stop":
            break
        gegevens.append(f"{ dicto["name"]} is {dicto["age"]} jaar")
    
    # for item in gegevens:
    #     print(item)
    
    return gegevens
lijst = data_verzamelen()
for x in lijst:
    print(x)