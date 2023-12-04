from time import sleep

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

option = ["a " , "b"]
keuze = ''

print("""Welkom bij 'Het Verloren Avontuur'
                        _____ _           _   _           _   _     _
                        / ____(_)         | | | |         | \\ | |   | |
                    | (___  _ _ __ __ _| |_| |__   __ _|  \\| |__ | | ___  _ __
                        \\___ \\| | '__/ _` | __| '_ \\ / _` | . ` |/ _` |/ _ \\| '_ \\
                        ____) | | | | (_| | |_| | | | (_| | |\\  | (_| | (_) | | | |
                    |_____/|_|_|  \\__,_|\\__|_| |_|\\__, |_| \\_|\\__,_|\\___/|_| |_|
                                                    __/ |
                                                    |___/
""")

slow_print("Het Verlaten Plein\nJe ziet een verlaten plein met twee verschillende paden.")
sleep(1)

while input not in option:
    keuze_1 = input("A: Volg het smalle steegje aan je linkerhand.\nB: Ga recht vooruit, naar het centrale plein ")

    if keuze_1.lower() == "a":
        slow_print("Het steegje is donker en gevuld met schaduwen. Terwijl je verder loopt, hoor je geluiden van vreemde wezens.")
        steegje = input("A: Keer onmiddellijk\nB: Observeer de wezens ")
        if steegje.lower() == "a":
            slow_print("Je keert onmiddellijk om en je komt in een vreemde kerk terecht. In de kerk is een witch die jou hulp biedt.")
            kerk = input("A: Witch hulp accepteren\nB: Witch hulp niet accepteren ")
            if kerk.lower() == "a":
                slow_print("De witch brengt jou naar mensen.")
                slow_print("Blijkbaar zijn het mensen, en mensen weten de weg.")
                vertrouwen = input("A: Mensen vertrouwen\nB: Nee ")
                if vertrouwen.lower() == "a":
                    slow_print("Mensen leiden jou naar de weg. Gefeliciteerd!")
                elif vertrouwen.lower() == "b":
                    slow_print("""Je blijft zelf zoeken en je gaat binnen 2 dagen dood.
.__           .__                        
|  |__   ____ |  | _____  _____    ______
|  |  \_/ __ \|  | \__  \ \__  \  /  ___/
|   Y  \  ___/|  |__/ __ \_/ __ \_\___ \ 
|___|  /\___  >____(____  (____  /____  >
     \/     \/          \/     \/     \/ """)
            else:
                slow_print("Fout teken.")
        elif kerk.lower() == "b":
            slow_print("Je onderzoekt zelf en je komt uit de kerk.")
            slow_print("Je komt op een kronkelig pad dat leidt naar een betoverend bos met zwevende lichten. Je hoort een betoverende melodie.")
            kronkeligpad = input("A: Volg de melodie\nB: Blijf op het pad ")
            if kronkeligpad.lower() == "a" or kronkeligpad.lower() == "b":
                slow_print("Je ontmoet een monster.")
                monster = input("A: Ren weg\nB: Vecht tegen het monster ")
                if monster.lower() == "a" or monster.lower() == "b":
                    slow_print("""Niet gelukt, het monster maakt jou dood.
                               .__           .__                        
|  |__   ____ |  | _____  _____    ______
|  |  \_/ __ \|  | \__  \ \__  \  /  ___/
|   Y  \  ___/|  |__/ __ \_/ __ \_\___ \ 
|___|  /\___  >____(____  (____  /____  >
     \/     \/          \/     \/     \/ """)
                else:
                    slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
            else:
                slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
        else:
            slow_print("Fout teken.")
    elif steegje.lower() == "b":
        slow_print("Blijkbaar zijn het mensen, en mensen weten de weg.")
        vertrouwen = input("A: Mensen vertrouwen\nB: Nee ")
        if vertrouwen.lower() == "a":
            slow_print("Mensen leiden jou naar de weg. Gefeliciteerd!")
        elif vertrouwen.lower() == "b":
            slow_print("Je blijft zelf zoeken en je gaat binnen 2 dagen dood.")
        else:
            slow_print("Fout teken.")
elif keuze_1.lower() == "b":
    slow_print("Je besluit rechtdoor te gaan naar het centrale plein.")
    slow_print("Op het centrale plein zie je een oude rivier en enkele gebouwen. Plotseling hoor je een vreemd geluid achter een van de gebouwen.")
    sleep(1)
    slow_print("A: Rivier inspecteren.")
    slow_print("B: Geluid onderzoeken.")
    keuze_2 = input("Welk pad wil je volgen? A of B: ")
    if keuze_2.lower() == "a":
        slow_print("Je valt in de rivier en het water trekt jou naar een splitsing.")
        sleep(1)
        slow_print("Je ziet een bos aan de linker kant en een berg aan de rechter kant.")
        slow_print("A: Naar rechts gaan.")
        slow_print("B: Naar links gaan.")
        keuze_3 = input("Wat doe je? A of B: ")
        if keuze_3.lower() == "a":
            slow_print("Je klimt de berg en je ziet een helikopter.")
            slow_print("Je stapt in de helikopter en vliegt weg. Gefeliciteerd!")
        elif keuze_3.lower() == "b":
            slow_print("Je gaat diep het bos in en je komt een beer tegen.")
            slow_print("A: Wegrennen.")
            slow_print("B: Vechten tegen de beer.")
            keuze_beer = input("Wat doe je? A of B: ")
            if keuze_beer.lower() == "a" or keuze_beer.lower() == "b":
                slow_print("De beer eet jou op omdat je niet snel/genoeg sterk bent.")
            else:
                slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
        else:
            slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
    elif keuze_2.lower() == "b":
        slow_print("Het geluid leidt naar een kerkje waar je een witch ontmoet.")
        sleep(1)
        slow_print("Je keert onmiddellijk om en je komt in een vreemde kerk terecht. In de kerk is een witch die jou hulp biedt.")
        kerk = input("A: Witch hulp accepteren\nB: Witch hulp niet accepteren ")
        if kerk.lower() == "a":
            slow_print("De witch brengt jou naar mensen.")
            slow_print("Blijkbaar zijn het mensen, en mensen weten de weg.")
            vertrouwen = input("A: Mensen vertrouwen\nB: Nee ")
            if vertrouwen.lower() == "a":
                slow_print("Mensen leiden jou naar de weg. Gefeliciteerd!")
            elif vertrouwen.lower() == "b":
                slow_print("Je blijft zelf zoeken en je gaat binnen 2 dagen dood.")
            else:
                slow_print("Fout teken.")
        elif kerk.lower() == "b":
            slow_print("Je onderzoekt zelf en je komt uit de kerk.")
            slow_print("Je komt op een kronkelig pad dat leidt naar een betoverend bos met zwevende lichten. Je hoort een betoverende melodie.")
            kronkeligpad = input("A: Volg de melodie\nB: Blijf op het pad ")
            if kronkeligpad.lower() == "a" or kronkeligpad.lower() == "b":
                slow_print("Je ontmoet een monster.")
                monster = input("A: Ren weg\nB: Vecht tegen het monster ")
                if monster.lower() == "a" or monster.lower() == "b":
                    slow_print("Niet gelukt, het monster maakt jou dood.")
                else:
                    slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
            else:
                slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
        else:
            slow_print("Fout teken.")
    else:
        slow_print("Ongeldige keuze. Het avontuur eindigt hier.")
else:
    slow_print("Ongeldige keuze. Het avontuur eindigt hier.")


