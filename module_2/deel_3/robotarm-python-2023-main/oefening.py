from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

robotArm.speed = 3
bloknummer = 9 
for x in range(8):
    robotArm.grab()
    color = robotArm.scan()

    if color == "white":
        bloknummer -=2

        robotArm.moveRight()
        robotArm.drop()

        
    else:
        robotArm.drop()


    robotArm.moveRight()  # Move to the next position after dropping the block
    print(x)

robotArm.wait()
