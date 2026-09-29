#Load a CSV file of Spotify song streams (with columns: song, artist, streams, date)
#into a pandas DataFrame and use drop_duplicates() to remove any duplicate song entries, keeping only the first occurrence.


import pandas as pd

df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/spotify_song_streams.csv")

df1 = df.drop_duplicates(['song'], keep='first').reset_index()

print(df1)
