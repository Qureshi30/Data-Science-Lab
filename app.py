import pandas as pd
import matplotlib.pyplot as plt

pf = pd.read_csv('titanic.csv')
# print(pf.head())
# print(pf.isnull().sum())
# print(pf['age'].mean())
# print(pf['age'].mean(skipna=True))

# counts = pf["survived"].value_counts()
# print("Not survived:", counts[0])
# print("Survived:", counts[1])

# pf["survived"].value_counts().plot(kind="bar")
# plt.title("Survived Count")
# plt.xlabel("0 = Died, 1 = Survived")
# plt.ylabel("Count")
# plt.show()

print(pf.groupby("sex")["survived"].value_counts())