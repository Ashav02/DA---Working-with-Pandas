"""Given a DataFrame of Zomato food orders with columns ['city', 'restaurant', 'order_amount'],
use groupby to calculate the average order_amount for each restaurant in each city using the agg() function.
"""

import pandas as pd

df = pd.DataFrame({'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai'],
    'resturant': ['Taj Palace', 'Curry House', 'Spice Garden', 'Biryani King', 'Masala Trail', 'South Flavours', 'Pizza Hut', 'Burger King', 'KFC', 'Dominos'],
    'order_amount': [450, 320, 580, 650, 290, 520, 380, 410, 470, 350]})
print(df)

#calculate the average order_amount using the egg()

df = df.groupby(['city','resturant'])['order_amount'].agg('mean').reset_index()
print(df)