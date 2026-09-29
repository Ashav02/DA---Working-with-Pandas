"""Given a Pandas Series of song titles from your Spotify playlist, use str.replace to remove all occurrences of the word 'Remix' from the titles and display the cleaned list."""

import pandas as pd

df = pd.DataFrame({'Song': [
        'Shape of You Remix',
        'Blinding Lights Remix',
        'Perfect',
        'Levitating Remix']})

df['Song'] = df['Song'].str.replace('Remix', 'Cover')

print(df)