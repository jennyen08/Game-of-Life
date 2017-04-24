# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:08:24 2017

@author: Jenny

LOVE AND WAR
"""

import numpy as np
import matplotlib.pyplot as plt

#grid = np.random.randint(2, size=(50,50))
#non = np.nonzero(grid)
N = 100
n = 50
A = 1
B = 0.5

grid = np.random.randint(3, size=(N,N))*0.5
#grid = np.zeros((N,N))
##int_state_1 = np.random.randint(2, size=(n,N))*A
##int_state_2 = np.random.randint(2, size=(n,N))*B
##grid[0:50,0:100] = int_state_1 #
##grid[50:100,0:100] = int_state_2 #
#grid[0::4,1:] = 1.0
#grid[1::5,1:] = 0.5

myobj = plt.matshow(grid, cmap=plt.cm.gray)
new_state = np.zeros((N,N))
neighood_1 = np.zeros((N,N))
neighood_2 = np.zeros((N,N))

for t in range(1,1000):
    neighood_1 = np.zeros((N,N))
    for i in range(1,N):
        for j in range(1,N):
            box = grid[i-1:i+2,j-1:j+2]
            neigh_num= np.nonzero(box == 1)
            neighood_1[i][j] = len(neigh_num[0])
            if grid[i][j] == 1:
                eigh_num= np.nonzero(box == 1)
                neighood_1[i][j] = len(neigh_num[0])-1

    neighood_2 = np.zeros((N,N))                
    for i in range(1,N):
        for j in range(1,N):
            box2 = grid[i-1:i+2,j-1:j+2]
            neigh_num2 = np.nonzero(box2 == 0.5)
            neighood_2[i][j] = len(neigh_num2[0])
            if grid[i][j] == B:
                eigh_num= np.nonzero(box2 == 0.5)
                neighood_2[i][j] = len(neigh_num2[0])-1                
                
    for i in range(1,N):
        for j in range(1,N):
            if grid[i][j] == 0:
                if neighood_1[i][j] > 2:
                    new_state[i][j] = A
                elif neighood_2[i][j] > 2:
                    new_state[i][j] = B
            if grid[i][j] != 0:
                if grid[i][j] == A and neighood_1[i][j] == 3:
                    new_state[i][j] = A
                elif grid[i][j] == B and neighood_2[i][j] == 3:
                    new_state[i][j] = B
                elif grid[i][j] == B and neighood_2[i][j] == 2:
                    new_state[i][j] = B
                elif grid[i][j] == A and neighood_1[i][j] == 2:
                    new_state[i][j] = A
                else:
                    grid[i][j] = 0
                    
    grid = new_state
    myobj.set_data(grid)
    plt.draw()
#    plt.pause(0.1)
