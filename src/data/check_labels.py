import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_dataset.csv",
    low_memory=False
)

print(df.columns[-1])

print(
    df[" Label"].value_counts()
)