from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self, mutate_brain=False):
        #time.sleep(0.5)
        os.system(f"del fitness*.txt")
        os.system(f"del brain*.txt")
        os.system(f"del body*.txt")

        self.parents = {} #generates an empty dictionary
        self.nextAvailableID = 0 #assigns a unique ID to each fitness level
        self.mutate_brain = mutate_brain #for test B in order to mutate brain
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)  # store solution object in dictionary
            self.nextAvailableID += 1  # increment the ID for the next solution

        #create new matrix for storing AB testing data P rows and G columns. P = pop size, g = number of generations
        self.ab_test_matrix = numpy.zeros((c.populationSize, c.numberOfGenerations))

    def Evolve(self):
        self.Evaluate(self.parents)
        self.Spawn() # unlocks children dictionary
        self.Mutate() #mutates values and prints them from before and after generation

        for currentGeneration in range(1, c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

        # Save matrix after evolution
        if self.mutate_brain:
            self.variant = "B"

        else:
            self.variant = "A"
        txt_filename = f"fitness_matrix_{self.variant}.txt" #save txt file
        npy_filename = f"fitness_matrix_{self.variant}.npy" #save npy file

        numpy.savetxt(txt_filename, self.ab_test_matrix, fmt="%.5f")
        numpy.save(npy_filename, self.ab_test_matrix)

        #save max fitness for plotting
        max_fitness_per_gen = numpy.abs(numpy.min(self.ab_test_matrix, axis=0))
        filename = f"run_fitness_curve_{self.variant}_{int(time.time())}.txt"
        numpy.savetxt(filename, max_fitness_per_gen, fmt="%.5f")

    def Evolve_For_One_Generation(self, generation):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, generation)
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
            before = ', '.join(f"{l:.3f}" for l in self.children[child].leg_length) #value before mutation
            print(f"Child {child} leg lengths BEFORE mutation: [{before}]")

            self.children[child].Mutate() #mutate

            after = ', '.join(f"{l:.3f}" for l in self.children[child].leg_length) #value after mutation
            print(f"Child {child} leg lengths AFTER mutation:  [{after}]")

            if self.mutate_brain:
                print(f"Child {child} brain was mutated.\n")

    def Select(self):
        for key in self.parents.keys():
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key] #if the child is better replace the parent value with the child value

    def Print (self):
        print ()
        for parent in self.parents.keys():
            print(f"Parent Fitness: {self.parents[parent].fitness}, Child Fitness: {self.children[parent].fitness}")
        print ()

    def Show_Best(self):
        best_key = min(self.parents, key=lambda k: self.parents[k].fitness) #find parent with lowest fitness
        self.parents[best_key].Start_Simulation("GUI") #print simulation in GUI for the best

    def Evaluate (self, solutions, generation=None):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")  # run evaluation in direct mode

        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()
            # Record fitness in the matrix if generation is provided
            if generation is not None:
                self.ab_test_matrix[key, generation] = solutions[key].fitness