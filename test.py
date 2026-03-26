from model.category import CategoryManager 
from model.other_role import NonTechRoleManager 
from model.resume import ResumeManager 
from model.role import TechRoleManager 
from model.score import ScoreManager 


r = ResumeManager() 
c = CategoryManager() 
t = TechRoleManager()
s = ScoreManager()

txt = r.getText("sample.pdf") 
role = c.makePrediction(txt)
projxon_role = t.predictRole(txt) 
print(projxon_role) 
print(s.isFit(txt, projxon_role)) 


