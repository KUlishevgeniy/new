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
    else:
        raise Exception("Not found something")
    return db


def search(login, password):
    mysqldb = mysql.connector.connect(**read_db())
    dbcursor = mysqldb.cursor()
    dbcursor.execute('SELECT * FROM login')
    users = dbcursor.fetchall()
    fl = -1
    for use in users:
        if login == use[1] and password == use[2]:
            fl = use[0]
            break
    dbcursor.close()
    return fl


def info(id_user):
    mysqldb = mysql.connector.connect(**read_db())
    dbcursor = mysqldb.cursor()
    dbcursor.execute('SELECT * FROM user WHERE id_user={0}'.format(id_user))
    users = dbcursor.fetchall()
    dbcursor.close()
    return users


def update(surname_e, name_e, secondname_e, birthday_e, email_e, telephone_e, id_user):
    mysqldb = mysql.connector.connect(**read_db())
    dbcursor = mysqldb.cursor()
    request = "UPDATE user SET surname={0}, name={1}, secondname={2}, birthday={3}, email={4}, telephone={5} WHERE " \
              "id_user={6}".format(
        "'" + surname_e + "'", "'" + name_e + "'", "'" + secondname_e + "'", "'" + birthday_e + "'",
        "'" + email_e + "'", "'" + telephone_e + "'", id_user)
    dbcursor.execute(request)
    mysqldb.commit()
    dbcursor.close()


def insert_parse(id, brand, name, price, category, ssil):
    mysqldb = mysql.connector.connect(**read_db())
    dbcursor = mysqldb.cursor()
    request = "INSERT INTO parse (id,brand,name,price,category,ssil) VALUES({0},{1},{2},{3},{4},{5})".format(
        "'" + id + "'", "'" + brand + "'", "'" + name + "'", "'" + price + "'",
        "'" + category + "'", "'" + ssil + "'")
    dbcursor.execute(request)
    mysqldb.commit()
    dbcursor.close()
    mysqldb.close()


def phones():
    mysqldb = mysql.connector.connect(**read_db())
    dbcursor = mysqldb.cursor()
    request = 'SELECT * FROM parse'
    dbcursor.execute(request)
    users = dbcursor.fetchall()
    ssil = []
    for use in users:
        ssil += [(use[0], use[5])]
    dbcursor.close()
    mysqldb.close()
    return ssil
