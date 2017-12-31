from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("span", {"class":"green"})
    except AttributeError as e:
        return None
    return nameList

list = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")

for name in list:
    print(name.get_text())
