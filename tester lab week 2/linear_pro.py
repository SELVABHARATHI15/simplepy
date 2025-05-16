import numpy as np
from scipy.odr import polynomial
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
x = np.array([1,2,3,4]).reshape(-1,1)
y = np.array([1,4,9,15])
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
model = LinearRegression()
model.fit(x_poly,y)
coeff = model.coef_q
print(f"co-efficient {coeff}")
print(f"intercept {model.intercept_}")
x_test = poly.transform([[10]])
y_pred = model.predict(x_test)
print(f"\nprediction for 10: {y_pred}")