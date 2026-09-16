#Suppose you have a DataFrame of IPL cricket matches with columns 'team1', 'team2', 'winner', and 'total_runs'.
#Write code to filter and display all matches where 'total_runs' is between 180 and 220 using boolean indexing.


import pandas as pd

df = pd.DataFrame({ 'team1':['CSK','GT','MI','Delhi'],
                   'team2' :['RCB','KKR','RR','SRH'],
                   'winner' :['RCB','GT','MI','SRH'],
                   'total_runs': [180,200,220,240]})

total_run = df[(df['total_runs']>= 180) & (df['total_runs']<= 200)]

print(total_run)
