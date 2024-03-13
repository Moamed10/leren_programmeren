from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
recht = 9
links = 8
for bloknummer in range(9):
    robotArm.grab()
    color = robotArm.scan()  
    if color == "red":
        for r in range(recht):
            robotArm.moveRight()
        robotArm.drop()      
        for l in range(links):  
            robotArm.moveLeft()       
        recht -= 1
        links -= 1
    else:
        robotArm.drop()
        robotArm.moveRight()
        recht -= 1
        links -= 1
robotArm.wait()
