
"""
e1 = 0.9*m1 + 0.3*m2 + 0.1*m3 - 30
e2 = 0.1*m1 + 0.5*m2 + 0.2*m3 - 25
e3 = 0.0*m1 + 0.2*m2 + 0.7*m3 - 10
"""

import numpy as np
import Direct_Solver as ds

A = np.array([[0.9, 0.3, 0.1], [0.1, 0.5, 0.2], [0.0, 0.2, 0.7]])
f = np.array([30.0, 25.0, 10.0])
print(A)
print(f)

A, f = ds.SolverGE(A, f)
x = ds.SolverBS(A, f)
print(x)
