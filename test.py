from model.category import CategoryManager 
from model.resume import ResumeManager


r = ResumeManager() 
c = CategoryManager() 


def testFunc(resume):  
    text = r.getText(resume) 
    return c.makePrediction(resume)

print(testFunc("resumesample1.pdf"))



