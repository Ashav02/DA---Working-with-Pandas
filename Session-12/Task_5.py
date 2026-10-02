"""Suppose you have a DataFrame of Spotify song streams with columns ['artist', 'genre', 'streams'].
Use groupby and agg() to find both the total and average streams for each genre,
then sort the result by total streams in descending order.
Your final DataFrame should have genres as the index and columns for total and average streams.
"""

import pandas as pd

df = pd.DataFrame({'artist': ['Taylor Swift', 'Taylor Swift', 'Drake', 'Drake', 'Bad Bunny'],
    'genre': ['Pop', 'Pop', 'Hip-Hop', 'Hip-Hop', 'Reggaeton'],
    'streams': [1500000, 2300000, 1800000, 1200000, 2100000]})


df1 = df.groupby(['artist','genre'])['streams'].agg(["sum","mean"]).reset_index()

print(df1)