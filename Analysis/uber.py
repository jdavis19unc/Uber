import numpy as np
import pandas as pd
import os
from typing import Union
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_file = pd.read_csv('Data\cab_rides.csv')
print("yes")



def getdict(column: str):
    data = data_file[str(column)]
    dictionary = {}
    for i in data:
        if i not in dictionary:
            print(i)
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary


def isolate_data(column: str, value: str):
    data_2 = data_file.loc[data_file[column] == value]
    return data_2



isolated_data = isolate_data('name', 'UberXL')

arr = []
s = ""
d = ""
dfNew = isolated_data.copy()
for index, row in isolated_data.iterrows():
    s = row['source']
    d = row['destination']
    arr.append(s + ", " + d )




dfNew["pair"] = arr
print(dfNew)



new = dfNew["pair"]


states=pd.get_dummies(new,drop_first=True)
#print(states)

isolated_data = dfNew.drop("pair", axis=1)
#print(data_file)


x=pd.concat([dfNew,states],axis=1)


x.to_csv('UberXL_Pairs.csv')










#isolated_data_2.to_csv("Curated_Uber2.csv")

#print(isolated_data_2)
