import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

print("===================================")
print("Isolation Forest Training Started")
print("===================================")

# =====================================
# LOAD DATASET
# =====================================

print("\nLoading dataset...")

df = pd.read_csv(
    "data/processed/sample_dataset.csv",
    low_memory=False
)

print(f"Original Shape: {df.shape}")

# =====================================
# DATA CLEANING
# =====================================

print("\nCleaning dataset...")

df.replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True
)

df.dropna(inplace=True)

print(f"Shape After Cleaning: {df.shape}")

# =====================================
# CREATE BINARY LABELS
# =====================================

print("\nCreating Binary Labels...")

df["binary_label"] = df[" Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

print("\nBinary Label Distribution:")
print(df["binary_label"].value_counts())

# =====================================
# FEATURES & TARGET
# =====================================

X = df.drop(
    columns=[" Label", "binary_label"]
)

y = df["binary_label"]

print(f"\nFeature Shape: {X.shape}")

# =====================================
# TRAIN ISOLATION FOREST
# =====================================

print("\nTraining Isolation Forest...")

iso = IsolationForest(
    n_estimators=100,
    contamination=0.15,
    random_state=42,
    n_jobs=-1
)

iso.fit(X)

print("Training Complete!")

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    iso,
    "models/isolation_forest.pkl"
)

print("Model saved:")
print("models/isolation_forest.pkl")

# =====================================
# PREDICTIONS
# =====================================

print("\nGenerating Predictions...")

pred = iso.predict(X)

# Isolation Forest:
# 1 = normal
# -1 = anomaly

pred = np.where(
    pred == 1,
    0,
    1
)

# =====================================
# EVALUATION
# =====================================

accuracy = accuracy_score(
    y,
    pred
)

report = classification_report(
    y,
    pred
)

cm = confusion_matrix(
    y,
    pred
)

print("\n==========================")
print("MODEL PERFORMANCE")
print("==========================")

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(report)

print("\nConfusion Matrix:")
print(cm)

# =====================================
# SAVE METRICS
# =====================================

with open(
    "results/metrics/isolation_forest_metrics.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("Isolation Forest Results\n\n")

    f.write(f"Accuracy: {accuracy:.4f}\n\n")

    f.write("Classification Report\n")
    f.write(report)

    f.write("\n\nConfusion Matrix\n")
    f.write(str(cm))

print("\nMetrics saved:")
print("results/metrics/isolation_forest_metrics.txt")

# =====================================
# SAVE CONFUSION MATRIX CSV
# =====================================

np.savetxt(
    "results/metrics/isolation_forest_confusion_matrix.csv",
    cm,
    delimiter=",",
    fmt="%d"
)

print("Confusion Matrix saved:")
print("results/metrics/isolation_forest_confusion_matrix.csv")

print("\n===================================")
print("Isolation Forest Training Complete")
print("===================================")