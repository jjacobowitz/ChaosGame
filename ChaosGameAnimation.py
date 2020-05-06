import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

# Vertex coordinates and number of dots
vertices = np.array([[0,0],
                     [4,0],
                     [2,np.sqrt(3)],
                     [0,0]])

dots = 2000

def newPos(index, old_x, old_y):
    """
    Halves the distance between the current (x,y) coordinate and the vertex
    Returns the new (x,y) coordinate
    -------
    index : index from 'vertices' of the vertex that was chosen
    vertex_x, vertex_y : x/y coordinate of the chosen vertex
    old_x, old_y : previous x/y coordinate
    new_x, new_y : x/y coordinate halfway between old and vertex coordinates
    -------
    """
    vertex_x = vertices[index][0]
    vertex_y = vertices[index][1]
    new_x = 0.5*(vertex_x + old_x)
    new_y = 0.5*(vertex_y + old_y)
    return([new_x,new_y])

# Evaluate points and add to 'points' array
points = np.array([[0.25, 0.1]])
for i in range(dots-1):
    points = np.concatenate((points, [newPos(random.randint(0,len(vertices)-2), points[i][0], points[i][1])]), axis=0)

# Initialize the figure and title
fig = plt.figure(figsize=(6.25,5))
ax = plt.gca()
ax.set_title('Chaos Game with {0} Vertices and {1} Steps'.format(len(vertices)-1, dots))

# Draw outside shape
ax.plot(vertices[:,0],vertices[:,1],'k-', linewidth=1)

# Initialize scatter object for current step and all evaluated dots
scat_curr = ax.scatter([], [], marker='X', s=15, c='black')
scat_dots = ax.scatter([], [], marker='o', s=5, c='#1f77b4', zorder=-1)
plt.axis('off')

def init():
    scat_curr.set_offsets(np.c_[vertices[0,0], vertices[0,1]])
    scat_dots.set_offsets(np.c_[vertices[0,0], vertices[0,1]])
    plt.axis('off')
    return scat_curr, scat_dots

def animate(i):
    scat_curr.set_offsets(np.c_[points[i,0], points[i,1]])  
    scat_dots.set_offsets(np.c_[points[:i,0], points[:i,1]]) 
    plt.axis('off')
    ax.legend([scat_curr], ['index = {0}'.format(i)], loc='upper left')      
    return scat_curr, scat_dots

anim = FuncAnimation(fig, animate, init_func=init, frames=dots, interval=1)

# plt.show()

# Create the gif animation
Writer = matplotlib.animation.writers['pillow']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=-1)
anim.save('ChaosGameAnimation.gif', writer=writer)