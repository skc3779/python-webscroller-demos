from io import open
from bs4 import BeautifulSoup
import re

# Extract text
fp = open("chapter3.html", 'rb')

# print(fp.read())
bsObj = BeautifulSoup(fp.read(), "html.parser")

bmi_arr = bsObj.find_all("div", style=re.compile("1075|1076|1077|1078|1079"))

for item in bmi_arr:
    i = item.find("span")
    if i:
        print("bmi:"+i.get_text())

fp.close()
