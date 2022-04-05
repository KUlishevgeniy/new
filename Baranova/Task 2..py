import mysql.connector as conn

db = conn.connect(host = '127.0.0.1', user = 'root', passwd = '', db = 'users')
curcor = db.cursor()
curcor.execute('SELECT * FROM user_id')
user = curcor.fetchall()
print(user)