import pyrosim.pyrosim as pyrosim

def Create_World ():
    pyrosim.Start_SDF("world.sdf")  # stores info about the world
    pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])  # sends cube for the world

#create generate body function
def Generate_Body ():
    pyrosim.Start_URDF("body.urdf")  # generate urdf file of the robot body
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])  # create torso
    pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                       position=[1, 0, 1])  # create joint
    pyrosim.Send_Cube(name="back", pos=[-0.5, 0, -0.5], size=[1, 1, 1])  # back leg
    pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                       position=[2, 0, 1])  # create join
    pyrosim.Send_Cube(name="front", pos=[0.5, 0, -0.5], size=[1, 1, 1])  # front leg
    pyrosim.End() #ends simulation

#create generate brain function using a neural network
def Generate_Brain ():
    pyrosim.Start_URDF("brain.nndf")  # generate nndf (neural network) file of the robot brain
    pyrosim.Send_Sensor_Neuron(name=0, linkName="torso") #this line assigns a numeric value with each neuron - this one is for torso
    pyrosim.Send_Sensor_Neuron(name=1, linkName="back")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="front")
    pyrosim.Send_Motor_Neuron(name=3, jointName="torso_back")
    pyrosim.Send_Motor_Neuron(name=4, jointName="torso_front")
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0) # generate a synapse - connects neuron 1 to neuron 3 #no ids because there is nothing that will be referring to them
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=10.0) # generate a synapse - connects neuron 2 to neuron 3
    pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=4, weight=1.0)
    pyrosim.End() #ends simulation

Generate_Body()
Generate_Brain()