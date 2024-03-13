from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
aantalkeer = 9
for aantal in range(1,aantalkeer):
    print(aantalkeer)
    if aantalkeer <= 0:
        break
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        aantalkeer -=2
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()
        aantalkeer -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()