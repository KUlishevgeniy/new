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


mysqldb = mysql.connector.connect(**read_db())
mysqldb.close()
