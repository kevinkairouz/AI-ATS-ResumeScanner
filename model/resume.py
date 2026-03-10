import pandas as pd 
import pdfplumber as plu 
from pypdf import PdfReader 
import pypdf as py 


class ResumeManager: 

    def getText(pdf):   
        reader = PdfReader(pdf) 
        file_info = ""
        for page in reader.pages: 
            file_info += page.extract_text() 
        return file_info 

     

#for testing purpose
# print(getText("sample.pdf"))






