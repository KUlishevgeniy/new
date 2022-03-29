import requests
from bs4 import BeautifulSoup
import re
import httplib2
import mysql.connector


def parser(i):
    regex_name = re.compile("name':\s'[^']{0,}")
    regex_id = re.compile("id':\s'[^']{0,}")
    regex_price = re.compile("price':\s[^,]{0,}")
    regex_brand = re.compile("brand':\s'[^']{0,}")
    regex_href = re.compile("href=\"[^\"]{0,}")
    p = []
    c = regex_name.findall(str(i))
    c = c[0]
    c = c.replace("name': '", "")
    name = c
    p.append(c)

    c = regex_id.findall(str(i))
    c = c[0]
    c = c.replace("id': '", "")
    p.append(c)

    c = regex_price.findall(str(i))
    c = c[0]
    c = c.replace("price': ", "")
    p.append(c)

    c = regex_brand.findall(str(i))
    c = c[0]
    c = c.replace("brand': '", "")
    p.append(c)

    c = regex_href.findall(str(i))
    c = c[0]
    c = c.replace('href="', "")
    href = "https://store77.net" + c
    r_tel = requests.get(href)
    soup_tel = BeautifulSoup(r_tel.text, 'lxml')
    descr_html = soup_tel.find_all('div', class_='col-sm-6 wrap_descr_b')
    #print(descr_html)
    descr = str(descr_html[0])[36:-7]
    print(name)

    img_html = soup_tel.find_all('img', alt=name)
    regex_img = re.compile('src=\"[^\"]{0,}')
    img_href = regex_img.search(str(img_html)).group()
    img_href = img_href.replace("src=\"", "")
    if img_href[:5] != "https":
        img_href = "https://store77.net"+img_href
    print(img_href)
    h = httplib2.Http('.cache')
    response_img, content_img = h.request(img_href)
    src = "images\img"+str(page)+"_"+str(k)+"("+str(num)+").jpg"
    out = open(src,'wb')
    out.write(content_img)
    out.close()

    h_html = soup_tel.find_all('table', class_='tabs_table')
    h_html = str(h_html).replace("</td>", "")
    h_html = h_html.replace("<td>", "").replace("<br/>","").replace("<br>","")
    if len(h_html) == 2:
        if len(descr) == 2:
            return p + ["-", "-", "-", "-", "-", "-", "-"]
        else:
            return p + [descr, "-", "-", "-", "-", "-", "-"]

    regex_type = re.compile("Тип\r[^<]{0,}")
    type = regex_type.search(str(h_html))
    #type = regex_type.findall(str(h_html))
    #print(type)
    type = type.group().replace("Тип","")
    type = type.replace("\r", "").replace("\t", "").replace("\n","").replace("\xa0", "")
    #type = str(type)[20:-10]

    regex_os = re.compile("Операционная система\r[^<]{0,}")
    os = regex_os.search(str(h_html))
    os = os.group().replace("Операционная система", "")
    os = os.replace("\r", "").replace("\t", "").replace("\n","").replace("\xa0", "")
    #os = str(os)[20:-10]

    regex_sim = re.compile("Тип SIM-карты\r[^<]{0,}")
    sim = regex_sim.search(str(h_html))
    sim = sim.group().replace("Тип SIM-карты", "")
    sim = sim.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0", "")
    #sim = str(sim)[20:-10]

    regex_sim_amount = re.compile("Количество SIM-карт\r[^<]{0,}")
    sim_amount = regex_sim_amount.search(str(h_html))
    sim_amount = sim_amount.group().replace("Количество SIM-карт", "")
    sim_amount = sim_amount.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0", "")
    #sim_amount = str(sim_amount)[20:-10]

    regex_weight = re.compile("Вес\r[^<]{0,}")
    weight = regex_weight.search(str(h_html))
    weight = weight.group().replace("Вес", "")
    weight = weight.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0", "")
    #weight = str(weight)[20:-10]

    regex_dimensions = re.compile("Размеры[^<]{0,}")
    dimensions = regex_dimensions.search(str(h_html))
    dimensions = dimensions.group().replace("Размеры ", "").replace("(ШxВxТ)","").replace("(ВxШxТ)","")
    #dimensions = dimensions[:-7]
    #dimensions = re.sub(r'\(\w\)',"",dimensions)
    #print(dimensions)
    dimensions = dimensions.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0", "")

    p += [descr, type, os, sim, sim_amount, weight, dimensions]
    return p

def page():
    URL_TEMPLATE = "https://store77.net/telefony/"
    r = requests.get(URL_TEMPLATE)
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    regex_page = re.compile(">[0-9]+<")
    html_page_amounts = soup.find_all('ul', class_='pagination')
    page_amounts = regex_page.findall(str(html_page_amounts))
    page_amounts = [int(i[1:-1]) for i in page_amounts]
    page_amount = max(page_amounts)
    return page_amount

mas = []

page_amount = page()
mydb = mysql.connector.connect(host='127.0.0.1', database='new2', user='root', password='')
cursor = mydb.cursor()
k = 0
num_page = 0
num = 0
for page in range(1, page_amount+1):
    num_page = page
    print(page)
    URL_TEMPLATE = "https://store77.net/telefony/" + "?PAGEN_1="+str(page)
    r = requests.get(URL_TEMPLATE)
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    html_phones = soup.find_all('h2', class_='bp_text_info bp_width_fix')
    k = 0
    for phone in html_phones:
        k+=1
        num+=1
        parser_phone = parser(phone)
        mas.append(parser_phone)
        print(parser_phone)
        print(num)
        query = "INSERT INTO phones(name, id, price, brand, description, type, os, sim, sim_amount, weight, dimensions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, parser_phone)
mydb.commit()
cursor.close()
mydb.close()
