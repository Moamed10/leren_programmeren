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

def hangman_game():
    te_raden = "huis"
    geraden_letters = ""
    
    while True:
        huidige_staat = ""
        for letter in te_raden:
            if letter in geraden_letters:
                huidige_staat += letter
            else:
                huidige_staat += "_"
        print(f"Huidige staat van het woord: {huidige_staat}")
        
        letter = get_letter()
        
        if letter in te_raden:
            if letter not in geraden_letters:
                print(f"Goed zo! De letter '{letter}' zit in het woord.")
                geraden_letters += letter
            else:
                print(f"Je hebt de letter '{letter}' al geraden.")
        else:
            print(f"Helaas, de letter '{letter}' zit niet in het woord.")
        
        # Controleer of alle letters geraden zijn
        volledig_geraden = True
        for letter in te_raden:
            if letter not in geraden_letters:
                volledig_geraden = False
                break

        if volledig_geraden:
            print(f"Gefeliciteerd! Je hebt het woord '{te_raden}' geraden.")
            break

# Start het spel
hangman_game()
