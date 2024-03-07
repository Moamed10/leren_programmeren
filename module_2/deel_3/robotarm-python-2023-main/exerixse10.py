from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    for r in range(9):
        robotArm.moveRight()
    if x == 0 :
        r -=1
    robotArm.drop()
    for l in range(8):
        robotArm.moveLeft()
    
    
   
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()