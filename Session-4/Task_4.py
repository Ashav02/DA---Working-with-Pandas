#You have a DataFrame of Zomato restaurant names and their ratings. Use reindex() to rearrange
#the rows so that your favorite restaurant appears first, followed by the rest in any order.

import pandas as pd

df = pd.DataFrame({'Resturant_name':['The Great Indian Dhaba','The Spice House','Curry in a Hurry','Tandoori Tales'],
                   'ratings':[4.5, 4.8, 4.9, 3.8],})

df = df.reindex([3, 0, 1, 2])
print(df)