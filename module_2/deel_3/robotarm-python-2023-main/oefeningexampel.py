from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 3

# Lijst van stapels met het aantal blokken in elke stapel
stapels = [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]

# Lijst van doelrijen voor elke stapel
doelrijen = [5, 6, 7, 8]

# Loop over elke stapel en verplaats de blokken naar de bijbehorende doelrij
for stapel, doelrij in zip(stapels, doelrijen):
    for blok in stapel:
        robotArm.grab()
        for _ in range(blok - 1):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(blok - 1):
            robotArm.moveLeft()
    for _ in range(len(stapel)):
        robotArm.moveRight()  # Verplaats de arm naar de volgende stapel

robotArm.wait()
