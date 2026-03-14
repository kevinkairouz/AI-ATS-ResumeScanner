import pandas as pd  
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("data/roles.csv")  

# print(df.groupby("Category").count())
cleaned_df = df[(df["Category"] == "Web Designing")|(df["Category"] == "Network Security Engineer") |
                (df["Category"] == "Business Analyst") | (df["Category"] == "Database") | (df["Category"] == "Data Science") |
                (df["Category"] == "Python Developer")].copy()

rows_make_analyst = cleaned_df[(cleaned_df["Category"] == "Python Developer") | (cleaned_df["Category"] == "Database") |
                               (cleaned_df["Category"] == "Data Science")]
rows_make_cyber = cleaned_df[cleaned_df["Category"] == "Network Security Engineer"]

cleaned_df.loc[rows_make_analyst.index, "Category"] = "Business Analyst"  
cleaned_df.loc[rows_make_cyber.index, "Category"] = "Cybersecurity" 





# print(cleaned_df.groupby("Category").count())
X = cleaned_df["Resume"] 
Y = cleaned_df["Category"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y, test_size=0.3, random_state=42) 

model = LogisticRegression()  
tf = TfidfVectorizer(stop_words="english", max_features=3000,ngram_range=(1,2)) 
cv = CountVectorizer(stop_words="english", max_features=3000)
X_train_data = tf.fit_transform(X_train) 
X_test_data = tf.transform(X_test) 
model.fit(X_train_data, Y_train)  

# print(model.score(X_test_data,Y_test))  

class TechRoleManager: 

    def predictRole(self, resume): 
        resume_data = tf.transform([resume]) 
        role = model.predict(resume_data) 
        return role



