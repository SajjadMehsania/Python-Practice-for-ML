import numpy as np
arr=np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(arr)
print(arr.shape)  #2, 4 i.e 2 rows 4 columns

print(arr.size) #8 i.e total numer of elements in an array

print(arr.ndim) #2 i.e dimension of the array

# arr=np.array([
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ],
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ],
#     [
#         [1,2,3,4],
#         [5,6,7,8]
#     ]
# ])
# print(arr.ndim) 3-d

print(arr.dtype) #Data type of elements

age=np.array(['89','52'])
print(age.dtype)
age=age.astype(int) #type conversion
print(age.dtype)