# rekenmachine.py

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

def main():
    result = None
    while True:
        if result is None:
            choice = get_user_choice()
        else:
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

        if choice == 'I':
            print(f"Eindprogramma. Laatste resultaat: {result}")
            return

        if choice in ['A', 'B', 'C', 'D']:
            n1 = float(input("Voer het eerste getal in: ")) if result is None else result
            n2 = float(input("Voer het tweede getal in: "))
        elif choice in ['E', 'F', 'G', 'H']:
            n1 = float(input("Voer het getal in: ")) if result is None else result
            n2 = 1 if choice in ['E', 'F'] else 2
        else:
            print("Ongeldige keuze, probeer opnieuw.")
            continue

        if choice == 'A':
            result = addition(n1, n2)
            operation = '+'
        elif choice == 'B':
            result = subtraction(n1, n2)
            operation = '-'
        elif choice == 'C':
            result = multiplication(n1, n2)
            operation = 'x'
        elif choice == 'D':
            result = division(n1, n2)
            operation = ':'
        elif choice == 'E':
            result = addition(n1, n2)
            operation = '+'
        elif choice == 'F':
            result = subtraction(n1, n2)
            operation = '-'
        elif choice == 'G':
            result = multiplication(n1, n2)
            operation = 'x'
        elif choice == 'H':
            result = division(n1, n2)
            operation = ':'
        else:
            print("Ongeldige keuze, probeer opnieuw.")
            continue

        print(f"Resultaat: {n1} {operation} {n2} = {result}")

main()
