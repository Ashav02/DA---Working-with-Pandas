"""Use ChatGPT to suggest two additional univariate or bivariate analyses you could perform on the IPL_2023_Batsmen dataset,
then implement one of them in code and show the output."""

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Admin/Documents/Ashav/Pandas Assignment/DA---Working-with-Pandas/DataSets/IPL_2023_Batsmen.csv")
print(df)

correlation = df["Runs"].corr(df["Strike_Rate"])

print("Correlation between Runs and Strike Rate:", correlation)

#Scatter plot
plt.scatter(df["Runs"], df["Strike_Rate"])
plt.xlabel("Runs")
plt.ylabel("Strike Rate")
plt.title("Runs vs Strike Rate")
plt.show()