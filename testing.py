from model.resume import ResumeManager
from model.category import CategoryManager 


resumeManager = ResumeManager()  
cManager = CategoryManager() 


text = resumeManager.getText("sample.pdf")  

classification = cManager.makePrediction(text)

print(classification)

