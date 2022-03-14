# Задание необходимо выполнить на основе задания 3
# создать класс авторизациию
# class User:
#   def __init__(self,name):
# В функции def __init__(self,name): прописать проверку на соответсвие в базе данных
# в результате выпонения init выдается
# 1.либо сообщение об ошибке
# 2. либо self.userid присвоить значение идентификатора

import mysql.connector as conn
from tkinter import *
from tkinter import messagebox


def click():
    user = User(login_in=log.get(), password_in=pas.get())

class User:
    def __init__(self, login_in, password_in):
        mydb = conn.connect(host='127.0.0.1', database='users', user="root", password="")
        c = mydb.cursor()
        c.execute(f"SELECT * FROM login WHERE login = '{login_in}'")
        ent = c.fetchall()
        c1 = mydb.cursor()
        c1.execute(f"SELECT * FROM login WHERE login = '{login_in}'AND password = '{password_in}'")
        ent2 = c1.fetchall()

        if len(ent) == 0:
            messagebox.showerror('Ошибка', 'Пользователь не найден')
        elif len(ent2) == 0:
            messagebox.showerror('Ошибка', 'Неверный пароль')
        else:
            window_2 = Tk()
            window_2.title("Вход")
            window_2.geometry("200x200")
            inf = Label(window_2, text=ent2[0][0])
            inf.grid(column=0, row=0)
            self.userid = ent2[0][0]

window = Tk()
window.title("Окно авторизации")
window.geometry("500x500")

login = Label(window, text="Введите логин:")
login.grid(column=0, row=0)
password = Label(window, text="Введите пароль:")
password.grid(column=0, row=1)

log = Entry(window, width=15)
log.grid(column=1, row=0)
pas = Entry(window, width=15)
pas.grid(column=1, row=1)

A_btn = Button(window, text="Войти", command=click)
A_btn.grid(column=1, row=2)

window.mainloop()