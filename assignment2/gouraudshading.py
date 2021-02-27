'''
Mayavi is one of the most booming application for visualization.
It has MatLab feature in it 
It has mlab library which includes most of MatLab features for 3D ploting
It does support vtk features
For installing mayavi which is little have packge since it has following prerequisits  so to include this we should install before installing:
    - import vtk (pip install vtk)
    - import pyQt (pip install pyQt5)
    - import pySide (pip install pySide6)
    - import mayavi (pip install mayavi)
Then we are ready to incorporate matlab features in python code.
'''
import numpy as np
from mayavi import mlab      #mayavi library for mlab

##  data: Matlab `peaks()`
x, y = np.mgrid[-1:1:30j,-1:1:30j]
Z1 = np.exp(-((x)**2+(y)**2))

## data: for domain for superimposing function.

z = np.linspace(0, 0, 900)  # 30 * 30 = 900 values, 1 for each possible combination of (x,y)
Z = np.reshape(z, x.shape)  # Z.shape must be equal to X.shape = Y.shape

## Mayavi
## Superimposed gaussian function surface generation for using mlab
surf = mlab.surf(x,y,Z, color =(0.0,0.0,0.0),representation = 'wireframe')
surf = mlab.surf(x, y, Z1, color =(0.0,1.0,0.0))

# Change the visualization parameters. Which allow to choose shade feature in interpolation as 'flat|Gouraud| phong'

surf.actor.property.interpolation = 'gouraud'   # for flat shading of plot we must select imterpolation as flat 
surf.actor.property.specular = 0.1
surf.actor.property.specular_power = 5

## lets plot the fucntion on mlab version of mayavi
mlab.title('Gouraud shading on superimposed plot of 30*30 grid domain')
mlab.savefig('Gouraud shading superimposed 30by30.png')
mlab.show()