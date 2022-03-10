## Задание необходимо выполнить на основе задания 3
## создать класс авторизациию
#class User:
#   def __init__(self,name):
## В функции def __init__(self,name): прописать проверку на соответсвие в базе данных
## в результате выпонения init выдается
# 1.либо сообщение об ошибке либо
# 2. либо #self.userid присвоить значение идентификатора



import person
from tkinter import *

def auth(password, login):
    a = person.Person(login, password)


def main():
    root = Tk()
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

    message_button = Button(text="Авторизация", command=lambda: auth(password.get(), login.get()))
    message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    message_leave = Button(text="Выход", command=exit)
    message_leave.grid(row=4, column=1, padx=5, pady=5, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    main()