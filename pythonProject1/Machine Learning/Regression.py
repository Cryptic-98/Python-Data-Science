import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('Iris.csv')
# print(df.head())
# y = mx + c
# y - dependent variable, x - independent variable
# m - coefficient, c - intercept
# feature selection ↓
data = df[['PetalLengthCm', 'PetalWidthCm']]
x = df['PetalLengthCm']
y = df['PetalWidthCm']
# create scatter plot to see if there's any relation between x and y
plt.scatter(x, y)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
# plt.show()
# for us to have a line of best fit we need to train our model by splitting our data into train and test sets.
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.4, random_state=20)
# now let's split our data into training (40%) and testing (60%)↑
# random_state ensures that the data is not recreated each time the model is created.↑
# put x_train and y_train into a numpy array ↓
x_train = np.array(x_train).reshape(-1, 1)
y_train = np.array(y_train).reshape(-1, 1)
lr = LinearRegression()
lr.fit(x_train, y_train)
# y = mx + c
c = lr.intercept_
print(c)
m = lr.coef_
print(m)
