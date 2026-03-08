import pandas as pd 
import pdfplumber as plu
import numpy as np

class ResumeManager:

    def __init__(self, resume_file):
        self.resume_file = resume_file

    def getText(self, pdf): 
        with plu.open(pdf) as resume: 
            file_info = ""
            for page in resume.pages:  
                file_info += page.extract_text_simple() 
            return file_info 








    






