#Написать функцию подключения к базе данных

import mysql.connector

mydb = mysql.connector.connect(host = '127.0.0.1', database = 'new1', user = 'root', password='')
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM user')
user = mycursor.fetchall()
print(user)