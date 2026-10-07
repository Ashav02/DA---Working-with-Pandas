"""Download a publicly available CSV dataset of IPL cricket matches (for example, from Kaggle or data.world),
and use pandas to load it into a DataFrame named ipl_df. Display the first 5 rows.
"""

import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/ipl_matches_dataset.csv")

print(df)

#print first 5 rows
df1 = df.head(5)
print(df1)