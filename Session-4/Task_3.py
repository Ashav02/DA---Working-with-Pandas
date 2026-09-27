#Reset the index of a DataFrame containing a list of trending YouTube videos (columns: 'video_title', 'views', 'likes'),
#and make sure the old index is not added as a column in the result.

import pandas as pd

df = pd.DataFrame({'video_title':['Om Namo Bhagavate Vasudevaya','Ghaghro','Namo Namo','Vishwambhari Stuti'],
                   'views':[1000000, 500000, 750000, 250000],
                   'likes':[50000, 25000, 35000, 15000]})

df = df.reset_index(drop=True)
print(df)