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
print(df.groupby("Category").count())



