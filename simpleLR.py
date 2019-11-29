# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

X = np.array([50,53,54,55,56,59,62,65,67,71,72,74,75,76,79,80,82,85,87,90,93,94,95,97,100])
Y = np.array([122,118,128,121,125,136,144,142,149,161,167,168,162,171,175,182,180,183,188,200,194,206,207,210,219])
n = X.shape[0]

xx = np.sum([X[i]*X[i] for i in range(n)])
xy = np.sum([X[i]*Y[i] for i in range(n)])
yy = np.sum([Y[i]*Y[i] for i in range(n)])
x = np.sum(X)
y = np.sum(Y)

w2 = (x*y - n*xy)/(x**2 - n*xx)
w1 = (y - w2*x)/n


Y_pred = [ w1 + w2 * X[i] for i in range(n)]

plt.scatter(X,Y,color = 'red')
plt.plot(X,Y_pred,color = 'blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['Regression line', 'Actual'])
plt.show()

error = np.sum([(Y_pred[i] - Y[i])**2 for i in range(n)])/n
print('Mean square error is ', error)