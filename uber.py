import numpy as np
import pandas as pd
import os
from typing import Union
import datetime

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


def isolate_data(column: str, value: str):
    data_2 = data_file.loc[data_file[column] == value]
    return data_2


isolated_data = isolate_data('cab_type', 'Uber')

isolated_data_2 = isolate_data('name', 'UberX')


isolated_data_2.to_csv("Curated_Uber.csv")

print(isolated_data_2)
