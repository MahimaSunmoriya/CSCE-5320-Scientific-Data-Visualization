import matplotlib as py
import numpy as np
import pandas as pd
import numdifftools as nd
First,Second = -1 , 1
function = lambda xandy: np.exp(-((xandy[0]**2)+(xandy[1]**2)))
Hess = nd.Hessian(function)([10,10])
print("Hessian Metric for f(10,10):\n" ,Hess)
eigenval, eigenvect = np.linalg.eig(Hess)
print("eigenvalue for f(10,10) is : ", eigenval )
print("eigenvector for f(10,10) is : \n ", eigenvect )
Lemda = round(eigenval[0])

#### Proof
print( "Hs: \n", np.matmul(Hess,eigenvect[0]))
print("lemdas", (Lemda * eigenvect[0]))
