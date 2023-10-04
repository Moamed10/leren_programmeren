a = float(input("Voer de getal  a in: "))
b = float(input("Voer de getal  b in: "))

if a > b:
    groot = a
    klein = b
    print(f"a is het grootste getal {a}")
   

elif a < b:
    klein = a
    groot = b
    print(f"a is het kleinste {b} ")
    

else:
    klein = a
    groot = b 
    print(" beide zijn gelijk ")


print(f"groot getal was {groot}")
print(f"klein getal was {klein}")




