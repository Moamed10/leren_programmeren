PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
kleuren = ("blauw", "rood")

leeftijd = int(input("Hoe oud ben je? "))
leeftijd_verschil = 18 - leeftijd

if leeftijd >= 18:
    naam = input("Wat is je naam? ")
    if naam.lower() in VIP_LIST and leeftijd >= 21:
        print("Je krijgt een blauw bandje.")
        bandje = True
        kleur = "blauw"
    elif naam.lower() in VIP_LIST and leeftijd < 21:
        print("Je krijgt een rood bandje.")
        bandje = True
        kleur = "rood"
    elif naam.lower() not in VIP_LIST and leeftijd >= 21:
        print("Je krijgt van mij een stempel.")
        bandje = False
        stammbel = True
    elif naam.lower() not in VIP_LIST and leeftijd < 21:
        bandje = False
        stammbel = False
    drinken = input("Wat wil je drinken? 'cola', 'bier', 'champagne' ")
    if bandje is True and kleur == "blauw" and drinken.lower() in DRANKJES:
        print("Alsjeblieft, complimenten!")
    elif drinken.lower() not in DRANKJES:
        print("Sorry, geen idee wat je bedoelt. Hier is een glas water.")
    elif bandje is True and kleur == "rood" and drinken.lower() in DRANKJES:
        if drinken.lower() == "cola" or drinken.lower() == "bier":
            print("Aub, complimenten van het huis.")
        elif drinken.lower() == 'champagne':
            print("Sorry, je mag geen alcohol drinken onder de 21.")
        else:
            print("Hier is een glas water.")
    elif bandje is False and stammbel is True:
        if drinken.lower() == "cola":
            print(f"Het wordt {PRIJS_COLA}.")
        elif drinken.lower() == "bier":
            print(f"Het wordt {PRIJS_BIER}.")
        elif drinken.lower() == 'champagne':
            print("Sorry, alleen VIP's kunnen champagne drinken.")
        else:
            print("Ik snap het niet. Hier is een glas water.")
    elif bandje is False and stammbel is False:
        if drinken.lower() == "cola":
            print(f"Het wordt {PRIJS_COLA}.")
        elif drinken.lower() == "bier":
            print("Je mag geen alcohol drinken onder de 21.")
        elif drinken.lower() == "champagne":
            print("Alleen VIP's mogen champagne en onder de 21 mag je geen alcohol drinken. Probeer het in 2025.")
else:
    print(f"Je mag niet naar binnen. Probeer het in {2024 + leeftijd_verschil}.")
