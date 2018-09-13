"""
This is a direct solution method for lnear systems of equations. 
First part is Gaussian Elimination (SolverGE) and Second part is for Backward Substitution (SolverBS). 
"""

import numpy


def SolverGE(A, f):
    n = f.size
    if (A.shape[0] != n or A.shape[1] != n):
        print("Error! Wrong input sizes!")
        return f

    for i in range(0, n-1):
        for j in range(i+1, n):
            if A[i, i] == 0:
                print("Error! Zero on diagonal is not acceptable.")
                print("Algorithm with pivoting is required.")
                return f

            m = A[j, i]/A[i, i]
            A[j, :] = A[j, :]-m*A[i, :]
            f[j] = f[j]-m*f[i]
    return A, f


def SolverBS(A, f):
    n = f.size
    # Check for compatible matrix and rhs sizes
    if (A.shape[0] != n or A.shape[1] != n):
        print("Error! Wrong input sizes!")
        return f
    # initialize the solution vector, x, to zero
    x = numpy.zeros((n, 1))
    # solve for last entry first
    x[n-1] = f[n-1]/A[n-1, n-1]
    # loop from the end to the beginning
    for i in range(n-2, -1, -1):
        sum = 0
    #    for known x values, sum and move to rhs
        for j in range(i+1, n):
            sum = sum + A[i, j]*x[j]
        x[i] = (f[i] - sum)/A[i, i]
    return x
