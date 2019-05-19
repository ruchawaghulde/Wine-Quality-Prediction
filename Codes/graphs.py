
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('wines_red_all_parameters.csv')


fixed_acidity= data.iloc[:,0]
volatil_acidity= data.iloc[:,1]
pH = data.iloc[:, 8]
alcohol = data.iloc[:,10]
quality = data.iloc[:,11]



plt.figure()
plt.scatter(quality,fixed_acidity)
plt.xlabel('Quality')
plt.ylabel('Fixed Acidity')
plt.show()


plt.figure()
plt.scatter(quality,volatil_acidity)
plt.xlabel('Quality')
plt.ylabel('Volatil Acidity')
plt.show()


plt.figure()
plt.scatter(quality,pH)
plt.xlabel('Quality')
plt.ylabel('pH')
plt.show()


plt.figure()
plt.scatter(quality,alcohol)
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.show()
