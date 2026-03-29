from model.category import CategoryManager 
from model.resume import ResumeManager 

c = CategoryManager() 
r = ResumeManager() 

txt = r.getText("sample2.pdf") 
a = c.makePrediction(txt) 
print(a)