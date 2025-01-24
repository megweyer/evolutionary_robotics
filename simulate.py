import pybullet as p
import time as t

#import physics engine and
pysicsClient = p.connect(p.GUI)

#add forces into world
p.setGravity(0,0,-9.8)

#allow box to show in simulation
p.loadSDF("box.sdf")

#steps inside the physics world
for i in range (1000):
    p.stepSimulation()
    #call times sleep function to slow down the simulation
    t.sleep(1. / 100)
    print (i) #tell us how long each iteration takes

p.disconnect()

