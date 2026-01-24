import numpy as np
import matplotlib 
import matplotlib as plt

# random data 
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# visualize data

plt.plot(A,b,'ro')

#Change row vector to column vector
# In linear regression, to account for the y-intercept, we usually add a column of 1s to our feature matrix
A = np.array([A]).T
B = np.array([b]).T

# Create vector 1
ones = np.ones()