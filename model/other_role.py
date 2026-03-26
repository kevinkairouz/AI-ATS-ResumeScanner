#targeted for non-tech roles such as HR, Operations, etc 

def good_fit(resume): 
    resume = str(resume) 
    resume = resume.upper()
    if "MASTERS" in resume or "EXCEL" in resume: 
        return True 
    else: 
        return False