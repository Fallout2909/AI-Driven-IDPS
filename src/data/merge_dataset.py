import pandas as pd
import glob

files = glob.glob("data/raw/*.csv")

dataframes = []

for file in files:
    print(f"Loading {file}")

    df = pd.read_csv(
        file,
        low_memory=False
    )

    dataframes.append(df)

merged_df = pd.concat(
    dataframes,
    ignore_index=True
)

print("Merged Shape:")
print(merged_df.shape)

merged_df.to_csv(
    "data/processed/merged_dataset.csv",
    index=False
)

print("Saved Successfully")