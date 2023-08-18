x = "Hola mundo"

import numpy as np
import matplotlib.pyplot as plt

M = np.zeros((2,2))

M[0,0] = 1
M[0,0] = 3
M[0,0] = 5
M[0,0] = 7

M.T

def Transpose(M):
    
    T = M.copy()
    print(id(T),id(M))
    
    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            T[j,i] = M[i,j]
    return T 

# Graficacion 3d

A = 1
B = 3
omega = 2*np.pi/10
N = 50

t = np.linspace(0,10,N)
#t
r = np.zeros((N,3))


