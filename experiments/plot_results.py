import pandas as pd
import matplotlib.pyplot as plt


# Read experimental results
results = pd.read_csv("results/comparison_results.csv")


# Create utilisation graph
plt.figure(figsize=(8, 5))

plt.plot(
    results["Boxes"],
    results["EP_Utilisation"],
    marker="o",
    label="Extreme Point"
)

plt.plot(
    results["Boxes"],
    results["MILP_Utilisation"],
    marker="o",
    label="MILP"
)

plt.plot(
    results["Boxes"],
    results["GA_Avg_Utilisation"],
    marker="o",
    label="Genetic Algorithm"
)

plt.xlabel("Number of Boxes")
plt.ylabel("Container Utilisation (%)")
plt.title("Container Utilisation vs Problem Size")

plt.xticks(results["Boxes"])
plt.ylim(0, 100)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/utilisation_graph.png",
    dpi=300
)

plt.show()


#------- Runtime Plot --------

# Create runtime graph
plt.figure(figsize=(8, 5))

plt.plot(
    results["Boxes"],
    results["EP_Runtime"],
    marker="o",
    label="Extreme Point"
)

plt.plot(
    results["Boxes"],
    results["MILP_Runtime"],
    marker="o",
    label="MILP"
)

plt.plot(
    results["Boxes"],
    results["GA_Avg_Runtime"],
    marker="o",
    label="Genetic Algorithm"
)

plt.xlabel("Number of Boxes")
plt.ylabel("Runtime (seconds)")
plt.title("Algorithm Runtime vs Problem Size")

plt.xticks(results["Boxes"])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/runtime_graph.png",
    dpi=300
)

plt.show()