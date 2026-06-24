import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cm = np.loadtxt(
    "results/metrics/random_forest_confusion_matrix.csv",
    delimiter=",",
    dtype=int
)

labels = [
    "BENIGN",
    "Bot",
    "DDoS",
    "DoS GoldenEye",
    "DoS Hulk",
    "DoS Slowhttptest",
    "DoS slowloris",
    "FTP-Patator",
    "PortScan",
    "SSH-Patator",
    "Brute Force",
    "XSS"
]

plt.figure(figsize=(12,10))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels
)

plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()

plt.savefig(
    "results/figures/random_forest_confusion_matrix.png",
    dpi=300
)

plt.show()