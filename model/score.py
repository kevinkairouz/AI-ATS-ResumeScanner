import pandas as pd  
#excess file not needed 

class ScoreManager: 

    def isFit(self, resume, role): 
        match role: 
            case "Business Analyst": 
                return self.isAnalyst(resume) 
            case "Web Designing": 
                return self.isWebDev(resume) 
            case "Cybersecurity": 
                return self.isCyber(resume) 
            case _: 
                return False
        

    def isAnalyst(self, resume):  
        resume = str(resume) 
        resume = resume.lower()  
        if "python" in resume or "sql" in resume or "excel" in resume:
            return True 
        else: 
            return False 
        
    def hasFrontend(self, resume): 
        resume = str(resume) 
        if "react" in resume: 
            return True 
        else: 
            return False

    def hasBackend(self, resume): 
        resume = str(resume) 
        if "node" in resume or "next" in resume:
            return True 
        else: 
            return False 
        
    def isCyber(self, resume): 
        resume = str(resume) 
        resume = resume.lower() 
        if "python" in resume or "sql" in resume or "linux" in resume: 
            return True
        else: 
            return False
        

    def isWebDev(self, resume):  
        resume = str(resume) 
        if "javascript" in resume and "html" in resume and "css" in resume: 
            if self.hasFrontend(resume) and self.hasBackend(resume): 
                return True
            else: 
                return False
        
