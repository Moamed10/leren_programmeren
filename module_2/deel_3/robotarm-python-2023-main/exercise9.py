from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for x in range(10):
    robotArm.grab()
    for r in range(5):
        robotArm.moveRight()
        if x == 2:
            r+=1
    robotArm.drop()
    print(x)
    for l in range(4):
        robotArm.moveLeft()
        if x == 2:
            l-=1

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


