"""Use the IQR method to detect outliers in the 'order_amount' column of a Zomato orders DataFrame and print
the order IDs that are considered outliers.
Calculate Q1, Q3, and IQR, then filter orders outside the [Q1 - 1.5*IQR, Q3 + 1.5*IQR] range.
"""

import pandas as pd

df = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'order_amount': [250, 300, 280, 1500, 320, 290, 40, 310, 270, 2500]
})
print(df)

#calculet Q1 & Q3 

Q1 = df['order_amount'].quantile(0.25)
print(Q1)
Q3 = df['order_amount'].quantile(0.75)
print(Q3)

IQR = Q3 - Q1
print(IQR)

#calculet lower & upper limit

lower = Q1 - 1.5 * IQR
upper = Q3 - 1.5 * IQR

#find outliner

outliners = df[(df['order_amount']<lower)|(df['order_amount']>upper)]

print(outliners)
