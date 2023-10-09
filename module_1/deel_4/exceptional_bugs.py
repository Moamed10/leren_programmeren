import random

#selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

#vraag om een antwoord
try:
 oke = True
 number = int(input('Weet jij wat {} + {} is? ' . format(num1,num2)))
except ValueError:
 print('Dat is geen nummer!')
 oke = False

#geef reactie op het antwoord

if oke == True and number == num1 + num2:
     print('Dat is juist')
else:
      print("fout")

        

