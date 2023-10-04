def vraag_woord(aantal):
    antwoord = str(input(f"voer {aantal} in"))
    woord = str(antwoord)
    return woord

def tel_woord(a,b):
  aantoord = len(a) and len(b)
  return aantoord

woord_1 = vraag_woord("eerste")
woord_2 = vraag_woord("tweede")


resultat = tel_woord(woord_1,woord_2)
if woord_1 > woord_2:     
    print('Woord 1 heeft meer letters dan woord 2')
elif woord_1 < woord_2:   
    print('Woord 1 heeft minder letters dan woord 2')
else:                   
    print('Woord 1 en woord 2 hebben evenveel letters')