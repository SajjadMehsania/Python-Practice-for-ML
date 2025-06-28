'''
splitting means dividing array into multiple sub arrays

np.split() -->divides in equal part
np.hsplit()--> horizontal split
np.vsplit()-->vertical split
'''
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(np.split(arr,3))

arr=np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.vsplit(arr,2))
print(np.hsplit(arr,2))