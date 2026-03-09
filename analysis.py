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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv("datasets/UpdatedResume.csv")
rows_to_delete = df[(df["Category"] == "Advocate") | (df["Category"] == "BlockChain") | (df["Category"] == "Hadoop") | (df["Category"] == "PMO") | (df["Category"] == "Testing")] 
df = df.drop(rows_to_delete.index, axis=0)  

key_info = {"Data Science": "", "Cybersecurity": ""}

location1 = df[df["Category"] == "DotNet Developer"].index  
location2 = df[df["Category"] == "ETL Developer"].index
location3 = df[df["Category"] == "Network Security Engineer"].index
df.loc[location1, "Category"] = "C# Developer" 
df.loc[location2, "Category"] = "Data Engineer" 
df.loc[location3, "Category"] = "Cybersecurity"
# print(df.groupby("Category").count()) 
X = df["Resume"] 
Y = df["Category"]

cv = TfidfVectorizer(stop_words="english", max_features=3000)  

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.25) 


X_train_data = cv.fit_transform(X_train) 
X_test_data = cv.transform(X_test) 

X_train_data = X_train_data.toarray() 
X_test_data = X_test_data.toarray() 


model = RandomForestClassifier(n_estimators=50, max_depth=10, min_samples_leaf=3) 

model.fit(X_train_data, Y_train) 

print(model.score(X_test_data, Y_test))



