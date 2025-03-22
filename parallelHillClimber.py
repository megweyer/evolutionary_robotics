from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {} #generates an empty dictionary
        self.nextAvailableID = 0 #assigns a unique ID to each fitness level

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)  # store solution object in dictionary
            self.nextAvailableID += 1  # increment the ID for the next solution

    def Evolve(self):
        #for key in self.parents:
            #self.parents[key].Start_Simulation("DIRECT")  # run evaluation in direct mode

        #for key in self.parents:
            #self.parents[key].Wait_For_Simulation_To_End()
        for key in self.parents:
            self.parents[key].Evaluate("GUI")

        #for currentGeneration in range(c.numberOfGenerations):
            #self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}  # Dictionary to store child solutions
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])  # Clone parent
            self.children[key].Set_ID(self.nextAvailableID)  # Assign new unique ID
            self.nextAvailableID += 1  # Increment ID for the next child

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child #if the child is better replace the parent value with the child value

    def Print (self):
        print (self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        pass