import os
import glob
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

#robot = 5
#for i in range(robot):
#    os.system("python generate.py")
#    os.system("python simulate.py")

phc = PARALLEL_HILL_CLIMBER ()
phc.Evolve()
phc.Show_Best()
