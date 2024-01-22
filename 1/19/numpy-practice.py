
#Here, NumPy is imported with the alias np. A list data is defined, 
#and then converted into a NumPy array arr. 
#The array arr is printed, showing its contents.
import numpy as np
data = [1, 5, 2, 6, 10, 2]
arr = np.array(data)
print(arr)


#This code creates a two-dimensional array arr2 from the list of lists data2, and prints it.
data2 = [[4, 5, 1], [7, -2, 3]]
arr2 = np.array(data2)
print(arr2)


#Here, data3 is a list with mixed data types (integer, string, boolean). 
#When this is converted into a NumPy array arr3, NumPy converts all elements to a common data type, 
#which is object in this case. This is printed along with the type of the array and the type of the 
#first element.
# nand --> not number
data3 = [4, 'a', False]  # has object data type
arr3 = np.array(data3)
print(arr3)
print(type(arr3)) #ndarry is a n-dimensional array. A multidimensional container of items
# array prints out strings because it has to be homogeneous
print(type(arr3[0]))

# arrays are fast cause you know where the array is(need to know how far to jump)
# memory is random access --> that's what arrays jump for
# random data types mixing(like data3) cannot work. Will always come out as string


#These lines print the number of dimensions (ndim) and the shape of the arrays. 
#The shape is a tuple indicating the size of the array in each dimension.
print()
print(arr.ndim)  # google
print(arr2.ndim)
print(arr3.ndim)

print()
print(arr.shape)  # one dimensional. (6,)
print(arr2.shape)  # two dimensional(2,3)
print(arr3.shape)  # one dimensional(3,)

# tuples

# note, len(arr,shape) == arr.ndim (number of dimensions)
print(len(arr2.shape))  # for instance

# creation


#This creates a 3D array arr4 filled with zeros, with the shape (2, 4, 5). 
#The dimensions and shape are then printed.
arr4 = np.zeros((2, 4, 5))
print(arr4)
# is 3D object so will print out as such

print(arr4.ndim)
print(arr4.shape)

#arr5 is created with values from -5 to 5 (exclusive) with a step of 0.5. 
#arr6 is created with 50 linearly spaced numbers between -5 and 5.
arr5 = np.arange(-5, 5, .5)  # Array with steps of 0.5 from -5 to 5
print(arr5)
arr6 = np.linspace(-5, 5, 50) # 50 evenly spaced numbers from -5 to 5
print(arr6)


# reshaping
#Here, various reshaping operations are demonstrated. 
#reshape changes the shape of an array without changing its data, 
#ravel flattens the array into 1D. The -1 in reshape infers the size of that dimension 
#from the length of the array.
print(arr6.shape)
# has to multiply out to be same numbe of things in (so here, it should multiply to be 50)
arr7 = arr6.reshape((2, 5, 5))
print(arr7)

# could also do arr7 = arr6.reshape((1,50)) or arr7 = arr6.reshape((50,1)) but it will print different
# means opposite of unravel, so folding back in. Kind of like flattening
arr8 = arr7.ravel()
print(arr8)
print(arr8.shape)

arr9 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr9)

# gives more flexibility. When you don't want to decide rest of your dimensions, change it to -1
arr9a = arr9.reshape(-1)
print(arr9a)
print(arr9a.shape)

arr9b = arr9.reshape((3, -1))  # google
print(arr9b)
print(arr9b.shape)

# review

arr9c = arr9.reshape((1,1,-1,2))
print(arr9c)

#This transposes arr9, swapping rows and columns.
arr9T = arr9.T #.T means transpose
print(arr9T)

#Finally, the transposed array arr9T is saved to a file named arr.npy. 
#It is then loaded back into a new variable arr10.
#loading and saving
with open("arr.npy","wb") as f: #wb is to write to it
    np.save(f, arr9T)    #save(f, what you want to save)

with open("arr.npy","rb") as f: #rb is to read from it
    arr10 = np.load(f)
