import pandas as pd
# import resume 
import numpy as np
from sklearn.ensemble import RandomForestClassifier  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report  
from sklearn.ensemble import GradientBoostingClassifier 

#V2 model will use the following new dataset (dataset.txt) 
#For App.py we may have to change the filepath
df = pd.read_csv("../data/Dataset.txt") 


#Cleaning Data
records_keep = df[(df["Category"] == "Consultant") | (df["Category"] == "Business Analyst") | (df["Category"] == "Digital Media")
                  | (df["Category"] == "Human Resources") | (df["Category"] == "Blockchain") | 
                  (df["Category"] == "Network Security Engineer") | (df["Category"] == "PMO") | (df["Category"] == "Sales") | (df["Category"] == "Web Designing")    
                ].index
df = df.loc[records_keep] 



#Lowering Entropy 
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



model = GradientBoostingClassifier(n_estimators=250, learning_rate=1.0, max_depth=7)  
model.fit(X_train_data, Y_train)
print(model.score(X_test_data, Y_test)) 

#after training will make the selections using the prob inside of the predict function and itr 
#over df and we can make another class that is record 







# model = RandomForestClassifier(n_estimators=400, max_depth=100) 
# model.fit(X_train_data, Y_train)  

#Benchmarked at 91.4% accuracy as of March 28th for Random Forest 
# print(model.score(X_test_data, Y_test)) 
# Y_predicted = model.predict(X_test_data)
# print(classification_report(Y_test, Y_predicted)) 


#Gradient Boosting Benchmarked at 92.5% accuracy as of March 28th

class CategoryManager: 
    def makePrediction(self, text):   
        data = tf.transform([text])  
        y_predict_prba = model.predict_proba(data)  
        

    
    def displaySampleReport(self): 
        res = self.makePrediction(Y_test)
        print(classification_report(Y_test,res))
        return None
     










