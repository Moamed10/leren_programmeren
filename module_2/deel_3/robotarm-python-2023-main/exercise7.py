from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed=3
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for stabel in range(5):

    for blokje in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if stabel < 4:
        robotArm.moveRight()
        robotArm.moveRight()
    print(stabel)


        
# for x in range(30):
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()
#     robotArm.moveRight()
#     print(x)
#     if x == 5 or x == 11 or x == 17 or x == 23:
#         robotArm.moveRight()
#         robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()