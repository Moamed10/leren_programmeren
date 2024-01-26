dagen_van_de_week = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

print (f"dagen van de week : {dagen_van_de_week}")


# print("\nWerkdagen", end=" : ")
# for x in dagen_van_de_week[0:5]:
#     print( x,end = ",")
# print("\n")
# print(dagen_van_de_week[0:5])
# print( "\n\nweekend : " , end= ":")
# for d in dagen_van_de_week[-2:]:
#     print(   d , end= ",")



# print("\n\nAlle dagen van de week in omgekeerde volgorde zijn:", end = " ," )
# for a in range( 6 , -1, -1):
#     print(dagen_van_de_week[a] , end = " ,")



# print("\n\ne werkdagen in omgekeerde volgorde zijn: ", end = " ,")
# for a in range( 4 , -1, -1):
#     print(dagen_van_de_week[a] , end = " ,")



for a in dagen_van_de_week[6::-1]:
    print(a)
