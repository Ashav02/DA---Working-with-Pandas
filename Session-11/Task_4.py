"""Given a DataFrame of Zomato restaurant orders (with columns: restaurant, month, total_amount)
,use pivot_table to calculate the average order amount per restaurant for each month."""

import pandas as pd

#load csv file
df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/zomato_restaurant_orders.csv")
print(df)

df = df['total_amount']
