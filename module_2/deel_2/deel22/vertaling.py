vertaal_dict = {
    "hart": "ingang",
    "grot": "geit",
    "Draganthor": "Drakanthor",
    "schubben": "teennagels",
    "vurige": "waterende"
}

input_tekst = input("Voer een stukje tekst in: ")


# fouten  = 0
for key in vertaal_dict:
    if key in input_tekst:
     input_tekst = input_tekst.replace(key,vertaal_dict[key])


print(input_tekst)

# print(vertaal_dict)