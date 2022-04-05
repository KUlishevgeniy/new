import mysql.connector
from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception("Не найдено")

    return db


def poisk(name, password):
    mydb = mysql.connector.connect(**read_db_config())
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM user')
    users = mycursor.fetchall()
    for user in users:
        if user[1] == name and user[2] == password:
            return user[0]
    return -100