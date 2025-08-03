class Meal:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = None
        self.set_quantity(quantity)

    def calculate_total(self):
        return self.__price * self.__quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        if 1 <= quantity <= 10:
            self.__quantity = quantity
        else:
            print("Quantity must be between 1 and 10")

    def get_name(self):
        return self.__name

# Get user input for meal name and quantity
meal_name = input("Enter the name of the meal: ")
meal_quantity = int(input("Enter the quantity (1-10): "))

meal1 = Meal(meal_name, 12.5, meal_quantity)
print(meal1.get_name(), "costs", meal1.calculate_total(), 
      "for", meal1.get_quantity(), "items.")