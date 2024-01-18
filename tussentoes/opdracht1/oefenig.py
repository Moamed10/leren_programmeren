import time
import math
import random

player_attack = 1
player_defense = 1
player_health = 3

# === Kamer 1 === #
print('Je staat voor de imposante deuren van de mysterieuze dungeon.')
print('Met een lichte huivering duw je ze open en betreed je een gang.')
print('Een muffe en vochtige geur omringt je. Voor je zie je een deur.')
print('')
time.sleep(1)

# === Kamer 2 === #
print('Je opent de deur en wordt begroet door een standbeeld met een sleutel in zijn hand.')
print('Op de borst van het standbeeld bevindt zich een numpad met de cijfers 9 t/m 0.')
a = random.randint(10, 25)
b = random.randint(-5, 75)
som = a + b
print(f'Daarboven zie je een som staan: {a} + {b} = ?')
antwoord = int(input('Wat toets je in? '))

if antwoord == som:
    print('Het standbeeld laat de sleutel vallen, en je pakt het op.')
else:
    print('Er gebeurt niets...')

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(1)

# === Kamer 3 === #
item = random.choice(['schild', 'zwaard'])
if item == 'schild':
    player_defense += 1
else:
    player_attack += 1

print('Je duwt de deur open en stapt een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houdt het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === Kamer 4 === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2

print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_health -= player_attack_amount * zombie_hit_damage
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === Kamer 5 === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

# Check of de speler de sleutel heeft om de schatkist te openen
if 'sleutel' in locals() or 'sleutel' in globals():
    print('Je gebruikt de sleutel om de schatkist te openen.')
    print('Gefeliciteerd, je hebt de schat gevonden en het spel gewonnen!')
else:
    print('Helaas, je hebt geen sleutel en kunt de schatkist niet openen.')
    print('Game over.')



