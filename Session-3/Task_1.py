#Download a CSV file containing a list of movies with columns like 'title', 'genre', 'rating', and 'box_office',
#then use pandas to load this file and select only the 'title' and 'rating' columns using the loc method.


import pandas as pd

df = pd.read_csv("tmdb_5000_movies.csv")

result = df.loc[100:110,['title','vote_count']]

print(result)