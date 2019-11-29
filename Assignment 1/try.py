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

x_riv = [159,158,153,154,163,167,171,217,160,213,173,163,185,216,159,162,186,170,
          150,159,186,211,164,218,228,156,179,151,173,145,185,186,181,213,159,208,
          158,191,224,218,178,170,183,171,218,214,218,151,158,225]
y_riv =[6,38,16,7,30,129,166,292,32,287,127,159,254,286,156,156,233,461,
          12,45,229,347,47,324,322,16,120,6,457,19,233,232,228,282,18,292,
          20,247,314,344,120,34,233,128,351,287,280,7,9,313]
    
x_nonriv = [230,216,489,311,120,137,417,302,89,427,369,88,79,476,70,316,48,394,
           32,448,416,360,287,91,31,293,92,418,68,344,428,55,294,53,380,371,
           486,238,446,131,125,308,312,311,275,359,132,210,457,246,299,360,421,493,
           236,375,392,48,478,254,427,57,445,448,50,404,392,424,451,379,359,269,
           147,412,236,337,232,362,479,475,306,91,462,275,468,102,306,237,338,405,
           264,410,220,106,389,110,247,391,63,433]

y_nonriv = [83,214,163,85,402,430,307,49,436,425,244,374,227,43,296,70,118,366,
           411,215,113,333,24,235,383,109,402,444,261,420,245,438,149,416,245,66,
           18,55,411,226,271,100,336,208,253,444,387,123,340,108,334,365,375,445,
           158,355,377,233,75,441,103,404,308,313,96,83,49,173,185,406,458,460,
           253,464,98,478,471,327,240,489,239,425,452,65,173,441,478,149,475,90,
           289,198,150,168,147,95,457,93,414,197]
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