

import pandas as pd 

#CSV file read
jan_sales = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/sales_jan.csv")
feb_sales = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/sales_feb.csv")
march_sales = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/sales_mar.csv")

#concat DataFrames
df = pd.concat([jan_sales, feb_sales, march_sales], axis=0)
print(df)
