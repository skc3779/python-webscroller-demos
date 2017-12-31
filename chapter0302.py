from lxml import html
import requests

page = requests.get('http://www.kormedi.com/news/article/newsTemplete.aspx')
print(page.content)
tree = html.fromstring(page.content)

#article list
list = tree.xpath('//*[@id="wrap"]/div[2]/table/tbody/tr[2]/td[3]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr')

for item in list:
    print(item)