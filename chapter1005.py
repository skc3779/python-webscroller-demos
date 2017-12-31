from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 페이지를 완전히 불러왔을 때만 존재하는 id가 loadedButton인 버튼을 검사합니다.

#REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS

driver = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-windows/bin/phantomjs.exe')
#driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')

driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

# 셀레니움dptjsms 묵시적 대기 (implicit wait)라는 기능을 제공
# WebDriverWait, expected_condition
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
