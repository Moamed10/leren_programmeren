from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2
for _ in range(9):
    robotArm.grab()
    color = robotArm.scan()  
    if color == "red":
        for _ in range(9):
            robotArm.moveRight()
        robotArm.drop()      
        for _ in range(8):  
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()
