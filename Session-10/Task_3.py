"""Imagine you have two DataFrames: restaurants (restaurant_id, name, city) and zomato_reviews (review_id, restaurant_id, rating, reviewer_city).
Merge them using an outer join on restaurant_id to show all restaurants and all reviews, even if some restaurants have no reviews or some reviews are for restaurants not in your list.
"""


import pandas as pd

df1 = pd.DataFrame({'resturant_id':['ID01','ID02','ID03','ID04','ID05'],
                    'name':['A','B','C','D','E'],
                    'city':['Surat','Vadodra','Ahemdabad','Vapi','Rajkot']})

df2 = pd.DataFrame({'reviwe_id':[110,111,112,113,114],
                    'resturant_id':['ID01','ID02','ID03','ID04','ID05'],
                    'rating':[4.5,4.7,4.3,4.1,4],
                    'city':['Surat','Surat','Ahemdabad','Vapi','Rajkot']})

merge = pd.merge(df1,df2, on='resturant_id',how='outer')
print(merge)