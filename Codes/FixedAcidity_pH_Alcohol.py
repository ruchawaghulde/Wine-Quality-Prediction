#This program computes the quality equation for the following parameters:
#FIXED ACIDITY
#pH
#ALCOHOL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Preprocessing Input data
data = pd.read_csv('FixedAcidity_pH_Alcohol.csv')

fixed_acidity= data.iloc[:,0]
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

# Performing Gradient Descent for getting the quality equation
for i in range(epochs):

    q_pred = fixed_acidity*X + pH*Y + alcohol*Z  # The current predicted value of quality
    D_fixed_acidity = (-2.0/n)* sum(fixed_acidity * (quality - q_pred))  # Parial derivative weight fixed acidity
    D_pH = (-2.0/n) * sum(pH*(quality - q_pred))  # Partial derivaitve weight pH
    D_alcohol = (-2.0/n) * sum(alcohol*(quality-q_pred))
    X = X - L * D_fixed_acidity  # Update X weight of fixed acidity
    Y = Y - L * D_pH  # Update Y weight of pH
    Z = Z - L * D_alcohol  # Update Z weight of alcohol


#There are two standard wines found on the internet with the value for each of the parameters used for the quality equation

print("Weight of the fixed acidity parameter: ")
print(X)
print("Weight of the pH parameter: ")
print(Y)
print("Weight of the Alcohol parameter: ")
print(Z)



print("Some randow wine on the internet evaluate as standard wine, Santa Rita 120. Computed quality qith our model: ")
q_computed_Santa_Rita_120=5.03*X+3.66*Y+12.8*Z
print(q_computed_Santa_Rita_120)

print("Some randow wine on the internet evaluate as standard wine, Joseph Carr. Computed quality qith our model: ")
q_computed_Joseph_Carr=6.1*X+3.71*Y+13.4*Z
print(q_computed_Joseph_Carr)
