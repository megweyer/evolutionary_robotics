import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_to_Act()

    def Prepare_to_Act (self):
        #create vector for motor
        self.motorValues = np.zeros(c.num_iterations)

        #set motor parameters
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        #modify frequency for torso front so it oscillates at half the frequency.
        if self.jointName == "torso_front":
            self.frequency = c.frequency / 2.0

    def Set_Value (self, robot, t):
        # Calculate the target motor command using a sine function.
        self.motorValues[t] = self.amplitude * np.sin(self.frequency * t + self.offset)

        #command the motor using PyBullet.
        jointIndex = pyrosim.jointNamesToIndices[self.jointName]

        #command the motor through pybullet
        (p.setJointMotorControl2
            (bodyIndex=robot.robotId,
            jointIndex=jointIndex,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            force=c.max_force))