import numpy as np
from matplotlib import pyplot as plt
#import divergence

# Input X and Y limits.
X1,Y1=np.meshgrid(np.linspace(-1,1,15),np.linspace(-1,1,15))
Z1=np.exp(-((X1**2)+(Y1**2)))             # Z function

def divergence(f):
    num_dims = len(f)
    return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])

# gradient calculation
du,dv = np.gradient(Z1)
F = (du,dv)
# call divergence fucntion
div= divergence(F)
fig, ax = plt.subplots()

# magnitutude Calculation
mag = np.linalg.norm(F)
fig = plt.figure()
ax = fig.add_subplot()
# plotting on the quiver
ax.quiver(X1,Y1,div,div,scale=mag)
ax.set_aspect('equal')
plt.title('Divergence HedgeHog Plot')
plt.savefig('diveregenceHedgehog.png')
plt.show()