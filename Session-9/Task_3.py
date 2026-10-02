"""Generate a date range for the next 7 days starting from today using pd.date_range, and display the list of dates in the console.
"""

import pandas as pd

df = pd.date_range(start=pd.Timestamp.today(), periods=7, freq="D")

print(df)