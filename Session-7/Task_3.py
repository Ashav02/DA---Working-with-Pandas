"""You have a DataFrame of Instagram posts with columns: PostID, Likes, and Comments. Use applymap() to convert all numeric values in the Likes and Comments columns to strings formatted as '1.5K', '2M', etc., similar to how Instagram displays large numbers.
"""

import pandas as pd

df = pd.DataFrame({'PostID':['ID01','ID02','ID03','ID04','ID05','ID06','ID07','ID08','ID09','ID10'],
                   'Likes':[150000,2500000,2600000,4500000,6500000,1000000,25000000,35000000,100000000,12500000],
                   'Comments':[2000,1000,5000,60000,7000,50000,100000,10000,15000,45000]})

print(df)

def format_number(x):
    if x >= 1000000:
        return f'{x/1000000:.1f}M'
    elif x >= 1000:
        return f'{x/1000:.1f}K'
    else:
        return str(x)

df[['Likes','Comments']] = df[['Likes','Comments']].map(format_number)
print(df)