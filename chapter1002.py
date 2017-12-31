from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://www.google.co.kr')

# assert 'Yahoo' in browser.title

elem = browser.find_element_by_id('lst-ib')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
time.sleep(5)
browser.quit()
