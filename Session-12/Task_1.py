"""Download a dataset of IPL cricket matches (CSV) and use pandas to group the data by 'team' to find the total runs scored by h eacteam.
Display the result as a DataFrame.
"""

import pandas as pd

#Read CSV file
df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/matches.csv")


#o group the data by 'team'
df = df.groupby(['team_1','team_2'])[['team_1_score','team_2_score']].sum().reset_index()
print(df)


