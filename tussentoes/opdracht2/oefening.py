import time, math,random

player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
a = random.randint(10,25)
b = random.randint(-5,75)
som = a + b
print(f'Daarboven zie je een som staan {a} + {b}=?')
antwoord = int(input('Wat toest je in?'))

if antwoord == som:
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
else:
    print('Er gebeurt niets....')
    

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1)


# === [kamer 6] === #

zombie_attack = 1
zombie_defense = 0
zombie_health = 2

item = random.choice(['schild', 'zwaard'])

if item == "zwaard":
    player_attack += 2
else:
    player_defense += 1

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









# === [kamer 3] === #


item = random.choice(['schild', 'zwaard'])

if item == "zwaard":
    player_attack += 2
else:
    player_defense += 1
# item = 'schild'
# player_defense += 1
print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)



# === Kamer 4 === #


vijnd_attack = 2
vijnd_defense = 0
vijnd_health = 3

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











# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if antwoord == som:
    print("met de sleuetl maak je  de schatkist open\n gefeliciteerd je hebt de spel gewonne   ")
else:
    print("je hebt de sleutel niet omdat je de som in het begin fout had \n verlore  ")