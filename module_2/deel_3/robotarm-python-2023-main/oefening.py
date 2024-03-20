from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3
aantalkeer = 9

for _ in range(aantalkeer):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
        aantalkeer -= 2
    else:
        robotArm.drop()
        robotArm.moveRight()
        aantalkeer -= 1

robotArm.wait()
