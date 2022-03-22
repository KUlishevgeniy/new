import requests
from bs4 import BeautifulSoup
import re
import Search
name=[]
URL="https://store77.net/telefony"
r=requests.get(URL)
content=r.text
# print(content)
soup=BeautifulSoup(content,'lxml')
html_name=soup.find_all('h2',class_='bp_text_info bp_width_fix')
# html_id=soup.find_all('h2',class_='bp_text_info bp_width_fix')
# html_price=soup.find_all('h2',class_='bp_text_info bp_width_fix')
# html_brand=soup.find_all('h2',class_='bp_text_info bp_width_fix')
# html_category=soup.find_all('h2',class_='bp_text_info bp_width_fix')
regex_name=re.compile("name':\s'[^']*")
regex_id=re.compile("id':\s'[^']*")
regex_price=re.compile("price':\s[^,]*")
regex_brand=re.compile("brand':\s'[^']*")
regex_category=re.compile("category':\s'[^']*")
regex_list=re.compile("list':\s'[^']*")
i=0
# Search.insert_parse("1","3","3",4,"e")
for a in html_name:
    # c1=regex_category.findall(str(html_name[i]))[1]
    id=str(regex_id.findall(str(html_name[i]))).replace("id': '","")[2:-2]
    brand=str(regex_brand.findall(str(html_name[i]))).replace("brand': '","")[2:-2]
    name=str(regex_name.findall(str(html_name[i]))).replace("name': '","")[2:-2]
    price=str(regex_price.findall(str(html_name[i]))).replace("price': ","")[2:-2]
    category=str(regex_category.findall(str(html_name[i]))[1]).replace("category': '","")
    print(id)
    # c=regex_name.findall(str(html_name[i]))+regex_id.findall(str(html_name[i]))+regex_price.findall(str(html_name[i]))\
    #   +regex_brand.findall(str(html_name[i]))+[c1]

    # print(c)
    i+=1
    Search.insert_parse(id,brand,name,price,category)