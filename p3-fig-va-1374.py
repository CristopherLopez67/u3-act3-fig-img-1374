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