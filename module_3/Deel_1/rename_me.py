def is_even(getal:int) -> bool:
    return getal % 2 == 0

def keer_zin_om(zin:str) -> str:
    woorden = zin.split()
    omgekeerd = woorden[::-1]
    keer_zin_om = ' '.join(omgekeerd)
    return keer_zin_om

def aantal_uniek_letters(tekst:str) -> int:
    unieke_karakters = set(tekst)
    aantal_uniek = len(unieke_karakters)
    return aantal_uniek

def gemiddelde_lengte_woorden(zin:str) -> float:
    woorden = zin.split()
    totale_lengte = sum(len(woord) for woord in woorden)
    gemiddelde_lengte = totale_lengte / len(woorden)
    return gemiddelde_lengte

def print_zin_meerdere_keer(zin:str, aantal_keer:int=10) -> None:
    for keer in range(1, aantal_keer+1):
        print(f'{keer} keer: {zin}')

print_zin_meerdere_keer("mo,le,ka.", 4)
