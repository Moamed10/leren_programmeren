import random

kleuren = ("oranje", "blauw", "groen", "bruin")

aantal = int(input("Hoeveel M&M's in de zak? "))
lijst = []

def fun():
    for _ in range(aantal):
        R = random.choice(kleuren)
        lijst.append(R)

fun()
print("Inhoud van de zak met M&M's:")
print(lijst)



