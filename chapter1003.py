from selenium import webdriver
import time

# 팬텀 JS는 완전한 브라우저이고 파이썬 라이브러리가 아니므로  pip같은
# 패키지 관리자로는 설치할 수 없고 직접 내려바당서 설치해야 한다.
# http://phantomjs.org/download.html


# REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
driver = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-windows/bin/phantomjs.exe')
# driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
print(driver.find_element_by_id("content").text)
driver.close()