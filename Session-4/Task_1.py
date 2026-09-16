#Create a DataFrame named 'movies' with columns: 'title', 'rating', and 'release_year' for at least 6 popular Bollywood films.
#Use sort_values() to display the movies sorted by 'rating' from highest to lowest.


import pandas as pd

movies = pd.DataFrame({'title':['Jailer','KGF-2','Salaar','Avenger-Endgame','Spider Man-Brand new day','The Fantastic 4 First Steps'],
                       'rating':[4.5,4.3,4.1,4.7,4.8,4],
                        'release_year':[2023,2022,2023,2019,2026,2026]})

sort = movies.sort_values(('rating'))

print(sort)