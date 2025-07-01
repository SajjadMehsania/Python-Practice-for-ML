'''Vectorization in NumPy means performing operations on entire arrays without using explicit loops'''

list1=[1,2,3]
list2=[4,5,6]
result=[x+y for x,y in zip(list1,list2)]
print(result)
'''This above methods works. But will be slow to handle large data. 

To overcome this we use vectorization
'''
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=arr1+arr2
print(result) #This approach is faster then python loops

result=arr1*arr2
print(result) 

'''broadcasting     vs   vectorization
   expands smaller       performs operation on
   arrays to larger      entire array

   faster than loops     100*faster than loops

   Can expand 1D to 2d   Helps in matrix operations
'''