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
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv("datasets/resumes.csv") 

X = df["Resume"] 
Y = df["Category"] 
cv = CountVectorizer(stop_words="english") 
tf = TfidfVectorizer(stop_words="english") 
X = cv.fit_transform(X) 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, random_state=42, test_size=0.3)

rf = RandomForestClassifier() 
lr = LogisticRegression() 
dt = DecisionTreeClassifier() 
kn = KNeighborsClassifier() 

