### TODO создать форму ввода логина и пароля
## TODO проверить содержимое ввода данных в на соответствие в базе данных

import mysql.connector
from tkinter import *
from tkinter import messagebox

window1 = Tk()  
window1.geometry("300x300")
window1.title("Авторизация")


def auth():
    mydb = mysql.connector.connect(host='127.0.0.1', database='new1', user='root', password='')
    mycursor = mydb.cursor()
    login = l.get()
    password = p.get()
    mycursor.execute(
        "SELECT * FROM login WHERE name={0} AND password = {1}".format("'" + login + "'", "'" + password + "'"))
    user = mycursor.fetchall()

    if len(user) > 0:
        window1.destroy()
        window2 = Tk()
        window2.geometry("300x300")
        window2.title("Вход")
        lbl1 = Label(window2, text=user[0])
        lbl1.grid(column=0, row=0)
        window2.mainloop()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


login = Label(window1, text="Введите логин:")
login.grid(column=0, row=0)
password = Label(window1, text="Введите пароль:")
password.grid(column=0, row=1)

l = Entry(window1, width=20)
l.grid(column=1, row=0)
p = Entry(window1, width=20)
p.grid(column=1, row=1)

message_button = Button(window1, text="Авторизироваться", command=auth)
message_button.grid(column=1, row=2)
window1.mainloop()

