import pandas as pd 
from pypdf import PdfReader  
import numpy as np


reader = PdfReader("sample.pdf", strict=True)

pages = reader.pages

for i in range(len(pages)): 
    if 

