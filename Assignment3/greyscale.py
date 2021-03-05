import numpy as np
from matplotlib import pyplot as plt

# Input X and Y limits, where 30 * 30 is domain plane size . On which our function plot will supure imposed.
X1,Y1=np.meshgrid(np.linspace(-1,1,30),np.linspace(-1,1,30))
Z1=np.exp(-10*((X1**4)+(Y1**4)))             # Domain Plane Z value
fig = plt.figure()
ax = fig.add_subplot()
ax.set_axis_off()
#Ploting the colormap for our function greyscale 

greymap =ax.contourf(X1, Y1, Z1, 30, cmap="gray")
# Lets Plot colorbar for Z values
cbar =fig.colorbar(greymap, orientation='horizontal', spacing= 'proportional', shrink=1.2, ticks = range(0,30))
plt.title('greyscale colormap')
plt.savefig('greyscale.png')
plt.show()  # Plot Figure