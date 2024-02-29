# for tijdzone in["am" , "pm"]:
#     for uur in range(1,13):
#         tijd= f"{uur:02d} {tijdzone}"
        
#         if tijd == '12 pm':
#             print("12 am")
#         elif tijd == '12 am':
#             print("12 pm")
#         else:
#             print(tijd)


for tijdzone in["am" , "pm"]:
    for uur in range(1,13):
        print(f"{uur:02d} {tijdzone}")
print ("12 am")