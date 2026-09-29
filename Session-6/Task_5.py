"""Use ChatGPT or Copilot to generate a pandas function that finds and returns all outlier transaction amounts in a Paytm wallet DataFrame using the Z-score method,
then test the function with sample data.
"""


import pandas as pd
from scipy.stats import zscore

def find_outliers(df, column='transaction_amount'):
    z_scores = zscore(df[column])
    
    outliers = df[abs(z_scores) > 2]
    
    return outliers


# Sample Paytm wallet data
df = pd.DataFrame({
    'transaction_id': [101, 102, 103, 104, 105, 106, 107],
    'transaction_amount': [500, 700, 600, 550, 650, 5000, 750]
})

# Test the function
outliers = find_outliers(df)

print("Outlier Transactions:")
print(outliers)