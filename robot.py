from generate import Generate_Body as GB
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #import robot
        GB()
        # Add robot
        self.robotId = p.loadURDF("body.urdf")
        #prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        #call function/method
        self.Prepare_To_Sense()
        self.Prepare_to_Act()

        self.nn = NEURAL_NETWORK("brain.nndf")

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
        self.nn.Print()
