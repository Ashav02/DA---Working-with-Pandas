"""Perform univariate analysis on the 'runs' column:
calculate and print the mean, median, mode, minimum, and maximum runs scored by batsmen in the IPL_2023_Batsmen dataset.
"""

import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/IPL_2023_Batsmen.csv")

print(df)

#.mean()
avg = df['Runs'].mean()
print("Average Runs: ",avg)

#.median()
med = df['Runs'].median()
print("Median : ",med)

#.mode()
mod = df['Runs'].mode()
print("Mode : ",mod)

#.minimum()
min = df['Runs'].min()
print("Minimum Runs :",min)

#.maximum()
min = df['Runs'].max()
print("Maximum Runs :",max)