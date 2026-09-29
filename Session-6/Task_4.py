"""For a DataFrame containing daily IPL match ticket sales (columns: date, tickets_sold),
calculate the Z-score for each day's tickets_sold, and print the dates where the absolute Z-score is greater than 2.
<br><br><em><strong>Constraint:</strong> Use pandas and scipy.stats.zscore for calculations.</em>"""

import pandas as pd
from scipy.stats import zscore

# Calculate Z-score
df['z_score'] = zscore(df['tickets_sold'])

# Filter rows where absolute Z-score > 2
outliers = df[abs(df['z_score']) > 2]

# Print dates of outliers
print(outliers['date'])