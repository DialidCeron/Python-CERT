#!/usr/bin/env python
#Cerón Rodríguez Lezly Dialid
#UNAM-CERT

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib.widgets import Button

ON = 255
OFF = 0
vals = [ON, OFF]
generacion=0

#Devuelve una matriz de n*n con valores aleatorios dada cierta probabilidad
def matriz_random(n):
	return np.random.choice(vals, n*n, p=[0.5,0.5]).reshape(n,n)
#Actualiza los valores de la matriz de acuerdo a las reglas de Conway

def actualizar(frameNum, img, matriz, n):
    nueva_matriz = matriz.copy()
    for i in range(n):
        for j in range(n):
            total = int((matriz[i, (j-1)%n] + matriz[i, (j+1)%n] + 
                         matriz[(i-1)%n, j] + matriz[(i+1)%n, j] + 
                         matriz[(i-1)%n, (j-1)%n] + matriz[(i-1)%n, (j+1)%n] + 
                         matriz[(i+1)%n, (j-1)%n] + matriz[(i+1)%n, (j+1)%n])/255)
            if matriz[i, j]  == ON:
                if (total < 2) or (total > 3):
                    nueva_matriz[i, j] = OFF
            else:
                if total == 3:
                    nueva_matriz[i, j] = ON
    img.set_data(nueva_matriz)
    matriz[:] = nueva_matriz[:]
    global generacion
    generacion+=1
    global txt
    txt.remove()
    txt=plt.text(0,0,'Generación: '+ str(generacion))
    
    return img,
  
#Condiciones de ejecución
n=300
tiempo=1000
matriz=np.array([])
matriz=matriz_random(n)
fig,ax=plt.subplots()
img=ax.imshow(matriz, interpolation='nearest')
ani = animation.FuncAnimation(fig, actualizar, fargs=(img,matriz,n,), frames=10,  interval=tiempo, save_count=50)
txt=plt.text(0,0,'Generación: '+ str(generacion))

plt.show()