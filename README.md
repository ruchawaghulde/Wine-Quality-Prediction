# Wine Quality Prediction
Wine Certification and assessment are essential elements in the wine industry that prevent adulteration and are important for quality assurance. Wine certification includes physiochemical tests like determination of pH, alcohol quantity, fixed and volatile acidity etc. We have a large dataset having the physiochemical tests (features) results and quality on the scale of 1 to 10 of wines.
We aim to make a model to predict the quality of red wine on a scale of 0–10 given a set of features as inputs by using Stochastic Gradient Descent Algorithm.
Such a model can be used not only by the certification bodies but also by the wine producers to improve wine quality based on the physiochemical properties and by the consumers to predict the quality of wines.

## Optimization Model
The optimization model we have used is Stochastic Gradient Descent. 
This algorithm tries to find the right weights by constantly updating them using the value of gradient, and returning the values that minimises the loss function. 
### Training: 
Model is trained using Stochastic Gradient Descent based on the important parameters like pH, alcohol, fixed acidity and volatile acidity.
### Validation: 
For validation of our model, we collected the data of several good and bad quality wines from the internet. We fed the data into our quality equation (objective function) and got the predicted values for the quality of wine.

## Conclusion
We have successfully used Stochastic Gradient Descent to predict the quality of wine. We got 7-8 for good quality, 5-6 for average quality wines and root ean-squared error = 0.75.
