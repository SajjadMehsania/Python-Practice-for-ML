import pandas as pd
data1={
    "empid":['E01','E02','E03','E04','E05'],
    'Names':['Elijah','Klaus','Reekah','Stefen','Forbes'],
    'Age':[34,56,78,99,56]
    }
data2={
    "empid":['E01','E02','E03','E04','E05'],
    'Salary':[45555,67666,89000,45666,80000]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(df1)
print()
print(df2)

print(pd.merge(df1,df2,on='empid'))


data1={
    "empid":['E01','E02','E03','E04','E08'],
    'Names':['Elijah','Klaus','Reekah','Stefen','Forbes'],
    'Age':[34,56,78,99,56]
    }
data2={
    "empid":['E01','E02','E03','E07','E05'],
    'Salary':[45555,67666,89000,45666,80000]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print()
print(pd.merge(df1,df2,on='empid',how='left')) #all data from df1 and common from df2 and df1 will be used
print()
print(pd.merge(df1,df2,on='empid',how='right'))#all data from df2 and common from df1 and df2 will e merged
print()

print(pd.merge(df1,df2,on='empid',how='outer'))#join both df1 and df2


data1={
    "empid":['E01','E02','E03','E04','E05'],
    'Names':['Elijah','Klaus','Reekah','Stefen','Forbes'],
    'Age':[34,56,78,99,56]
    }
data2={
    "empid":['E06','E07','E08','E09','E010'],
    'Names':['Mikel','Puthawala','Topiwala','Shaikh','Momin'],
    'Age':[18,16,21,22,20]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(pd.concat([df1,df2]))
print(df1+df2)