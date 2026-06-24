import pandas as pd

print("Loading dataset...")

df = pd.read_csv(
    "data/processed/cleaned_dataset.csv",
    low_memory=False
)

sample_df = df.sample(
    n=200000,
    random_state=42
)

sample_df.to_csv(
    "data/processed/sample_dataset.csv",
    index=False
)

print(sample_df.shape)