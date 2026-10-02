"""Take a Flipkart-style product sales DataFrame with columns ['category', 'region', 'sales', 'units_sold'],
and apply multiple aggregations: for each (category, region) pair,
calculate the total sales and the average units_sold using groupby and agg().
"""

import pandas as pd

df = pd.DataFrame({
    'category': ['Electronics', 'Fashion', 'Home & Kitchen', 'Electronics', 'Fashion', 'Home & Kitchen', 'Electronics', 'Fashion', 'Home & Kitchen', 'Electronics', 'Beauty', 'Sports', 'Beauty', 'Sports', 'Electronics'],
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East'],
    'sales': [125000, 95000, 87500, 110000, 78000, 92500, 135000, 88000, 105000, 115000, 65000, 72000, 58000, 81000, 142000],
    'units_sold': [250, 190, 175, 220, 156, 185, 270, 176, 210, 230, 130, 144, 116, 162, 284]})

#calculate the total sales and the average units_sold using groupby and agg()


df1 = df.groupby(['category','region'])[['sales','units_sold']].agg(sum).reset_index()

print(df1)