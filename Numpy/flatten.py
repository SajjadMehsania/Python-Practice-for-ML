import numpy as np
#When u want to convert multi dimensional array into 1d array
arr=np.array([[[1,2,3,4],[5,6,7,8]],[[3,4,5,6],[7,8,9,10]],[[1,2,3,4],[5,6,7,8]]])
print(arr.shape)#Total 3 blocks and each block has 2 rows and 4 columns i.e (3,2,4)
print(arr) 
print('-----------------------------------')
'''
.ravel() returns a view. original array will be modified
.flatten() returns copy and original array isnt affected
'''
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d.ndim)
print(arr_2d.ravel())
print(arr_2d.flatten())

print('Ravel------------')
ravel=arr_2d.ravel()
ravel[0]=99
print(arr_2d) #Created a view and not copy thats why i changed the 0th element of ravel and it affected arr_2d also

print('Flatten--------------')
flatten=arr_2d.flatten()
print(flatten)
flatten[0]=1
print(flatten)
print(arr_2d) #Creates a copy and not view thats why on changing the value of flatten , arr_2d is'nt affected