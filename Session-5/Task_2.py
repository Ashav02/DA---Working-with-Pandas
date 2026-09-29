#Using a dataset of food delivery orders (with columns: order_id, customer_name, delivery_rating),
#use pandas to drop all rows where the delivery_rating is missing and display the cleaned DataFrame.


import pandas as pd

df = pd.DataFrame({
    'order_id': [101,102,103,104,105,106,107,108,109,110],
    'customer_name': ['Ashav','Ashu','Sneha','Seyu','Diya','Jugal','Nensi','Harsh','Savan','Dhaval'],
    'delivery_rating': [4.5, None, 5.0, None, 4.0, None, 4.8, None, 4.2, 4.4]
})

df1 = df.dropna(subset=['delivery_rating'])

print(df1)