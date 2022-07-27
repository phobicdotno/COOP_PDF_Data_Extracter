
# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('/Users/phobic/Library/Mobile Documents/com~apple~CloudDocs/Python/PDF/coop-2241821-4-106480.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print('Number of pages: ', pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.getPage(0)
fields = pdfReader.metadata()
    
# extracting text from page 
#print(pageObj.extractText()) 
print(fields) 


# closing the pdf file object 
pdfFileObj.close() 