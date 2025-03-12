import os

robot = 5
for i in range(robot):
    os.system("python generate.py")
    os.system("python simulate.py")