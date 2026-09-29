""""Create a Pandas DataFrame with a column 'username' containing 5 Instagram usernames in mixed case (e.g., 'CoolDude', 'foodieQueen', etc.),
then use str.lower to convert all usernames to lowercase and print the result."""

import pandas as pd

df = pd.DataFrame({'username': ['Ashav211','SnehaPatelll_','DiyaPatelll','HerryPatel','Savan1117']})

df['username'] = df['username'].str.lower()
print(df)