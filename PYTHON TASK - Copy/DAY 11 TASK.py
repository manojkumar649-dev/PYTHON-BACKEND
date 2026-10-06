class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

class ElectronicProduct(Product):
    def display_electronic(self):
        print("This is an electronic product")
        
obj1 = ElectronicProduct(101, "Laptop", 50000, 2)
obj1.display_product()
obj1.display_electronic()


#task  2

class Laptop:

    def __init__(self, brandmodel, price, RAM, storage):
        self.brandmodel = brandmodel
        self.price = price
        self.RAM = RAM
        self.storage = storage

    def display_details(self):
        print("Brand Model:", self.brandmodel)
        print("RAM:", self.RAM)
        print("Storage:", self.storage)

    def show_price(self):
        print("Price:", self.price)

laptop1 = Laptop("Dell Inspiron", 55000, "8GB", "512GB SSD")
laptop2 = Laptop("HP Pavilion", 65000, "16GB", "1TB SSD")

laptop1.display_details()
laptop1.show_price()

print()

laptop2.display_details()
laptop2.show_price()
