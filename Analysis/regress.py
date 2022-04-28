import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('UberXl_Pairs.csv', index_col=False, header=0)
data = data.dropna()



pairs = []
t = ["distance","cab_type","time_stamp","destination","source","price","surge_multiplier","id","product_id","name","pair", "Unnamed: 0"]
for i in data:
    if i not in t:
        pairs.append(i)

print(pairs)

#x = data[['distance',
#'Boston University', 'Fenway', 'Financial District', 'Haymarket Square', 'North End', 'North Station', 
#'Northeastern University', 'South Station', 'Theatre District', 'West End']] 
#x = data['distance']
#>>> y = [2*a for a in x if a % 2 == 1]
params = []
params.append("distance")
for i in pairs:
    params.append(i)

print(params)

x = data[params] 
print(x)
y = data['price']
print(y)
print(x)


x = sm.add_constant(x) # adding a constant
 
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
 
print_model = model.summary()


print(print_model)



result = model.params


print(result)





result.plot(kind='bar', yticks=range(0,8, 1))
plt.show()
print(1)
exit()




# with sklearn
#regr = linear_model.LinearRegression()
#regr.fit(x, y)

#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)


# with statsmodels







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