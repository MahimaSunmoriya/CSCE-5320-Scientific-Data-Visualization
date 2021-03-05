import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl


# Input X and Y limits, where 30 * 30 is domain plane size . On which our function plot will supure imposed.
X1,Y1=np.meshgrid(np.linspace(-1,1,30),np.linspace(-1,1,30))
Z1=np.exp(-10*((X1**4)+(Y1**4)))             # Domain Plane Z value
fig = plt.figure()
ax = fig.add_subplot()
ax.set_axis_off()
# Making band of 30 black white stripes
col = mpl.colors.ListedColormap(['black','white','black','black' , 'white','black', 'white','black','black','white','black','white', 'black',
                'white','black','black', 'white','black', 'white','black', 'white','white', 'black','white', 'black', 'white', 'black','black',
                 'white','black'])
bounds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
norm = mpl.colors.BoundaryNorm(bounds, col.N)

# Plot 2D colormap with discrte 30 bands
zebra =ax.contourf(X1, Y1, Z1, 30, cmap=col )
# Lets Plot colorbar for Z values

cbar =fig.colorbar(zebra, orientation='horizontal', spacing= 'proportional', shrink=1.2,ticks = range(0,30) )

plt.title('Zebra colormap ')
plt.savefig('zebra.png')
plt.show()  # Plot Figure