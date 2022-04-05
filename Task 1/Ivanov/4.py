from tkinter import *
import mysql.connector as sql
from tkinter import messagebox

class User:
    userid = 0
    def __init__(self, name):
        connection = sql.connect(host="localhost", user="root", passwd="", database="users")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM passw WHERE name = '{name}'")
        user = cursor.fetchall()
        if len(user) != 0:
            self.userid = user[0][0]
        else:
            messagebox.showinfo('Окно авторизации', 'Неправильное имя пользователя!!')

def entry():
    try:
        flag = 0
        connection = sql.connect(host="localhost", user="root", passwd="", database="users")
        cursor = connection.cursor()
        login = log.get()
        password = int(passw.get())
        cursor.execute("SELECT * FROM passw")
        res = cursor.fetchall()
        for row in res:
            if row[1] == log.get() and row[2] == int(passw.get()):
                flag = 1
        if (flag == 1):
            messagebox.showinfo("Окно авторизации", "Данные введены верно")
        else:
            messagebox.showinfo("Окно авторизации", "Данные введены неверно")
    except:
        print("Error!")
window = Tk()
window.title("Окно авторизации")
window.geometry("300x300")
lbl_log = Label(window, text="Логин: ")
lbl_log.grid(column=0, row=0)
log = StringVar()
txt_log = Entry(window, width=20, textvariable=log)
txt_log.grid(column=1, row=0, padx=(10,0))
lbl_passw = Label(window, text="Пароль: ")
lbl_passw.grid(column=0, row=1, pady=(10,0))
passw = StringVar()
txt_passw = Entry(window, width=20, show="*", textvariable=passw)
txt_passw.grid(column=1, row=1, padx=(10,0), pady=(10,0))
but = Button(text="Войти в систему!", command=entry)
but.grid(column=1, row=2, padx=(10,0), pady=(10,0))

window.mainloop()

user1 = User(log.get())
print(user1.userid)