import mysql.connector
from tkinter import *

def auth():
    mydb = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM login WHERE login = '" + login.get() + "'")
    users = mycursor.fetchall()
    if(len(users) == 0):
        print("Account not found")
    else:
        for user in users:
            if (password.get() == user[2]):
                print("Authorization successful")
                return
        print("Invalid password")

root = Tk()
root.geometry("250x300")
root.title("Authorization")

password = StringVar()
login = StringVar()

login_label = Label(text="Enter login:")
password_label = Label(text="Enter password:")

login_label.grid(row=0, column=0, sticky="w")
password_label.grid(row=1, column=0, sticky="w")

password_entry = Entry(textvariable=password)
login_entry = Entry(textvariable=login)

login_entry.grid(row=0, column=1, padx=7, pady=7)
password_entry.grid(row=1, column=1, padx=7, pady=7)

message_button = Button(text="Authorization", command=auth)
message_button.grid(row=3, column=1, padx=7, pady=7, sticky="w")

message_leave = Button(text="Exit", command=exit)
message_leave.grid(row=4, column=1, padx=7, pady=7, sticky="w")

root.mainloop()