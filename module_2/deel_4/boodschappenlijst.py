def maak_boodschappenlijst():
    boodschappenlijst = {}

    while True:
        item = input("Voer het item in (of typ 'stop' om te stoppen): ").strip().lower()
        
        if item == 'stop':
            break
        
        hoeveelheid = int(input("Voer de hoeveelheid in: "))

        if item in boodschappenlijst:
            boodschappenlijst[item] += hoeveelheid
        else:
            boodschappenlijst[item] = hoeveelheid

    print("\nBoodschappenlijstje:")
    for item, hoeveelheid in boodschappenlijst.items():
        print(f"{item.capitalize()}: {hoeveelheid}")

maak_boodschappenlijst()
