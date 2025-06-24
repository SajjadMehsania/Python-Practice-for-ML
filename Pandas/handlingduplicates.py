import pandas as pd
# df=pd.read_excel("customers.xlsx")
# print(df.head(5))
data={
    "id":[1,2,1,1,5,6,7,8,9,7,7,8],
    "name":["John","Jane","Doe","John","Alice","Bob","Charlie","John","Eve","Bob","Charlie","Jane"],
    "age":[28,34,29,28,22,30,25,40,35,45,25,40]
}
df=pd.DataFrame(data)
print(df['id'].duplicated().sum())
print(df.drop_duplicates("id"))#delete duplicates based on id
