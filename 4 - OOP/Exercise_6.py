class Device: #Initial class Device
    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer

    def show_info(self):
        print(f"Device Model: {self.model}, Manufacturer: {self.manufacturer}")

class SmartDevice(Device):  #Subclass SmartDevice innheriting from Device
    def __init__(self, model, manufacturer, os):
        super().__init__(model, manufacturer)
        self.os = os

    def show_os(self):
        print(f"Operating System: {self.os}")

class Smartphone(SmartDevice):  #Subclass Smartphone innheriting from SmartDevice
    def __init__(self, model, manufacturer, os, sim_count):
        super().__init__(model, manufacturer, os)
        self.sim_count = sim_count

    def show_sim_info(self):
        print(f"SIM Card Count: {self.sim_count}")

my_phone = Smartphone("iPhone 12", "Apple", "iOS", 1) # Demonstration of multilevel inheritance
my_phone.show_info()
my_phone.show_os()
my_phone.show_sim_info()