import pandas as pd   

#Helper Functions     
def isAnalyst(resume):  
    resume = str(resume) 
    resume = resume.lower()  
    if "python" in resume or "sql" in resume or "excel" in resume:
        return True 
    else: 
        return False 
    
def hasFrontend(resume): 
    resume = str(resume) 
    if "react" in resume: 
        return True 
    else: 
        return False

def hasBackend(resume): 
    resume = str(resume) 
    if "node" in resume or "next" in resume:
        return True 
    else: 
        return False 
    

def isWebDev(resume):  
    resume = str(resume) 
    if "javascript" in resume and "html" in resume and "css" in resume: 
        if hasFrontend(resume) and hasFrontend(resume): 
            return True
        else: 
            return False
        
