from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
s = requests.get('https://www.naver.com', headers=headers)

print(s.content)
print("--------------------------------\n\n\n\n")

soup = BeautifulSoup(s.content,'html.parser')

for item in soup.find("ul", {"class":"aplc_list"}).findAll("li"):
    print(item)

