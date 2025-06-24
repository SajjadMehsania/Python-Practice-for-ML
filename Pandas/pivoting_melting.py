import pandas as pd
data={
    'keys':['k1','k2','k1','k2'],
    'names':['Elijah','Klaus','Rebekah','Stefen'],
    'house':['Red','green','yellow','blue'],
    'grades':[3,5,6,8]

}
df=pd.DataFrame(data)
print(df)

print(df.pivot(index='keys',columns='names',values=['house','grades']))


data={
    'names':['Elijah','Klaus','Rebekah','Stefen'],
    'gender':['F','M','M','F'],
    'Age':[31,15,26,84]

}
df1=pd.DataFrame(data)
print(df1)
print(pd.melt(df1,id_vars=['names'],value_vars=['gender','Age']))
