


import pandas as pd

df = pd.DataFrame({'Restaurant':['Banney By KP','La Pinoz','KFC','MacD','South Indian'],
                   'Price':[199,299,399,249,149],
                   'Qty':[2,3,5,6,4],
                   'DeliveryCharge':[30,50,70,80,50]})

df['FinalAmount'] = df.apply(lambda row:(row['Price'] * row['Qty']) + row['DeliveryCharge'],axis=1)

print(df)