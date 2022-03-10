import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM login");
users = mycursor.fetchall()
print(users)