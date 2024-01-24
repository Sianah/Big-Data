#This imports the NumPy library as np and the rich library, 
#specifically importing the print function from rich for formatted output in the console.
import numpy as np
import rich
from rich import print

console= rich.get_console()
#Two 2-dimensional arrays arr and arr2 are created using np.array. 
#Both arrays have a shape of 2x3 (two rows and three columns).
arr = np.array([[9, 2, 3], [0, 2, 4]])  # 2x3
arr2 = np.array([[-1, -2, 0], [3, 2, 1]])

#These lines use the print function from the Rich library to output arr and arr2. 
#Rich's print enhances the output with better formatting compared to Python's built-in print.
print(arr)
print(arr2)

#Here, element-wise addition is performed between arr and arr2, resulting in arr3. 
#This demonstrates how NumPy supports element-wise operations on arrays of the same shape.
arr3 = arr+arr2
print(arr3)  #prints out the added matrices together

#This line performs an element-wise comparison between arr and arr2. 
#It outputs a boolean array where each element is True if the condition 
#(arr element < arr2 element) is met, and False otherwise.
print(arr < arr2)  # prints out if the elements are less than the other with true and false statements

# broadcasting: make the shapes match by duplicating data
#Broadcasting is a powerful feature in NumPy that automatically expands the dimensions 
#of arrays to make shapes compatible for element-wise operations. 
#Here, [5] is broadcasted to match the shape of arr before addition. 
#This might raise a ValueError because the shapes are not directly compatible for broadcasting.
print(arr + np.array([5])) #in this case, it added 5 to each element in arr

# 5, 4, 3 added to original. Can add things to shape if they can be made to add to shape
#In this case, the 1D array [5, 4, 3] is broadcasted across the rows of arr, 
#meaning each row of arr is added element-wise to [5, 4, 3].
print(arr+np.array([5, 4, 3])) #adds [5 4 3] to each row

# Numpy is based on APL

#1/24 notes
console.rule()

arr = np.array([4,7,9])
print("arr =")
print(arr)
arr2 = np.array([2])
print("arr2 = ")
print(arr2)
print("arr + arr2 =")
print(arr+arr2)
print(arr2+np.zeros(arr.shape))
