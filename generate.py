import pyrosim.pyrosim as pyrosim
import random

def Create_World ():
    pyrosim.Start_SDF("world.sdf")  # stores info about the world
    pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])  # sends cube for the world

#create generate body function
def Generate_Body ():
    pyrosim.Start_URDF("body.urdf")  # generate urdf file of the robot body
    pyrosim.Send_Cube(name="torso", pos=[0, 0, 1], size=[1, 1, 1])  # create torso
    pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                       position=[0, -0.5, 1], jointAxis = "1 0 0")  # create joint
    pyrosim.Send_Cube(name="back", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])  # back leg
    pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                       position=[0, 0.5, 1], jointAxis = "1 0 0")  # create join
    pyrosim.Send_Cube(name="front", pos=[0, 0.5, 0], size=[0.2,1,0.2])  # front leg
    pyrosim.End() #ends simulation

#create generate brain function using a neural network
def Generate_Brain ():
    pyrosim.Start_URDF("brain.nndf")  # generate nndf (neural network) file of the robot brain
    pyrosim.Send_Sensor_Neuron(name=0, linkName="torso") #this line assigns a numeric value with each neuron - this one is for torso
    pyrosim.Send_Sensor_Neuron(name=1, linkName="back")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="front")
    pyrosim.Send_Motor_Neuron(name=3, jointName="torso_back")
    pyrosim.Send_Motor_Neuron(name=4, jointName="torso_front")

    #assign variables
    sensor_neurons = [0, 1, 2]  #IDs of sensor neurons
    motor_neurons = [3, 4]  #IDs of motor neurons

    # Generate synapses using nested loops
    for i in sensor_neurons:
        for j in motor_neurons:
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1,1))


Generate_Body()
Generate_Brain()