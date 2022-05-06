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


isolated_data = isolate_data('name', 'WAV')

isolated_data_2 = isolate_data('name', 'UberX')
s = []
for i in isolated_data_2['time_stamp']:
    epoch_time = i
   
    date_time = datetime.datetime.fromtimestamp(i / 1000)   
    s.append(date_time)

#isolated_data_2['Dates'] = s




new = isolated_data["source"]

states=pd.get_dummies(new,drop_first=True)
#print(states)

isolated_data = isolated_data.drop("source", axis=1)
#print(data_file)


x=pd.concat([isolated_data,states],axis=1)


x.to_csv('UberX_Source.csv')










#isolated_data_2.to_csv("Curated_Uber2.csv")

#print(isolated_data_2)