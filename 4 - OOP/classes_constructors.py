class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def show_specs(self):
        print(f"{self.brand} Laptop | RAM: {self.ram} | Price: ${self.price}")

my_laptop = Laptop("Dell", 8, 850)
my_laptop.show_specs()