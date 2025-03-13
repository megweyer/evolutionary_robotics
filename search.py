import os
from hillclimber import HILL_CLIMBER

#robot = 5
#for i in range(robot):
#    os.system("python generate.py")
#    os.system("python simulate.py")

hc = HILL_CLIMBER ()
hc.Evolve()
hc.Show_Best()