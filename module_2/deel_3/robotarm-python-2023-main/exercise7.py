from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed=4
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for x in range(30):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    print(x)
    if x == 5 or x == 11 or x == 17 or x == 23:
        robotArm.moveRight()
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()