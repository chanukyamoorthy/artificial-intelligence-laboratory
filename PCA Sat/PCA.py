import numpy as np
import matplotlib.image as ming
import matplotlib.pyplot as plt
from numpy import linalg as LA

r = ming.imread("1.jpg")
print(r.shape)

g = ming.imread("2.jpg")
print(g.shape)

b = ming.imread("3.jpg")
print(b.shape)

img_i = ming.imread("4.jpg")
print(img_i.shape)

rows, cols, dim = r.shape
r_mean = 0
g_mean = 0
b_mean = 0
i_mean = 0

for i in range(0,rows):
    for j in range(0,cols):
        r_mean = r_mean+r[i][j][0]

for i in range(0,rows):
    for j in range(0,cols):
        g_mean = g_mean+g[i][j][0]

for i in range(0,rows):
    for j in range(0,cols):
        b_mean = b_mean+b[i][j][0]

for i in range(0,rows):
    for j in range(0,cols):
        i_mean = i_mean+img_i[i][j][0]


r_mean = r_mean/(rows*cols)
g_mean = g_mean/(rows*cols)
b_mean = b_mean/(rows*cols)
i_mean = i_mean/(rows*cols)

org_mean = [r_mean, g_mean, b_mean, i_mean]
print(org_mean)

res_img = np.empty([rows,cols,4])
print(res_img.shape)

for i in range(0,rows):
    for j in range(0,cols):
        res_img[i][j][0] = r[i][j][0]
        res_img[i][j][1] = g[i][j][0]
        res_img[i][j][2] = b[i][j][0]
        res_img[i][j][3] = img_i[i][j][0]

# subtract _mean
for i in range(0,rows):
    for j in range(0,cols):
        res_img[i][j][0] = r[i][j][0]-org_mean[0]
        res_img[i][j][1] = g[i][j][0]-org_mean[1]
        res_img[i][j][2] = b[i][j][0]-org_mean[2]
        res_img[i][j][3] = img_i[i][j][0]-org_mean[3]


cov = np.empty(shape=(4,4))

for i in range(0,4):
    for j in range(0,4):
        cov[i][j] = 0
        for k in range(0,rows):
            for l in range(0,cols):
                cov[i][j] = cov[i][j] + res_img[k][l][i]*res_img[k][l][j]
        cov[i][j] = cov[i][j]/(rows*cols-1)

print(cov)

eival, eivec = LA.eig(cov)
print(eival)
print(eivec)

eigen1 = np.array(eivec[:][0])
eigen2 = np.array(eivec[:][1])
eigen3 = np.array(eivec[:][2])
eigen4 = np.array(eivec[:][3])

comp1 = np.empty([rows,cols])
comp2 = np.empty([rows,cols])
comp3 = np.empty([rows,cols])
comp4 = np.empty([rows,cols])

for i in range(rows):
    for j in range(cols):
        comp1[i][j] = np.matmul(eigen1.T,res_img[i][j].T)+org_mean[0]
        comp2[i][j] = np.matmul(eigen2.T,res_img[i][j].T)+org_mean[1]
        comp3[i][j] = np.matmul(eigen3.T,res_img[i][j].T)+org_mean[2]
        comp4[i][j] = np.matmul(eigen4.T,res_img[i][j].T)+org_mean[3]

fig = plt.figure(figsize = (8,8))
fig.add_subplot(2,2,1)
plt.imshow(comp1, cmap = "gray")
fig.add_subplot(2,2,2)
plt.imshow(comp2, cmap = "gray")
fig.add_subplot(2,2,3)
plt.imshow(comp3, cmap = "gray")
fig.add_subplot(2,2,4)
plt.imshow(comp4, cmap = "gray")

plt.show()








