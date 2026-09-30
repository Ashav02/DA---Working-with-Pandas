"""Take a Pandas Series of Flipkart product categories in the format 'Electronics/Mobiles/Smartphones', 'Home/Kitchen/Appliances', etc.
Use str.split to extract just the main category (the part before the first '/') and create a new column with these values."""


import pandas as pd

df = pd.DataFrame({
    'category': ['Electronics/Mobiles/Smartphones','Home/Kitchen/Appliances','Fashion/Accessories/Jewelry']})

df['main_category'] = df['category'].str.split('/').str[0]

print(df)