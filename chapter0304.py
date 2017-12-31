from robobrowser import RoboBrowser

browser = RoboBrowser()
browser.open("https://www.naver.com/")

for item in browser.select('ul.aplc_list li'):
    print(item)