import random

#selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

#vraag om een antwoord
number = int(input('Weet jij wat {} + {} is? ' . format(num1,num2)))
# number = (input('Weet jij wat '+num1+'+'+num2+' is? '))

#geef reactie op het antwoord
try:
    if number == num1 + num2:
     print('Dat is juist')
    else:
      print("fout")
except ValueError:
 print('Dat is geen nummer!')
        

