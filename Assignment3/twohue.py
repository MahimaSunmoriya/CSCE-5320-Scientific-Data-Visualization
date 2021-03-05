import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input X and Y limits, where 30 * 30 is domain plane size . On which our function plot will supure imposed.
X1,Y1=np.meshgrid(np.linspace(-1,1,30),np.linspace(-1,1,30))
Z1=np.exp(-10*((X1**4)+(Y1**4)))             # Domain Plane Z value
fig = plt.figure()
ax = fig.add_subplot()
ax.set_axis_off()
#Ploting the figure with our function for domain superimposed 
twohuemap =ax.contourf(X1, Y1, Z1, 30, offset=0, cmap='RdBu' )
# # Lets Plot colorbar for Z values
cbar =fig.colorbar(twohuemap, orientation='horizontal', spacing= 'proportional', shrink=1.2, ticks = range(0,30))

plt.title('Two Hue colormap with red and Blue')
plt.savefig('twohue.png')
plt.show()  # Plot Figure