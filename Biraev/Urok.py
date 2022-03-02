from tkinter import *

def auth():
    sa=name.get()+ " " + surname.get()

    window1 = Tk()
    window1.title("Окно 2")
    window1.geometry('800x600')
    lbl1 = Label(window1, text=sa)
    lbl1.grid(column=0, sticky="e")
    window1.mainloop()


root = Tk()
root.geometry("300x300")
root.title("Форма 1")

name_label = Label(text="Введите имя")
surname_label = Label(text="Введите фамилию")
name_label.grid(row=1, column=0, sticky="w")
surname_label.grid(row=2, column=0, sticky="w")

name = StringVar()
surname = StringVar()
surname_entry = Entry(textvariable=surname)
name_entry = Entry(textvariable=name)
name_entry.grid(row=1, column=1, padx=5, pady=5)
surname_entry.grid(row=2, column=1, padx=5, pady=5)

message_botton = Button(text="Авторизация", command=auth)
message_botton.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()