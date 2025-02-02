import pybullet as p
import pybullet_data
import time as t
from generate import Create_world as CW
from generate import Create_robot as CR
from generate import Create_link_practice as CLP

#call create world
#CW()
#CLP ()
# call robot function
CR()

#import physics engine and
pysicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#add gravity into world
p.setGravity(0,0,-9.8)

#add a floor so the box doesn't fall indefinitely
planeId = p.loadURDF("plane.urdf")

#add a floor so the box doesn't fall indefinitely
robotId = p.loadURDF("body.urdf")

#allow box to show in simulation
#p.loadSDF("world.sdf")

#steps inside the physics world
for i in range (1000):
    p.stepSimulation()
    #call times sleep function to slow down the simulation
    t.sleep(1. / 100)
    print (i) #tell us how long each iteration takes


p.disconnect()

