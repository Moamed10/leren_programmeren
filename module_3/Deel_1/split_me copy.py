import math
import random
from collections import Counter

def is_lijst_leeg(getallen):
    return not getallen

def controleer_getal(getal):
    return str(getal).isnumeric()

def bereken_som(getallen):
    return sum(getallen)

def tel_aantal(getallen):
    return len(getallen)

def bereken_gemiddelde(getallen):
    som = bereken_som(getallen)
    aantal = tel_aantal(getallen)
    return som / aantal

def vind_grootste_getal(getallen):
    return max(getallen)

def vind_kleinste_getal(getallen):
    return min(getallen)

def eerste_getal(getallen):
    return getallen[0]

def deel_door_getal(getal, controlegetal):
    return getal / controlegetal

def unieke_getallen(getallen):
    return list(set(getallen))

def tel_unieke_elementen(unieke_getallen):
    return len(unieke_getallen)

def verschil_tussen_getallen(getal1, getal2):
    return abs(getal1 - getal2)

def sorteer_lijst(getallen):
    return sorted(getallen)

# dit heb ik met behulp van chat_gbt 
def tel_elementen(getallen):  
    return dict(Counter(getallen))

def deelbaar_door_getal(getallen, controlegetal):
    return sorted([getal for getal in getallen if getal % controlegetal == 0])

def controleer_aanwezigheid(getallen, controlegetal1, controlegetal2):
    return controlegetal1 in getallen and controlegetal2 in getallen

def vind_posities(getallen, controlegetal):
    return [index for index, getal in enumerate(getallen) if getal == controlegetal]

def bereken_standaardafwijking(getallen, gemiddelde):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / len(getallen)
    return math.sqrt(variantie)

def shuffle_lijst(getallen):
    random.shuffle(getallen)
    return getallen

def kies_random_getal(getallen):
    return random.choice(getallen)

def analyseer_getallenlijst(getallen, controlegetal1, controlegetal2):
    if is_lijst_leeg(getallen):
        return {"Lijst is leeg, voer getallen in.": getallen}

    if not controleer_getal(controlegetal1):
        return {"Eerste controle getal incorrect.": controlegetal1}

    if not controleer_getal(controlegetal2):
        return {"Tweede controle getal incorrect.": controlegetal2}

    aantal = tel_aantal(getallen)
    som = bereken_som(getallen)
    gemiddelde = bereken_gemiddelde(getallen)
    grootste_getal = vind_grootste_getal(getallen)
    kleinste_getal = vind_kleinste_getal(getallen)
    eerste = eerste_getal(getallen)
    delen1 = deel_door_getal(kleinste_getal, controlegetal1)
    delen2 = deel_door_getal(grootste_getal, controlegetal2)
    unieke_getallen_lijst = unieke_getallen(getallen)
    aantal_unieke_elementen = tel_unieke_elementen(unieke_getallen_lijst)
    verschil1 = verschil_tussen_getallen(aantal_unieke_elementen, controlegetal1)
    gesorteerde_lijst = sorteer_lijst(getallen)
    gesorteerde_unieke_lijst = sorteer_lijst(unieke_getallen_lijst)
    telling_elementen = tel_elementen(getallen)
    deelbaar1 = deelbaar_door_getal(unieke_getallen_lijst, controlegetal1)
    deelbaar2 = deelbaar_door_getal(unieke_getallen_lijst, controlegetal2)
    komtvoor = controleer_aanwezigheid(getallen, controlegetal1, controlegetal2)
    posities = vind_posities(getallen, controlegetal1)
    standaardafwijking = bereken_standaardafwijking(getallen, gemiddelde)
    geshuffelde_lijst = shuffle_lijst(getallen[:])  # Gebruik een kopie van de lijst om de originele lijst te behouden
    random_getal = kies_random_getal(geshuffelde_lijst)
    verschil2 = verschil_tussen_getallen(random_getal, controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_unieke_lijst,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": geshuffelde_lijst,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten

# Voorbeeld van het gebruik van de functie:
if __name__ == "__main__":
    getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
    controlegetal1 = 8
    controlegetal2 = 3
    analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
    print("Analyse resultaten:")
    for key, value in analyse_resultaat.items():
        print(f"{key}: {value}")
