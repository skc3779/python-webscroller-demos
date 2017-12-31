from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter #process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    sio = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfFile, 'rb')

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    content = sio.getvalue()
    device.close()
    sio.close()
    return content

# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF("chapter5.pdf")
print(outputString)
# pdfFile.close()
