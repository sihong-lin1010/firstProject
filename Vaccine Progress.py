import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("country_vaccinations.csv", index_col=False)

# print(data.head())
# print(data.shape)
# print(data.isnull().sum())
# print([column for column in data])


data = data.drop(['source_name','source_website'], axis=1)
# print([column for column in data])
# print(data.isnull().sum())
# print(data.info())

date = data.groupby(by=["date"])['daily_vaccinations'].sum().reset_index()
date.plot()
plt.show()