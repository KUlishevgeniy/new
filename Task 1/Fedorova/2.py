###Написать функцию подключения к базе данных
#######
import mysql.connector

datebase = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
curs = datebase.cursor()
curs.execute("SELECT * FROM login");
users = curs.fetchall()
print(users)