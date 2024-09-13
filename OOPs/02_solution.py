

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year 
        self.color = color

    def display_car_info(self):
        return f"{self.model} {self.year} {self.color} {self.make}"
    

my_car = Car("Toyota", "Supra", "2025", "white")
print(my_car.display_car_info())
