while True:
    kaas_geel = input("Is de kaas geel? Ja/Nee: ").lower()
    
    if kaas_geel == "ja":
        gaten_in = input("Zitten er gaten in? Ja/Nee: ").lower()
        if gaten_in == "ja":
            duur = input("Is de kaas duur? Ja/Nee: ").lower()
            if duur == "nee":
                print("Je bedoelt Leerdammer.")
                break  
            elif duur == "ja":
                print("Je bedoelt Emmentaler.")
                break  
        elif gaten_in == "nee":
            hard_kaas = input("Is de kaas hard als steen? Ja/Nee: ").lower()
            if hard_kaas == "nee":
                print("Je bedoelt Goudse kaas.")
                break  
            else:
                print("Je bedoelt Parmigiano Reggiano.")
                break  
    elif kaas_geel == "nee":
        schemmel = input("Heeft de kaas blauwschimmel? Ja/Nee: ").lower()
        if schemmel == "ja":
            korst = input("Heeft de kaas een korst? Ja/Nee: ").lower()
            if korst == "ja":
                print("Je bedoelt Blue de Roquefort.")
                break  
            elif korst == "nee":
                print("Je bedoelt Fourme d'Ambert.")
                break  
        else:
            print("Je bedoelt Mozzarella.")
            break  
    else:
        print("fout.")
