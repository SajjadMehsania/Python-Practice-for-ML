import pandas as pd
data1={
 'Fruits':['Mango','Apple','Banana'],
 'Price':[100,40,50],
 'quantity':[15,10,5]
}
df1=pd.DataFrame(data1)
print(df1)

####After a month
data2={
 'Fruits':['Mango','Apple','Banana'],
 'Price':[120,50,50],
 'quantity':[12,7,3]
}
df2=pd.DataFrame(data2)
print(df2)

print(df1.compare(df2,keep_equal=True))