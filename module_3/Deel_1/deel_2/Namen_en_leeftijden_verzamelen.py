def data_verzamelen():
    gegevens = []
    while True:
        naam = input("Wat is je naam: ")
        if naam.lower() == "stop":
            break
        leeftijd = int(input("Hoe oud bent u: "))
        gegevens.append(f"{naam} is {leeftijd} jaar")
    
    for item in gegevens:
        print(item)
    
    return gegevens

data_verzamelen()
