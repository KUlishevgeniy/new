from bs4 import BeautifulSoup
import requests
import mysql.connector as connection


def getname(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    name = soup.find("h1", class_="ProductHeader__title").text

    return name


def getprice(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="js--ProductHeader__price-default_current-price").text

    return price


def getos(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    os = soup.find(class_="Specifications__column_value").text

    return os


def getrate(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    rate = soup.find(class_="Rating__number").text

    return rate


n = 1  # количество страниц с телефонами

result = []

for i in range(1, n + 1):
    if i == 1:
        url = "https://www.citilink.ru/catalog/smartfony/"
    else:
        url = f"https://www.citilink.ru/catalog/smartfony/?p={i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    allinfo = soup.find_all("a", {"class": "Link js--Link Link_type_default"})

    for j in range(len(allinfo)):
        data = str(allinfo[j])
        if "otzyvy" in data:
            data = data.split("otzyvy")[0].split("href=\"")[1]
            result.append(data)

db = connection.connect(host='127.0.0.1', database='phones', user="root", password="")
cursor = db.cursor()

for i in range(len(result)):
    namex = getname(result[i])
    namey = namex.split()
    namey.pop(0)
    name = ''.join(namey)

    pricex = getprice(result[i])
    pricey = pricex.split()
    price = ''.join(pricey)

    osx = getos(result[i])
    osy = osx.split()
    os = ''.join(osy)

    ratex = getrate(result[i])
    ratey = ratex.split()
    rate = ''.join(ratey)

    data_phones = (i, name, os, rate, price)

    insert_phones = """
    INSERT INTO phones_descriprion(id,name,os,rating,price)
    VALUES ('%s','%s','%s','%s','%s')
    """ % data_phones
    cursor.execute(insert_phones)
    db.commit()
