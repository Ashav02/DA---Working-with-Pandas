"""Refactor the code that groups a DataFrame by 'region' and sums 'revenue' so 
it also returns the maximum and minimum revenue per region in the same result.
Use agg() with a dictionary to specify multiple aggregation functions for the 'revenue' column.
"""

import pandas as pd

df = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'revenue': [50000, 65000, 45000, 72000, 55000, 68000, 48000, 75000,
                35000, 40000, 25000, 150000, 12000, 124500, 60000, 95000]})

#Maximum revenue per region
df1 = df.groupby('region')['revenue'].agg(max).reset_index()
print(df1)

#Minimum revenue per region
df2 = df.groupby('region')['revenue'].agg(min).reset_index()
print(df2)
