import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import glob
from matplotlib.lines import Line2D

def to_subscript(n):
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(subscript_map)

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
    plt.savefig("fitness_rainbow_plot.png")  # save the figure

    # Plot all individual run best fitness curves
    files = sorted(glob.glob("run_fitness_curve_*.txt"))
    if not files:
        print("No run fitness files found.")
        return

    A_files = [f for f in files if "_A_" in f]
    B_files = [f for f in files if "_B_" in f]

    plt.figure()

    # Plot A runs (shades of red)
    for i, file in enumerate(A_files):
        curve = np.abs(np.loadtxt(file))
        color = plt.cm.Reds((i + 1) / (len(A_files) + 1))
        label = f"A"
        plt.plot(curve, label=label, color=color)

    # Plot B runs (shades of blue)
    for i, file in enumerate(B_files):
        curve = np.abs(np.loadtxt(file))
        color = plt.cm.Blues((i + 1) / (len(B_files) + 1))
        label = f"B"
        plt.plot(curve, label=label, color=color)

    # Save the final plot
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Best Fitness per Generation (A vs B)")
    # Create custom legend handles
    custom_legend = [
    Line2D([0], [0], color='red', label='Variant A'),
    Line2D([0], [0], color='blue', label='Variant B')]
    plt.legend(handles=custom_legend, loc='upper right', fontsize='small')
    plt.tight_layout()
    plt.savefig("best_fitness_all_runs.png")