# matplotlib is a plotting utility
# extremely versatile, can be used to generate various kinds 2d and 3d plots
# within matplotlib, pyplot is one of the most widely used libraries

import numpy as np
import matplotlib.pyplot as plt

# sine and cosine function plot
x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)

# plt.plot(x, y, label='sin(x)')
# plt.plot(x, z, label='cos(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sines and cosines')
# plt.show()

# plt.plot(x, y, label='sin(x)')
# plt.plot(x, z, label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sines and Cosines')
# plt.legend()
# plt.show()

# # scatter plot

# x = np.random.normal(size=100000) # variance=1
# y = np.random.normal(size=100000) # variance=1
# plt.scatter(x, y, alpha=0.4)
# plt.axis('square')
# plt.axvline(0.0,color='k')
# plt.axhline(0.0,color='k')
# plt.show()