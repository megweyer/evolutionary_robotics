import os
import pybullet as p
import pybullet_data
import time as t
import numpy
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

# Create a numpy vector filled with zeros
backLegSensorValues = numpy.zeros(10000)
#Create a numpy vector filled with zeros
frontLegSensorValues = numpy.zeros(10000)

# Steps inside the physics world
for i in range(1000):
    p.stepSimulation()
    # Retrieve sensor value inside the loop
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("back")
    # Retrieve sensor value inside the loop
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("front")
    # Slow down simulation
    t.sleep(1. / 100)

# Ensure 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Save sensor data to disk
numpy.save("data/back_leg_sensor.npy", backLegSensorValues)
numpy.save("data/front_leg_sensor.npy", frontLegSensorValues)

# Print the vector
print(backLegSensorValues)
print(frontLegSensorValues)

p.disconnect()
