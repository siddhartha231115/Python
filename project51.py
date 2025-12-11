import numpy as np
arr = np.array([1, 2, 3, 4])
mat = np.array([[1, 2], [3, 4]])
np.zeros((2,3))
np.ones((3,3))
np.full((2,2), 7)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b
a - b
a * b
a * 5
a + 10
arr = np.array([10, 20, 30, 40, 50])
arr[0]  
arr[1:4] 
mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
mat[1,2]
mat[:,1]
a = np.array([1,2,3,4,5,6])
a.reshape(2,3)
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])
np.dot(A, B)
arr = np.array([10, 25, 5, 30])
arr > 10 
arr[arr > 10] 