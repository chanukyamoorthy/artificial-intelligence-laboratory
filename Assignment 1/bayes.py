# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:20:54 2019

@author: 
"""

import matplotlib.pyplot as plt
import numpy as np
import math

p_riv = 0.1
p_nonriv = 0.9

x_riv = [149, 166, 175, 169, 166, 170, 192, 214, 207, 187, 183, 169, 147]
y_riv = [13, 42, 80, 125, 165, 206, 251, 291, 343, 380, 419, 467, 500]
    
x_nonriv = [24, 93, 120, 36, 139, 49, 158, 102, 131, 33, 232, 355, 477, 281, 416, 259, 364, 455, 437, 360, 278, 232, 313, 406, 460]
y_nonriv = [45, 42, 100, 173, 224, 291, 307, 76, 438, 464, 35, 63, 98, 138, 157, 228, 223, 232, 311, 331, 343, 428, 472, 411, 437]
band1=plt.imread('band1.gif')
band2=plt.imread('band2.gif')
band3=plt.imread('band3.gif')
band4=plt.imread('band4.gif')
riv_band = []
nonriv_band = []
for i in range(0,len(x_riv)):
    riv_band.append([band1[x_riv[i]][y_riv[i]][0], band2[x_riv[i]][y_riv[i]][0], band3[x_riv[i]][y_riv[i]][0], band4[x_riv[i]][y_riv[i]][0]])
for i in range(0,len(x_nonriv)):
    nonriv_band.append([band1[x_nonriv[i]][y_nonriv[i]][0], band2[x_nonriv[i]][y_nonriv[i]][0], band3[x_nonriv[i]][y_nonriv[i]][0], band4[x_nonriv[i]][y_nonriv[i]][0]])
riv_band = np.array(riv_band).T
nonriv_band = np.array(nonriv_band).T
riv_cov = np.cov(riv_band)
nonriv_cov = np.cov(nonriv_band)
t1 = [np.mean(riv_band[0]), np.mean(riv_band[1]), np.mean(riv_band[2]), np.mean(riv_band[3])]
t2 = [np.mean(nonriv_band[0]), np.mean(nonriv_band[1]), np.mean(nonriv_band[2]), np.mean(nonriv_band[3])]
test_data = []
for i in range(0,512):
    test_data1 = []
    for j in range(0,512):
        test_data1.append([band1[i][j][0], band2[i][j][0], band3[i][j][0], band4[i][j][0]])
    test_data.append(test_data1)
result = []
riv_class = []
nonriv_class = []
sigma1 = math.sqrt(np.linalg.det(riv_cov))
sigma2 = math.sqrt(np.linalg.det(nonriv_cov))
for i in range(0,512):
    temp = []
    for j in range(0,512):
        dev1 = [test_data[i][j][0]-t1[0], test_data[i][j][1]-t1[1], test_data[i][j][2]-t1[2], test_data[i][j][3]-t1[3]]
        dev2 = [test_data[i][j][0]-t2[0], test_data[i][j][1]-t2[1], test_data[i][j][2]-t2[2], test_data[i][j][3]-t2[3]]
        riv_class = np.dot(np.dot(dev1,np.linalg.inv(riv_cov)), np.array(dev1).T)
        nonriv_class = np.dot(np.dot(dev2,np.linalg.inv(nonriv_cov)), np.array(dev2).T)
        p1 = math.exp((-0.5)*riv_class)/sigma1
        p2 = math.exp((-0.5)*nonriv_class)/sigma2
        if p1*p_riv >= p2*p_nonriv:
            temp.append([255,255,255,255])
        else:
            temp.append([0,0,0,255])
    result.append(temp)
result = np.array(result)
result = np.uint8(result)
plt.imsave('new1.jpg',result)