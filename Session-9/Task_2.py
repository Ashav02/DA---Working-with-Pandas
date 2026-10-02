"""Given a DataFrame with a 'release_date' column containing movie release dates (as strings),
add three new columns: 'year', 'month', and 'day' by extracting these values from the 'release_date' column using Pandas.
<br><br><em><strong>Hint:</strong> Use the .dt accessor after converting to datetime.</em>
"""

import pandas as pd

df = pd.DataFrame({
    "movie": ["Movie A", "Movie B", "Movie C", "Movie D"],
    "release_date": ["15-03-2024", "07-11-2023", "22-01-2025", "30-08-2022"]})

#Convert release_date to datetime
df["release_date"] = pd.to_datetime(df["release_date"],format="%d-%m-%Y")

#Extract year, month, and day
df["year"] = df["release_date"].dt.year
df["month"] = df["release_date"].dt.month
df["day"] = df["release_date"].dt.day

print(df)