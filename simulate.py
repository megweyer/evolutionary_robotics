from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1] #extract command-line argument to determine mode (GUI or direct)
solutionID = sys.argv [2] #extracts the third variable in python (0,1,etc.) extract the ID
#run simulation
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run(directOrGUI)
simulation.Get_Fitness()