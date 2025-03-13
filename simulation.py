#import packages
import pybullet as p
import pybullet_data
import time
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        #connect to the physics engine and set up the simulation environment
        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI) #heads up mode
        else:
            self.physicsClient = p.connect(p.DIRECT) #blind mode

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.xGrav, c.yGrav, c.zGrav)

        #create instances
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.num_iterations):
            p.stepSimulation()
            #call robot method sense
            self.robot.Sense(t)
            # allow the robot to think
            self.robot.Think()
            #call the motors
            self.robot.Act(t)
            #slow down the simulation
            time.sleep(c.sleep)

    def Get_Fitness (self):
        self.robot.Get_Fitness()

    #def __del__(self):
        #disconnect from simulation
        #p.disconnect()