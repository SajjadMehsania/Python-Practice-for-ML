'''
np.concatenate((array1,array2),axis=0)
axis=0 i.e row wise add / stacking
axis=1 i.e column wise add / stacking
'''
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

print(np.concatenate((arr1,arr2)))