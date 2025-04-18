import numpy as np
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend
import matplotlib.pyplot as plt

def PLOT():
    # Load the matrices
    matrix_A = np.load("fitness_matrix_A.npy")
    matrix_B = np.load("fitness_matrix_B.npy")

    # Compute mean and std across the population (axis=0 means per generation)
    mean_A = np.mean(matrix_A, axis=0)
    std_A = np.std(matrix_A, axis=0)

    mean_B = np.mean(matrix_B, axis=0)
    std_B = np.std(matrix_B, axis=0)

    generations = np.arange(matrix_A.shape[1])

    # Plot Variant A rainbow
    plt.plot(generations, mean_A, label="Variant A Mean", color="blue")
    plt.fill_between(generations, mean_A - std_A, mean_A + std_A, color="blue", alpha=0.3)

    # Plot Variant B rainbow
    plt.plot(generations, mean_B, label="Variant B Mean", color="green")
    plt.fill_between(generations, mean_B - std_B, mean_B + std_B, color="green", alpha=0.3)

    # Labeling and legend
    plt.title("Average Fitness Over Generations (with Std Dev)")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.savefig("fitness_rainbow_plot.png") #save the figure
