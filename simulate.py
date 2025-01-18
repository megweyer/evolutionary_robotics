import pybullet as p
import time as t

#import physics engine and
pysicsClient = p.connect(p.GUI)

#steps inside the physics world
for i in range (1000):
    p.stepSimulation()
    #call times sleep function to slow down the simulation
    t.sleep(1. / 240)
    print (i) #tell us how long each iteration takes

p.disconnect()

