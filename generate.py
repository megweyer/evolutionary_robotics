import pyrosim.pyrosim as pyrosim


#create a function called create_world
def Create_world ():
    # where information about my world will be stored
    pyrosim.Start_SDF("world.sdf")

    # Send the cube with the current position and size
    pyrosim.Send_Cube(name=f"Box_1", pos=[1, 1, 1], size=[1, 1, 1])

    # close the sdf file
    pyrosim.End()

#create new robot with joints
def Create_robot ():
    pyrosim.Start_URDF("body.urdf")  # generate urdf file
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])  # create torso
    pyrosim.Send_Joint(name="torso_back", parent="torso", child="back", type="revolute",
                       position=[1, 0, 1])  # create joint
    pyrosim.Send_Cube(name="back", pos=[-0.5, 0, -0.5], size=[1, 1, 1])  # back leg
    pyrosim.Send_Joint(name="torso_front", parent="torso", child="front", type="revolute",
                       position=[2, 0, 1])  # create join
    pyrosim.Send_Cube(name="front", pos=[0.5, 0, -0.5], size=[1, 1, 1])  # front leg
    pyrosim.End()
