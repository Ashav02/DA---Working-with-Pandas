#Given a DataFrame of Spotify songs with columns 'song', 'artist', 'streams', and 'duration',
#use the query() method to select all songs with more than 1,000,000 streams and duration less than 180 seconds.


import pandas as pd

df = pd.DataFrame({'song': ['Shape of You', 'Blinding Lights', 'Believer', 'Dance Monkey', 'Perfect'],
                    'artist': ['Ed Sheeran', 'The Weeknd', 'Imagine Dragons', 'Tones and I', 'Ed Sheeran'],
                    'streams': [5000000, 4500000, 2000000, 1500000, 800000],
                    'duration': [233, 200, 204, 210, 263]})


print(df.query('streams > 1000000 and duration < 180'))
