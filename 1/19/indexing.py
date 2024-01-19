import numpy as np
import rich
from rich import print

console= rich.get_console()

arr = np.arange(0,30).reshape((2,3,5)) #makes array between 0-30, then reshaped to be a 2x3x5, two arrays, each 3x5
print(arr)
print(arr.shape)

print(arr[0]) #getting elements out of the array. 0 is taking the first thing which is the first out of the whole thing
print(arr[0].shape)

print(arr[-1]) #takes the second thing

arr2 = np.array([-1,4,10,47,2,59])
print(arr2[1:4]) #takes array 1 up to 4. In this case, the 4, 10, and 47
print(arr2[::2]) #takes every other one. Jumps by 2
print(arr2[1:5:2]) #starts at one, go up to 5, then every other one
print(arr2[::-1]) #prints in reverse order

console.rule()

print(arr)

print(arr[0][0:2]) #takes first two rows, but not the third row

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
print(arr2)
print(arr2[np.array([1,2,2,1])]) #gathers positions 1, 2, 2, and 1 from the initial array

print(arr2[np.array([True,True,False,False,True,False])]) #True(keep the -1, True(keep the 4), False(don't keep the 2, etc.))
print(arr2<10)
print(arr2[arr2<10])

