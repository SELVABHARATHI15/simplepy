import numpy as np
from sklearn.linear_model import LinearRegression
x = list(map(eval,input("enter the x values:").split(',')))
y = list(map(eval,input("enter the y values:").split(',')))
X = np.array(x).reshape(-1,1)
Y = np.array(y)
model = LinearRegression()
model.fit(X,Y)
x_pred = eval(input("enter the prodict:"))
y_pred =model.predict([[x_pred]])
print(f"predict of {x_pred} : {y_pred}")