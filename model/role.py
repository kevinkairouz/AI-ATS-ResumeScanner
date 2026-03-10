import pandas as pd 


df = pd.read_csv("datasets/roles.csv") 

print(df.groupby("Category").count())