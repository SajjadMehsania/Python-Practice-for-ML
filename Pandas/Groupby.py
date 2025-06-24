import pandas as pd
#for summerising data
data = {
    'Person': ['Alice', 'Bob', 'Alice', 'Bob', 'Alice', 'Bob'],
    'Product': ['Pen', 'Pen', 'Book', 'Book', 'Pen', 'Book'],
    'Sales': [5, 7, 10, 15, 3, 8]
}

df=pd.DataFrame(data)
# print(df)


gp=df.groupby('Product')['Sales'].sum()
print(gp)
print('-------------------------')


gp=df.groupby(['Person','Product'])['Sales'].sum()
print(gp)
print('-------------------------')


gp=df.groupby('Person')['Product'].count()
print(gp)
print('-------------------------')

gp=df.groupby('Person')['Product'].unique()
print(gp)
print('-------------------------')

gp=df.groupby(['Person','Product']).size()
print(gp)
print('-------------------------')

gp=df.groupby(['Product','Person']).agg({'Sales':'sum'})
print(gp)
print('-------------------------')

gp=df.groupby(['Product','Person']).agg({'Sales':['sum','mean']})
print(gp)

print('-------------------------')

