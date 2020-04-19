import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import xlrd 

Kmean = KMeans(n_clusters=2)

# Read file
loc = ('../Datasets/real_data.xlsx') 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
city = sheet.col_values(1)
hotel = sheet.col_values(2)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
city1 = labelencoder.fit_transform(city)
hotel1 = labelencoder.fit_transform(hotel)

print(city1)
array= [city1, hotel1]
Kmean.fit(array)

print(Kmean.cluster_centers_)