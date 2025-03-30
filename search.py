import pyrosim
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()

#print the values in the new leg lengths vector - then end simulation
for i, parent in phc.parents.items():
    print(f"Parent {i} leg lengths: {parent.leg_length}")
exit()

phc.Evolve()
phc.Show_Best()
