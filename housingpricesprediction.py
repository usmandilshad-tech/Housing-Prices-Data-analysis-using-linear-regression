import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


##using data from https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
#reading data using Numpy
##houses_data=np.genfromtxt("Housing.csv",delimiter=',')
##print(houses_data)
##houses_array=np.array(houses_data)
##print(houses_array.shape)
##print(houses_array.ndim)
##print(houses_array.size)
##print(houses_array.dtype)
##print(houses_array)

#reading data using Pandas
df=pd.read_csv('Housing.csv')
print(df)
df.info()