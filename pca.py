import cv2
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

im1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE).flatten()
im2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE).flatten()
im3 = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE).flatten()
im4 = cv2.imread('4.jpg', cv2.IMREAD_GRAYSCALE).flatten()


aux_img = np.array([im1, im2, im3, im4])


aux_img = aux_img.T

def cov(im1,im2):
    global aux_img
    add = 0
    n = aux_img.shape[0]
    for x, y in zip(aux_img[:, i], aux_img[:, j]):
        add += x * y
        
    return add / (n - 1)

cov_matrix = np.array([[0]*4]*4, dtype = np.float)



for i in range(4):
    for j in range(4):
        cov_matrix[i, j] = cov(i,j)
        
print(cov_matrix)


eigen_values , eigen_vectors = LA.eig(cov_matrix)
print(eigen_values)
print(eigen_vectors)


pca = []

for i in range(4):
    temp = np.matmul(eigen_vectors[:, i].T, aux_img.T)
    pca.append(temp)
    
pca = np.array(pca)

plt.figure(figsize = (15, 15))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(pca[i].reshape(598, 676), cmap = 'gray')