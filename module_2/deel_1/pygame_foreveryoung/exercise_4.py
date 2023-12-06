from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for x in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.operate()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()