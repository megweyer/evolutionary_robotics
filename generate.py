import pyrosim.pyrosim as pyrosim

#where information about my world will be stored
pyrosim.Start_SDF("box.sdf")

#stores box
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

#close the sdf file
pyrosim.End()
