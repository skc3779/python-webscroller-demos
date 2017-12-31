import os
from urllib.request import urlretrieve
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

downloadDirectory = "imhealth"

def getRelativeURL(source):
    url = urlparse(source)
    return url.path

def getDownloadPath(absoluteUrl, downloadDirectory):
    path = downloadDirectory+absoluteUrl
    list = path.split("?")
    directory = os.path.dirname(list[0])

    if not os.path.exists(directory):
        os.makedirs(directory)

    return list[0]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
html = requests.get('https://api.imhealth.co.kr/Test/Patient/1488778872933/DiagnosticReport/r29/mediage', headers=headers)

bsObj = BeautifulSoup(html.content, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fullUrl = download["src"]
    relativeUrl = getRelativeURL(fullUrl)
    if relativeUrl is not None:
        print(fullUrl + " | " + getDownloadPath(relativeUrl, downloadDirectory))
        urlretrieve(fullUrl, getDownloadPath(relativeUrl, downloadDirectory))