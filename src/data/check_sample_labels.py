import pandas as pd

df = pd.read_csv(
    "data/processed/sample_dataset.csv"
)

print(df[" Label"].value_counts())