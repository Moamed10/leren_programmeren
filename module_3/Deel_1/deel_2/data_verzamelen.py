def data_verzamelen():
    gegevens = []
    while True:
        naam = input("Wat is je naam: ")
        if naam.lower() == "stop":
            break
        leeftijd = int(input("Hoe oud bent u: "))
        woonplaats = input("Wat is je woonplaats: ")
        gegevens.append({"name": naam, "age": leeftijd, "city": woonplaats})
    
    return gegevens
