import time

def intro():
    print("Welkom bij het avonturenspel!")
    time.sleep(1)
    print("Je bent een dappere avonturier genaamd Derf.")
    time.sleep(1)
    print("Je staat voor een donkere grot. Wat doe je?")
    time.sleep(1)

def keuze_a():
    print("Je hebt gekozen om de grot in te gaan.")
    time.sleep(1)
    print("Binnen in de grot ontdek je een glinsterende schat.")
    time.sleep(1)
    print("Gefeliciteerd, je hebt de schat gevonden!")

def keuze_b():
    print("Je hebt besloten om terug te keren naar het dorp.")
    time.sleep(1)
    print("Terug in het dorp ontmoet je een oude man die je een magische kaart geeft.")
    time.sleep(1)
    print("De kaart wijst naar een verborgen tempel in het bos. Wil je de tempel verkennen? (A/B)")
    antwoord = input().upper()

    if antwoord == 'A':
        print("Je besluit de tempel te verkennen.")
        time.sleep(1)
        print("Binnen in de tempel vind je mysterieuze artefacten.")
        time.sleep(1)
        print("Gefeliciteerd, je hebt een nieuw avontuur ontdekt!")
    else:
        print("Je besluit de kaart te negeren en verder te gaan met je avontuur.")

# Hoofdprogramma
intro()
print("A. Ga de grot in.")
print("B. Keer terug naar het dorp.")

keuze = input("Maak je keuze (A/B): ").upper()

if keuze == "A":
    keuze_a()
elif keuze == "B":
    keuze_b()
else:
    print("Ongeldige keuze. Probeer opnieuw.")
