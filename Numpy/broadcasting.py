'''
[100,200,300]=>price of products
10% off on aal products today
[90,180,270]

So to get this final price we need to create list and implementing for loop resulting in slowing down the program
'''

prices=[100,200,300]
discount=10 # 10%
final_prices=[]
for i in prices:
    final=i-(i*discount/100)
    final_prices.append(final)
print(final_prices)
#This above method is correct but it would slow down the program if the data is huge.
#to overcome this we use broadcasting. It is a numpy way to perform different operations without using loops

import numpy as np
prices=np.array([100,200,300])
discount=10 #scalar=> single value
final_prices=prices-(prices*discount/100)
print(final_prices)

'''how numpy handles array of different shapes?
'''
arr=np.array([100,200,300])
result=arr*2 #roadcasting of single value
print(result)

'''broadcasting of 1D and 2D array'''
matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30])
result=matrix+vector
print(result)

'''
incompatible shapes [1,2,3,4]+[1,2] ==>error

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20])  
matrix+vector ==>>>ERROR
'''