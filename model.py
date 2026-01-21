import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv("Heart_disease_statlog.csv") 
df = df.rename(columns={"target": "class"}) 

