def leeftijd_naam():
    dictonary = {}
    dictonary["name"] = input("Wat is je naam: ")
    dictonary["age"] = int(input("Hoe oud bent u: "))
    return dictonary
    # return {"name": naam, "age": leeftijd}

resultaat = leeftijd_naam()
print(f"{resultaat['name']} is {resultaat['age']} jaar")


# def leeftijd_naam():
#     dictonary = {}
#     naam = input("Wat is je naam: ")
#     leeftijd = int(input("Hoe oud bent u: "))
#     dictonary["name"] = naam
#     dictonary["age"] = leeftijd
#     return dictonary
    # return {"name": naam, "age": leeftijd}