import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#reading data
houses_data=np.genfromtxt("Housing.csv",delimiter=',')
houses_array=np.array(houses_data)
print(houses_array.shape)
print(houses_array.ndim)
print(houses_array.size)
print(houses_array.dtype)
print(houses_array)