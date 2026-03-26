from model.category import CategoryManager 
from model.other_role import NonTechRoleManager 
from model.resume import ResumeManager 
from model.role import TechRoleManager 
from model.score import ScoreManager 


r = ResumeManager() 
c = CategoryManager() 
t = TechRoleManager()
s = ScoreManager() 
o = NonTechRoleManager()

tech_roles = ["BUSINESS","ENGINEERING","FINANCE","INFORMATION-TECHNOLOGY"]
def testFunc():
    txt = r.getText("resumesample1.pdf") 
    role = c.makePrediction(txt) 
    if role in tech_roles: 
        projxon_role = t.predictRole(txt) 
        return s.isFit(txt,projxon_role)
    else:  
        return o.is_Fit(txt, role)


