import mysql.connector


class DataBase:

    def __init__(self, _host, _name, _user, _password):
        self.mydb = mysql.connector.connect(host=_host, database=_name, user=_user, password=_password)
        self.mycursor = self.mydb.cursor()

    def clear(self, table):
        self.mycursor.execute("TRUNCATE TABLE " + table)

    def add(self, phones):
        str = ''
        for phone in phones:
            str = str + " ('" + phone.id + "', '" + phone.name + "', '" + phone.brand + "', '" + phone.price + "'),"
        str = str[:len(str) - 1]
        print("INSERT INTO phone (id, name, brand, price) VALUES" + str)
        self.mycursor.execute("INSERT INTO phone (id, name, brand, price) VALUES" + str)
        self.mydb.commit()


    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
