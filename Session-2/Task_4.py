#Export the DataFrame from your IPL or food delivery dataset to a new CSV file called 'filtered_data.csv', but only include the first 20 rows.

import pandas as pd

df = pd.read_csv("Zomato Chennai Listing 2020.csv")

filtered_file = df.head(20)

filtered_file.to_csv("filter_data.csv", index=False)



