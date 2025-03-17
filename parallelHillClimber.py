from solution import SOLUTION
import constants as c
import copy
import os
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #time.sleep(0.5)
        os.system(f"del brain*.nndf")
        os.system(f"del fitness*.txt")

        self.parents = {} #generates an empty dictionary
        self.nextAvailableID = 0 #assigns a unique ID to each fitness level

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)  # store solution object in dictionary
            self.nextAvailableID += 1  # increment the ID for the next solution

    def Evolve(self):
        self.Evaluate(self.parents)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()


    def Spawn(self):
        self.children = {}  # Dictionary to store child solutions
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])  # Clone parent
            self.children[key].Set_ID(self.nextAvailableID)  # Assign new unique ID
            self.nextAvailableID += 1  # Increment ID for the next child

    def Mutate(self):
        for child in self.children.keys():
            self.children[child].Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child #if the child is better replace the parent value with the child value

    def Print (self):
        print ()
        for parent in self.parents.keys():
            print(f"Parent Fitness: {self.parents[parent].fitness}, Child Fitness: {self.children[parent].fitness}")
        print ()

    def Show_Best(self):
        best_key = min(self.parents, key=lambda k: self.parents[k].fitness) #find parent with lowest fitness
        self.parents[best_key].Start_Simulation("GUI") #print simulation in GUI for the best

    def Evaluate (self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")  # run evaluation in direct mode

        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()
