"""You have a DataFrame with a 'review' column containing user reviews from Zomato. Use str.contains to filter and display only the reviews that mention the word 'delivery'.<br><br><em><strong>Hint:</strong> Remember to handle case sensitivity so that 'Delivery' and 'delivery' are both matched.</em>
"""

import pandas as pd 

df = pd.DataFrame({
    'review': [
        'Fast delivery and good food',
        'The Delivery was late',
        'Food quality was excellent',
        'Quick delivery service',
        'Taste was amazing']})

df['review'] = df[df['review'].str.contains('delivery', case=False, na=False)]
print(df)