import mysql.connector as conn
from tkinter import *
from tkinter import messagebox
from UserClass import User

window = Tk()
window.title("Окно Авторизации")
window.geometry("300x150")
window.resizable(False, False)

font_header = ('Roboto', 15)
font_entry = ('Roboto', 12)
label_font = ('Roboto', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def Entrydef():
    db = conn.connect(host='127.0.0.1', database='users', user="root", password="")
    login = loginEntry.get()
    password = passwordEntry.get()
    curcor = db.cursor()
    curcor.execute(f"SELECT * FROM user_id WHERE login = '{login}'AND password = '{password}'")
    user = curcor.fetchall()

    if len(user) != 0:
        window_2 = Tk()
        window_2.title("Вход")
        window_2.geometry("200x200")
        lbll = Label(window_2, text=user[0])
        lbll.grid(column=0, row=0)
        window_2.mainloop()
    else:
        messagebox.showerror('Ошибка', 'Неправильное имя пользователя или пароль')


login = Label(window, text="Введите логин:", font=font_header, justify=CENTER, **header_padding)
login.grid(column=0, row=0)
password = Label(window, text="Введите пароль:", font=font_header, justify=CENTER, **header_padding)
password.grid(column=0, row=1)

loginEntry = Entry(window, width=15)
loginEntry.grid(column=1, row=0)
passwordEntry = Entry(window, width=15)
passwordEntry.grid(column=1, row=1)

send_but = Button(window, text="Войти", command=Entrydef)
send_but.grid(column=1, row=2)

window.mainloop()

user1 = User("maria")
print(user1.userid)
print(dir(user1))
