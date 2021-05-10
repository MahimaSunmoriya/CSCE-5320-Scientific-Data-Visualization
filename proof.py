### From above we have Hessian Matrix, eigenValue and eigenvector 
## Now Les Proof  HS = LemdaS, S is and eigenVector , H is Hessian Matrix and Lemda is eigenval


## Lets First do for F(0,0)
import numpy as np
H = np.array([[-2,0],[0,-2]])
Lemda = -2 
s = np.array([[1],[0]])
print("For F(0,0")
print("Value of Hs \n", np.matmul(H,s))
print("Value of Lemdas \n", Lemda*s)

# For F(10,10)
H = np.array([[5.50790820e-85,5.53558614e-85],[5.53558614e-85,5.50790820e-85]])
Lemda = -2.76779341e-87
s = np.array([[0.70710678],[-0.70710678]])
print("For F(10,10")
print("Value of Hs \n", np.matmul(H,s))
print("Value of Lemdas \n", Lemda*s)


H = np.array([[5.50790820e-85,5.53558614e-85],[5.53558614e-85,5.50790820e-85]])
Lemda = 1.10434943e-84
s = np.array([[0.70710678],[0.70710678]])
print("For F(10,10")
print("Value of Hs \n", np.matmul(H,s))
print("Value of Lemdas \n", Lemda*s)