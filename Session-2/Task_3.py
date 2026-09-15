#Use describe() and info() on a DataFrame loaded from a Zomato restaurant dataset (or any food delivery data you can find online),
#and write down 2 insights about the data (for example: number of restaurants, missing values, or average ratings).

import pandas as pd

df = pd.read_csv("Zomato Chennai Listing 2020.csv").reset_index()

df.info()

print(df.describe())
