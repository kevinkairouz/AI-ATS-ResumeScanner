import pandas as pd 
import resume 
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import recall_score 
from sklearn.metrics import recall_score
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv("datasets/UpdatedResume.csv")
rows_to_delete = df[(df["Category"] == "Advocate") | (df["Category"] == "BlockChain") | (df["Category"] == "Hadoop") | (df["Category"] == "PMO") | (df["Category"] == "Testing")] 
df = df.drop(rows_to_delete.index, axis=0)  

location1 = df[df["Category"] == "DotNet Developer"].index  
location2 = df[df["Category"] == "ETL Developer"].index
location3 = df[df["Category"] == "Network Security Engineer"].index
df.loc[location1, "Category"] = "C# Developer" 
df.loc[location2, "Category"] = "Data Engineer" 
df.loc[location3, "Category"] = "Cybersecurity"
print(df.groupby("Category").count())



