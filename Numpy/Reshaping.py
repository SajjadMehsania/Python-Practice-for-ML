#Reshaping and manipulating arrays
#Without modifing the data of the array we change the dimensions of that array is called reshaping

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(4,2)) #(Rows,Columns)
#Reshaping does not creates a copy. It returns a view

