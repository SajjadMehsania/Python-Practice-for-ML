'''
vertically
horizontally

vstack() row wise
hstack() column wise
'''
import numpy as np
arr=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

print(np.vstack((arr,arr2)),'Vertically stacked')
print(np.hstack((arr,arr2)),'Horizontally stacked')
'''
Helps in merging arrays row wise and column wise
'''