import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input X and Y limits, where 30 * 30 is domain plane size . On which our function plot will supure imposed.
X1,Y1=np.meshgrid(np.linspace(-1,1,20),np.linspace(-1,1,20))
Z1=np.exp(-((X1**2)+(Y1**2)))             # Domain Plane Z value
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

#Ploting the figure 
surf = ax.plot_surface(X1, Y1, Z1, cmap = 'spring_r')
plt.title('Elevation Plot with domain plane')
plt.savefig('elevationplot.png')
plt.show()  # Plot Figure