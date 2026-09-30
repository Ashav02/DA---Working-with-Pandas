#Create two DataFrames: one called users with columns user_id, username, and city (add at least 5 rows), and another called orders with columns order_id, user_id, and order_amount (add at least 7 rows). Merge them using pd.merge() to show only users who have placed an order (inner join)

import pandas as pd

df1 = pd.DataFrame({'user_id':['ID01','ID02','ID03','ID04','ID05'],
                   'username':['A','B','C','D','E'],
                  'city':['Surat','Vadodra','Ahemdabad','Vapi','Rajkot']})

df2 = pd.DataFrame({'oder_id':[100,110,120,130,140,150,160],
                    'user_id':['ID01','ID02','ID04','ID05','ID06','ID07','ID09'],
                    'oder_amount':[599,469,499,299,600,700,800]})

#using .merge() 
merged = pd.merge(df1,df2, on='user_id',how='outer')
print(merged)

merged1 = pd.merge(df1,df2, on='user_id', how='inner')
print(merged1)