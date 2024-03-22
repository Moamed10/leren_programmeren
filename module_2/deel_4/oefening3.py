import random

score = 0
round_number = 1

while round_number <= 20:
    secret_number = random.randint(1, 1000)
    guesses = 0
    print(secret_number)
    
    print(f"\nRonde {round_number}")
    
    while guesses < 10:
        guess = int(input("Raad een getal tussen 1 en 1000: "))
        guesses += 1
        
        if guess == secret_number:
            score += 1
            print("Gefeliciteerd! Je hebt het geraden!")
            break
        else:
            if abs(guess - secret_number) < 50:
                print("Je bent warm")
            elif abs(guess - secret_number) < 20:
                print("Je bent heel warm")
            else:
                print("Fout geraden")
            
            if guesses == 10:
                print(f"Je hebt 10 keer geraden. Het geheime getal was {secret_number}.")
    
    print(f"Score tot nu toe: {score}")
    round_number += 1
    
    if round_number <= 20:
        play_again = input("Nog een getal raden? (ja/nee): ").lower()
        if play_again != "ja":
            break

print(f"Eindscore: {score}")
