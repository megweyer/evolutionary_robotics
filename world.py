from generate import Create_world as CW
import pybullet as p

class WORLD:
    def __init__(self):
        #create the world
        CW()

        #add a floor
        self.planeId = p.loadURDF("plane.urdf")