import pandas as pd 
import pdfplumber as plu


def getText(self, pdf): 
    with plu.open(f"resumes/{pdf}") as resume:  
        file_info = ""
        for page in resume.pages:  
            file_info += page.extract_text_simple() 

    






