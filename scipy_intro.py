# LECTURE 01
# import scipy 
# from scipy import constants
# constants 


# print(constants.pi) // 3.141592653589793


# constants unit
# print(dir(constants))
# unit category
# print(constants.h) // 6.62607015e-34
# Binary Prefixes
# print(constants.kibi) //1024
# Mass
# print(constants.gram) //0.001
# Angle
# print(constants.degree) //0.017453292519943295
# Time
# print(constants.minute) // 60.0
# print(constants.hour) // 3600.0
# # Length
# print(constants.mile) // 1609.3439999999998
# print(constants.light_year) // 9460730472580800.0
# # Pressure
# print(constants.atm) // 101325.0
# print(constants.bar) // 100000.0
# # Volume
# print(constants.liter) // 0.001
# print(constants.gallon) // 0.0037854117839999997
# # Speed 
# print(constants.kmh) // 0.2777777777777778
# print(constants.mph) // 0.447039999999999942
# # Temperature
# print(constants.zero_Celsius) // 273.15
# print(constants.degree_Fahrenheit) // 0.5555555555555556
# # Energy
# print(constants.eV) // 1.602176634e-19
# print(constants.calorie) // 4.184
# # Power
# print(constants.horsepower) // 745.6998715822701
# print(constants.dyn) // 1e-05


# LECTURE 02

# Root of an Equation 
# we will solve it using optomize.root function
# this fn takes 2 arguments: "fn" and x0 (assumed root)
# example: x + cos(x)

# import scipy
# from scipy.optimize import root
# # from math import cos
# import numpy as np
# def eqn(x):
#     return x + np.cos(x)
# my_root = root(eqn, 0) # Second argument is your guess of the root
# print(my_root.x) // [-0.73908513]

# A VERY IMP POINT 
# TypeError: 
# only 0-dimensional arrays can be conve  rted to Python scalars
# this error shows up becuase 
# This error occurs because scipy.optimize.root evaluates your objective 
# function by passing a NumPy array of 
# inputs (even if you only provided a single starting guess like x0=0), 
# but your objective function is trying to 
# force that array into a single plain Python number (scalar).
# With the release of NumPy 2.x, the rules for scalar conversion became much stricter. 


# # Minimizing aa data
# from scipy.optimize import minimize
# import numpy as np
# we will minimize the function 
# x**2 + x + 2
# in the minimize function these are the arguments used 
# "function_name", "assumed value of x say 0", method: "CG", 
# "BFGS", "NEWTON-CG", "L-BFGS-B", "TNC", "COBYLA", "SLSQP"


# def eqn(x):
#     return x**2 + x + 2
# minValue = minimize(eqn, 0, method='BFGS')
# print(minValue)
#   message: Optimization terminated successfully.
#   success: True
#    status: 0
#       fun: 1.75
#         x: [-5.000e-01]
#       nit: 2
#       jac: [ 0.000e+00]
#  hess_inv: [[ 5.000e-01]]
#      nfev: 8
#      njev: 4


# LECTURE 3
# Sparse Data
# Useless data is called sparse data
# method to use sparse data: 
# there are 2 matrix in sparse CSC(Comporssed Sparse Column)
# CSR(Comporssed Sparse Rows)
# Here we will create Sparse Matirx
# import numpy as np
# from scipy.sparse import csr_matrix

# arr1 = np.array([0, 0, 0, 1, 0, 0, 2, 0])
# print(csr_matrix(arr1))
#   (0, 3)        1 1 is at 3rd pos 3rd colmn pr 1
#   (0, 6)        2 2 is at 6th pos 6th column pr 2
# THIS IS NOT THE CORECT NOTATION BUT FOR UNDERSTANDING

# sparse arrays we need onyl useful values not 0s
# sparse matrix methods

# import numpy as np
# from scipy.sparse import csr_matrix
# arr1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# print(csr_matrix(arr1).data)
# [1 1 2] OUTPUT
# .data shows only the useful values

# import numpy as np
# from scipy.sparse import csr_matrix
# # to count non zeros
# arr1 = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0], [0, 2, 3]]) # 2D Array
# print(csr_matrix(arr1).count_nonzero())
# 4


# # to remove zero elemtns we use eliminate zeros
# import numpy as np
# from scipy.sparse import csr_matrix
# arr1 = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 3], [0, 0, 0]])
# new = csr_matrix(arr1)
# new.eliminate_zeros()
# print(new)
# <Compressed Sparse Row sparse matrix of dtype 'int64'
#         with 3 stored elements and shape (4, 3)>
#   Coords        Values
#   (1, 1)        1
#   (2, 1)        2
#   (2, 2)        3



# # duplicate values eliminate
# import numpy as np
# from scipy.sparse import csr_matrix
# arr1 = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 3], [0, 0, 0]])
# new = csr_matrix(arr1)
# new.sum_duplicates()
# print(new)
#   (1, 1)        1
#   (2, 1)        2
#   (2, 2)        3

# # here we will convert csr to csc using tocsc()
# import numpy as np
# from scipy.sparse import csr_matrix
# arr1 = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 3], [0, 0, 0]])
# new = csr_matrix(arr1).tocsc()
# print(new)
# <Compressed Sparse Column sparse matrix of dtype 'int64'
#         with 3 stored elements and shape (4, 3)>
#   Coords        Values
#   (1, 1)        1
#   (2, 1)        2
#   (2, 2)        3

# csr used more
