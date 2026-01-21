import pandas as pd 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 

df = pd.read_csv("Heart_disease_statlog.csv") 
df = df.rename(columns={"target": "class"}) 
print(df.info())