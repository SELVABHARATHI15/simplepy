import random as r
import pandas as pd
# df = pd.read_excel('data2.xls', sheet_name='Sheet1')
# print(df)
df = pd.read_excel("health+.xlsx")
df.fillna({"age":r.randint(10,50)},inplace=True)
x = df["weight"].mean()
y = df.fillna({"weight":x},inplace=True)
m = df["bp"].mode()
n = df.fillna({"bp":m},inplace=True)
h = df.loc[1,'height'] = 156
print(df)
print(y)
print(n)
