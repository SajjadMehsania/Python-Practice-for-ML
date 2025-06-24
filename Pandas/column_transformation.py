import pandas as pd
data={
    'bonus':[0.00,0.24,1.23,0.00,0.76],
    'First Name':['elijah','klaus','rebekah','stefen','damon'],
    'Last Name':['mikelson','john','salvatore','gilbert','fores'],
    'Months':['January','February','March','April','May'],
    'Salary':[20000,30000,400000,120000,45600]
}
df=pd.DataFrame(data)
print(df)
print('----------------------------------')

df.loc[(df['bonus']==0),'getbonus']='No Bonus -'
df.loc[(df['bonus']>0),"getbonus"]='Bonus+'
print(df)

print('----------------------------------')

print(df.loc[1,'First Name'])
print(df.loc[1])

print('----------------------------------')

df['bopercent']=(df['Salary']/100)*20
print(df)
print('----------------------------------')

def extract(value):
    return value[0:3]
df['shortmonth']=list(map(extract,df['Months']))
print(df['shortmonth'])
print('----------------------------------')


#merge two columns
df['Full Name']=df['First Name'].str.capitalize() + ' ' +df['Last Name'].str.capitalize()
print('----------------------------------')
print(df['Full Name'].str.upper())
print(df['Full Name'])
print('----------------------------------')
