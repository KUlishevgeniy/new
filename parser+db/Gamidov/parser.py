import re
import product
import dataBase
import specification

import requests
from bs4 import BeautifulSoup



def parsSpecific(_href):
    r = requests.get(_href)
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    html_temp = soup.find_all('table', class_='tabs_table')
    if(len(html_temp) == 0):
        return specification.Specification('', '', '', '', '', '')
    html_name = html_temp[0]

    temp1 = re.compile("<td class=" + '"' + "tt_td_title" + '"' + ">[^<]{1,}").findall(str(html_name))
    temp2 = re.compile("<td>[^<]{1,}").findall(str(html_name))

    for i in range(len(temp1)):
        temp1[i] = temp1[i].replace('<td class="tt_td_title">', "")
    for i in range(len(temp2)):
        temp2[i] = temp2[i].replace('<td>', "")

    left = []
    right = []

    for i in temp1:
        left.append(str(i).strip())
    for i in temp2:
        right.append(str(i).strip())

    type = ''
    OC = ''
    typeSim = ''
    countSim = ''
    weight = ''
    proportions = ''

    for i in range(len(left)):
        if(left[i] == 'Тип'): type = right[i]
        elif(left[i] == 'Операционная система'): OC = right[i]
        elif(left[i] == 'Тип SIM-карты'): typeSim = right[i]
        elif(left[i] == 'Количество SIM-карт'): countSim = right[i]
        elif(left[i] == 'Вес'): weight = right[i]
        elif(left[i].find("Размеры") != -1): proportions = right[i]
    return specification.Specification(type, OC, typeSim, countSim, weight, proportions)


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

regex_num = [re.compile("name':\s'[^']{1,}"), re.compile("id':\s'[^']{1,}"), re.compile("price':\s[^,]{1,}"), re.compile("brand':\s'[^']{1,}"), re.compile("<a href=" + '"' +"[^" + '"' + "]{1,}")]
rep = ["name': '", "id': '", "price': ", "brand': '", '<a href="']

phones = []

for i in range(1, page_max + 1):
    r = requests.get(URL_TEMPLATE + "?pagesize=12&PAGEN_1=" + str(i))
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    html_name = soup.find_all('h2', class_='bp_text_info bp_width_fix')
    print(i)

    for a in html_name:
        _name = regex_num[0].findall(str(a))[0]
        _name=_name.replace(rep[0], "")

        _id = regex_num[1].findall(str(a))[0]
        _id = _id.replace(rep[1], "")

        _price = regex_num[2].findall(str(a))[0]
        _price = _price.replace(rep[2], "")

        _brand = regex_num[3].findall(str(a))[0]
        _brand = _brand.replace(rep[3], "")

        _href = regex_num[4].findall(str(a))[0]
        _href = _href.replace(rep[4], "")
        _href = 'https://store77.net' + _href

        phones.append(product.Product(_name, _id, _price, _brand, _href, parsSpecific(_href)))

db = dataBase.DataBase('127.0.0.1', 'new', 'root', '')

db.clear("phone")
db.clear("specification")
db.add_phone(phones)



