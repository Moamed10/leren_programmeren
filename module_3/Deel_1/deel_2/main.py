from data_verzamelen import data_verzamelen

def print_gegevens(gegevens):
    for x in gegevens:
        print(f"{x["city"] } is mooi stad ")

gegevens = data_verzamelen()
print_gegevens(gegevens)
