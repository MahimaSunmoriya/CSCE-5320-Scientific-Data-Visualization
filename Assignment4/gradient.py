import numpy as np
from matplotlib import pyplot as plt

#Input X1 and Y1 value
X1,Y1=np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10))
Z1=np.exp(-((X1**2)+(Y1**2)))             # Function for 2D plot
dx, dy = np.gradient(Z1)
n = -2

# Defining color
color = np.sqrt(((dx-n)/2)*2 + ((dy-n)/2)*2) 
fig, ax = plt.subplots()

fig = plt.figure()
ax = fig.add_subplot()
q = ax.quiver(X1,Y1,dx,dy,color)
ax.set_aspect('equal')
plt.title('Gradient HedgeHog Plot')
plt.savefig('gradientHedgehog.png')
plt.show()