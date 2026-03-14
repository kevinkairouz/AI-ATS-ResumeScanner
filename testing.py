from model.resume import ResumeManager
from model.category import CategoryManager  
from model.role import TechRoleManager
from model.score import ScoreManager


resumeManager = ResumeManager()  
cManager = CategoryManager() 
tf = TechRoleManager()

""" 
if engineering or info tech we put it through the layered role of 
"""
text = resumeManager.getText("sample.pdf")  


classification = cManager.makePrediction(text) 

print(classification[0])






