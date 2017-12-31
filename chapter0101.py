from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.html.body.h1)

print(bsObj.body.h1)

print(bsObj.h1)

# div print
print(bsObj.div)
