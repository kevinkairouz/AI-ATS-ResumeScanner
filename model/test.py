import pandas as pd 

#for testing pandas syntax
df = pd.DataFrame({"Name": ["Bart", "Derek"], "Salary": [100,200]}) 
df = df.sort_values(by="Salary", ascending=False)
print(df.iloc[0])