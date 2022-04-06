###Написать функцию подключения к базе данных
#######

import mysql.connector as mysql

db = mysql.connect(host='127.0.0.1', user='root', passwd='', db='new')
cur = db.cursor()
cur.execute('SELECT * FROM user_id')
user = cur.fetchall()
print(user)
