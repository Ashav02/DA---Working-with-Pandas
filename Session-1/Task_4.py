#Create a DataFrame called 'playlist' with columns: 'Song', 'Artist', and 'Duration' (in minutes).
#Enter details for 4 songs you recently listened to on Spotify or YouTube Music, then print only the 'Song' and 'Duration' columns.

import pandas as pd

playlist = pd.DataFrame({'Song':['Teri Yaado Se','Forever','Tum Ho Mera Pyar','Gunaah'],
                    'Artist':['Mustafa Zahid','Martin Garrix','KK','Mustafa Zahid'],
                    'Duration':[267,280,315,205]})

print(playlist[['Song','Duration']])
