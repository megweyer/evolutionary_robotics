from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION () #generates a random solution

    def Evolve(self):
        self.parent.Evaluate("DIRECT") #run in blind mode
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        self.parent.Evaluate("GUI") #run with visuals
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child #if the child is better replace the parent value with the child value

    def Print (self):
        print (self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI") #show the best evolved solution