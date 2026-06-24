import pandas as pd
import joblib
import matplotlib.pyplot as plt

print("Loading dataset...")

df = pd.read_csv(
    "data/processed/sample_dataset.csv",
    low_memory=False
)

# Remove rare classes
counts = df[" Label"].value_counts()
valid_classes = counts[counts >= 50].index
df = df[df[" Label"].isin(valid_classes)]

X = df.drop(columns=[" Label"])

print("Loading model...")

rf = joblib.load(
    "models/random_forest.pkl"
)

importance = rf.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 Features:")
print(feature_importance.head(20))

top20 = feature_importance.head(20)

plt.figure(figsize=(12,8))

plt.barh(
    top20["Feature"],
    top20["Importance"]
)

plt.xlabel("Importance Score")
plt.ylabel("Feature")

plt.title(
    "Top 20 Important Features - Random Forest"
)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "results/figures/feature_importance.png",
    dpi=300
)

plt.show()