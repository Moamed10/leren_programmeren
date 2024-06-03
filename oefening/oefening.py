import string
def get_letter() -> str:
    while True:
        letter = input("voer een letter in: ")
        if len(letter) != 1:
            print("vul 1 letter in.")
        elif letter not in string.ascii_lowercase:
            print("je moet een kleine letter invoeren.")
        else:
            return letter



te_raden =("huis")
print(te_raden)
geraden = '-' + len(te_raden)


if get_letter in te_raden:
    print("zit  er in")


for letter in te_raden:
    print(letter)

while True:
    huidige_staat = ""
    for letter in te_raden:
        if letter in geraden:
                huidige_staat += letter
        else:
                huidige_staat += "_"
        print(f"Huidige staat van het woord: {huidige_staat}")
