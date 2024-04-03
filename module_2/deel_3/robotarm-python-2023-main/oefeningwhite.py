from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
aantalkeer = 10
for x in range (8):
    robotArm.moveRight()
for aantal in range(1,aantalkeer):
    print(aantalkeer)
    if aantalkeer <= 0:
        break
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        aantalkeer -=1
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft
        aantalkeer -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()