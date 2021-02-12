import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Input X and Y limits and convering it in matrix to input our fucntion
X,Y=np.meshgrid(np.linspace(-1,1,30),np.linspace(-1,1,30))
G=np.exp(-((X)**2+(Y)**2))
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#Ploting the figure with our function
surf=ax.plot_surface(X,Y,G,color='green')
ax.set_axis_off()
plt.title("Elevation plot without domain plane for 30 * 30 grid ")
plt.show()
plt.savefig('withoutdomain30.jpeg')      # Plot Figure