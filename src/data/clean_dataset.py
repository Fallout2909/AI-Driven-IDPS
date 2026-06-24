import pandas as pd
import numpy as np

print("Loading dataset...")

df = pd.read_csv(
    "data/processed/merged_dataset.csv",
    low_memory=False
)

print("Original Shape:")
print(df.shape)

# Replace Infinity values
df.replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True
)

# Remove rows containing NaN
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Cleaned Shape:")
print(df.shape)

df.to_csv(
    "data/processed/cleaned_dataset.csv",
    index=False
)

print("Dataset cleaned successfully")