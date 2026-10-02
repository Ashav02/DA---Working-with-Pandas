"""Suppose you have a DataFrame of Zomato Gold subscriptions with columns 'user_id' and 'start_date' (as strings).
Calculate the tenure (in days) for each user by subtracting the 'start_date' from today's date, and add it as a new column 'tenure_days'.
<br><br><em><strong>Hint:</strong> Use pd.to_datetime for conversion and (today - start_date).dt.days for calculation.</em>"""

import pandas as pd

df = pd.DataFrame({"user_id": [101, 102, 103, 104, 105],
                   "start_date": ["15-03-2024","07-11-2023","22-01-2025","30-08-2024","12-06-2025"]})

#convert start_date to datetime
df["start_date"] = pd.to_datetime(df["start_date"],format="%d-%m-%Y")

#get today's date
today = pd.Timestamp.today().normalize()

#calculate tenure in days
df["tenure_days"] = (today - df["start_date"]).dt.days

print(df)