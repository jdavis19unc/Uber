import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Curated_uber.csv', index_col=False, header=0)
data.dropna()
y = data.price.values
x = data.distance.values
print(x)
print(y)





x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)

regr = linear_model.LinearRegression()
regr = linear_model.LinearRegression()
regr.fit(x, y)
coef = regr.coef_
intercept = regr.intercept_

plt.scatter(x, y,  color='black', label="testing")
plt.plot(x, regr.predict(x), color='blue', linewidth=3, label = "tests")

plt.xlabel("Distance (Miles) ")
plt.ylabel("Price (Dollars)")
plt.title("Linear Regression of Price and Distance for UBERX")
annotation = f"Equation: y =  {coef}x  + {intercept}"
plt.annotate(annotation, (5,40), size=7)















plt.show()