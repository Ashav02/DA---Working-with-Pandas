#Given a DataFrame of IPL teams with columns 'team', 'points', and 'net_run_rate',
#use sort_index() to sort the DataFrame by the default index in descending order,then print the result.


import pandas as pd

ipl_teams = pd.DataFrame({'team':['CSK','GT','MI','KKR','RCB','Punjab','Delhi'],
                          'points':[5,9,7,6,6,4,4],
                          'new_run_rate':[0.25,0.30,0.20,0.15,0.17,0.12,0.09]})

sort = ipl_teams.sort_index(ascending=False)

print(sort)