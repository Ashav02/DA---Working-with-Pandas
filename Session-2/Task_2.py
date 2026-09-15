#Find a small Excel file of your own mobile expenses (or create one with 5-10 rows),
#then use pandas read_excel() to load it and print the last 3 rows using tail().


import pandas as pd

expense = pd.read_excel("mobile_expenses.xlsx")

print(expense.tail(3))