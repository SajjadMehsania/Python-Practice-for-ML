'''
Remove/ Delete element from array
np.delete(array,index,axis)
'''
import numpy as np
arr=np.array([1,2,3,4])
new_arr=np.delete(arr,3)
print(new_arr)

print('2D--------------')
arr2=np.array([[1,2],[3,4]])
new_arr=np.delete(arr2,1,axis=0)
print(arr2)
print('\n',new_arr)

new_arr=np.delete(arr2,1,axis=1)
print('\n',new_arr)
