from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    
    # Beweeg naar rechts voordat je het blok laat vallen
    robotArm.moveRight()
    
    robotArm.drop()
    
    # Beweeg naar rechts voordat je terugkeert naar de meest linkerpositie
    robotArm.moveRight()
    
    for l in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van het window:
robotArm.wait()
