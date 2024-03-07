from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 2
recht = 9
links = 8
for bloknummer in range(1,6):
    robotArm.grab()
    for r in range(recht):
        robotArm.moveRight()
    recht -=2
    robotArm.drop()
    for l in range(links):
     robotArm.moveLeft()
    links-=2
robotArm.wait()