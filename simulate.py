import pybullet as p

#import physics engine and
pysicsClient = p.connect(p.GUI)

#steps inside the physics world
for i in range (1000):
    p.stepSimulation()

p.disconnect()

