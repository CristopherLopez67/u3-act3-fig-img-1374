import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

# Cristopher Lopez NC 1374
print("Cristopher Lopez Nc 1374")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_img = cv2.imread('ciudad.PNG')
plt.imshow(mi_img)
plt.title('ciudad y Cristopher Lopez Nc 1374')
plt.show()
print("+--+- Puntos de la imagen +--+-")
plt.imshow(mi_img)
x = [100,100,300,500]
y = [100,400,500,400]
plt.scatter(x,y,s=20,c="red")
plt.show()
print("-+-+-+  Cuadro azul en la imagen -+-+-+")
img_ciudad=cv2.imread('ciudad.PNG')
plt.imshow(img_ciudad)
x = [100,200,500,500,200]
y = [500,100,200,500,500]
plt.plot(x,y, c='blue')
plt.show()
print("+--++- circulo verde en la imagen ")
I = cv2.imread('ciudad.PNG')
plt.imshow(I)
N = 30 # lados del poligono 
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150
for i in range(N+1):
    t = 2*np.pi/N*i 
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x,y,c='green')
plt.show()