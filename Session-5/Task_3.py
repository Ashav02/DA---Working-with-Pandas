#Given a Flipkart-style product reviews dataset with some missing 'rating' values,
#use pandas to fill all missing ratings with the mean rating of the dataset and print the updated DataFrame.

import pandas as pd

df = pd.DataFrame({'product_name':['Laptop','Smartphone','Tablet','Smartwatch'],
                   'price':[1000, 500, 300, 200],
                   'rating':[4.5, None, 5.0, None]})

df1 = df.fillna(df['rating'].mean())
print(df1)