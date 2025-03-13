from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1] #extract command-line argument to determine mode (GUI or direct)

#run simulation
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()