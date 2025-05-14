import numpy as np
from sklearn.linear_model import LinearRegression
x = [[1],[2],[3],[4],[5]]
y = [1.2,1.8,2.6,3.2,3.8]
model = LinearRegression()
model.fit(x,y)
coff = model.coef_[0]
print(coff)
pre = model.predict([[7]])
print("prediction of 7", pre[0])
pre = model.predict([[12]])
print("prediction of 12", pre[0])