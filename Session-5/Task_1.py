#Download a CSV file of IPL cricket players with columns for player name, team, and age,
#then use pandas to load it and print out all rows where the age column has missing values.


import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Dataset/IPL.csv")

df1 = df[df["AGE"].isna()]

print(df1)