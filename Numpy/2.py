#np.array will convert the list into array
#np.array([LIST])



import numpy as np
lst=[1,2,3,4,5]
arr=np.array([1,2,3,4,5])

print(lst)
print(arr)

#1-D Array
arr=np.array([1,2,3,4,5])

#2-D Array also called matrix
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

#multi-D Array 
arr=np.array([
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ],
    [
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ]
])
print(arr)