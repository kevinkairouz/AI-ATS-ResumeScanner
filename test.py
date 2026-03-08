import pdfplumber as pdp 


with pdp.open("sample.pdf") as pdf: 
    firstPage = pdf.pages[0]
    text = firstPage.extract_text() 
    print(text)