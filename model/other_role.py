#targeted for non-tech roles such as HR, Operations, etc 


class NonTechRoleManager: 
    def is_Fit(self, resume, role): 
        resume = str(resume) 
        resume = resume.upper()
        if "MASTERS" in resume or "EXCEL" in resume or "MASTER": 
            return True 
        else: 
            return False