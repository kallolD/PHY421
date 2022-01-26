# using the numpy library for numerical computations

# import the library for use in the code using the import command
# here I import the numpy library 'as np' meaning I use np as an alias for numpy

import numpy as np

# # numpy library numberous utilities like 
# # - zeros, to define empty matrices
# # - transpose, for matrix transpose calculaiton
# # - dot, for dot product of 2 arrays

# # it also contains sub-libraries to deal 
# # with specific types of mathematical operations 
# # - random, for random sampling
# # - linalg, for linear algebra
# # - fft, for fourier transforms

# # define a matrix in numpy
# x = np.array([1,2,3])
# print(x)

# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)
# # get the dimensions of the matrix
# print('dimensions of matrix :', x.shape)

# # (3,3) identity matrix
# y = np.eye(3)
# print(y)

# # adding arrays
# z = x + y
# print(z)

# # matrix multiplication using dot (can also be done with matmul)
# # dot adjusts itself depending on the input
# print(np.dot(x,z))

# # arrays starting at a and ending at b
# # using linspace or arange
# x = np.linspace(0,10,100)
# print(x)
# print(x.shape)

# x = np.arange(0,10,0.1) # does not include 10
# print(x)
# print(x.shape)

# # sine function
# x = np.linspace(0,10,100)
# y = np.sin(x)

# print(y)





