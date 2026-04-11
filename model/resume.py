import pandas as pd 
import pdfplumber as plu 
from pypdf import PdfReader 

class ResumeManager: 
    def getText(self, pdf):   
        reader = PdfReader(pdf) 
        file_info = ""
        for page in reader.pages: 
            file_info += page.extract_text() 
        return file_info 



