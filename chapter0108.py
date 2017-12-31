from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime


def getLinks(url):
    try:
        html = urlopen("http://en.wikipedia.org"+url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        return None
    return nameList

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
