class Product:
    name: str
    id: str
    price: str
    brand: str

    def __init__(self, _name, _id, _price, _brand):
        self.name = _name
        self.id = _id
        self.price = _price
        self.brand = _brand

    def print(self):
        print("name: " + self.name + " id: " + self.id + " price: " + self.price + " brand: " + self.brand)

