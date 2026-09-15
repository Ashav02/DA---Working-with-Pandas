#Download a CSV file of IPL match results from Kaggle or any open dataset,
#then use pandas read_csv() to load it into a DataFrame and display the first 10 rows using head().

import pandas as pd

ipl = pd.read_csv("each_match_records.csv")


print(ipl.head(10))