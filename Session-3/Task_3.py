#Using a DataFrame of food orders from Zomato with columns 'restaurant', 'order_amount', and 'delivery_time',
#filter and display only those orders where 'order_amount' is greater than 500 using a boolean condition.


import pandas as pd

df = pd.DataFrame({'Restaurant':['La Pinoz','MaC D','Benne by KP','Gustos','Charcol Dosa'],
                   'Order_amount':[599,215,150,499,699],
                   'Deilivery_time':[30,40,50,45,35]})

filter_order_amount = df[df['Order_amount'] > 500]
print(filter_order_amount)