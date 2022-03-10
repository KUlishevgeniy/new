import mysql.connector
from tkinter import *

def  authSuccess(human):
    window1 = Tk()
    window1.title("Success")
    window1.geometry('1000x1000')
    all = "Авторизация успешна id = " + str(human.id) + ". Фамилия = " + human.surname +". Имя = " + human.name +". Отчество = " + human.secondname + ". Email = " + human.email +". Телефон = " + human.telephone
    lbl1 = Label(window1, text= all)
    lbl1.grid(column=0, row=0)
    window1.mainloop()


def  authUnsuccessLogin():
    window1 = Tk()
    window1.title("UnsuccessLogin")
    window1.geometry('500x500')
    lbl1 = Label(window1, text="Учетная запись не найдена")
    lbl1.grid(column=0, row=0)
    window1.mainloop()

def  authUnsuccessPassword():
    window1 = Tk()
    window1.title("UnsuccessPassword")
    window1.geometry('500x500')
    lbl1 = Label(window1, text="Неверный пароль")
    lbl1.grid(column=0, row=0)
    window1.mainloop()

class Person:
    login: str
    password: str
    id: int
    surname: str
    name: str
    secondname: str
    birthday: str
    email: str
    telephone: str

    def __init__(self, _login, _password):
        self.login = _login
        self.password = _password
        mydb = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE login = '" + self.login + "'")
        user = mycursor.fetchall()
        if(len(user) == 0):
            authUnsuccessLogin()
        elif(self.password == user[0][2]):
            self.id = user[0][0]
            self.setAll(mycursor)
            authSuccess(self)
        else:
            authUnsuccessPassword()

    def setAll(self, mycursor):
        mycursor.execute("SELECT * FROM user WHERE id_user = '" + str(self.id) + "'")
        human = mycursor.fetchall();
        self.surname = human[0][1]
        self.name = human[0][2]
        self.secondname = human[0][3]
        self.birthday = human[0][4]
        self.email = human[0][5]
        self.telephone = str(human[0][6])








