import random
import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import os
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = 2 * np.random.rand(c.numSensorNeuron, c.numMotorNeurons) - 1 #this generates 3x2 matrix with random values between -1 and 1
        self.leg_length = np.random.uniform(1, 1.5,size=4)  # generates values between 1 and 4 for the length of the leg
        self.fitness = None #initialize the fitness attribute
        self.myID = nextAvailableID #assigns each ID to a new variable called my ID

    def Evaluate (self,directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"start /B python simulate.py {directOrGUI} {self.myID}")

        fitnessFileName = f"fitness{str(self.myID)}.txt"

        # Wait for the simulation to finish and the file to be created
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)  # Wait 10ms before checking again

        # Read fitness once file is available
        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        print(f"Solution {self.myID} fitness: {self.fitness}")

    def Start_Simulation(self, directOrGUI):
        # this method is going to generate the robots world, body, neural network, and send the six random weights
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"start /B python simulate.py {directOrGUI} {self.myID}")

    def Wait_For_Simulation_To_End (self):
        fitnessFileName = f"fitness{str(self.myID)}.txt"  # gives the name of file a variable
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)  # if the file can't be found it sleeps for a very short period of time

        #with open(fitnessFileName, "r") as fitnessFile:  # open file
         #   fitnessValue = fitnessFile.read()  # read the fitness value as a string

        #self.fitness = float(fitnessValue)  # convert to float
        #print(self.fitness)

        while True:
            try:
                with open(fitnessFileName, "r") as fitnessFile:
                    fitnessString = fitnessFile.read().strip()
                    self.fitness = float(fitnessString)
                    print(self.fitness)
                break
            except PermissionError:
                time.sleep(0.01)

        fitnessFile.close()

        os.system(f"del fitness{self.myID}.txt")  #delete in cmd

    def Mutate(self, mutate_brain = False):
        #mutate random
        randomRow = random.randint(0,2) #random row index (0,1, or 2)
        randomColumn = random.randint(0,1) #random column index (0 or 1)

        #mutate all legs
        mutation_strength = 3  # max size of mutation
        for i in range(len(self.leg_length)):
            self.leg_length[i] += random.uniform(-mutation_strength, mutation_strength)
            self.leg_length[i] = np.clip(self.leg_length[i], 0.5, 4.5)  # keep it within range

        if mutate_brain:
            #randomly mutate one synapse weight to mutate the brain and get it to evolve
            row = random.randint(0, self.weights.shape[0] - 1)
            col = random.randint(0, self.weights.shape[1] - 1)
            old_weight = self.weights[row, col]
            self.weights[row, col] = random.uniform(-1, 1)
            print(f"Brain weight mutated at [{row}, {col}]: {old_weight:.2f} -> {self.weights[row, col]:.2f}") #ensures brain has been mutated

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID  # assigns a new unique ID to the solution

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  # stores info about the world
        pyrosim.Send_Cube(name=f"Box_1", pos=[4, 2, 0.5], size=[1, 1, 1])  # sends cube for the world

    # create generate body function
    def Generate_Body(self):
        bodyFileName = f"body{self.myID}.urdf"
        pyrosim.Start_URDF(bodyFileName)  # generate urdf file of the robot body
        # body
        length = self.leg_length[0]
        length1 = self.leg_length[1]
        length2 = self.leg_length[2]
        length3 = self.leg_length[3]

        pyrosim.Send_Cube(name="torso", pos=[0, 0, length], size=[1, 1, 1])  # create torso

        # right leg
        pyrosim.Send_Joint(name="torso_right", parent="torso", child="right", type="revolute",
                               position=[0.5, 0, length], jointAxis="0 1 0")  # create joint
        pyrosim.Send_Cube(name="right", pos=[(length / 2), 0, 0], size=[length, 0.2, 0.2])
        # right lower leg
        pyrosim.Send_Joint(name="right_rightLower", parent="right", child="rightLower", type="revolute",
                               position=[length, 0, 0], jointAxis="0 1 0")  # c reate joint
        pyrosim.Send_Cube(name="rightLower", pos=[0, 0, -(length / 2)], size=[0.2, 0.2, length])  # back leg

        # back leg
        pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                               position=[0, -0.5, length], jointAxis="1 0 0")  # create joint
        pyrosim.Send_Cube(name="back", pos=[0, -(length / 2), 0], size=[0.2, length, 0.2])  # back leg
        # back lower leg
        pyrosim.Send_Joint(name="back_backLower", parent="back", child="backLower", type="revolute",
                               position=[0, -length, 0], jointAxis="1 0 0")  # create join
        pyrosim.Send_Cube(name="backLower", pos=[0, 0, -(length / 2)], size=[0.2, 0.2, length])

        # left leg
        pyrosim.Send_Joint(name="torso_left", parent="torso", child="left", type="revolute",
                               position=[-0.5, 0, length], jointAxis="0 1 0")  # create join
        pyrosim.Send_Cube(name="left", pos=[-(length / 2), 0, 0], size=[length, 0.2, 0.2])
        # lower left leg
        pyrosim.Send_Joint(name="left_leftLower", parent="left", child="leftLower", type="revolute",
                               position=[-length, 0, 0], jointAxis="0 1 0")  # create join
        pyrosim.Send_Cube(name="leftLower", pos=[0, 0, -(length / 2)], size=[0.2, 0.2, length])

        # front leg
        pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                               position=[0, 0.5, length], jointAxis="1 0 0")  # create join
        pyrosim.Send_Cube(name="front", pos=[0, (length / 2), 0], size=[0.2, length, 0.2])  # front leg
        # front lower leg
        pyrosim.Send_Joint(name="front_frontLower", parent="front", child="frontLower", type="revolute",
                               position=[0, length, 0], jointAxis="1 0 0")  # create join
        pyrosim.Send_Cube(name="frontLower", pos=[0, 0, -(length / 2)], size=[0.2, 0.2,
                                                                                  length])  # replace last value because this is going to change how tall the leg is # back leg

        pyrosim.End()  # ends simulation

    # create generate brain function using a neural network
    def Generate_Brain(self):
        pyrosim.Start_URDF(f"brain{self.myID}.nndf")  # generate nndf (neural network) file of the robot brain
        pyrosim.Send_Sensor_Neuron(name=0,
                                       linkName="torso")  # this line assigns a numeric value with each neuron - this one is for torso
        pyrosim.Send_Sensor_Neuron(name=1, linkName="back")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="front")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="left")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="right")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="frontLower")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="backLower")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="leftLower")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="rightLower")

        pyrosim.Send_Motor_Neuron(name=9, jointName="torso_back")
        pyrosim.Send_Motor_Neuron(name=10, jointName="torso_front")
        pyrosim.Send_Motor_Neuron(name=11, jointName="torso_left")
        pyrosim.Send_Motor_Neuron(name=12, jointName="torso_right")
        pyrosim.Send_Motor_Neuron(name=13, jointName="front_frontLower")
        pyrosim.Send_Motor_Neuron(name=14, jointName="back_backLower")
        pyrosim.Send_Motor_Neuron(name=15, jointName="left_leftLower")
        pyrosim.Send_Motor_Neuron(name=16, jointName="right_rightLower")

        # assign variables
        sensor_neurons = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # IDs of sensor neurons
        motor_neurons = [9, 10, 11, 12, 13, 14, 15, 16]  # IDs of motor neurons

        # Generate synapses using nested loops
        #for i in sensor_neurons:
         #   for j in motor_neurons:
          #      pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1, 1))
        for i in range(len(sensor_neurons)):
            for j in range(len(motor_neurons)):
                pyrosim.Send_Synapse(sourceNeuronName=sensor_neurons[i], targetNeuronName=motor_neurons[j],
                                     weight=self.weights[i][j])
