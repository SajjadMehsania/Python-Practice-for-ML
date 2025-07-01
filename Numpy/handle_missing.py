#handling missing values using numpy
#NaN = not a number
import numpy as np
arr=np.array([1,2,3,np.nan,4,5,np.nan])
print(np.isnan(arr))

#replace missing
print(np.nan_to_num(arr)) #replaces missing with number. Default is 0
print(np.nan_to_num(arr,nan=9))

#Hndling infinite values. eg 10^1000 , 1/0, etc
arr=np.array([1,2,np.inf,4,-np.inf])
print(np.isinf(arr))
#replace infinite value with finite value
cleaned_arr=np.nan_to_num(arr,posinf=30,neginf=-30)
print(cleaned_arr)
