import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_excel("linear_data.xlsx")
x = df[['x']]
y = df[['y']]
model = LinearRegression()
model.fit(x,y)
coff = model.coef_[0]
print(coff)
pre7 = pd.DataFrame([[7]], columns=['x'])
pre = model.predict(pre7)
print("prediction of 7", pre[0])
pre12 = pd.DataFrame([[12]], columns=['x'])
pre = model.predict(pre12)
print("prediction of 12", pre[0])