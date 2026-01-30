import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
# random data 
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# visualize data

plt.plot(A,b,'ro')


# For linear algebra array, the notation starts with row and then column
#Change row vector to column vector
# In linear regression, to account for the y-intercept, we usually add a column of 1s to our feature matrix
A = np.array([A]).T

B = np.array([b]).T
# np.array : 1x15 - row array
# array().T: 15 x1 - column array

# Create vector 1
ones = np.ones((A.shape[0],1) , dtype =np.int8)
#np.ones() : initialize array in value 1 
A=np.concatenate((A,ones), axis=1)
# np.concatenate: join arrays A and 1
# np.concatenate: design column matrix (15x2)

# Use formular to solve for x 
x= np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(B)
# A.transpose : Transpose row  matrix (2x15)
# A: design column matrix (15x2)
# x = 1x2 [0.3226, 1.8804] (slope, intercept)

x0 = np.array([[1,46]]).T
y0 = x0*x[0][0] + x[1][0]
#[[1,46]]: list of list - create 2 D matrix with 1 row and 2 column 

# line equation : y = 0.326 x+ 1.8804 

plt.plot(x0,y0)

# Test predicting data
x_test = 12
y_test = x_test*x[0][0] + x[1][0]

print(y_test)
plt.show()


