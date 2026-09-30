"""Use pd.concat to combine two DataFrames representing January and February orders from a Swiggy-style food delivery app,
stacking them row-wise to create a single DataFrame with all orders."""

import pandas as pd 

january_orders = pd.DataFrame({
    "Order_ID": [101, 102, 103],
    "Customer": ["Ashav", "Sneha", "Diya"],
    "Amount": [250, 180, 320]
})

february_orders = pd.DataFrame({
    "Order_ID": [104, 105, 106],
    "Customer": ["Jugal", "Nensi", "Fenil"],
    "Amount": [220, 350, 190]})

df = pd.concat([january_orders,february_orders], axis=0, ignore_index=True)

print(df)