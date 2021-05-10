import matplotlib as py
import numpy as np
import numdifftools as nd
First,Second = -1 , 1
function = lambda xandy: np.exp(-((xandy[0]**2)+(xandy[1]**2)))
Hess = nd.Hessian(function)([0,0])
print("Hessian Metric for f(0,0):\n" ,Hess)
eigenval, eigenvect = np.linalg.eig(Hess)
print("eigenvalue for f(0,0) is : ", eigenval )
print("eigenvector for f(0,0) is : \n ", eigenvect )

#### Proof

Lemda = round(eigenval[0])

eigenVctTran = np.array(eigenvect[0])


print(eigenVctTran.T)
print( "Hs: \n", np.matmul(Hess,eigenvect[0]))
print("lemdas", (Lemda * eigenvect[0]))

