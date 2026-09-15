#Load any dataset of your choice (not the one used in the class demo), and export it to Excel format with a custom sheet name like 'Analysis2024'.

import pandas as pd

df = pd.read_excel("mobile_expenses.xlsx")


df.to_excel("analysis2024.xlsx", sheet_name="Analysis2024",index=False)
