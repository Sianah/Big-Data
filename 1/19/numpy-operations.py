import numpy as np
import rich
from rich import print

arr = np.array([[9, 2, 3], [0, 2, 4]])  # 2x3
arr2 = np.array([[-1, -2, 0], [3, 2, 1]])

print(arr)
print(arr2)
arr3 = arr+arr2
print(arr3)  # all matrix operations

print(arr < arr2)  # all matrix operations

# broadcasting: make the shapes match by duplicating data
print(arr + np.array([5]))

# 5, 4, 3 added to original. Can add things to shape if they can be made to add to shape
print(arr+np.array([5, 4, 3]))

# Numpy is based on APL
