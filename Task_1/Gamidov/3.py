import mysql.connector
from tkinter import *

def  authSuccess():
    window1 = Tk()
    window1.title("Success")
    window1.geometry('500x500')
    lbl1 = Label(window1, text="Авторизация успешна")
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

def auth():
    mydb = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM login WHERE login = '" + login.get() + "'");
    users = mycursor.fetchall()
    if(len(users) == 0):
        authUnsuccessLogin()
        return
    else:
        for user in users:
            if (password.get() == user[2]):
                authSuccess()
                return
        authUnsuccessPassword()




root = Tk();
root.geometry("300x300")
root.title("Авторизация")

password = StringVar()
login = StringVar()

login_label = Label(text="Введите логин:")
password_label = Label(text="Введите пароль:")

login_label.grid(row=0, column=0, sticky="w")
password_label.grid(row=2, column=0, sticky="w")

password_entry = Entry(textvariable=password)
login_entry = Entry(textvariable=login)

login_entry.grid(row=1, column=1, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)

message_button = Button(text="Авторизация", command=auth)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

message_leave = Button(text="Выход", command=exit)
message_leave.grid(row=4, column=1, padx=5, pady=5, sticky="e")

root.mainloop()