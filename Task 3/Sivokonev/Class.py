import Search


class Ok:
    def __init__(self, login="", password=""):
        id = Search.search(login, password)
        self.id = id
        if id != -1:
            request = Search.info(self.id)
            self.surname = request[0][1]
            self.name = request[0][2]
            self.secondname = request[0][3]
            self.birthday = request[0][4]
            self.email = request[0][5]
            self.telephone = request[0][6]
        else:
            pass
