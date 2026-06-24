import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/sample_dataset.csv"
)

counts = df[" Label"].value_counts()

plt.figure(figsize=(10,6))
counts.plot(kind="bar")

plt.title("Attack Class Distribution")
plt.xlabel("Attack Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    "results/figures/class_distribution.png"
)

plt.show()