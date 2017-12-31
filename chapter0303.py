from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.kormedi.com/news/article/newsTemplete.aspx")

print(html.read())
bsObj = BeautifulSoup(html, "html.parser")

print(len(bsObj.findAll("a", href=re.compile("^(/news/)*$"))))

for text in bsObj.findAll("a", href=re.compile("^(/news/)*$")):
    print(text)
