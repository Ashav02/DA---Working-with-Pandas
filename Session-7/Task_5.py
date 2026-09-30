"""Use ChatGPT to generate a pandas code snippet that adds a column 'GST' to a DataFrame of Myntra orders, where GST is calculated as 5% of (Price * Qty). Paste the AI-generated code, run it, and write 2 lines about what you learned from the AI's explanation.
"""

import pandas as pd

import pandas as pd

df = pd.DataFrame({
    'Order_ID': [101, 102, 103, 104, 105],
    'Product': ['T-Shirt', 'Jeans', 'Shoes', 'Kurti', 'Jacket'],
    'Price': [799, 1499, 2499, 999, 1999],
    'Qty': [2, 1, 1, 3, 2]})

print(df)

df['GST'] = (df['Price'] * df['Qty']) * 0.05

print(df)