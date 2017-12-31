from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

# parser 종류에 대해서 나와 있는 문서 Installing a parser
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# lxml’s XML parser	BeautifulSoup(markup, "lxml-xml") BeautifulSoup(markup, "xml")

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "lxml-xml")

textStrings = wordObj.findAll("w:t")

for textElem in textStrings:
    print(textElem.text)