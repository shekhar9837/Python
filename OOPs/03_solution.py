
# inheritance

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand}-{self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

# my_tesla = ElectricCar("tesla", "S", "85kWh")
# print(my_tesla.full_name())

my_tesla = ElectricCar("tesla", "S", "85kWh")
print(my_tesla.brand)