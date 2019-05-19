#This program gives the weight of wine parameters for the quality equation
#Parameters taking into consideration: FIXED ACIDITY, pH, ALCOHOL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
import quality_equation as qe


# Preprocessing Input data
data = pd.read_csv('wines_red_all_parameters.csv')


#Compute the weight of each parameter on the qaulity equation,
par=qe.parameters()

#Create computed quality and real quality vector
q_computed=[]
q=[]

number_samples=1000
start=0
for i in range(start,start+number_samples):
    wine = data.iloc[i,:]

    q_pred =  wine[0]*par[0] + wine[8]*par[1] + wine[10]*par[2]
    q_computed.append(round(q_pred))
    q.append(wine[11])



error=0
for i in range(number_samples):
    er=(q[i]-q_computed[i])*(q[i]-q_computed[i])
    error = error + er
print(error)


RMSE=sqrt(error/number_samples)
print('The value of the RMSE is: ' + str(RMSE))
