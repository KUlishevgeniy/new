import mysql.connector


class DataBase:

    def __init__(self, _host, _name, _user, _password):
        self.mydb = mysql.connector.connect(host=_host, database=_name, user=_user, password=_password)
        self.mycursor = self.mydb.cursor()

    def clear(self, table):
        self.mycursor.execute("TRUNCATE TABLE " + table)

    def add_phone(self, phones):
        str1 = ''
        str2 = ''
        for phone in phones:
            str1 = str1 + " ('" + phone.id + "', '" + phone.name + "', '" + phone.brand + "', '" + phone.price + "'),"
            str2 = str2 + " ('" + phone.specific.type + "', '" + phone.specific.OC + "', '" + phone.specific.typeSim + "', '" + phone.specific.countSim + "', '" + phone.specific.weight + "', '" + phone.specific.proportions + "'),"
        str1 = str1[:len(str1) - 1]
        str2 = str2[:len(str2) - 1]
        self.mycursor.execute("INSERT INTO phone (id, name, brand, price) VALUES" + str1)
        self.mydb.commit()
        self.mycursor.execute("INSERT INTO specification (Type, OC, TypeSim, CountSim, Weight, Proportions) VALUES" + str2)
        self.mydb.commit()


    def __del__(self):
        self.mydb.close()
