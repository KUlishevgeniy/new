#Написать функцию подключения к базе данных
import mysql.connector as conn

mydb = conn.connect(host = '127.0.0.1', database='users',user="root",password="")

login = input()

c = mydb.cursor()


c.execute(f"SELECT * FROM login WHERE login = '{login}'")

user = c.fetchall()

print(user)
