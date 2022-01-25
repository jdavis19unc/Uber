import numpy as np
import pandas as pd
from typing import Union

data_file = pd.read_csv('cab_rides.csv')

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

#destinations = getdict('destination')
#print(destinations)

def getavg(column: Union[int, float]):
    if isinstance(column, int) == True:
        print("int")

getavg(1)


def isolate_data(column: str, value: str):
    data_2 = data_file.loc[data_file[column] == value]
    return data_2


isolated_data = isolate_data('destination', 'North Station')

print(isolated_data)





    
  