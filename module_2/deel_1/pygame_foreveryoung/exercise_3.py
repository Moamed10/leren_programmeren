from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')
robotArm.speed = 3

for _ in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
robotArm.moveRight()

# Wait for the window to close
robotArm.wait()
