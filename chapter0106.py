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
        nameList = bsObj.find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as e:
        return None
    return nameList

list = getTitle("http://www.pythonscraping.com/pages/page3.html")

for sibling in list:
    print(sibling)
