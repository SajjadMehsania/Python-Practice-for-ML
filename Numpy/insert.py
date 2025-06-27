'''
add, remove, stack, split an array
remove unnecessary data
adding new data

ARRAYS HAVE FIXED SIZE SO YO PERFORM ANY OPERATION YOU HAVE TO MAKE A NEW ARRAY
'''
import numpy as np
arr=np.array([1,2,3,4,5])
#np.insert(array,index,value,axis=None)
#axis is non means value is inseted into flattened array
#In 2D array axis=0 means insert data row wise and axis=1 means insert data column wise
new_arr=np.insert(arr,2,10,axis=None)
print(new_arr)
print('---------------------------------')
print('Insert in 2D')
arr=np.array([[1,2],[3,4]])
print(arr)
new_arr=np.insert(arr,1,[5,6],axis=1) #Adds column
print('New Column added \n',new_arr)
new_arr=np.insert(arr,1,[5,6],axis=0) #Adds Row
print('New Row Added \n',new_arr)
new_arr=np.insert(arr,1,[5,6],axis=None)
print('Array flattened and element inserted \n',new_arr)