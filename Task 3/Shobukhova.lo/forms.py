import mysql.connector
from tkinter import *
from tkinter import messagebox

import lil
import lol

def auth():
    global password_e
    global name_e
    mydb = mysql.connector.connect(host='127.0.0.1', database='ksrwq', user='root', password='')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM user ')
    user = mycursor.fetchall()

    sa = name.get() + " " + password.get()
    window1 = Tk()
    window1.title("Окно 2")
    window1.geometry("800x600")
    root.quit()

    flag = False
    for c in user:
        if c[1] == name.get() and c[2] == password.get():
            flag=True

    if flag == True:

        name_e = Entry(window1, textvariable=name)
        password_e = Entry(window1, textvariable=password)

        name_e.insert(0, name.get())
        password_e.insert(0, password.get())

        name_e.grid(row=1, column=2, padx=5, pady=5)
        password_e.grid(row=1, column=1, padx=5, pady=5)

        message_but = Button(window1, text="Сохранить", command=save)
        message_but.place(relx=0.5, rely=0.5)

        lbll = Label(window1, text="Поздравляем! Вы вошли!")
        lbll.grid(column=0, row=0)
       # mycursor.execute.update(name_e.get(), password_e.get())
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")
        # lbll = Label(window1, text="Error")
        # lbll.grid(column=0, row=0)

    window1.mainloop()
    # return flag

def Update(name, password):
    query = "UPDATE `user` SET `name` = %s,`password` = %s"+str(id)
    args = [name, password]
    conn = mysql.connector.connect(host='127.0.0.1', database='ksrwq', user='root', password='')
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
# Update(name.get(), password.get())
def save():
    lol.Update(name_e.get(), password_e.get())
    return tkinter.messagebox.showinfo("Успешно", "Данные сохранены")

root = Tk()
root.geometry("300x300")
root.title("Форма 1")

name = StringVar()
password = StringVar()

name_label = Label(text="Введите имя:")
password_label=  Label(text="Введите пароль: ")
name_label.grid(row=0, column=0, sticky="w")
password_label.grid(row=2, column=0, sticky="w")
name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry=Entry(textvariable=password)
password_entry.grid(row=2,column=1,sticky="w")

message_button = Button(text="Авторизация", command=auth)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()

