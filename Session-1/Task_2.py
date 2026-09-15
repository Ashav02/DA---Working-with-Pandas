
#Create a DataFrame named 'food_orders' with columns: 'Item', 'Restaurant', and 'Price'. Add 3 rows representing your last 3 Zomato or Swiggy orders and display the DataFrame.


import pandas as pd 

food_order = pd.DataFrame({"Item":['Dosa','Benne Dosa','Masala Dosa'],
                             "Resturant":['Benne by KP','Malhar Dosa','Roshni Fast Food'],
                             "Price":[150,170,200]})
print("Food Order List: ",food_order)
