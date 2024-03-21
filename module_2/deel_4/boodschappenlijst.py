boodschappenlijst = {}

while True:
    artikel = input("Welk artikel wil je toevoegen? ")
    aantal = int(input(f"Hoeveel {artikel} wil je toevoegen? "))

    if artikel in boodschappenlijst:
        boodschappenlijst[artikel] += aantal
    else:
        boodschappenlijst[artikel] = aantal

    stoppen = input("Wil je nog meer dingen toevoegen? (j/n) ")
    if stoppen.lower() == "n":
        break



print("-[BOODSCHAPPENLIJST]-")
for x,y in boodschappenlijst.items():
    print(" ",y, "x" ,x)

print("----------------------")