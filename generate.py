import pyrosim.pyrosim as pyrosim
import random

def Create_World ():
    pyrosim.Start_SDF("world.sdf")  # stores info about the world
    pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])  # sends cube for the world

#create generate body function
def Generate_Body ():
    pyrosim.Start_URDF("body.urdf")  # generate urdf file of the robot body
    #body
    pyrosim.Send_Cube(name="torso", pos=[0, 0, 1], size=[1, 1, 1])  # create torso
    #back leg
    pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                       position=[0, -0.5, 1], jointAxis = "1 0 0")  # create joint
    pyrosim.Send_Cube(name="back", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])  # back leg
    #front leg
    pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                       position=[0, 0.5, 1], jointAxis = "1 0 0")  # create join
    pyrosim.Send_Cube(name="front", pos=[0, 0.5, 0], size=[0.2,1,0.2])  # front leg
    #left leg
    pyrosim.Send_Joint(name="torso_left", parent="torso", child="left", type="revolute",
                       position=[-0.5, 0, 1], jointAxis="0 1 0")  # create join
    pyrosim.Send_Cube(name="left", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])  # back leg
    #right leg
    pyrosim.Send_Joint(name="torso_right", parent="torso", child="right", type="revolute",
                       position=[0.5, 0, 1], jointAxis="0 1 0")  # create join
    pyrosim.Send_Cube(name="right", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])  # back leg
    #front lower leg
    pyrosim.Send_Joint(name="front_frontLower", parent="front", child="frontLower", type="revolute",
                       position=[0, 1, 0], jointAxis="1 0 0")  # create join
    pyrosim.Send_Cube(name="frontLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])  # back leg
    #back lower leg
    pyrosim.Send_Joint(name="back_backLower", parent="back", child="backLower", type="revolute",
                       position=[0,-1,0], jointAxis="1 0 0")  # create join
    pyrosim.Send_Cube(name="backLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])  # back leg
    #lower left leg
    pyrosim.Send_Joint(name="left_leftLower", parent="left", child="leftLower", type="revolute",
                       position=[-1, 0, 0], jointAxis="1 0 0")  # create join
    pyrosim.Send_Cube(name="leftLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])  # back leg
    # lower right leg
    pyrosim.Send_Joint(name="right_rightLower", parent="right", child="rightLower", type="revolute",
                       position=[1, 0, 0], jointAxis="1 0 0")  # create join
    pyrosim.Send_Cube(name="rightLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])  # back leg

    pyrosim.End() #ends simulation

#create generate brain function using a neural network
def Generate_Brain ():
    pyrosim.Start_URDF("brain.nndf")  # generate nndf (neural network) file of the robot brain
    pyrosim.Send_Sensor_Neuron(name=0, linkName="torso") #this line assigns a numeric value with each neuron - this one is for torso
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

    #assign variables
    sensor_neurons = [0, 1, 2, 3, 4, 5, 6, 7, 8]  #IDs of sensor neurons
    motor_neurons = [9, 10, 11, 12, 13, 14, 15]  #IDs of motor neurons

    # Generate synapses using nested loops
    for i in sensor_neurons:
        for j in motor_neurons:
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1,1))


Generate_Body()
Generate_Brain()