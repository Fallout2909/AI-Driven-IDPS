import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cm = np.loadtxt(
    "results/metrics/isolation_confusion_matrix.csv",
    delimiter=",",
    dtype=int
)

labels = [
    "BENIGN",
    "ATTACK"
]

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels
)

plt.title("Isolation Forest Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()

plt.savefig(
    "results/figures/isolation_confusion_matrix.png",
    dpi=300
)

plt.show()