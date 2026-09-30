"""Using the same users and orders DataFrames, perform a left join to display all users along with their orders.
If a user has not placed any orders, show NaN for order_id and order_amount."""


import pandas as pd

df1 = pd.DataFrame({'user_id':['ID01','ID02','ID03','ID04','ID05'],
                   'username':['A','B','C','D','E'],
                  'city':['Surat','Vadodra','Ahemdabad','Vapi','Rajkot']})

df2 = pd.DataFrame({'oder_id':[100,110,120,130,140,150,160],
                    'user_id':['ID01','ID02','ID04','ID05','ID06','ID07','ID09'],
                    'oder_amount':[599,469,499,299,600,700,800]})

merged = pd.merge(df1,df2, on='user_id', how='left')

print(merged)