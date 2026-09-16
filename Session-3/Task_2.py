#Given a DataFrame of Flipkart products with columns 'product_name', 'category', and 'price',
#use iloc to select the first 10 rows and all columns, and print the result.


import pandas as pd

df = pd.DataFrame({
    'product_name': [
        'Samsung Galaxy M14 5G',
        'boAt Rockerz 450',
        'HP 15s Laptop',
        'Redmi Smart TV 32',
        'Puma Running Shoes',
        'Prestige Electric Kettle',
        'Canon EOS 1500D',
        'Wildcraft Backpack',
        'Philips Trimmer',
        'Lenovo Wireless Mouse'
    ],
    'category': [
        'Mobile', 'Audio', 'Computers', 'Television', 'Footwear',
        'Kitchen', 'Camera', 'Bags', 'Personal Care', 'Accessories'
    ],
    'price': [
        13999, 1499, 42990, 11999, 2499,
        1299, 35999, 1799, 1199, 699
    ]
})

result = df.iloc[ :10, : ]
print(result)