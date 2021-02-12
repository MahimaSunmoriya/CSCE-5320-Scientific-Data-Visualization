import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input X and Y limits, where 10 is domain plane size . On which our function plot will supure imposed.
X1,Y1=np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10))
Z1=np.exp(-((X1**2)+(Y1**2)))             # Domain Plane Z value
z = np.linspace(0, 0, 100)  # 10 * 10 = 100 values, 1 for each possible combination of (x,y)
Z = np.reshape(z, X1.shape)  # Z.shape must be equal to X.shape = Y.shape
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
#Ploting the figure with our function
ax.plot_wireframe(X1, Y1, Z, color= 'black',facecolor = 'red')
ax.plot_surface(X1, Y1, Z1, color ='green')
plt.title('Superimposed Plot with 10 * 10 domain')
plt.savefig('superimposed with 10 cross 10 domain.png')
plt.show()         # Plot Figure