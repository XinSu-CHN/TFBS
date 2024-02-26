import numpy
import pickle
import pandas
file_path = 'C:/Users/18101/Desktop/station_data_dict.pkl'

with open(file_path, 'rb') as f:
    data = pickle.load(f)

print(type(data))

if isinstance(data, dict):
    print(data.keys())