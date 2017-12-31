from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    except AttributeError as e:
        return None
    return nameList

list = getTitle("http://www.pythonscraping.com/pages/page3.html")

for image in list:
    print(image, image["src"])
