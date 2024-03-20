from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3
aantalblokken = 10
for _ in range(aantalblokken):
    recht, links = 5, 5
    robotArm.grab()
    for _ in range(recht):
        robotArm.moveRight()
    robotArm.drop()
    if aantalblokken in (10, 8, 5):
        links = 4
    for _ in range(links):
        robotArm.moveLeft()
    aantalblokken -= 1
robotArm.wait()
