from generate import Create_robot as CR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #import robot
        CR()

        # Add robot
        self.robotId = p.loadURDF("body.urdf")

        #prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        #call function/method
        self.Prepare_To_Sense()
        self.Prepare_to_Act()

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
        for motor in self.motors.values():
            motor.Set_Value(self, t)

    def Save_Values (self):
        #Save the motor command vectors for analysis
        pass