from functions import addition, subtraction, multiplication, division

def get_user_choice():
    print("Wat wilt u doen? ")
    print("A) getallen optellen")
    print("B) getallen aftrekken")
    print("C) getallen vermenigvuldigen")
    print("D) getallen delen")
    print("E) getal ophogen")
    print("F) getal verlagen")
    print("G) getal verdubbelen")
    print("H) getal halveren")
    print("I) niets")

    choice = input("Maak een keuze: ").strip().upper()
    return choice

def calculate_operation(nr1, nr2, operation):
    if operation == "A":
        result = addition(nr1, nr2)
    elif operation == "B":
        result = subtraction(nr1, nr2)
    elif operation == "C":
        result = multiplication(nr1, nr2)
    elif operation == "D":
        if nr2 == 0:
            print("Fout: Delen door nul is niet toegestaan.")
            result = None
        else:
            result = division(nr1, nr2)
    elif operation == "E":
        result = nr1 + nr2
    elif operation == "F":
        result = nr1 - nr2
    elif operation == "G":
        result = nr1 * 2
    elif operation == "H":
        result = nr1 / 2
    else:
        result = None
        print("Ongeldige keuze.")

    return result

def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")

def process_result(result):
    while True:
        print(f"Wil je wat met de uitkomst ({result}) doen?")
        print("A) iets optellen")
        print("B) iets aftrekken")
        print("C) met iets vermenigvuldigen")
        print("D) ergens door delen")
        print("E) ophogen")
        print("F) verlagen")
        print("G) verdubbelen")
        print("H) halveren")
        print("I) niets")

        choice = input("Maak een keuze: ").strip().upper()

        if choice == "I":
            break  # stop de loop als de gebruiker niets wil doen

        try:
            nr3 = get_float_input("Voer het derde getal in: ")

            if choice in ["A", "B", "C"]:
                result = calculate_operation(result, nr3, choice)
                if result is not None:
                    print("Nieuwe resultaat:", result)
            elif choice == "D":
                if nr3 == 0:
                    print("Fout: Delen door nul is niet toegestaan.")
                else:
                    result = calculate_operation(result, nr3, choice)
                    if result is not None:
                        print("Nieuwe resultaat:", result)
            elif choice == "E":
                result += nr3
                print("Nieuwe resultaat:", result)
            elif choice == "F":
                result -= nr3
                print("Nieuwe resultaat:", result)
            elif choice == "G":
                result *= 2
                print("Nieuwe resultaat:", result)
            elif choice == "H":
                result /= 2
                print("Nieuwe resultaat:", result)
            else:
                print("Ongeldige keuze.")

        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")

    print(f"Uiteindelijke resultaat: {result}")
    print("Einde van de bewerkingen.")

def bereken1():
    keuze = get_user_choice()
    nr1 = get_float_input("Voer eerste getal in: ")
    nr2 = get_float_input("Voer tweede getal in: ")

    resultaat = calculate_operation(nr1, nr2, keuze)
    
    if resultaat is not None:
        process_result(resultaat)

# Voorbeeld van hoe je het kunt gebruiken:
bereken1()
