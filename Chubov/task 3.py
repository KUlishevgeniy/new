from tkinter import *
from tkinter import messagebox

def click():
    username=user_entry.get()
    password=user_entry1.get()

    messagebox.showinfo('Авторизация прошла успешно',f'{username},{password}')


root = Tk()
root.title('Авторизация')
root.geometry=('450×230')
root['bg']= 'black'

main_label = Label(root,text='Авторизация',font='arial 15 bold',bg='black',fg='white')
main_label.pack()

user_label = Label(root, text='id пользователя', font='arial 15 bold', bg='black', fg='white',padx=100,pady=15)
user_label.pack()

user_entry = Entry(root,font='arial 11 bold',bg='black',fg='lime')
user_entry.pack()

user_password=Label(root, text='Пароль', font='arial 15 bold', bg='black', fg='white',padx=100,pady=15)
user_password.pack()

user_entry1 = Entry(root,font='arial 11 bold',bg='black',fg='lime')
user_entry1.pack()

send_btn = Button(root, text='Войти', command=click)
send_btn.pack(padx=10,pady=8)




root.mainloop()