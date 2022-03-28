class Product:

    def __init__(self, _name, _id, _price, _brand, _href, _specific):
        self.name = _name
        self.id = _id
        self.price = _price
        self.brand = _brand
        self.href = _href
        self.specific = _specific

    def print(self):
        print("name: " + self.name + " id: " + self.id + " price: " + self.price + " brand: " + self.brand + " url: " + self.href)
        print("Type: " + self.specific.type + " OC: " + self.specific.OC + " typeSim: " + self.specific.typeSim + " countSim: " + self.specific.countSim + " weight: " + self.specific.weight + " proportions:" + self.specific.proportions)
        print()

