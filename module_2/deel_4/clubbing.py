PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
kleuren = ("blauw" , "rood")

#bouw hieronder de floowchart na
leeftijd = int(input("hoe oud ben je ? "))
leeftijd_verschil = 18 - leeftijd
if leeftijd >= 18:
    naam = input("wat is je naam ? ")
    if naam.lower() in VIP_LIST and leeftijd >=21 :
        print("je krijgt blauw bandje ")
        bandje = True 
        kleur = "blauw"
    elif naam.lower() in VIP_LIST and leeftijd < 21 :
        print("je krijgt rood bandje ")
        bandje = True
        kleur = "rood"
    elif naam.lower()  not in VIP_LIST and leeftijd >=21:
        print("je krijgt van mij stembel")
        bandje = False
        stammbel = True
    elif naam.lower()  not in VIP_LIST and leeftijd <21:
        bandje = False
        stammbel = False
    drinken = input("wat wil je drinken ? 'cola', 'bier', 'champagne' ")
    if bandje is True and kleur == "blauw" and drinken.lower() in DRANKJES:
        if drinken ==""
        print("alsjeblieft complimenten ")
    elif drinken.lower() not in DRANKJES:
        print("sorry gen idee wat je bedoelt hier is een glasje water ")
    elif bandje is True and kleur == "rood" and drinken.lower() in DRANKJES:
        if drinken.lower() == "cola" or "bier":
            print("aub compimenten van het huis ")
        elif drinken.lower() == 'champagne':
            print("sorry je mag geen alcohol drinken onder 21")
        else:
            print("hier is een glas water ")
    elif bandje is  False and stammbel is True:
        if drinken.lower() == "cola":
            print(f"het wordt {PRIJS_COLA}")
        elif drinken.lower() =="bier":
            print(f"wordt {PRIJS_BIER}")
        elif drinken.lower() == 'champagne':
            print("sorry allen vip kan champagne drinken ")
        else:
            print("ik snap het niet hier is een glas water ")
    elif  bandje is  False and stammbel is False:
        if drinken.lower() == "cola":
            print(f"het wordt {PRIJS_COLA}")
        elif drinken.lower() =="bier":
            print("je mag geen alcohol drinken onder 21 ")
        elif drinken =="champagne":
            print(f"allen vip mogen champagne en onder 21 mag je geen alcohol propeer het in 2025 ")
else:
    print(f"je mag niet naaaar binnen propeer het in {2024 + leeftijd_verschil}")


            
        


    







    