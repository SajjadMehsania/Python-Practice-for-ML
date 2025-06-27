import numpy as np

'''
numpy has 0 based index.
+ve and -ve indexing both exists.
12345 i.e index -1==>5 and index 1==>1

array[index] for 1d
array[row,column] for 2d
'''

arr=np.array([10,22,34,43,55])
print(arr[-1])
print(arr[3])
# print(arr[-10]) ==>INDEXOUTOFBOUND

#Slicing=>extracting subset of array
print('-------------------')
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:3])
print(arr[:4])
print(arr[::2])
print(arr[:-3])
print(arr[:-1])
print(arr[::-1])
print(arr[-4:-1])
print(arr[::-3])
print('-------------------')
#Fancy indexing :-> Selecting multiple elements at one
arr=np.array([5,6,7,8,9,10])
print(arr[[0,3,1]])
print('-------------------')

#Data filtering / Boolean Masking :-> Elements are filtered based on conditions
arr=np.array([5,6,7,8,9,10])
print(arr[arr>7]) #10 times faster than loops.


