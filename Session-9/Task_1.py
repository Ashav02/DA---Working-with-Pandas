"""Create a Pandas Series of 5 random date strings in the format 'DD-MM-YYYY',
then convert this Series to datetime objects using pd.to_datetime and print the result."""

import pandas as pd

df = pd.DataFrame({"Date": ["15-03-2026","07-11-2025","22-01-2026","30-08-2025","12-06-2026"]})
print(df)

#convert this Series to datetime

df1 = pd.to_datetime(df["Date"])
print(df1)


