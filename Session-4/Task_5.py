#Take a DataFrame of Flipkart products with columns 'product_name', 'price', and 'discount'.
#First, sort the products by 'discount' descending, then reset the index so it starts from 0 and is sequential after sorting.


import pandas as pd

df = pd.DataFrame({'product_name':['Laptop','Smartphone','Tablet','Smartwatch'],
                   'price':[1000, 500, 300, 200],
                   'discount':[100, 50, 30, 20]})

df1 = df.sort_values(by='discount', ascending=False)

print(df1)

df2 = df1.reset_index(drop=True)
print(df2)