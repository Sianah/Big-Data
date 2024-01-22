#This imports NumPy and Rich, and then initializes a Rich console object 
#for enhanced output formatting.
import numpy as np
import rich
from rich import print

console= rich.get_console()

#Here, arr is created using np.arange(0, 30) which generates an array with values from 0 to 29. 
#It is then reshaped into a 3D array with the shape (2, 3, 5) and printed along with its shape.
arr = np.arange(0,30).reshape((2,3,5)) #makes array between 0-30, then reshaped to be a 2x3x5, two arrays, each 3x5
print(arr)
print(arr.shape)

#These lines demonstrate accessing specific elements or slices of arr. 
#arr[0] accesses the first element (2D array) and arr[-1] accesses the last element (2D array). 
#Their shapes are also printed.
print(arr[0]) #getting elements out of the array. 0 is taking the first thing which is the first out of the whole thing
print(arr[0].shape)

print(arr[-1]) #takes the second thing

#This creates a 1D array arr2 and demonstrates various slicing techniques: range slicing, 
#step slicing, and reversing.
arr2 = np.array([-1,4,10,47,2,59])
print(arr2[1:4]) #takes array 1 up to 4. In this case, the 4, 10, and 47. Slices elements 1 to 3
print(arr2[::2]) # Takes every other element. Jumps by 2
print(arr2[1:5:2]) #starts at one, go up to 5, then every other one. Slices and steps through the array
print(arr2[::-1]) #prints in reverse order

#This uses the Rich console to print a horizontal rule for better visual separation in the output.
console.rule()

print(arr)

#These lines demonstrate more advanced slicing techniques, including slicing specific dimensions, 
#using ellipsis (...) for shorthand, and adding a new axis with np.newaxis.
print(arr[0][0:2]) #takes first two rows, but not the third row. Aka, takes the first array, 
#then the first two rows of it

console.rule()
print(arr[:,:,0:2])
print(arr[:,:,0:2].shape) #shape is now 2x3x2 instead of 2x3x5. For 0.2, keep two things that are tied

console.rule()
print(arr[...,0:2]) #everything should stay the same till the last dimension. Should be the same as the last one

console.rule()
print(arr)
print(arr[...,1,0:2]) #yada yada yada, keep the first(0), or second(1) row, then keep first two numbers of each row
print(arr[...,1:2,0:2]) #should be same as last one

console.rule()
print(arr[:,np.newaxis,0,:]) #keep all the same so now there's two of something, then keep the first row, and all the values in that row
print(arr[:,np.newaxis,0,:].shape)

console.rule()
#The final part showcases fancy indexing (using an array of indices to select elements) and boolean 
#indexing (using a boolean array to filter elements). The code also demonstrates how to create a 
#boolean condition (arr2 < 10) and then use it to select elements from arr2.
print(arr2)
print(arr2[np.array([1,2,2,1])]) #gathers positions 1, 2, 2, and 1 from the initial array

print(arr2[np.array([True,True,False,False,True,False])]) #True(keep the -1, True(keep the 4), False(don't keep the 2, etc.))
print(arr2<10)
print(arr2[arr2<10]) #prints off the values that are less than 10

