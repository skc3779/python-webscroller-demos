from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pthonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)
    print("error-------------------------------")
    # null을 반환하거나  break 문을 실행하거나 기타 다른 방법을 사용
else:
    # 프로그램을 계속 실행
    print("정상처리에만 실행")
    bsObj = BeautifulSoup(html.read(), "html.parser")