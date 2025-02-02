import pyrosim.pyrosim as pyrosim


#create a function called create_world
def Create_world ():
    # where information about my world will be stored
    pyrosim.Start_SDF("world.sdf")

    # Send the cube with the current position and size
    pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])

    # close the sdf file
    pyrosim.End()

#create function for robot
def Create_link_practice ():
    pyrosim.Start_URDF("body.urdf")

    #create practice for joints and links
    pyrosim.Send_Cube(name= "link0", pos=[0,0, 0.5], size=[1, 1, 1])
    #create joint
    pyrosim.Send_Joint(name = "link0_link1", parent = "link0", child = "link1", type = "revolute", position = [0, 0, 1.0])
    #create leg - position is relative to joint 1, that's why it is 0,0,0.5 again
    #everything from here on out will be relative to the previous joint
    pyrosim.Send_Cube (name = "link1", pos = [0.0,0,0.5], size = [1,1,1])
    #create the next joint
    pyrosim.Send_Joint(name="link1_link2", parent="link1", child="link2", type="revolute", position=[0, 0, 1.0])
    #create next link
    pyrosim.Send_Cube(name="link2", pos=[0.0, 0, 0.5], size=[1, 1, 1])
    #create new joint
    pyrosim.Send_Joint(name="link2_link3", parent="link2", child="link3", type="revolute", position=[0, 0.5, 0.5])
    #create new link
    pyrosim.Send_Cube(name="link3", pos = [0,0.5,0], size = [1,1,1])
    #create new joint
    pyrosim.Send_Joint(name="link3_link4", parent="link3", child="link4", type="revolute", position=[0, 1, 0])
    #create new link
    pyrosim.Send_Cube(name="link4", pos = [0,0.5,0], size = [1,1,1])
    #create new joint
    pyrosim.Send_Joint(name="link4_link5", parent="link4", child="link5", type="revolute", position=[0, 0.5, -0.5])
    #create new link
    pyrosim.Send_Cube(name="link5", pos = [0,0,-0.5], size = [1,1,1])
    #create new joint
    pyrosim.Send_Joint(name="link5_link6", parent="link5", child="link6", type="revolute", position=[0, 0, -1])
    #create new link
    pyrosim.Send_Cube(name="link6", pos = [0,0,-0.5], size = [1,1,1])
    pyrosim.End()

#create new robot with joints
def Create_robot ():
    pyrosim.Start_URDF("body.urdf")
    #create torso
    pyrosim.Send_Cube(name="torso", pos=[0.0, 1, 1.5], size=[1, 1, 1])
    # create joint
    pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute", position=[0, 0.5, 1.0])
    #create back leg
    pyrosim.Send_Cube(name= "back", pos=[0,-0.5, -0.5], size=[1, 1, 1])
    #create joint
    pyrosim.Send_Joint(name = "torso_front", parent = "torso", child = "front", type = "revolute", position = [0,1,0])
    #create leg
    pyrosim.Send_Cube(name = "front", pos = [0,1,0.5], size = [1,1,1])

    pyrosim.End()


