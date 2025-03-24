import numpy
#import all constants from other files

#simulation parameters
num_iterations = 1000
max_force = 500
sleep = 1/100000
slowsleep = 1/240 #to slow down for GUI

#gravity constants
xGrav = 0
yGrav = 0
zGrav = -9.8

#motor parameters
amplitude = numpy.pi / 4
frequency = (2* numpy.pi)/num_iterations
offset = numpy.pi

#hill climber variables
numberOfGenerations = 10

#parallel hill climber variables
populationSize = 10

#quadruped variables
numSensorNeuron = 9
numMotorNeurons = 8
motorJointRange = 0.3


