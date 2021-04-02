import numpy as np
from matplotlib import pyplot as plt

# Input X and Y limits
X1,Y1=np.meshgrid(np.linspace(-1,1,15),np.linspace(-1,1,15))
Z1=np.exp(-((X1**2)+(Y1**2)))             #function for 2d plot

# function defination
def divergence(f):
    num_dims = len(f)
    return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])

# Gradient calculation
du,dv = np.gradient(Z1)
F = (du,dv)
# divergence function calling for gradient value
div= divergence(F)
mag = np.linalg.norm(div)         # magnitutude Calculation 
fig, ax = plt.subplots()
ax = fig.add_subplot()
ax.pcolormesh(X1,Y1,div,cmap= 'hsv',shading = 'auto')  # colordivergence 
ax.set_aspect('equal')
plt.title('Color Divergence HedgeHog Plot')
plt.savefig('colordiveregenceHedgehog.png')
plt.show()