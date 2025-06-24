import pandas as pd
df=pd.read_csv("customers.csv")
print(df)
print(df.head())
print(df.info()) # Display basic information about the DataFrame
print(df.describe()) # Display statistical summary of the DataFrame
print(df.isnull().sum())