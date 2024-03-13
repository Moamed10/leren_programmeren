from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1, 7)
robotArm.speed = 3
recht = 1
links = 1
kleuren = ["red", "blue", "white", "green", "yellow"]

# Jouw python instructies zet je vanaf hier:

while True:
    robotArm.grab()
    color = robotArm.scan()
    print(color)
    
    if color in kleuren:
        for r in range(recht):
            robotArm.moveRight()
        robotArm.drop()
        recht += 1
        
        for l in range(links):
            robotArm.moveLeft()
        links += 1

    else:
        break

# Na jouw code wachten tot het sluiten van het venster:
robotArm.wait()
