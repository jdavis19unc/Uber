import numpy as np
import pandas as pd

data_file = pd.read_csv('cab_rides.csv')

def getdict(column: str):
    data = data_file[str(column)]
    dictionary = {}
    for i in data:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

destinations = getdict('cab_type')
print(destinations)