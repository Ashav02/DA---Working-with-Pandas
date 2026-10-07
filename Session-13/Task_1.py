#Load the 'IPL_2023_Batsmen.csv' dataset (containing player name, runs, matches, average, strike rate) into a Pandas DataFrame and display the first 10 rows.


import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/IPL_2023_Batsmen.csv")

#First 10 Rows

print(df.head(10))