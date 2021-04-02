import numpy as np
from matplotlib import pyplot as plt

# Input X and Y limits
X1,Y1=np.meshgrid(np.linspace(-1,1,15),np.linspace(-1,1,15))
Z1=np.exp(-((X1**2)+(Y1**2)))             # Domain Plane Z value
#  defining Verocity function
def verocity(field):
    num_dims = len(field)
    return np.ufunc.reduce(np.subtract, [np.gradient(field[i], axis=i) for i in range(num_dims)])
dx,dy = np.gradient(Z1)   # gardient calculation
F = (dx,dy)
# verocity calling function 
u = verocity(F)
v= verocity(F)
fig, ax = plt.subplots()
# plot quiver verocity
ax.quiver(X1,Y1,u,v)
ax.set_aspect('equal')
plt.title('Veocity HedgeHog Plot')
plt.savefig('verocityHedgehog.png')
plt.show()