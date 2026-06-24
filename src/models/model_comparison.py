import matplotlib.pyplot as plt
import pandas as pd

# Metrics from your experiments

data = {
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Random Forest": [0.9973, 0.87, 0.83, 0.84],
    "Isolation Forest": [0.8389, 0.71, 0.69, 0.70],
}

df = pd.DataFrame(data)

# Set metric names as index
df.set_index("Metric", inplace=True)

# Create bar chart
ax = df.plot(kind="bar", figsize=(10, 6))

plt.title("Performance Comparison of Random Forest and Isolation Forest Models")
plt.ylabel("Metric Value")
plt.xlabel("Evaluation Metric")
plt.ylim(0, 1.1)

# Display values on top of bars
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f")

plt.tight_layout()

plt.savefig("results/figures/model_comparison.png", dpi=300)

plt.show()
