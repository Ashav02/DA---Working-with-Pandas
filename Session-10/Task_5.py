

import pandas as pd

products = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'name': ['Laptop', 'Mobile', 'Headphones', 'Shoes'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Fashion']})

ratings = pd.DataFrame({
    'rating_id': [1, 2, 3, 4, 5],
    'product_id': [101, 102, 105, 103, 106],
    'rating': [4.5, 4.0, 3.5, 5.0, 2.5]})

# Right Join
result = pd.merge(products,ratings,on='product_id',how='right')

print(result)