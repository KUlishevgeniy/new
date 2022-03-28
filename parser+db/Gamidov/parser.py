import re
import product
import dataBase

import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = "https://store77.net/telefony/"
r = requests.get(URL_TEMPLATE)
content = r.text

soup = BeautifulSoup(content, 'lxml')

html_name = soup.find_all('ul', class_ = 'pagination')
temp = re.compile("href=" + '"' + "/telefony/\?PAGEN_1=[^" + '"' + "]{0,}").findall(str(html_name[0]))
page_max = 0

for page in temp:
    page = page.replace("href=" + '"' + "/telefony/?PAGEN_1=", "")
    if(page_max < int(page)): page_max = int(page)

html_name = soup.find_all('h2', class_ = 'bp_text_info bp_width_fix')

regex_num = [re.compile("name':\s'[^']{1,}"), re.compile("id':\s'[^']{1,}"), re.compile("price':\s[^,]{1,}"), re.compile("brand':\s'[^']{1,}")]
rep = ["name': '", "id': '", "price': ", "brand': '"]

phones = []

for i in range(1, page_max + 1):
    r = requests.get(URL_TEMPLATE + "?pagesize=12&PAGEN_1=" + str(i))
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    html_name = soup.find_all('h2', class_='bp_text_info bp_width_fix')

    for a in html_name:
        _name = regex_num[0].findall(str(a))[0]
        _name=_name.replace(rep[0], "")

        _id = regex_num[1].findall(str(a))[0]
        _id = _id.replace(rep[1], "")

        _price = regex_num[2].findall(str(a))[0]
        _price = _price.replace(rep[2], "")

        _brand = regex_num[3].findall(str(a))[0]
        _brand = _brand.replace(rep[3], "")
        phones.append(product.Product(_name, _id, _price, _brand))

db = dataBase.DataBase('127.0.0.1', 'new', 'root', '')

db.clear("phone")

db.add(phones)



