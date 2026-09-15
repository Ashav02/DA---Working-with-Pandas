#Given a list of follower counts for 5 Instagram influencers: [1200, 54000, 780, 150000, 32000], create a pandas Series called 'followers', then print the influencer(s) with the highest and lowest follower counts.

import pandas as pd

influencers = pd.Series([1200, 54000, 780, 150000, 32000])

maximum = pd.Series.max(influencers)
print("Maximum: ",maximum)

minimum = pd.Series.min(influencers)
print("Minimum: ",minimum)