import mysql.connector
from configparser import ConfigParser


def read_db(filename='cfg.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
            # print(db[item[0]])
    else:
        raise Exception("Not found something")
    # print(db)
    return db


def search(login, password, users):
    fl = 0
    for use in users:
        if login == use[1] and password == use[2]:
            fl = 1
    return fl


mydb = mysql.connector.connect(**read_db())
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM user')
user = mycursor.fetchall()

print("Введите логин:")
lg = input()
print("Введите пароль:")
pas = input()

if search(lg, pas, user):
    print("Пароль и логин найден")
else:
    print("Пароль либо логин неправильные")
