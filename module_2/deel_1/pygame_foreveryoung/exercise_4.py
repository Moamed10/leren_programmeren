from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
# robotArm.speed = 3


for x in range(5):

    robotArm.grab()
    if x < 4 :
     robotArm.moveRight()
    robotArm.moveRight()
    if x < 4:
     robotArm.drop()
    if x  < 4 :
        robotArm.moveLeft()
        robotArm.moveLeft()
    

robotArm.drop()
robotArm.moveRight()


for x in range(4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()