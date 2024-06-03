def leeftijd_naam():
    naam = input("Wat is je naam: ")
    leeftijd = int(input("Hoe oud bent u: "))
    return {"name": naam, "age": leeftijd}

resultaat = leeftijd_naam()
print(f"{resultaat['name']} is {resultaat['age']} jaar")
