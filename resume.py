import pandas as pd 
import pdfplumber as plu

class ResumeManager:
    def __init__(self, resume_file):
        self.resume_file = resume_file

    def getText(self, pdf): 
        with plu.open(pdf) as resume: 
            file_info = ""
            for page in resume.pages:  
                file_info += page.extract_text_simple() 
            return file_info 
    
    def convertToDF(self, pdf_string): 
        df = pd.DataFrame({"Resume": [pdf_string]}) 
        return df 

    def concatDF(self, df1, df2): 
        df_concat = pd.concat([df1,df2]) 
        return df_concat





    






