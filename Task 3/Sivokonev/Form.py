import tkinter.messagebox
from tkinter import *

import Class
import Search


def auth():
    global surname_e
    global name_e
    global secondname_e
    global birthday_e
    global email_e
    global telephone_e
    global id_user
    global User
    User = Class.Ok(login.get(), password.get())
    id_user = User.id
    if User.id != -1:
        Second = Tk()
        center(Second, 800, 600)
        Second.title("Окно 2")
        Second.geometry("800x600")
        surname_e = Entry(Second, textvariable=User.surname)
        name_e = Entry(Second, textvariable=User.name)
        secondname_e = Entry(Second, textvariable=User.secondname)
        birthday_e = Entry(Second, textvariable=User.birthday)
        email_e = Entry(Second, textvariable=User.email)
        telephone_e = Entry(Second, textvariable=User.telephone)

        surname_e.insert(0, User.surname)
        name_e.insert(0, User.name)
        secondname_e.insert(0, User.secondname)
        birthday_e.insert(0, User.birthday)
        email_e.insert(0, User.email)
        telephone_e.insert(0, User.telephone)

        surname_e.grid(row=1, column=1, padx=5, pady=5)
        name_e.grid(row=1, column=2, padx=5, pady=5)
        secondname_e.grid(row=1, column=3, padx=5, pady=5)
        birthday_e.grid(row=1, column=4, padx=5, pady=5)
        email_e.grid(row=1, column=5, padx=5, pady=5)
        telephone_e.grid(row=1, column=6, padx=5, pady=5)

        message_but = Button(Second, text="Сохранить", command=save,bg='#567', fg='White')
        # message_but.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        message_but.place(relx=0.5, rely=0.5, anchor=CENTER)
        Main.quit()
        Main.destroy()
        Second.mainloop()
    else:
        # label1 = Label(Second, text="Неверный логин или пароль")
        # label1.grid(row=0, column=0)
        tkinter.messagebox.showerror("Ошибка", "Неверный логин или пароль")
        # Second.quit()
        # Second.destroy()


def save():
    # print(surname_e.get()+" "+name_e.get())
    Search.update(surname_e.get(), name_e.get(), secondname_e.get(), birthday_e.get(), email_e.get(), telephone_e.get(),
                  id_user)
    # print(User.surname.get())
    return tkinter.messagebox.showinfo("Успешно", "Данные сохранены!")


def center(root, w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = int(sw - w) / 2
    y = int(sh - h) / 2
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))


Main = Tk()
# Main.eval('tk::PlaceWindow . center')
center(Main, 300, 300)
Main.geometry("300x300")
Main.title("Форма 1")
login = StringVar()
password = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите пароль:")
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=0, column=1, sticky="w")
surname_entry = Entry(textvariable=password)
name_entry = Entry(textvariable=login)
name_entry.grid(row=1, column=0, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
message_button = Button(text="Авторизация", command=auth)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

Main.mainloop()
