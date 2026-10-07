"""Transform the ipl_df DataFrame to add a new column 'match_margin_type' that labels each match as 'Runs' if the 'win_by_runs' value is greater than 0,
'Wickets' if 'win_by_wickets' is greater than 0, or 'Tie/No Result' otherwise.
<br><br><em><strong>Hint:</strong> Use numpy.select() or pandas' apply() for this transformation.</em>"""


import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/ipl_matches_dataset.csv")

