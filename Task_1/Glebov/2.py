from tkinter import *
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from User import User

def check(root, name, password):
    query = "SELECT password FROM login WHERE name = %s"
    args = [name]
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)
        a = cursor.fetchall()
        if len(a) == 0:
            authWrongName()
        elif a[0][0] == password:
            root.destroy()
            authSuccess(name, password)
        else:
            authWrongPassword()
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def authSuccess(login, password):
    user = User(login, password)
    window1 = Tk()
    window1.title("Круто")
    window1.geometry('800x600')
    surname = StringVar()
    surname_entry = Entry(window1, textvariable=surname)
    surname_entry.insert(0, user.surname)
    lbl2 = Label(window1, text="Фамилия")
    lbl2.grid(column=0, row=0)
    surname_entry.grid(column=1, row=0)

    name = StringVar()
    name_entry = Entry(window1, textvariable=name)
    name_entry.insert(0, user.name)
    lbl1 = Label(window1, text="Имя")
    lbl1.grid(column=0, row=1)
    name_entry.grid(column=1, row=1)

    secondname = StringVar()
    secondname_entry = Entry(window1, textvariable=secondname)
    secondname_entry.insert(0, user.secondname)
    lbl3 = Label(window1, text="Отчество")
    lbl3.grid(column=0, row=2)
    secondname_entry.grid(column=1, row=2)

    birthday = StringVar()
    birthday_entry = Entry(window1, textvariable=birthday)
    birthday_entry.insert(0, user.birthday)
    lbl4 = Label(window1, text="ДР")
    lbl4.grid(column=0, row=3)
    birthday_entry.grid(column=1, row=3)

    email = StringVar()
    email_entry = Entry(window1, textvariable=email)
    email_entry.insert(0, user.email)
    lbl5 = Label(window1, text="Майл")
    lbl5.grid(column=0, row=4)
    email_entry.grid(column=1, row=4)

    telephone = StringVar()
    telephone_entry = Entry(window1, textvariable=telephone)
    telephone_entry.insert(0, user.telephone)
    lbl6 = Label(window1, text="Телефон")
    lbl6.grid(column=0, row=5)
    telephone_entry.grid(column=1, row=5)
    message_button = Button(window1, text="Клик", command=lambda: update(user.id, name.get(), surname.get(), secondname.get(), birthday.get(), email.get(),telephone.get()))
    message_button.grid(row=7, column=5, padx=5, pady=5, sticky="e")
    window1.mainloop()

def update(id, name, surname, secondname, birthday, email, telephone):
    query = "UPDATE new2.user SET surname = %s, name = %s, secondname = %s, birthday = %s, email = %s, telephone = %s  WHERE user.id_user =" + str(id) + ";"
    args = [surname, name, secondname, birthday, email, telephone]
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    cursor.close()
    conn.close()

def authWrongPassword():
    sa="Пароль не верен"
    window1 = Tk()
    window1.title("Неуспех(")
    window1.geometry('800x600')
    lbl1 = Label(window1, text=sa)
    lbl1.grid(column=0, row=0)
    window1.mainloop()

def authWrongName():
    sa = "Данного пользователя не существует"
    window1 = Tk()
    window1.title("Неуспех(")
    window1.geometry('800x600')
    lbl1 = Label(window1, text=sa)
    lbl1.grid(column=0, row=0)
    window1.mainloop()

def main():
    root = Tk()
    root.geometry("300x300")
    root.title("Форма 1")

    name = StringVar()
    name_label = Label(text="Введите логин:")
    password_label = Label(text="Введите пароль:")
    name_label.grid(row=0, column=0, sticky="w")
    password_label.grid(row=2, column=0, sticky="w")
    name_entry = Entry(textvariable=name)
    password = StringVar()
    password_entry = Entry(textvariable=password)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry.grid(row=2, column=1, padx=5, pady=5)
    message_button = Button(text="Авторизация", command=lambda: check(root, name.get(), password.get()))
    message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    exit_button = Button(text="Уйти отсюда", command=exit)
    exit_button.grid(row=5, column=1, padx=5, pady=5, sticky="e")
    root.mainloop()


if name == 'main':
    main()