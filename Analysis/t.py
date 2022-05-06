from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('UberX_Source.csv', index_col=False, header=0)
data = data.dropna()

print(data)
x = data[['distance',
'Boston University', 'Fenway', 'Financial District', 'Haymarket Square', 'North End', 'North Station', 
'Northeastern University', 'South Station', 'Theatre District', 'West End']] 
#x = data['distance']
y = data['price']
print(y)
print(x)


x = sm.add_constant(x) # adding a constant

model = sm.OLS(y, x).fit()
predictions = model.predict(x) 

print_model = model.summary()
print(print_model)






exit()




# with sklearn
#regr = linear_model.LinearRegression()
#regr.fit(x, y)

#print('Intercept: \n', regr.intercept_)
#print('Coefficients: \n', regr.coef_)


# with statsmodels