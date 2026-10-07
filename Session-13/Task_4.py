"""Generate summary statistics (count, mean, std, min, 25%, 50%, 75%, max)
for all numeric columns in the IPL_2023_Batsmen DataFrame using the describe() function and interpret any one interesting insight you observe.
<br><br><em><strong>Hint:</strong> Look for outliers or surprising averages in the summary.</em>"""

import pandas as pd 

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/IPL_2023_Batsmen.csv")

print(df.describe())

"""Insight: The maximum runs are much higher than the average runs,
indicating that a few top-performing batsmen scored significantly more runs than the rest of the players."""