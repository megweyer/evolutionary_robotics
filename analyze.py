import numpy
import matplotlib.pyplot as plt

#load in data
backLegSensorValues = numpy.load("data/back_leg_sensor.npy")
print (backLegSensorValues)

#plot the data
#plt.subplot(1,2,1)
plt.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
#plt.title("Back Leg Sensor Values Over Time")


#do the same for front leg
#load in data
frontLegSensorValues = numpy.load("data/front_leg_sensor.npy")
print (frontLegSensorValues)

#plot the data
#plt.subplot(1,2,2)
plt.plot(frontLegSensorValues, label = "Front Leg", linewidth = 0.5)
#plt.title("Front Leg Sensor Values Over Time")


#show data
plt.legend()
plt.show()