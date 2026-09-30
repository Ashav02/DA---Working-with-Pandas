"""Given a DataFrame of food items with columns: Item, Price, and Qty,
use the apply() function with a lambda to create a new column 'DiscountedPrice' that applies a 10% discount to the Price for each item.
"""

import pandas as pd

df = pd.DataFrame({ 'item':['Dosa','Pizza','Momos','Pasta','Benne Dosa'],
                    'Price':[150,259,120,249,160],
                    'Qty':[3,2,1,2,4]})

df['total'] = df['Price'] * df['Qty']
print(df)

#10% discount

df['DiscountedPrise'] = df['total'].apply(lambda total, : total * 0.9)

print(df)