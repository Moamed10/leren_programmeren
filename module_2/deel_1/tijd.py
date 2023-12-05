# from time import sleep

# for x in range(24):
#     if x <= 12:
#         print(f"{x} am")
#     else:
#         print(f"{x} pm")


for tijdzone in["am" , "pm"]:
    for uur in range(13):
        print(f"{uur} {tijdzone}")