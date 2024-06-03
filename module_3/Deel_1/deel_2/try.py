def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Hoe oud bent u? "))
    return {'name': naam, 'age': leeftijd}

# Roep de functie aan en print het resultaat
resultaat = vraag_naam_en_leeftijd()
print(f"{resultaat['name']} is {resultaat['age']} jaar")
