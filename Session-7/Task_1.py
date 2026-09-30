"""Download a sample Flipkart-style product sales CSV with columns: ProductName, Price, Qty.
Using pandas, add a new column called 'TotalValue' that multiplies Price and Qty for each row, then display the updated DataFrame.
"""

import pandas as pd

df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/flipkart_product_sales.csv")

print(df)


df['Total_value'] = df['Price'] * df['Qty']

print(df.reset_index())