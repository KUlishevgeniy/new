import mysql.connector as conn
from tkinter import messagebox
from tkinter import *

class User:
    userid = None

    def __init__(self, login, password):
        db = conn.connect(host='127.0.0.1', database='users', user="root", password="")
        curcor = db.cursor()
        curcor.execute(f"SELECT * FROM user_id WHERE login = '{login}' AND password = '{password}'")
        user = curcor.fetchall()

        if len(user) != 0:
            self.userid = user[0][0]
            window_2 = Tk()
            window_2.title("Вход")
            window_2.geometry("200x200")
            lbll = Label(window_2, text=user[0])
            lbll.grid(column=0, row=0)
            window_2.mainloop()
        else:
            messagebox.showerror('Ошибка', 'Неправильное имя пользователя или пароль')
