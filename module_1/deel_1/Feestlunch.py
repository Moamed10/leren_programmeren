aantal_croissantjes = 17
prijs_per_croissantje = 0.39

aantal_stokbroden = 2
prijs_per_stokbrood = 2.78

aantal_kortingsbonnen = 3
waarde_per_kortingsbon = 0.50

totale_kosten_zonder_korting = (aantal_croissantjes * prijs_per_croissantje) + (aantal_stokbroden * prijs_per_stokbrood)

totale_korting = aantal_kortingsbonnen * waarde_per_kortingsbon

uiteindelijke_kosten = totale_kosten_zonder_korting - totale_korting

print(f"Totale kosten zonder korting: {totale_kosten_zonder_korting:.2f} euro")
print(f"Totale korting: {totale_korting:.2f} euro")
print(f"Uiteindelijke kosten met korting: {uiteindelijke_kosten:.2f} euro")
