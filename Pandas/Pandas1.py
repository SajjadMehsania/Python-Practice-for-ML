import pandas as pd
data={
    "name":["john","peter","elijah"],
    "age":[25,56,78],
    "salary":[3000,5000,10000]
}
# pd.read_excel() for reading excel files
# pd.read_csv() for reading csv files
df=pd.DataFrame(data)
print(df)
print(data)

df=pd.read_csv("customers.csv")
print(df)
