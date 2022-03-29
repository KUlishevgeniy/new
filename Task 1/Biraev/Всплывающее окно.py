from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("Форма 1")
surname = StringVar()
name_label = Label(text="Введите имя")
surname_label = Label(text="Введите фамилию")
name_label.grid(row=1, column=0, sticky="w")
surname_label.grid(row=2, column=0, sticky="w")








root.mainloop()