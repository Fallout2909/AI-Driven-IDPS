import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("Loading dataset...")

df = pd.read_csv("data/processed/sample_dataset.csv", low_memory=False)

print(f"Original Shape: {df.shape}")

# =====================================
# DATA CLEANING
# =====================================

print("Cleaning dataset...")

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.dropna(inplace=True)

# =====================================
# REMOVE RARE CLASSES
# =====================================

counts = df[" Label"].value_counts()

valid_classes = counts[counts >= 50].index

df = df[df[" Label"].isin(valid_classes)]

print("\nClasses Used For Training:")
print(df[" Label"].value_counts())

print(f"\nDataset Shape After Filtering: {df.shape}")

# =====================================
# FEATURES & LABELS
# =====================================

X = df.drop(columns=[" Label"])
y = df[" Label"]

# =====================================
# TRAIN TEST SPLIT
# =====================================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training Size: {X_train.shape}")
print(f"Testing Size : {X_test.shape}")

# =====================================
# RANDOM FOREST TRAINING
# =====================================

print("\nTraining Random Forest...")

rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

rf.fit(X_train, y_train)

print("Training Complete!")

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(rf, "models/random_forest.pkl")

print("Model saved to models/random_forest.pkl")

# =====================================
# PREDICTIONS
# =====================================

print("\nGenerating Predictions...")

y_pred = rf.predict(X_test)

# =====================================
# EVALUATION
# =====================================


accuracy = accuracy_score(y_test, y_pred)

report = classification_report(y_test, y_pred)

report = report.encode("utf-8", errors="ignore").decode("utf-8")

cm = confusion_matrix(y_test, y_pred)

print("\n==========================")
print("MODEL PERFORMANCE")
print("==========================")

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(report)

print("\nConfusion Matrix:")
print(cm)

# =====================================
# SAVE RESULTS
# =====================================

with open("results/metrics/random_forest_metrics.txt", "w", encoding="utf-8") as f:

    f.write(f"Accuracy: {accuracy:.4f}\n\n")

    f.write("Classification Report\n")
    f.write(report)

    f.write("\n\nConfusion Matrix\n")
    f.write(str(cm))

print("\nMetrics saved to:")
print("results/metrics/random_forest_metrics.txt")

np.savetxt("results/metrics/random_forest_confusion_matrix.csv", cm, delimiter=",", fmt="%d")
