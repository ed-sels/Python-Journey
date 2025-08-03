class Bicycle:
    def __init__(self, brand, type, gear_count):
        self.brand = brand
        self.type = type
        self.gear_count = gear_count

    def describe(self):
        print(f"This is a {self.brand} {self.type} bicycle with {self.gear_count} gears.")

#Displaying bicycle specs
Road_bike = Bicycle("Trek", "Road", 18)
Road_bike.describe()
Mountain_bike = Bicycle("Giant", "Mountain", 21)
Mountain_bike.describe()
Electric_bike = Bicycle("Specialized", "Electric", 7)
Electric_bike.describe()