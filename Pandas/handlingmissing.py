import pandas as pd
import numpy as np
df=pd.read_excel("customers.xlsx")
# print(df)
print(df.isnull().sum())  # Count of missing values in each column

print(df.dropna())#we cant use thisfor every column because it will delete all rows with any missing value. SO oneshould figure out which columns are important and then drop the rows with missing values in those columns.

print(df['city'].replace(np.nan,"HI")) 
df['city']=df['city'].replace(np.nan,"New orleans")
print(df)

print(df['number'].mean())
df['number']=df['number'].replace(np.nan,"396.55")
print(df)

# df['name']=df['name'].bfill()
# print(df)

df.fillna('unknown')
print(df)

value=df['segment'].mode()[0]
df['segment']=df['segment'].fillna(value)
print(df['segment'])

df['name']=df['name'].fillna('Misiing')
print(df)
value=df['age'].median()
print(df['age'].fillna(value))