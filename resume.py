import pandas as pd 
import pdfplumber as plu


class ResumeManager:

    def __init__(self):
        pass
    def getText(self, pdf): 
        with plu.open(f"resumes/{pdf}") as resume:  
            file_info = ""
            for page in resume.pages:  
                file_info += page.extract_text_simple() 

    def prepareDF(self): 
        """
        This will do loop for all of the sample resumes and get all of the text 
        run the getText function 28 times
        """
        return None 

             
    
    def convertToDF(self, pdf_string): 
        df = pd.DataFrame({"Resume": [pdf_string], "class": []}) 
        return df 

    def concatDF(self, df1, df2): 
        df_concat = pd.concat([df1,df2]) 
        return df_concat

r = ResumeManager() 




