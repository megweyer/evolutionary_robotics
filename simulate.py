import os
import pybullet as p
import pybullet_data
import time as t
import numpy
import random
import pyrosim.pyrosim as pyrosim
from generate import Create_world as CW
from generate import Create_robot as CR

# Call create world
CW()

# Call robot function
CR()

# Import physics engine and
pysicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity into world
p.setGravity(0,0,-9.8)

# Add a floor so the box doesn't fall indefinitely
planeId = p.loadURDF("plane.urdf")

# Add robot
robotId = p.loadURDF("body.urdf")

# Prepare simulation
pyrosim.Prepare_To_Simulate(robotId)

# Number of simulation steps
num_iterations = 1000

# Define BackLeg motor command parameters
amplitudeBackLeg = numpy.pi / 4  # Ensures values are in [-π/4, π/4]
frequencyBackLeg = 9*((2 * numpy.pi) / num_iterations)  # Makes one full cycle
phaseOffsetBackLeg = numpy.pi  # Starts at zero

# Define motor parameters for FrontLeg
amplitudeFrontLeg = numpy.pi / 2  # Ensures values are in [-π/4, π/4]
frequencyFrontLeg = 9*((2 * numpy.pi) / num_iterations)  # One full cycle
phaseOffsetFrontLeg = numpy.pi  # Offset by π/2 for phase difference

# Generate BackLeg motor command vector
i_values = numpy.arange(num_iterations)
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * i_values + phaseOffsetBackLeg)
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * i_values + phaseOffsetFrontLeg)

# Create a numpy vector filled with zeros for sensor values
backLegSensorValues = numpy.zeros(num_iterations)
frontLegSensorValues = numpy.zeros(num_iterations)

# Steps inside the physics world
for i in range(1000):
    p.stepSimulation()

    # Retrieve sensor value inside the loop
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("back")
    # Retrieve sensor value inside the loop
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("front")

    #motor that supplies force to each one of the robots back leg
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="torso_back",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesBackLeg[i],
                                maxForce= 500.0)

    #motor that supplies force to each one of the robots joints
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="torso_front",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesFrontLeg[i],
                                maxForce= 500.0)

    # Slow down simulation
    t.sleep(1. / 240)

# Ensure 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Save the motor command vectors for analysis
numpy.save("data/target_angles_back.npy", targetAnglesBackLeg)
numpy.save("data/target_angles_front.npy", targetAnglesFrontLeg)
#numpy.save("data/target_angles.npy", targetAngles)

# Print the vector
print(backLegSensorValues)
print(frontLegSensorValues)

p.disconnect()
