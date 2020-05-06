"""
Jared Jacobowitz
April 2020
Recreating: https://youtu.be/kbKtFN71Lfs
"""

import matplotlib.pyplot as plt
import numpy as np
import random


vertices = np.array([[0,0],
                     [4,0],
                     [2,np.sqrt(3)],
                     [0,0]])

points = np.array([[0.25, 0.1]]) # Starting point

dots = 100 # number of dots

def newPos(index, old_x, old_y):
    vertex_x = vertices[index][0]
    vertex_y = vertices[index][1]
    new_x = 0.5*(vertex_x + old_x) # new x value
    new_y = 0.5*(vertex_y + old_y) # new y value
    return([new_x,new_y])

rand_prev = -1

def uniqueRand(rand_prev):
    rand = random.randint(0,len(vertices)-1)
    if rand != rand_prev:
        return(rand)
    else:
        uniqueRand(rand_prev)
    

if len(vertices) < 5:
    for i in range(dots-1):
        rand = random.randint(0,len(vertices)-2)
        points = np.concatenate((points, [newPos(rand, points[i][0], points[i][1])]), axis = 0)

else:
    for i in range(dots-1):
        rand = random.randint(0,len(vertices)-1)
        while rand == rand_prev:
            rand = random.randint(0,len(vertices)-1)
        points = np.concatenate((points, [newPos(rand, points[i][0], points[i][1])]), axis = 0)
        rand_prev = rand
            
    

# Plotting
plt.scatter(points[:,0], points[:,1], marker='o', s=5, color = '#1f77b4')
plt.plot(vertices[:,0],vertices[:,1],'k-', linewidth=1)
plt.axis('off')

plt.title('Chaos Game with {0} Vertices and {1} Steps'.format(len(vertices)-1, dots))

plt.tight_layout()

plt.savefig('ChaosGamewith{0}Verticesand{1}Steps.png'.format(len(vertices)-1, dots), dpi = 600)

plt.show()