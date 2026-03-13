import pandas as pd 
from model.resume import ResumeManager
import numpy as np
from sklearn.ensemble import RandomForestClassifier  
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV  
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report

df = pd.read_csv("datasets/Resume.csv")
df = df.drop(["ID","Resume_html"], axis=1) 

rows_to_drop = df[(df["Category"] == "ADVOCATE") | (df["Category"] == "AGRICULTURE") | (df["Category"] == "APPAREL") | (df["Category"] == "AUTOMOBILE") | 
                  (df["Category"] == "AVIATION") | (df["Category"] == "BPO") | (df["Category"] == "CHEF") |
                  (df["Category"] == "CONSTRUCTION") | (df["Category"] == "DESIGNER") | (df["Category"] == "FITNESS") |
                  (df["Category"] == "HEALTHCARE") | (df["Category"] == "TEACHER") | (df["Category"] == "CONSULTANT") 
                  | (df["Category"] == "BANKING") | (df["Category"] == "ACCOUNTANT") | (df["Category"] == "ARTS") 
                  
                  ] 
merge_marketing_categories = df[(df["Category"] == "DIGITAL-MEDIA") | (df["Category"] == "PUBLIC-RELATIONS")]
merge_into_business = df[(df["Category"] == "SALES") | (df["Category"] == "BUSINESS-DEVELOPMENT")]
df = df.drop(rows_to_drop.index, axis=0) 

df.loc[merge_marketing_categories.index, "Category"] = "MARKETING" 
df.loc[merge_into_business.index, "Category"] = "BUSINESS"
X = df["Resume_str"] 
Y = df["Category"] 

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,stratify=Y, random_state=42) 
tf = TfidfVectorizer(stop_words="english",max_features=3000,ngram_range=(1,2)) 
cv = CountVectorizer(stop_words="english", max_features=2600)
X_train_data = tf.fit_transform(X_train) 
X_test_data = tf.transform(X_test)  



model = RandomForestClassifier(n_estimators=400, max_depth=100) 
model.fit(X_train_data, Y_train) 
# print(model.score(X_test_data,Y_test))

class CategoryManager: 
    def makePrediction(self, file):  
        r = ResumeManager()
        resume_data = r.getText(file)  
        data = tf.transform(resume_data) 
        classification = model.predict(data) 
        return classification 
    
    def displaySampleReport(self): 
        res = self.makePrediction(Y_test)
        print(classification_report(Y_test,res))
        return None
     







