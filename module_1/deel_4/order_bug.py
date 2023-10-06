a = input(('Geef een woord'))
b = input('Geef nog een woord')

len_woord1 = len(a)
len_woord2 = len(b)

if len_woord1 > len_woord2:     
    print('Woord 1 heeft meer letters dan woord 2')
elif len_woord1 < len_woord2:   
    print('Woord 1 heeft minder letters dan woord 2')
else:                   
    print('Woord 1 en woord 2 hebben evenveel letters')
    



