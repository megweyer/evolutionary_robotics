import numpy
import matplotlib.pyplot as plt

# Load the saved motor command vectors
targetAnglesBackLeg = numpy.load("data/target_angles_back.npy")
targetAnglesFrontLeg = numpy.load("data/target_angles_front.npy")

# Generate x-values for plotting
num_iterations = len(targetAnglesBackLeg)
x_values = numpy.arange(num_iterations)
# Plot both motor values
plt.plot(x_values, targetAnglesFrontLeg, label="Front Leg", linewidth=2.5)
plt.plot(x_values, targetAnglesBackLeg, label="Back Leg", linewidth=1)
plt.xlabel("Time Step")
plt.ylabel("Target Angle (radians)")
plt.title("Front vs. Back Leg Motor Commands")
plt.legend()
# Show the plot
plt.show()



#load in target angle data
targetAngles = numpy.load("data/target_angles.npy")
plt.plot(targetAngles, label = "Target Angles", linewidth = 0.5)
plt.xlabel("Steps")
plt.ylabel("Value in Radians")
plt.title("Motor Commands")
plt.legend()
plt.show()