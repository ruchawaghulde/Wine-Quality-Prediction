#This program computes the quality equation for the following parameters:
#VOLATIL ACIDITY
#pH
#ALCOHOL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Preprocessing Input data
data = pd.read_csv('VolatilAcidity_pH_Alcohol.csv')

volatil_acidity= data.iloc[:,0]
pH = data.iloc[:, 1]
alcohol = data.iloc[:,2]
quality = data.iloc[:,3]


# Building the model
X=0 #Weigh of the FIXED ACIDITY on the quality function
Y=0 #Weigh of the PH on the quality function
Z=0 #Weigh of the ALCOHOL on the quality function

L = 0.0001  # The learning Rate
epochs = int(1000)  # The number of iterations to perform gradient descent

n = len(quality) # Number of elements in X

# Performing Gradient Descent for getting the quality equati
for i in range(epochs):

    q_pred = volatil_acidity*X + pH*Y + alcohol*Z  # The current predicted value of quality
    D_volatil_acidity = (-2.0/n)* sum(volatil_acidity * (quality - q_pred))  # Parial derivative weight fixed acidity
    D_pH = (-2.0/n) * sum(pH*(quality - q_pred))  # Partial derivaitve weight pH
    D_alcohol = (-2.0/n) * sum(alcohol*(quality-q_pred))
    X = X - L * D_volatil_acidity  # Update X weight of fixed acidity
    Y = Y - L * D_pH  # Update Y weight of pH
    Z = Z - L * D_alcohol  # Update Z weight of alcohol


print("Weight of the fixed volatil parameter: ")
print(X)
print("Weight of the pH parameter: ")
print(Y)
print("Weight of the Alcohol parameter: ")
print(Z)



#List of good wines found in the internet that have actually won awards

print("Wine found on the internet that has actually won awards, Duckhorn. Computed quality qith our model: ")
q_computed_Duckhorn=0.58*X+3.46*Y+14.9*Z
print(q_computed_Duckhorn)

print("Wine found on the internet that has actually won awards, Antler Hill. Computed quality qith our model: ")
q_computed_Antler_Hill=0.57*X+3.59*Y+15.2*Z
print(q_computed_Antler_Hill)

print("Wine found on the internet that has actually won awards, Cune. Computed quality qith our model")
q_computed_Cune=0.47*X+3.64*Y+13.5*Z
print(q_computed_Cune)
