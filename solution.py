import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        self.weights = 2 * np.random.rand(3, 2) - 1 #this generates 3x2 matrix with random values between -1 and 1
        self.fitness = None #initialize the fitness attribute

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  # stores info about the world
        pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])  # sends cube for the world

    # create generate body function
    def Generate_Body (self):
        pyrosim.Start_URDF("body.urdf")  # generate urdf file of the robot body
        pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])  # create torso
        pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                           position=[1, 0, 1])  # create joint
        pyrosim.Send_Cube(name="back", pos=[-0.5, 0, -0.5], size=[1, 1, 1])  # back leg
        pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                           position=[2, 0, 1])  # create join
        pyrosim.Send_Cube(name="front", pos=[0.5, 0, -0.5], size=[1, 1, 1])  # front leg
        pyrosim.End()  # ends simulation

    # create generate brain function using a neural network
    def Generate_Brain (self):
        pyrosim.Start_URDF("brain.nndf")  # generate nndf (neural network) file of the robot brain
        pyrosim.Send_Sensor_Neuron(name=0,
                                   linkName="torso")  # this line assigns a numeric value with each neuron - this one is for torso
        pyrosim.Send_Sensor_Neuron(name=1, linkName="back")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="front")
        pyrosim.Send_Motor_Neuron(name=3, jointName="torso_back")
        pyrosim.Send_Motor_Neuron(name=4, jointName="torso_front")

        # assign variables
        sensor_neurons = [0, 1, 2]  # IDs of sensor neurons
        motor_neurons = [0, 1]  # IDs of motor neurons

        # Generate synapses using nested loops
        for currentRow in sensor_neurons:
            for currentColumn in motor_neurons:
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=weight)

    def Evaluate(self, directOrGUI):
        # this method is going to generate the robots world, body, neural network, and send the six random weights
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system (f"python simulate.py {directOrGUI}")

        with open("fitness.txt", "r") as fitnessFile:  #open file
            fitnessValue = fitnessFile.read()  #read the fitness value as a string

        self.fitness = float(fitnessValue)  #convert to float
        #print (self.fitness)

    def Mutate(self):
        randomRow = random.randint(0,2) #random row index (0,1, or 2)
        randomColumn = random.randint(0,1) #random column index (0 or 1)

        old_value = self.weights[randomRow, randomColumn]  #store the old weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1  #assign new random value
