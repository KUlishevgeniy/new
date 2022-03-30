import requests
from bs4 import BeautifulSoup
import re
name=[]

URL_TEMPLATE = "https://store77.net/telefony/"

r = requests.get(URL_TEMPLATE)
print(r.status_code)
contet = r.text
#print(contet)
soup = BeautifulSoup(contet, 'lxml')

html_name = soup.find_all('h2', class_='bp_text_info bp_width_fix')
print(html_name)
regex_num =re.compile("name':\s'[^']{0,}")

url = r'http://'+r'store77.net/telefony/telefon_samsung_galaxy_a03_core_2_32gb_chernyy/'

i = 0
for a in html_name:
    c=''
    c=regex_num.findall(str(html_name[i]))
    print(c)
    c=str(c)
    c=c.replace("name': '", "")
    i=i+1
    mass=[c, 'id', url]
    name.append(mass)

print(name)


p = requests.get(url)
print(p.status_code)