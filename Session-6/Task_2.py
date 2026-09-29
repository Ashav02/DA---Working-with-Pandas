"""Given a pandas DataFrame of Flipkart product reviews with columns: product_id, user_id, rating, review_text,
identify and print the number of duplicate reviews (where product_id and user_id are both the same)
before and after using drop_duplicates()."""


import pandas as pd


df = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/flipkart_reviews.csv")

#print(df.reset_index())

#count duplicate reviews befor removeing them
before_dup = df.duplicated(['product_id','user_id']).sum()

print("Before duplicates : ",before_dup)

print("--------------------")

#remove using drop_duplicates()

remove_dup = df.drop_duplicates(['product_id','user_id'])

print(remove_dup)

print("--------------------")

#count duplicate reviews after removeing them

after_dup = remove_dup.duplicated(['product_id','user_id']).sum()

print("After duplicates : ",after_dup)