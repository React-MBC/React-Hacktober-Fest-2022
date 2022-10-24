import pyttsx3
import PyPDF2
book=open("ml.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(book)
#pages=pdfReader.numPages()
#print(pages)
page=pdfReader.getPage(1)
assistant=pyttsx3.init()
text=page.extractText()
assistant.say(text)
assistant.runAndWait()
