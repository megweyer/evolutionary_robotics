import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        # create a numpy vector filled with zeros for sensor values
        self.values = numpy.zeros(c.num_iterations)

    def Get_value (self, t):
        #sensor value for back leg
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        #print last time step
        if t == c.num_iterations - 1:
            print(f"Sensor '{self.linkName}' values: {self.values}")