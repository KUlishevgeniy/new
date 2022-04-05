import lol


class Employee:
    def __init__(self, name="", password=""):
        otvet = lil.poisk(name, password)
        if otvet != (-100):
            self.id = otvet
            self.password = password
            print(self.id)
        else:
            print("Нет")


# emp1 = Employee("two", "qwert2")
