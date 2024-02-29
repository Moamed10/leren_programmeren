vertaal_dict = {
    "hart": "ingang",
    "grot": "geit",
    "Draganthor": "Drakanthor",
    "schubben": "teennagels",
    "vurige": "waterende"
}

input_tekst = input("Voer een stukje tekst in: ")

mo = 0
for key,waarde in vertaal_dict.items():
    if key in input_tekst:
     input_tekst = input_tekst.replace(key,waarde)


print(input_tekst)

# vertaal_dict["kleur"] = "rood "

print(vertaal_dict)