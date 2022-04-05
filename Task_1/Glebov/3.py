class User:
    def init(self, name, password):
        query = "SELECT password FROM login WHERE name = %s"
        query1 = "SELECT user_id FROM login WHERE name = %s"
        query2 = "SELECT * FROM user WHERE user_id = %s"
        args1 = [name]
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args1)
            mas = cursor.fetchone()
            cursor.execute(query1, args1)
            mas1 = cursor.fetchone()
            if mas[0] == password:
                self.id = mas1[0]

            args2 = [self.id]
            cursor = conn.cursor()
            cursor.execute(query2, args2)
            user_info = cursor.fetchone()
            self.surname = user_info[1]
            self.name = user_info[2]
            self.secondname = user_info[3]
            self.birthday = user_info[4]
            self.email = user_info[5]
            self.telephone = user_info[6]
            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()