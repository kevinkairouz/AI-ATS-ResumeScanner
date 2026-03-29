import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier  
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import GradientBoostingClassifier  
from dataclasses import dataclass 


#V2 model will use the following new dataset (dataset.txt) 
#For App.py we may have to change the filepath
df = pd.read_csv("../data/Dataset.txt") 


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
# model2 = GradientBoostingClassifier(n_estimators=250, learning_rate=1.0, max_depth=7) 
model = RandomForestClassifier(n_estimators=400, max_depth=100)
model.fit(X_train_data, Y_train)
# print(model.score(X_test_data, Y_test))  
#print(model2.score(X_test_data, Y_test))

#after training will make the selections using the prob inside of the predict function and itr 
#over df and we can make another class that is record 

# model = RandomForestClassifier(n_estimators=400, max_depth=100) 
# model.fit(X_train_data, Y_train)  

#Benchmarked at 91.4% accuracy as of March 28th for Random Forest 
# print(model.score(X_test_data, Y_test)) 
# Y_predicted = model.predict(X_test_data)
# print(classification_report(Y_test, Y_predicted)) 


#Gradient Boosting Benchmarked at 92.5% accuracy as of March 28th 

@dataclass
class Applicant:  
    Resume: str  
    PrimaryFit: str 
    Secondary1: str 
    Secondary2: str 
    score1: float 
    score2: float 
    score3: float



class CategoryManager: 
    def makePrediction(self, text):   
        data = tf.transform([text])  
        y_predict_prba = model.predict_proba(data)
        df = pd.DataFrame({"Classes": model.classes_, "Match": y_predict_prba[0].round(3) * 100}) 
        df = df.sort_values(by="Match", ascending=False)  
        # print(df)
        return Applicant(text, df["Classes"].iloc[0], df["Classes"].iloc[1], df["Classes"].iloc[2], df["Match"].iloc[0], df["Match"].iloc[1], df["Match"].iloc[2])

# for testing purpose
# c = CategoryManager() 
# c.makePrediction(X_test.iloc[4])
        

    
     










