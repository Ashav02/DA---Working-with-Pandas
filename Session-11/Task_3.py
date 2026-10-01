"""Create a DataFrame showing daily song streams for three users on Spotify for one week,
then use the pivot function to reshape the data so each row is a user and each column is a day."""

import pandas as pd

#Load CSV
df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/spotify_daily_streams.csv")
print(df)

#use the pivot function to reshape the data

df = df.pivot(index="User",columns="Day",values="Daily_Streams")
print(df)
