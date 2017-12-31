from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
html = requests.get('http://www.bloter.net/archives/294839', headers=headers)
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")

bsObj = BeautifulSoup(html.content, "html.parser")
content = bsObj.find("div", {"class":"article--content"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)