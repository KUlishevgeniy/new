import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(host = '127.0.0.1', database = 'ksrwq', user = 'root', password='')
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM user')
user = mycursor.fetchall()
print(user)

