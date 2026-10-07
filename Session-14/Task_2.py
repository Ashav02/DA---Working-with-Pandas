"""Clean the ipl_df DataFrame by removing any rows where the 'winner' column is missing or null, and reset the index afterwards.
"""

import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/ipl_matches_dataset.csv")

print(df)

#Remove rows where winner is missing
df = df.dropna(subset=["winner"])

#Reset index
df = df.reset_index(drop=True)

print(df)