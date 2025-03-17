from generate import Generate_Body as GB
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
import os
import time

class ROBOT:
    def __init__(self, solutionID):
        #import robot
        GB()
        # Add robot
        self.robotId = p.loadURDF("body.urdf")
        #prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        #call function/method
        self.Prepare_To_Sense()
        self.Prepare_to_Act()

        brainFileName ="brain{solutionID}.nndf"
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf") #use specific ID
        #if os.path.exists(brainFileName):
            #os.system(f"del {brainFileName}")
        os.system(f"del brain{solutionID}.nndf")

        self.solutionID = solutionID

    def Prepare_To_Sense(self):
        #create a dictionary to store sensor instances
        self.sensors = {}

        #iterate over the link names
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense (self, t):
        #update each sensor value by calling get_value
        for sensor in self.sensors.values():
            sensor.Get_value(t)

    def Prepare_to_Act(self):
        # create a dictionary to store sensor instances
        self.motors = {}

        # iterate over the link names
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act (self, t):
        for neuronName in self.nn.Get_Neuron_Names(): #iterates over all the neurons in the neural network
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self, desiredAngle)

    def Save_Values (self):
        #Save the motor command vectors for analysis
        pass

    def Think (self):
        self.nn.Update()
        #self.nn.Print() #prints all of the neural network values

    def Get_Fitness (self, fitnessFileName):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0] #the first x,y,z of the state of link zero
        xCoordinateOfLinkZero = positionOfLinkZero[0] #only the x coordinate

        tmpFileName = f"tmp{self.solutionID}.txt"

        with open(tmpFileName, "w") as f:  # "w" mode overwrites the file, we want to write the fitness to a txt file
            f.write(str(xCoordinateOfLinkZero))  # Write as string
        time.sleep(0.1)

        os.system(f"rename {tmpFileName} {fitnessFileName}")