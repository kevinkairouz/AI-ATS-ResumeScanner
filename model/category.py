import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier  
from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.model_selection import train_test_split  

df = pd.read_csv("data/Dataset.txt") 
#Cleaning Data
records_keep = df[(df["Category"] == "Consultant") | (df["Category"] == "Business Analyst") | (df["Category"] == "Digital Media")
                  | (df["Category"] == "Human Resources") | (df["Category"] == "Blockchain") | 
                  (df["Category"] == "Network Security Engineer") | (df["Category"] == "PMO") | (df["Category"] == "Sales") | (df["Category"] == "Web Designing")    
                ].index
df = df.loc[records_keep] 



#Lowering Entropy uncertainity in the data 
is_Cyber = df[(df["Category"] == "Network Security Engineer") | (df["Category"] == "Blockchain")].index  
is_TL = df[df["Category"] == "Management"].index 

df.loc[is_TL, "Category"] = "Team Lead"
df.loc[is_Cyber, "Category"] = "Cybersecurity" 

X = df["Text"] 
Y = df["Category"]


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,stratify=Y, random_state=42) 
tf = TfidfVectorizer(stop_words="english",max_features=3000,ngram_range=(1,2)) 
X_train_data = tf.fit_transform(X_train) 
X_test_data = tf.transform(X_test)  
model = RandomForestClassifier(n_estimators=400, max_depth=100)
model.fit(X_train_data, Y_train)
 
class CategoryManager: 
    def makePrediction(self, text):   
        data = tf.transform([text])  
        y_predict_prba = model.predict_proba(data)
        df = pd.DataFrame({"Classes": model.classes_, "Match": y_predict_prba[0].round(3) * 100}) 
        df = df.sort_values(by="Match", ascending=False)  
        return (df.iloc[0]["Classes"], df.iloc[1]["Classes"]) 

        

    
     










