"""Given a DataFrame of YouTube video titles, use str.upper to convert all titles to uppercase,
then chain str.replace to substitute every space with an underscore"""

import pandas as pd 

df = pd.DataFrame({'title':["jadal zamana (interval theme)",
    "lehanga lahke lahke",
    "casa tupka",
    "yeshanagula",
    "shararat"]})

df['title'] = df['title'].str.upper().str.replace(' ','_')

print(df)