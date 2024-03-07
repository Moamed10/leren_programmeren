vertaal_dict = {
    "hart": "ingang",
    "grot": "geit",
    "Draganthor": "Drakanthor",
    "schubben": "teennagels",
    "vurige": "waterende"
}

input_tekst = input("Voer een stukje tekst in: ")


# print(vertaal_dict.keys())
for key,waarde in vertaal_dict.items():
    if key in input_tekst:
        input_tekst=input_tekst.replace(key,waarde)

print(input_tekst)
