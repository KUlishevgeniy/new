from tkinter import *
from UserClass2 import User

window = Tk()
window.title("Окно Авторизации")
window.geometry("300x150")
window.resizable(False, False)

font_header = ('Roboto', 15)
font_entry = ('Roboto', 12)
label_font = ('Roboto', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def newEntrydef():
    global user
    login = loginEntry.get()
    password = passwordEntry.get()
    user = User(login, password)


login = Label(window, text="Введите логин:", font=font_header, justify=CENTER, **header_padding)
login.grid(column=0, row=0)
password = Label(window, text="Введите пароль:", font=font_header, justify=CENTER, **header_padding)
password.grid(column=0, row=1)

loginEntry = Entry(window, width=15)
loginEntry.grid(column=1, row=0)
passwordEntry = Entry(window, width=15)
passwordEntry.grid(column=1, row=1)

send_but = Button(window, text="Войти", command=newEntrydef)
send_but.grid(column=1, row=2)

window.mainloop()

print(user.userid)
