

import pandas as pd

df1 = pd.DataFrame({'playlist_id': [101, 102, 103, 104, 105],
                    'user_id': [1, 2, 3, 4, 5],
                    'genre': ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical'],
                    'city': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Surat']})

df2 = pd.DataFrame({'user_id': [1, 2, 3, 4, 5],
                    'username': ['Rahul', 'Amit', 'Priya', 'Neha', 'Karan'],
                    'city': ['Ahmedabad', 'Surat', 'Ahmedabad', 'Rajkot', 'Mumbai']})

merged = pd.merge(df1,df2, on='user_id', how='inner')
print(merged)
