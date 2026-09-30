"""Given two DataFrames — one with Flipkart product details 
and another with their respective ratings — use pd.concat to merge them column-wise so each product row includes its rating."""

import pandas as pd 

df = pd.DataFrame({
    "Product_ID": [101, 102, 103],
    "Product": ["Laptop", "Mobile", "Headphones"]})

ratings = pd.DataFrame({
    "Rating": [4.5, 4.2, 4.7]})

df1 = pd.concat([df, ratings], axis=1)
print(df1)