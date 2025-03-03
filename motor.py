import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value (self, robot, desiredAngle):
        #Calculate the target motor command using a sine function.
#        self.motorValues[t] = self.amplitude * np.sin(self.frequency * t + self.offset)

        jointIndex = pyrosim.jointNamesToIndices[self.jointName] #command the motor using PyBullet.
        (p.setJointMotorControl2 #command the motor through pybullet
            (bodyIndex=robot.robotId,
            jointIndex=jointIndex,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            force=c.max_force))