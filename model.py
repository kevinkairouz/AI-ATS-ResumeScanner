import pandas as pd 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 

df = pd.read_csv("Heart_disease_statlog.csv")

plt.scatter(df["age"], df["chol"]) 
plt.show()