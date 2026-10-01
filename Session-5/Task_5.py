"""Use ChatGPT to generate pandas code that replaces all missing values in a 'followers' column
(from a simulated Instagram user data CSV) with 0, then test the code on your own sample data and submit both the code and the result.
Ask ChatGPT: 'How do I replace missing values in a pandas DataFrame column with zero?'
"""

import pandas as pd

# Simulated Instagram user data
df = pd.DataFrame({
    "username": ["user1", "user2", "user3", "user4", "user5"],
    "followers": [1200, None, 3500, None, 5000]
})

print("Before:")
print(df)

# Replace missing followers with 0
df["followers"] = df["followers"].fillna(0)

print("\nAfter:")
print(df)

#my simulated instagram user data

df1 = pd.read_csv("C:/Users/Tops/Documents/Ashav/CSV file/instagram_user_data.csv")
print("Before: ")
print(df1)

#replace missing value followers with 0
df1["followers_count"] = df1["followers_count"].fillna(0)

print("\nAfter:")
print(df1)
