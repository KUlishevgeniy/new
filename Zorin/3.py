# создать форму ввода логина и пароля
# проверить содержимое ввода данных в на соответствие в базе данных
import mysql.connector as conn
from tkinter import *

def click():
    mydb = conn.connect(host='127.0.0.1', database='users', user="root", password="")
    login_in = log.get()
    password_in = pas.get()
    c = mydb.cursor()
    c.execute(f"SELECT * FROM login WHERE login = '{login_in}'AND password = '{password_in}'")
    user = c.fetchall()
    window_2 = Tk()
    window_2.title("Вход")
    window_2.geometry("200x200")

    inf = Label(window_2, text=user[0])
    inf.grid(column=0, row=0)
    window_2.mainloop()


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