import mysql.connector
from tkinter import *

def auth():
    mydb = mysql.connector.connect(host='127.0.0.1', database='ksrwq', user='root', password='')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM user ')
    user = mycursor.fetchall()

    sa = name.get() + " " + surname.get()
    window1 = Tk()
    window1.title("Окно 2")
    window1.geometry("800x600")
    root.quit()

    flag = False
    for c in user:
        if c[1] == name.get() and c[2] == surname.get():
            flag=True

    if flag == True:
        lbll = Label(window1, text=sa)
        lbll.grid(column=0, row=0)
    else:
        lbll = Label(window1, text="Error")
        lbll.grid(column=0, row=0)

    window1.mainloop()

root = Tk()
root.geometry("300x300")
root.title("Форма 1")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label=Label(text="Введите фамилию: ")
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=2, column=0, sticky="w")
name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry=Entry(textvariable=surname)
surname_entry.grid(row=2,column=1,sticky="w")

message_button = Button(text="Авторизация", command=auth)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()

