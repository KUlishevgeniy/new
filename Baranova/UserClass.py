import mysql.connector as conn


class User:
    userid = None

    def __init__(self, name):
        db = conn.connect(host='127.0.0.1', database='users', user="root", password="")
        curcor = db.cursor()
        curcor.execute(f"SELECT * FROM user_id WHERE login = '{name}'")
        user = curcor.fetchall()

        if len(user) != 0:
            self.userid = user[0][0]
        else:
            messagebox.showerror('Ошибка', 'Неправильное имя пользователя или пароль')
