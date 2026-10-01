"""You have a Spotify playlist CSV with missing 'duration' values for some songs.
Replace all missing durations with the median duration of the available songs using pandas,
then save the cleaned DataFrame to a new CSV file.
"""

import pandas as pd 

df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/playlist_missing_v2.csv")
print(df)

#find a median duration
median_duration = df["duration"].median()

#replace missing values with median
df["duration"] = df["duration"].fillna(median_duration)

#updated file store in new csv file
df.to_csv("playlist_missing_update.csv",index=False)
print(df)
