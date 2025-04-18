from parallelHillClimber import PARALLEL_HILL_CLIMBER
from plotFitnessValues import PLOT

#phc = PARALLEL_HILL_CLIMBER(mutate_brain=False)   # test A
phc = PARALLEL_HILL_CLIMBER(mutate_brain=True)  # Test B
phc.Evolve()
phc.Show_Best()
PLOT()
