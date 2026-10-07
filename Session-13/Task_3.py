"""Create a Pandas DataFrame for your top 5 favorite Zomato restaurants with columns: 'name', 'rating', 'votes', and 'avg_cost'.
Perform bivariate analysis between 'rating' and 'votes' by calculating their correlation coefficient.
"""

import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/top_zomato_restaurants.csv")

correlation = df['rating'].corr(df['votes'])

print("Correlation between rating and votes:", correlation)