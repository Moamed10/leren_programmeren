
import random
kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

nummer = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? :"))


mo = { }
def zakje():
       for x in range(nummer):
        kleur = random.choice(kleuren)
        if kleur is "blauw":
            continue

        
        if kleur in mo:
            mo[kleur] +=1
        else:
            mo[kleur] = 1
        

zakje()
print(mo)


