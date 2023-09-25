# Maak een programma person.py dat de gebruiker om zijn naam, adres, postcode en woonplaats vraagt met duidelijke prompts.

# Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal:

#  ----------------------------------------------------
# |  Naam      : Fabian van Zandt                
# |  Adres     : Koekenbakkersplein 23           
# |  Postcode  : 2834 EF                         
# |  Woonplaats: Houten                          
#  ----------------------------------------------------

name = str(input("what is your name ?"))
adres = str(input("what is your adres ?"))
postal_code = (input("what is your postal code ?"))
place = str(input("where do  you live ?"))

print("-" * 30)
print(f"| Name : {name}")
print(f"| Adres : {adres}")
print(f"| Postal code : {postal_code}")
print(f"| Place : {place}")
print("-" * 30)
